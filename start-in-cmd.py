from PTJC import convert

result = ""
print("Welcome to PTJC Terminal!")
while True:
    print("Chose convert type:")
    print("To txt (tt)")
    print("To pkl (tp)")
    print("To JSON (tj)")
    conOption = input("Enter convert type: ")
    if conOption == "tt":
        for count in range(1):
            print("Chose option:")
            print("Convert one pkl file to txt (1)")
            print("Convert folder with pkl files to txt (folder)")
            option = input("Enter option: ")
            if option == "cancel" or option == "back":
                break
            filepath = input("Enter file/folder path: ")
            if filepath == "cancel" or filepath == "back":
                break
            resultFilePath = input("Enter path to output folder: ")
            if resultFilePath == "cancel" or resultFilePath == "back":
                break
            if resultFilePath == "":
                if option == "1":
                    result = convert.toTxt.oneFile(filepath)
                elif option == "folder":
                    result = convert.toTxt.folder(filepath)
            else:
                if option == "1":
                    result = convert.toTxt.oneFile(filepath, resultFilePath)
                elif option == "folder":
                    result = convert.toTxt.folder(filepath, resultFilePath)
            print(result)
            print("")
    elif conOption == "tp":
        for count in range(1):
            print("Chose option:")
            print("Convert one file to .pkl (1)")
            print("Convert folder with files to Pickle format (folder)")
            option = input("Enter option: ")
            if option == "cancel" or option == "back":
                break
            filepath = input("Enter file/folder path: ")
            if filepath == "cancel" or filepath == "back":
                break
            resultFilePath = input("Enter path to output folder: ")
            if resultFilePath == "cancel" or resultFilePath == "back":
                break
            if resultFilePath == "":
                if option == "1":
                    result = convert.toPkl.oneFile(filepath)
                elif option == "folder":
                    result = convert.toPkl.folder(filepath)
            else:
                if option == "1":
                    result = convert.toPkl.oneFile(filepath, resultFilePath)
                elif option == "folder":
                    result = convert.toPkl.folder(filepath, resultFilePath)
            print(result)
            print("")
    elif conOption == "tj":
        for count in range(1):
            print("Chose option:")
            print("Convert one file to JSON format (1)")
            print("Convert folder with files to .json")
            option = input("Enter option: ")
            if option == "cancel" or option == "back":
                break
            filepath = input("Enter file/folder path: ")
            if filepath == "cancel" or filepath == "back":
                break
            resultFilePath = input("Enter path to output folder: ")
            if resultFilePath == "cancel" or resultFilePath == "back":
                break
            if resultFilePath == "":
                if option == "1":
                    result = convert.toJson.oneFile(filepath)
                elif option == "folder":
                    result = convert.toJson.folder(filepath)
            else:
                if option == "1":
                    result = convert.toJson.oneFile(filepath, resultFilePath)
                elif option == "folder":
                    result = convert.toJson.folder(filepath, resultFilePath)
            print(result)
            print("")
    elif conOption == "exit" or conOption == "break":
        break
    else:
        print("Incorrect input")