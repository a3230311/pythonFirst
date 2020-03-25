import json
import io

with open('usr.json', 'r') as f:
    user_json = json.load(f)
    print(user_json)
    print(len(user_json))

    for key in user_json.keys():
        print(key, user_json[key])
