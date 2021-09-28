import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/font.fe_settings")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)
class FontFamily:
      Console           = data["Console"]["FontFamily"]
      Editor            = data["Editor"]["FontFamily"]
class FontSize:
      FontSizeF         = data["Editor"]["FontSize"]
      FontSizeTerminal  = data["Console"]["FontSize"]