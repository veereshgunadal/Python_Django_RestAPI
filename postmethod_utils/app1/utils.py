import json

def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False


def request_fields_validation(req_data):
    pass