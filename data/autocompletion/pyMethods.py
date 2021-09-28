import json
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"
path = os.path.join(loc, "autocompletion\\addMore.fe_settings")
with open(path, "r") as file:
	_text = file.read()
data = json.loads(_text)
Methods = [
	"__init__?4","__name__","__main__","self?2","exec_?4","parent",
	"connect?4","triggered?4","clicked?4","toggled?4"
]

PyOthers = data["Python"]["Others"]