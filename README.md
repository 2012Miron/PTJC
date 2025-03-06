# PTJC
PTJC (Pickle-Txt-JSON Converter) is tool for convert data of Pickle, txt and JSON files among themselves. You can integrate him to your projects by
`from PTJC import convert`.

For start converting, run file start-in-cmd.py, and choose options. Or, run file start-with-gui.py, for run in GUI mode.

## Integrate details (or short documentation)

**First**: if you want to integrate this program in your projects, install PTJC to your project folder. 

After line with `from ptconverter import convert` you can use main class -- **convert**. He has three another classes: `toTxt`, `toPkl` and `toJson`.
The first of them convert any file to .txt, most simple type of text files.
The second class, convert any files to Pickle type, using string type. And, `toJson` do what you now.

In all of them, there two functions: `folder()`, and `oneFile()`. Their name makes it clear what they do.
They have only two arguments: path in string type, and path for converted files (by default this is folder 'converter-result').
They return the result of converting, and be good if you catch him by writing result in variable.
If converting was a success, result be 'f convert successful', where f is file or folder.

The finished code be looking like this:
``` Python
from PTJC import convert
# some code
def function():
  Path = input("Enter file path: ")
  result = convert.toPkl.oneFile(Path)
  print(result)
# some code...
```
