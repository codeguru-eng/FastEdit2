import json
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"
path = os.path.join(loc, "autocompletion\\addMore.fe_settings")
with open(path, "r") as file:
	_text = file.read()
data = json.loads(_text)
jsKeywords = [
      "break?2", "case?2", "catch?2", "continue?2", "debugger?2", "default?2", "delete?2", "do?2", "else?2", "finally?2", "for?2", "function?2", 
      "if?2", "in?2", "instanceof?2", "new?2", "return?2", "switch?2", "this?2", "throw?2", "try?2", "typeof?2", "var?2", "void?2", "while?2", 
      "let?2","null?2","true?2","false?2","class?2", "const?2", "enum?2", "export?2", "extends?2", "import?2","super?2","implements?2", 
      "interface?2", "package?2", "private?2", "protected?2", "public?2", "static?2", "yield?2","NaN?2","undefined?2","Infinity?2",
      "byte?2", "char?2", "goto?2", "long?2", "final?2", "float?2", "short?2", "double?2", "native?2", "throws?2", "boolean?2", "abstract?2", 
      "volatile?2", "transient?2", "synchronized?2",
]
JSOthers = data["JavaScript"]["Others"]