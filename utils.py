import re


def format_json(json):
    json = re.sub(r'": \[\s+', '": [', json)
    json = re.sub(r'",\s+', '", ', json)
    json = re.sub(r'"\s+\]', '"]', json)
    return json
