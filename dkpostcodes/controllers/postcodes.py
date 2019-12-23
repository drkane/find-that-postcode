from datetime import datetime
import bottle
import re

from ..metadata import AREA_TYPES, KEY_AREA_TYPES, OTHER_CODES, OAC11_CODE, RU11IND_CODES
from .controller import *
from . import areas
from . import areatypes


class Postcode(Controller):

    es_index = 'geo_postcode'
    url_slug = 'postcodes'
    date_fields = ["dointr", "doterm"]
    not_area_fields = ["osgrdind", "usertype"]

    def __init__(self, id, data=None, pcareas=None):
        super().__init__(id, data)
        if areas:
            self.relationships["areas"] = pcareas

    def __repr__(self):
        return '<Postcode {}>'.format(self.id)


    @classmethod
    def get_from_es(cls, id, es, es_config=None):
        if not es_config:
            es_config = {}
        data = es.get(
            index=es_config.get("es_index", cls.es_index),
            doc_type=es_config.get("es_type", cls.es_type),
            id=cls.parse_id(id),
            ignore=[404],
            _source_exclude=es_config.get("_source_exclude", []),
        )
        
        pcareas = []
        postcode = data.get("_source")
        for k in list(postcode.keys()):
            if isinstance(postcode[k], str) and re.match(r'[A-Z][0-9]{8}', postcode[k]):
                area = areas.Area.get_from_es(postcode[k], es, examples_count=0) 
                if area.found:
                    postcode[k + "_name"] = area.attributes.get("name")
                    pcareas.append(area)

        return cls(data.get("_id"), data.get("_source"), pcareas)
    
    def process_attributes(self, postcode):

        # turn dates into dates
        for i in self.date_fields:
            if postcode.get(i) and not isinstance(postcode[i], datetime):
                postcode[i] = datetime.strptime(postcode[i], "%Y-%m-%dT%H:%M:%S")

        if OAC11_CODE.get(postcode.get("oac11")):
            self.relationships["oac11"] = {
                "code": postcode["oac11"],
                "supergroup": OAC11_CODE.get(postcode["oac11"])[0],
                "group": OAC11_CODE.get(postcode["oac11"])[1],
                "subgroup": OAC11_CODE.get(postcode["oac11"])[2],
            }

        if RU11IND_CODES.get(postcode.get("ru11ind")):
            self.relationships["ru11ind"] = {
                "code": postcode["ru11ind"],
                "description": RU11IND_CODES.get(postcode["ru11ind"]),
            }

        return postcode

    def get_attribute(self, attr):
        """
        Get an attribute or area by the field name

        Adding "_name" to end of the code will return the name rather than code
        """
        if attr in self.attributes:
            return self.attributes.get(attr)

        for a in self.relationships["areas"]:
            if attr.endswith("_name"):
                if a.relationships["areatype"].id == attr[:-5]:
                    return a.attributes.get("name")
            else:
                if a.relationships["areatype"].id == attr:
                    return a.id

    @staticmethod
    def parse_id(postcode):
        """
        standardises a postcode into the correct format
        """

        if postcode is None:
            return None

        # check for blank/empty
        # put in all caps
        postcode = postcode.strip().upper()
        if postcode == '':
            return None

        # replace any non alphanumeric characters
        postcode = re.sub('[^0-9a-zA-Z]+', '', postcode)

        # check for nonstandard codes
        if len(postcode) > 7:
            return postcode

        first_part = postcode[:-3].strip()
        last_part = postcode[-3:].strip()

        # check for incorrect characters
        first_part = list(first_part)
        last_part = list(last_part)
        if last_part[0] == "O":
            last_part[0] = "0"

        return "%s %s" % ("".join(first_part), "".join(last_part))

    def toJSON(self, role="top"):
        json = super().toJSON(role)
        for i in self.date_fields:
            if json[1].get("attributes", {}).get(i) and isinstance(json[1]["attributes"][i], datetime):
                json[1]["attributes"][i] = json[1]["attributes"][i].strftime("%Y-%m-%d")

        # ats = areatypes.Areatypes(self.config, self.es)
        # ats.get()
        # for a in ats.attributes:
        #     json[2].append(a.toJSON()[1])

        return json
