import json
import os
import shutil
import sys


config_example_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs", "config.json")
user_config_loc = os.path.join(os.path.expanduser("~"), ".recordurbate", "config.json")


# opens file, returns json dict, returns None if error
def load_config():
    try:
        os.makedirs(os.path.dirname(user_config_loc), exist_ok=True)
        if not os.path.exists(user_config_loc):
            shutil.copyfile(config_example_loc, user_config_loc)
        with open(user_config_loc, "r") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        sys.exit(-1)


# opens file, writes config, returns True on success, False on error
def save_config(config):
    try:
        os.makedirs(os.path.dirname(user_config_loc), exist_ok=True)
        with open(user_config_loc, "w+") as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(e)
        sys.exit(-1)


# look for steamer in config, return True and idx, or False and None
def find_in_config(username, config):
    try:
        return True, config["streamers"].index(username)
    except ValueError:
        return False, None
