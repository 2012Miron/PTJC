# Pkl-to-txt-convertor
Pkl-to-txt-converter is tool for convert data of pkl files, to txt format, and vice versa. You can intagrate him to your projects by
`from PklTxt_converter import convert`.

For start converting, run file start-in-cmd.py, and choose options. Or, run file start-with-gui.py, for run in GUI mode.

After converting, all converted files be in folder "converter-result".

## Integrate details

**First**: if you want to integrate this program in your projects, do next steps:
  1. Move file ptconverter by this path: folder where you install python/Lib/
  2. Run start-with-GUI.py, and make sure everything works.

After line with `from ptconverter import convert` you can use main class -- **convert**. He have two another classes: `toTxt`, and `toPkl`. The first of them convert file Pickle file to .txt, most simple type of text files. The second class, convert .txt files to Pickle type, using string type.

In both of them, there two functions: `folder()`, and `oneFile()`. Their name makes it clear what they do. They have only one argument: path in string type.

The finished code be looking like this:
```
from ptconverter import convert
# some code
def function():
  Path = input("Enter file path: ")
  convert.onePkl.oneFile(Path)
# some code...
```
