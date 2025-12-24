import re

# Depot Mapping 

DEPOT_MAP = {
    "dublin": 7,
    "dublin 1": 7,
    "dublin 2": 7,
    "dublin 3": 8,
    "dublin 4": 4,
    "dublin 5": 8,
    "dublin 6": 4,
    "dublin 7": 7,
    "dublin 8": 2,
    "dublin 9": 10,
    "dublin 10": 9,
    "dublin 11": 10,
    "dublin 12": 2,
    "dublin 13": 8,
    "dublin 14": 4,
    "dublin 15": 9,
    "dublin 16": 2,
    "dublin 18": 4,
    "dublin 20": 9,
    "dublin 22": 3,
    "dublin 24": 3,
    "kildare": 11,
    "laois": 12,
    "kilkenny": 15,
    "wexford": 16,
    "waterford": 17,
    "carlow": 18,
    "wicklow": 19,
    "kerry": 22,
    "limerick": 23,
    "tipperary": 24,
    "clare": 25,
    "cork": 28,
    "galway": 31,
    "mayo": 33,
    "roscommon": 32,
    "longford": 32,
    "sligo": 34,
    "leitrim": 34,
    "donegal": 36,
    "louth": 41,
    "meath": 43,
    "westmeath": 44,
    "offaly": 44,
    "cavan": 45,
    "monaghan": 45,
    "antrim": 79, 
    "tyrone": 80,
    "derry": 87,
    "fermanagh": 88,
    "down": 89
}

# Syntax says that the function takes a string, and returns a string
def _normalise(area: str) -> str:

    area = area.lower().strip()

    # Remove unwanted county text
    area = re.sub(r"^(county|co\.?)\s+", "", area)
    return area


def depot_finder(area: str) -> int:
    normalised = _normalise(area)

    if normalised in DEPOT_MAP:
        return DEPOT_MAP[normalised]
    
    raise ValueError(f"Unknown county: '{area}")


