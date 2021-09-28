import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "fileData/folderPath.json")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)

Folder_Path = data["path"]
print(f"Folder: {Folder_Path}")