import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"
path = os.path.join(loc, "settings\\recentfiles.json")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)
RecentFileList = data["list"]