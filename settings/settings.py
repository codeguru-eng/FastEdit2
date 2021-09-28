import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/settings.fe_settings")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)
class Settings:
      TabMovable              = data["TabMovable"]
      TabClosable             = data["TabClosable"]
      TabScrollButtonsVisible = data["TabScrollButtonsVisible"]
      ExplorerAnimated        = data["ExplorerAnimated"]
      TabIconWidth            = data["TabIconWidth"]
      TabIconHeight           = data["TabIconHeight"]
      ExplorerBarMinWidth     = data["ExplorerBarMinWidth"]
      ExplorerBarMaxWidth     = data["ExplorerBarMaxWidth"]
      if data["CloseFilesOnOpeningFolder"] is True:
          CloseFilesOnOpeningFolder = True
      if data["CloseFilesOnOpeningFolder"] is False:
          CloseFilesOnOpeningFolder = False