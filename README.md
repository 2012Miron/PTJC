# PTJC
PTJC (Pickle-Txt-JSON Converter) is tool for convert data of Pickle, txt and JSON files among themselves. You can intagrate him to your projects by
`from PTJC import convert`.

For start converting, run file start-in-cmd.py, and choose options. Or, run file start-with-gui.py, for run in GUI mode.

## Integrate details (or short documentation)

**First**: if you want to integrate this program in your projects, install PTJC from [PyPI](https://pypi.org), or by pip:
```
PS C:/Users/User: pip install PTJC
```

After line with `from ptconverter import convert` you can use main class -- **convert**. He have three another classes: `toTxt`, `toPkl` and `toJson`. The first of them convert any file to .txt, most simple type of text files. The second class, convert any files to Pickle type, using string type. And, `toJson` do what you now.

In all of them, there two functions: `folder()`, and `oneFile()`. Their name makes it clear what they do. They have only two arguments: path in string type, and path for converted files (by default this is folder 'converter-result'). They returns the result of converting, and be good if you catch him by writing result in variable. If converting was a success, result be 'f convert successfull', where f is file or folder.

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
