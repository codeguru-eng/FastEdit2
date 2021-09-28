import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/keybindings.fe_settings")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)
class ShortcutKeys:
      """List of all shortcuts. 
      Note: You will need to restart app to implement new settings.
      """
      NewFile           = data["File"]["NewFile"]
      NewWindow         = data["File"]["NewWindow"]
      OpenFile          = data["File"]["OpenFile"]
      OpenFolder        = data["File"]["OpenFolder"]
      SaveFile          = data["File"]["SaveFile"]
      SaveFileAs        = data["File"]["SaveFileAs"]
      ReloadFile        = data["File"]["ReloadFileFromDisk"]
      RenameFile        = data["File"]["RenameFile"]
      CopyPath          = data["File"]["CopyFilePath"]
      DeleteFile        = data["File"]["DeleteFile"]
      CloseFile         = data["File"]["CloseFile"]
      CloseAll          = data["File"]["CloseAll"]
      CloseFolder       = data["File"]["CloseFolder"]
      CloseWindow       = data["File"]["CloseWindow"]
      
      Find              = data["Find"]["Find"]
      ReplaceOne        = data["Find"]["Replace"]
      ReplaceAll        = data["Find"]["ReplaceAll"]
      
      ToggleFullScreen  = data["View"]["ToggleFullScreen"]
      ToggleFocusMode   = data["View"]["ToggleFocusMode"]
      ZoomIn            = data["View"]["ZoomIn"]
      ZoomOut           = data["View"]["ZoomOut"]
      ToggleStatusBar   = data["View"]["ToggleStatusBar"]
      ToggleEditorArea  = data["View"]["ToggleEditorArea"]
      ToggleExplorer    = data["View"]["ToggleExplorer"]
      ToggleConsoleArea = data["View"]["ToggleConsoleArea"]
      ToggleReadOnly    = data["View"]["ToggleReadOnly"]
      
      Cut               = data["Edit"]["Cut"]
      Copy              = data["Edit"]["Copy"]
      Paste             = data["Edit"]["Paste"]
      Undo              = data["Edit"]["Undo"]
      Redo              = data["Edit"]["Redo"]
      SelectAll         = data["Edit"]["SelectAll"]
      CopyAll           = data["Edit"]["CopyAll"]
      
      GoToLine          = data["Go"]["ToLine"]
      GoToFileFolder    = data["Go"]["ToFile/Folder"]
      
      RunFile           = data["Run"]["Run/Stop"]
      StopRun           = data["Run"]["Stop"]
      ReloadRun         = data["Run"]["Restart"]
      
      Indentation       = data["Indentation"]
      DeleteLine        = data["DeleteLine"]

      About             = data["Help"]["About"]
      AskFromAssistant  = data["Help"]["AskFromAssistant"]