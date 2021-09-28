import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
loc = loc.replace("\\","/")
path = os.path.join(loc, "settings/recentFolders.json")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)
RecentFolderList = data