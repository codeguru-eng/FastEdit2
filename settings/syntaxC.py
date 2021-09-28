import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/editorTheme.fe_settings")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)

DefaultColor      = data["Color"]
DefaultBackground = data["Background"]
FoldArea          = data["FoldArea"]

Keyword           = data["Rules"]["keyword"]
String            = data["Rules"]["string"]
Comment           = data["Rules"]["comment"]
Number            = data["Rules"]["number"]
UnclosedString    = data["Rules"]["unclosedString"]

HtmlString        = data["Rules"]["html.string"]
HtmlTag           = data["Rules"]["html.tag"]
HtmlValue         = data["Rules"]["html.value"]
HtmlAtr           = data["Rules"]["html.attribute"]
HtmlEntity        = data["Rules"]["html.entity"]

cssTag            = data["Rules"]["css.tag"]
cssValue          = data["Rules"]["css.value"]
cssAtr            = data["Rules"]["css.attribute"]
cssPseudoElement  = data["Rules"]["css.pseudoElement"]
cssProperty       = data["Rules"]["css.property"]
cssExtendPseoudoEl= data["Rules"]["css.extendedPseudoElement"]
cssExtendPseoudoCl= data["Rules"]["css.extendedPseudoClass"]
cssPseudoCl       = data["Rules"]["css.pseudoClass"]
cssVar            = data["Rules"]["css.variables"]
cssClassSelector  = data["Rules"]["css.classSelector"]
cssIdSelector     = data["Rules"]["css.idSelector"]
cssMediaRule      = data["Rules"]["css.mediaRule"]

pyFString         = data["Rules"]["python.fString"]
pyClassName       = data["Rules"]["python.className"]
pyFunName         = data["Rules"]["python.methodName"]
pyDec             = data["Rules"]["python.decorator"]

jsonProperty      = data["Rules"]["json.property"]
jsonIri           = data["Rules"]["json.iri"]