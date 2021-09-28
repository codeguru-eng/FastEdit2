import json
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"
path = os.path.join(loc, "autocompletion\\addMore.fe_settings")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)
Values = data["JSON"]["Values"]
Others = [
      "null","rgb","hsl"
]