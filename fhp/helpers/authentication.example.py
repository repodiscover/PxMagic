from fhp.helpers.json_finder import _parse_json, _dump_json
import os

# Rename this file to authentication.py

CONSUMER_KEY = "__your_consumer_key__"
CONSUMER_SECRET = "__your_consumer_secret__"
VERIFY_URL = "__used_for_client_apps_optional__"

def root_dir():
    return os.path.join(os.path.dirname(__file__), "..")

def get_consumer_key():
    """ For more info on the API visit developer.500px.com.
    If you are logged in to your 500px account you can 
    go to: http://500px.com/settings/applications to retrieve
    your key.
    """
    return CONSUMER_KEY

def get_consumer_secret():
    """ For more info on the API visit developer.500px.com.
    If you are logged in to your 500px account you can 
    go to: http://500px.com/settings/applications to retrieve
    your key.
    """
    return CONSUMER_SECRET

def get_verify_url():
    """ Used for non-server applications """
    return VERIFY_URL
