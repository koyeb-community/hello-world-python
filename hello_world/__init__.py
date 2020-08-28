import requests

def handler(event, context):
    print("Got data", event)
    print("Got context", context)
    print("Got context event", context.event)
    return {"response": "ok"}
