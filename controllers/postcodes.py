from datetime import datetime
import bottle
import re

from metadata import AREA_TYPES, KEY_AREA_TYPES, OTHER_CODES

from .controller import *
import controllers.areas

class Postcode(Controller):

    es_type = 'postcode'
    url_slug = 'postcodes'
    date_fields = ["dointr", "doterm"]
    not_area_fields = ["osgrdind", "usertype"]

    def __init__(self, config):
        super().__init__(config)

    def get_by_id(self, id):
        id = self.parse_id(id)
        if id:
            result = self.config.get("es").get(index=self.config.get("es_index"), doc_type=self.es_type, id=id, ignore=[404])
            if result["found"]:
                self.set_from_data(result)

    def process_attributes(self, postcode, get_areas=True):
        self.relationships["areas"] = []
        for i in list(postcode.keys()):
            if postcode[i] and i not in self.not_area_fields:
                area  = controllers.areas.Area(self.config)
                area.get_by_id(postcode[i], examples_count=0)
                if area.found:
                    del postcode[i]
                    self.relationships["areas"].append(area)

        # turn dates into dates
        for i in self.date_fields:
            if postcode[i] and not isinstance(postcode[i], datetime):
                postcode[i] = datetime.strptime(postcode[i], "%Y-%m-%dT%H:%M:%S")

        return postcode

    def parse_id(self, postcode):
        """
        standardises a postcode into the correct format
        """

        if postcode is None:
            return None

        # check for blank/empty
        # put in all caps
        postcode = postcode.strip().upper()
        if postcode=='':
            return None

        # replace any non alphanumeric characters
        postcode = re.sub('[^0-9a-zA-Z]+', '', postcode)

        # check for nonstandard codes
        if len(postcode)>7:
            return postcode

        first_part = postcode[:-3].strip()
        last_part = postcode[-3:].strip()

        # check for incorrect characters
        first_part = list(first_part)
        last_part = list(last_part)
        if last_part[0]=="O":
            last_part[0] = "0"

        return "%s %s" % ("".join(first_part), "".join(last_part) )

    def toJSON(self, role="top"):
        json = super().toJSON(role)
        for i in self.date_fields:
            if json[1].get("attributes", {}).get(i) and isinstance(json[1]["attributes"][i], datetime):
                json[1]["attributes"][i] = json[1]["attributes"][i].strftime("%Y%m")

        return json

    def return_result(self, filetype):
        json = self.toJSON()
        if not self.found:
            return bottle.abort(404)

        if filetype=="html":
            return bottle.template(self.template_name(),
                result=self.data,
                postcode=self.id,
                point=None,
                area_types=AREA_TYPES,
                key_area_types=KEY_AREA_TYPES,
                other_codes=OTHER_CODES
                )
        elif filetype=="json":
            return {
                "data": json[1],
                "included": json[2],
                "links": {
                    "self": self.url(),
                    "html": self.url("html")
                }
            }