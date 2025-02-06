# PTJC
PTJC (Pickle-Txt-JSON Converter) is tool for convert data of Pickle, txt and JSON files among themselves. You can intagrate him to your projects by
`from PTJC import convert`.

For start converting, run file start-in-cmd.py, and choose options. Or, run file start-with-gui.py, for run in GUI mode.

After converting, all converted files be in folder "converter-result".

## Integrate details

**First**: if you want to integrate this program in your projects, do next steps:
  1. Install PTJC from PyPI, using website or by `pip install PTJC`

After line with `from ptconverter import convert` you can use main class -- **convert**. He have three another classes: `toTxt`, `toPkl` and `toJson`. The first of them convert any file to .txt, most simple type of text files. The second class, convert any files to Pickle type, using string type. And, `toJson` do what you now.

In all of them, there two functions: `folder()`, and `oneFile()`. Their name makes it clear what they do. They have only one argument: path in string type. They returns the result of converting, and be good if you catch him by writing result in variable.

The finished code be looking like this:
```
from PTJC import convert
# some code
def function():
  Path = input("Enter file path: ")
  result = convert.toPkl.oneFile(Path)
  print(result)
# some code...
```
