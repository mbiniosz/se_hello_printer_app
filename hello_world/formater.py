
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(mgs, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(mgs, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(mgs, imie)
    elif format == JSON:
        result = format_to_json(mgs, imie)
    return result


def format_to_json(msg, imie):
    return ('{ "imie" : "' + imie + '" , "mgs":' +
            mgs + '"}')


def plain_text(mgs, imie):
    return imie + ' ' + mgs

def plain_text_upper_case(msg, imie):
    return plain_text(mgs.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(mgs.lower(), imie.lower())
