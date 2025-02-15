import json

def is_json(req):
    try:
        json.loads(req)
        return True
    except:
        return False