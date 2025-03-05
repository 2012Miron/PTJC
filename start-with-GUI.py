import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from PTJC import convert

def convertAndPrint():
    if convertType.get() == "TT":
        if Option.get() == "file":
            if outputPath.get() == "":
                result = convert.toTxt.oneFile(path.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toTxt.oneFile(path.get(), outputPath.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
        elif Option.get() == "folder":
            if outputPath.get() == "":
                result = convert.toTxt.folder(path.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toTxt.folder(path.get(), outputPath.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
    elif convertType.get() == "TP":
        if Option.get() == "file":
            if outputPath.get() == "":
                result = convert.toPkl.oneFile(path.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toPkl.oneFile(path.get(), outputPath.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
        elif Option.get == "folder":
            if outputPath.get() == "":
                result = convert.toPkl.folder(path.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toPkl.folder(path.get(), outputPath.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
    elif convertType.get() == "TJ":
        if Option.get() == "file":
            if outputPath.get() == "":
                result = convert.toJson.oneFile(path.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toJson.oneFile(path.get(), outputPath.get())
                if result == "file convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
        elif Option.get == "folder":
            if outputPath.get() == "":
                result = convert.toJson.folder(path.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
            else:
                result = convert.toJson.folder(path.get(), outputPath.get())
                if result == "folder convert successful":
                    showinfo(title="PTJ Converter", message=result)
                else:
                    showerror(title="PTJ Converter", message=result)
    else:
        return

window = tk.Tk()
window.title("PTJ Converter")

# Variables
convertType = tk.StringVar()
Option = tk.StringVar()
path = tk.StringVar()
outputPath = tk.StringVar()

# Frames:
ConvertOption_frm = ttk.Frame(window)
ConvertOption_frm.pack()

Option_frm = ttk.Frame(window)
Option_frm.pack()

Path_frm = ttk.Frame(window)
Path_frm.pack()

# ConvertOption_frm widgets
ConvertOption_lbl = ttk.Label(ConvertOption_frm, text="Convert type:")
ConvertOption_lbl.pack()

TTConvert_rbt = ttk.Radiobutton(ConvertOption_frm, text="to Txt", variable=convertType, value="TT")
TTConvert_rbt.pack()

TPConvert_rbt = ttk.Radiobutton(ConvertOption_frm, text="to Pickle", variable=convertType, value="TP")
TPConvert_rbt.pack()

TJConvert_rbt = ttk.Radiobutton(ConvertOption_frm, text="to JSON", variable=convertType, value="TJ")
TJConvert_rbt.pack()

# Option_frm widgets
WhatConvert_lbl = ttk.Label(Option_frm, text="What convert:")
WhatConvert_lbl.pack()

File_rbt = ttk.Radiobutton(Option_frm, text="One file", variable=Option, value="file")
File_rbt.pack()

Folder_rbt = ttk.Radiobutton(Option_frm, text="Folder", variable=Option, value="folder")
Folder_rbt.pack()

# Path widgets
Path_lbl = ttk.Label(Path_frm, text="File/folder path:")
Path_lbl.pack()

Path_entr = ttk.Entry(Path_frm, textvariable=path, width=40)
Path_entr.pack()

OutputPath_lbl = ttk.Label(Path_frm, text="Output folder path:")
OutputPath_lbl.pack()

OutputPath_entr = ttk.Entry(Path_frm, textvariable=outputPath, width=40)
OutputPath_entr.pack()

# Start button
Start_btn = ttk.Button(window, text="Start converting", command=convertAndPrint)
Start_btn.pack()

window.mainloop()