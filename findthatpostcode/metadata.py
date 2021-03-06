import json
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "areatypes.json")) as a:
    AREA_TYPES = json.load(a)
    for k in AREA_TYPES:
        AREA_TYPES[k]["countries"] = list(
            set([e[0] for e in AREA_TYPES[k]["entities"]]))
    AREA_THEMES = list(set([a["theme"] for a in AREA_TYPES.values()]))
    ENTITIES = {
        e: k
        for k, v in AREA_TYPES.items()
        for e in v["entities"]
    }

# AREA_TYPES = [
#     ("oa11", ["E00", "W00", "S00", "N00"], "Output area", "2011 Census Output Area (OA)/ Small Area (SA)", "The 2011 Census OAs in GB and SAs in Northern Ireland were based on 2001 Census OAs, and they form the building bricks for defining higher level geographies. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference."),
#     ("cty", ["E10", "E11", "E42"], "County", "County", "The current county to which the postcode has been assigned. Pseudo codes are included for English UAs, Wales, Scotland, Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("laua", ["E06", "E07", "E08", "E09", "W06", "S12", "N09"], "Local Authority", "Local Authority District (LAD)/unitary authority (UA)/metropolitan district (MD)/London borough (LB)/ council area (CA)/district council area (DCA)", "The current district/UA to which the postcode has been assigned. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("ward", ["E05", "W05", "S13", "N08"], "Ward", "(Electoral) ward/division", "The current administrative/electoral area to which the postcode has been assigned. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("hlthau", ["S18"], "Strategic Health Authority", "Former Strategic Health Authority (SHA)/ Local Health Board (LHB)/ Health Board (HB)/ Health Authority (HA)/ Health & Social Care Board (HSCB)", "The health area code for the postcode. SHAs were abolished in England in 2013 but the codes remain as a 'frozen' geography. The field will otherwise be blank for postcodes with no OA code."),
#     ("hro", ["S19"], "Pan SHA", "Pan SHA", "The Pan SHA responsible for the associated strategic health authority for each postcode in England. Pseudo codes are included for Wales, Scotland, Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("ctry", ["E92", "W92", "S92", "N92", "L93", "M83", ], "Country", "Country", "The code for the appropriate country (i.e. one of the four constituent countries of the UK or Crown dependencies - the Channel Islands or the Isle of Man) to which each postcode is assigned."),
#     ("rgn", ["E12"], "Region", "Region (former GOR)", "The region code for each postcode. Pseudo codes are included for Wales, Scotland, Northern Ireland, Channel Island and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("pcon", ["E14", "W07", "S14", "N06"], "Westminster parliamentary constituency", "Westminster parliamentary constituency", "The Westminster parliamentary constituency code for each postcode. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("eer", ["E15", "W08", "S15", "N07"], "European Electoral Region", "European Electoral Region (EER)", "The European Electoral Region code for each postcode. A pseudo code is included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code"),
#     ("teclec", ["E24"], "Local Learning and Skills Council", "Local Learning and Skills Council (LLSC)/ Dept. of Children, Education, Lifelong Learning and Skills (DCELLS)/Enterprise Region (ER)", "The LLSC (England), DCELLS (Wales) or ER (Scotland) code for each postcode. Pseudo codes are included for Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("ttwa", ["E30", "W22", "S22", "N12", "K01"], "Travel to Work Area", "Travel to Work Area (TTWA)", "The TTWA code for the postcode. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("pct", ["E16"], "Primary Care Trust", "Primary Care Trust (PCT)/ Care Trust/Care Trust Plus (CT)/ Local Health Board (LHB)/Community Health Partnership (CHP)/ Local Commissioning Group (LCG)/Primary Healthcare Directorate (PHD)", "The code for the PCT/CT areas in England, LHBs in Wales, CHPs in Scotland, LCG in Northern Ireland and PHD in the Isle of Man. A pseudo code is included for Channel Islands. The field will otherwise be blank for postcodes with no OA code."),
#     ("nuts", ["S31"], "LAU2 area", "LAU2 area", "The national LAU2-equivalent code for each postcode. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference"),
#     ("park", ["E26", "W18", "W31", "S21"], "National park", "National park", "The National parks cover parts of England, Wales and Scotland. Pseudo codes are included for Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference."),
#     ("lsoa11", ["E01", "W01", "S01", "N00"], "Lower Super Output Area", "2011 Census Lower Layer Super Output Area (LSOA)/ Data Zone (DZ)/ SOA", "The 2011 Census LSOA code for England and Wales, SOA code for Northern Ireland and DZ code for Scotland. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code. N.B. NI SOAs remain unchanged from 2001."),
#     ("msoa11", ["E02", "W02", "W02"], "Middle Super Output Area", "Middle Layer Super Output Area (MSOA)/Intermediate Zone (IZ)", "The 2011 Census MSOA code for England and Wales and IZ code for Scotland. Pseudo codes are included for Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("wz11", ["E33", "W35", "S34", "N19"], "Workplace Zone", "2011 Census Workplace Zone", "The UK WZ code. Pseudo codes are included for Channel Islands and Isle of Man. The field will be blank for UK postcodes with no grid reference."),
#     ("ccg", ["E38"], "Clinical Commissioning Group", "Clinical Commissioning Group (CCG)/Local Health Board (LHB)/Community Health Partnership (CHP)/ Local Commissioning Group (LCG)/Primary Healthcare Directorate (PHD)", "The code for the CCG areas in England, LHBs in Wales, CHPs in Scotland, LCG in Northern Ireland and PHD in the Isle of Man. A pseudo code is included for Channel Islands. The field will be blank for postcodes in England or Wales with no OA code."),
#     ("bua11", ["E34", "W37", "K05"], "Built-up Area", "Built-up Area (BUA)", "The code for the BUAs in England and Wales. Pseudo codes are included for those OAs not classed as 'built-up' and cross-border codes are included for areas straddling the English/Welsh border. Pseudo codes are also included for Scotland, Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("buasd11", ["E35", "W38", "K06"], "Built-up Area Sub-division (BUASD)", "Built-up Area Sub-division", "The code for the BUASDs in England and Wales. Pseudo codes are included for those OAs not classed as 'built-up' and cross-border codes are included for areas straddling the English/Welsh border. Pseudo codes are also included for Scotland, Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code"),
#     ("ru11ind", [], "Rural/Urban Classification", "2011 Census rural-urban classification", "The 2011 Census rural-urban classification of OAs for England and Wales, Scotland and Northern Ireland. A pseudo code is included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
#     ("oac11", [], "Output Area Classification", "2011 Census Output Area classification (OAC)", "The 2011 Census OAC code for each postcode in the UK. A pseudo code is included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code"),
#     ("lep", ["E37"], "Local Enterprise Partnership", "Local Enterprise Partnership (LEP)", "The primary LEP code for each English postcode. Pseudo codes are included for the rest of the UK. The field will otherwise be blank for postcodes with no OA code."),
#     ("pfa", ["E23", "W15", "S23", "N23"], "Police Force Area", "Police Force Area (PFA)", "The PFA code for each postcode. A single PFA covers each of Scotland and Northern Ireland (not coded). A pseudo code is included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no OA code."),
# ]

KEY_AREA_TYPES = [
    ("Key", ["ctry", "rgn", "cty", "laua", "ward", "lsoa11", "pcon"]),
    ("Secondary", ["ttwa", "pfa", "lep", "msoa11", "oa11", "npark"]),
    ("Health", ["ccg", "nhser", "hb", "lhb"]),
    ("Other", ["eer", "bua11", "buasd11", "wz11", "teclec"]),
]

OTHER_CODES = {
    "osgrdind": [
        "",  # no code 0
        "within the building of the matched address closest to the postcode mean",
        "as for status value 1, except by visual inspection of Landline maps (Scotland only)",
        "approximate to within 50 metres",
        "postcode unit mean (mean of matched addresses with the same postcode, but not snapped to a building)",
        "imputed by ONS, by reference to surrounding postcode grid references",
        "postcode sector mean, (mainly PO Boxes)",
        "",  # code 7 missing
        "postcode terminated prior to Gridlink(R) initiative, last known ONS postcode grid reference",
        "no grid reference available",
    ],
    "usertype": ["Small user", "Large user"],
    "imd": {
        "E92000001": 32844,
        "W92000004": 1909,
        "S92000003": 6976,
        "N92000002": None,
        "L93000001": None,
        "M83000003": None
    }
}


DEFAULT_UPLOAD_FIELDS = ["latlng", "laua", "laua_name", "rgn", "rgn_name"]
BASIC_UPLOAD_FIELDS = [
    ("latlng", "Latitude / Longitude", False),
    ("estnrth", "OS Easting / Northing", False),
    ("pcds", "Standardised postcode", False),
    ("oac11", "2011 Output Area Classification (OAC)", True),
    ("ru11ind", "2011 Census rural-urban classification", True),
]
STATS_FIELDS = [
    ("imd2019_rank", "Index of multiple deprivation (2019) rank", False, "stats.imd2019.imd_rank"),
    ("imd2019_decile", "Index of multiple deprivation (2019) decile", False, "stats.imd2019.imd_decile"),
    ("imd2015_rank", "Index of multiple deprivation (2015) rank", False, "stats.imd2015.imd_rank"),
    ("imd2015_decile", "Index of multiple deprivation (2015) decile", False, "stats.imd2015.imd_decile"),
    # ("popn", "Total population (2015)", False, "stats.population2015.population_total"),
]


NAME_FILES = [
    {"file": "Documents/2011 Census Output Area Classification Names and Codes UK.csv", "type_field": "oac11", "code_field": "OAC11", "name_field": "Subgroup", "welsh_name_field": None},
    {"file": "Documents/BUASD_names and codes UK", "type_field": "buasd11", "code_field": "BUASD13CD", "name_field": "BUASD13NM", "welsh_name_field": None},
    {"file": "Documents/BUA_names and codes UK", "type_field": "bua11", "code_field": "BUA13CD", "name_field": "BUA13NM", "welsh_name_field": None},
    {"file": "Documents/CCG names and codes UK", "type_field": "ccg", "code_field": "CCG18CD", "name_field": "CCG18NM", "welsh_name_field": "CCG18NMW"},
    {"file": "Documents/Country names and codes UK", "type_field": "ctry", "code_field": "CTRY12CD", "name_field": "CTRY12NM", "welsh_name_field": "CTRY12NMW"},
    {"file": "Documents/County names and codes UK", "type_field": "cty", "code_field": "CTY10CD", "name_field": "CTY10NM", "welsh_name_field": None},
    {"file": "Documents/EER names and codes UK", "type_field": "eer", "code_field": "EER10CD", "name_field": "EER10NM", "welsh_name_field": None},
    {"file": "Documents/HLTHAU names and codes UK", "type_field": "hlthau", "code_field": "HLTHAUCD", "name_field": "HLTHAUNM", "welsh_name_field": "HLTHAUNMW"},
    {"file": "Documents/LAU2 names and codes UK", "type_field": "nuts", "code_field": "LAU216CD", "name_field": "LAU216NM", "welsh_name_field": None},
    {"file": "Documents/LA_UA names and codes UK", "type_field": "laua", "code_field": "LAD16CD", "name_field": "LAD16NM", "welsh_name_field": None},
    {"file": "Documents/LEP names and codes EN", "type_field": "lep", "code_field": "LEP13CD1", "name_field": "LEP13NM1", "welsh_name_field": None},
    {"file": "Documents/LSOA (2011) names and codes UK", "type_field": "lsoa11", "code_field": "LSOA11CD", "name_field": "LSOA11NM", "welsh_name_field": None},
    {"file": "Documents/MSOA (2011) names and codes UK", "type_field": "msoa11", "code_field": "MSOA11CD", "name_field": "MSOA11NM", "welsh_name_field": None},
    {"file": "Documents/National Park names and codes GB", "type_field": "park", "code_field": "NPARK16CD", "name_field": "NPARK16NM", "welsh_name_field": None},
    {"file": "Documents/Pan SHA names and codes EN", "type_field": "hro", "code_field": "PSHA10CD", "name_field": "PSHA10NM", "welsh_name_field": None},
    {"file": "Documents/PCT names and codes UK", "type_field": "pct", "code_field": "PCTCD", "name_field": "PCTNM", "welsh_name_field": "PCTNMW"},
    {"file": "Documents/PFA names and codes GB", "type_field": "pfa", "code_field": "PFA15CD", "name_field": "PFA15NM", "welsh_name_field": None},
    {"file": "Documents/Region names and codes EN", "type_field": "rgn", "code_field": "GOR10CD", "name_field": "GOR10NM", "welsh_name_field": "GOR10NMW"},
    {"file": "Documents/Rural Urban (2011) Indicator names and codes GB", "type_field": "ru11ind", "code_field": "RU11IND", "name_field": "RU11NM", "welsh_name_field": None},
    {"file": "Documents/TECLEC names and codes UK", "type_field": "teclec", "code_field": "TECLECCD", "name_field": "TECLECNM", "welsh_name_field": None},
    {"file": "Documents/TTWA names and codes UK", "type_field": "ttwa", "code_field": "TTWA11CD", "name_field": "TTWA11NM", "welsh_name_field": None},
    {"file": "Documents/Westminster Parliamentary Constituency names and codes UK", "type_field": "pcon", "code_field": "PCON14CD", "name_field": "PCON14NM", "welsh_name_field": None},
    {"file": "Documents/Ward names and codes UK", "type_field": "ward", "code_field": "WD16CD", "name_field": "WD16NM", "welsh_name_field": None},
    # {"file": "Documents/LAU216_LAU116_NUTS315_NUTS215_NUTS115_UK_LU.csv", "type_field": "", "name_field": "", "welsh_name_field": None},
]

# "Supergroup", "Group", "Subgroup"],
OAC11_CODE = {
    "1A1": ["Rural residents", "Farming communities", "Rural workers and families"],
    "1A2": ["Rural residents", "Farming communities", "Established farming communities"],
    "1A3": ["Rural residents", "Farming communities", "Agricultural communities"],
    "1A4": ["Rural residents", "Farming communities", "Older farming communities"],
    "1B1": ["Rural residents", "Rural tenants", "Rural life"],
    "1B2": ["Rural residents", "Rural tenants", "Rural white-collar workers"],
    "1B3": ["Rural residents", "Rural tenants", "Ageing rural flat tenants"],
    "1C1": ["Rural residents", "Ageing rural dwellers", "Rural employment and retirees"],
    "1C2": ["Rural residents", "Ageing rural dwellers", "Renting rural retirement"],
    "1C3": ["Rural residents", "Ageing rural dwellers", "Detached rural retirement"],
    "2A1": ["Cosmopolitans", "Students around campus", "Student communal living"],
    "2A2": ["Cosmopolitans", "Students around campus", "Student digs"],
    "2A3": ["Cosmopolitans", "Students around campus", "Students and professionals"],
    "2B1": ["Cosmopolitans", "Inner city students", "Students and commuters"],
    "2B2": ["Cosmopolitans", "Inner city students", "Multicultural student neighbourhood"],
    "2C1": ["Cosmopolitans", "Comfortable cosmopolitan", "Migrant families"],
    "2C2": ["Cosmopolitans", "Comfortable cosmopolitan", "Migrant commuters"],
    "2C3": ["Cosmopolitans", "Comfortable cosmopolitan", "Professional service cosmopolitans"],
    "2D1": ["Cosmopolitans", "Aspiring and affluent", "Urban cultural mix"],
    "2D2": ["Cosmopolitans", "Aspiring and affluent", "Highly-qualified quaternary workers"],
    "2D3": ["Cosmopolitans", "Aspiring and affluent", "EU white-collar workers"],
    "3A1": ["Ethnicity central", "Ethnic family life", "Established renting families"],
    "3A2": ["Ethnicity central", "Ethnic family life", "Young families and students"],
    "3B1": ["Ethnicity central", "Endeavouring ethnic mix", "Striving service workers"],
    "3B2": ["Ethnicity central", "Endeavouring ethnic mix", "Bangladeshi mixed employment"],
    "3B3": ["Ethnicity central", "Endeavouring ethnic mix", "Multi-ethnic professional service workers"],
    "3C1": ["Ethnicity central", "Ethnic dynamics", "Constrained neighbourhoods"],
    "3C2": ["Ethnicity central", "Ethnic dynamics", "Constrained commuters"],
    "3D1": ["Ethnicity central", "Aspirational techies", "New EU tech workers"],
    "3D2": ["Ethnicity central", "Aspirational techies", "Established tech workers"],
    "3D3": ["Ethnicity central", "Aspirational techies", "Old EU tech workers"],
    "4A1": ["Multicultural metropolitans", "Rented family living", "Social renting young families"],
    "4A2": ["Multicultural metropolitans", "Rented family living", "Private renting new arrivals"],
    "4A3": ["Multicultural metropolitans", "Rented family living", "Commuters with young families"],
    "4B1": ["Multicultural metropolitans", "Challenged Asian terraces", "Asian terraces and flats"],
    "4B2": ["Multicultural metropolitans", "Challenged Asian terraces", "Pakistani communities"],
    "4C1": ["Multicultural metropolitans", "Asian traits", "Achieving minorities"],
    "4C2": ["Multicultural metropolitans", "Asian traits", "Multicultural new arrivals"],
    "4C3": ["Multicultural metropolitans", "Asian traits", "Inner city ethnic mix"],
    "5A1": ["Urbanites", "Urban professionals and families", "White professionals"],
    "5A2": ["Urbanites", "Urban professionals and families", "Multi-ethnic professionals with families"],
    "5A3": ["Urbanites", "Urban professionals and families", "Families in terraces and flats"],
    "5B1": ["Urbanites", "Ageing urban living", "Delayed retirement"],
    "5B2": ["Urbanites", "Ageing urban living", "Communal retirement"],
    "5B3": ["Urbanites", "Ageing urban living", "Self-sufficient retirement"],
    "6A1": ["Suburbanites", "Suburban achievers", "Indian tech achievers"],
    "6A2": ["Suburbanites", "Suburban achievers", "Comfortable suburbia"],
    "6A3": ["Suburbanites", "Suburban achievers", "Detached retirement living"],
    "6A4": ["Suburbanites", "Suburban achievers", "Ageing in suburbia"],
    "6B1": ["Suburbanites", "Semi-detached suburbia", "Multi-ethnic suburbia"],
    "6B2": ["Suburbanites", "Semi-detached suburbia", "White suburban communities"],
    "6B3": ["Suburbanites", "Semi-detached suburbia", "Semi-detached ageing"],
    "6B4": ["Suburbanites", "Semi-detached suburbia", "Older workers and retirement"],
    "7A1": ["Constrained city dwellers", "Challenged diversity", "Transitional Eastern European neighbourhood"],
    "7A2": ["Constrained city dwellers", "Challenged diversity", "Hampered aspiration"],
    "7A3": ["Constrained city dwellers", "Challenged diversity", "Multi-ethnic hardship"],
    "7B1": ["Constrained city dwellers", "Constrained flat dwellers", "Eastern European communities"],
    "7B2": ["Constrained city dwellers", "Constrained flat dwellers", "Deprived neighbourhoods"],
    "7B3": ["Constrained city dwellers", "Constrained flat dwellers", "Endeavouring flat dwellers"],
    "7C1": ["Constrained city dwellers", "White communities", "Challenged transitionaries"],
    "7C2": ["Constrained city dwellers", "White communities", "Constrained young families"],
    "7C3": ["Constrained city dwellers", "White communities", "Outer city hardship"],
    "7D1": ["Constrained city dwellers", "Ageing city dwellers", "Ageing communities and families"],
    "7D2": ["Constrained city dwellers", "Ageing city dwellers", "Retired independent city dwellers"],
    "7D3": ["Constrained city dwellers", "Ageing city dwellers", "Retired communal city dwellers"],
    "7D4": ["Constrained city dwellers", "Ageing city dwellers", "Retired city hardship"],
    "8A1": ["Hard-pressed living", "Industrious communities", "Industrious transitions"],
    "8A2": ["Hard-pressed living", "Industrious communities", "Industrious hardship"],
    "8B1": ["Hard-pressed living", "Challenged terraced workers", "Deprived blue-collar terraces"],
    "8B2": ["Hard-pressed living", "Challenged terraced workers", "Hard pressed rented terraces"],
    "8C1": ["Hard-pressed living", "Hard pressed ageing workers", "Ageing industrious workers"],
    "8C2": ["Hard-pressed living", "Hard pressed ageing workers", "Ageing rural industry workers"],
    "8C3": ["Hard-pressed living", "Hard pressed ageing workers", "Renting hard-pressed workers"],
    "8D1": ["Hard-pressed living", "Migration and churn", "Young hard-pressed families"],
    "8D2": ["Hard-pressed living", "Migration and churn", "Hard-pressed ethnic mix"],
    "8D3": ["Hard-pressed living", "Migration and churn", "Hard-Pressed European Settlers"],
    "9Z9": ["(pseudo) CI, IoM", "(pseudo) CI, IoM", "(pseudo) CI, IoM"],
}

RU11IND_CODES = {
    "A1": "Urban major conurbation",
    "B1": "Urban minor conurbation",
    "C1": "Urban city and town",
    "C2": "Urban city and town in a sparse setting",
    "D1": "Rural town and fringe",
    "D2": "Rural town and fringe in a sparse setting",
    "E1": "Rural village",
    "E2": "Rural village in a sparse setting",
    "F1": "Rural hamlet and isolated dwellings",
    "F2": "Rural hamlet and isolated dwellings in a sparse setting",
    "1": "Large Urban Area",
    "2": "Other Urban Area",
    "3": "Accessible Small Town",
    "4": "Remote Small Town",
    "5": "Very Remote Small Town",
    "6": "Accessible Rural",
    "7": "Remote Rural",
    "8": "Very Remote Rural",
}
