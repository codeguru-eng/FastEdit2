import json
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"
path = os.path.join(loc, "autocompletion\\addMore.fe_settings")
with open(path, "r") as file:
	_text = file.read()
data = json.loads(_text)
HTMLOtherList = [
	"class","onclick","onmousedown","onmouseup","stylesheet",
	"&lt;",
	# Other english words
	"do","you","is","was","will","have","had","shall","should","editor","editing","document","website",
	"microsoft","observation","experience","browser","text","javascript"
]
HTMLOthers = data["HTML"]["Others"]