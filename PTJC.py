"""
PTJC (Pickle-Text-JSON Converter) is a tool for convert pickle, txt and json files, to him format
(like json to pkl).

You can integrate him in your projects for make configs, and easy convert him to your favorite file format, using `from PTJC import convert`.

Project: https://github.com/2012Miron/PTJC

Short documentation: https://github.com/2012Miron/PTJC#integrate-details-or-short-documentation
"""

import json
import pickle
import os
import glob

class convert:
    class toTxt:
        """
        Convert Pickle files to Text files.
        """
        def oneFile(filePath: str, resultPath: str = 'converter-result'):
            """
            Convert one file to text file
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            try:
                if filePath.find(":") == -1:
                    if filePath.find(".pkl") != -1:
                        with open(filePath, 'rb') as file1:
                            file1data = pickle.load(file1)
                    elif filePath.find(".json") != -1:
                        with open(filePath, 'r') as file1:
                            file1data = json.load(file1)
                    else:
                        with open(filePath, 'r') as file1:
                            file1data = file1.read()
                    if not os.path.exists(resultPath):
                        os.mkdir(resultPath)
                    filePath = filePath[:filePath.find('.')]
                    resultPath = resultPath + f'/{filePath}.txt'
                    with open(resultPath, 'w') as file1:
                        file1.write(file1data)
                    return "file convert successful"
                elif filePath.find(":") != -1:
                    with open(filePath, 'rb') as file1:
                        file1data = pickle.load(file1)
                    if not os.path.exists(resultPath):
                        os.mkdir(resultPath)
                    filePath = os.path.basename(filePath)
                    resultPath = resultPath + f'/{filePath.replace('.*', '.txt')}'
                    with open(resultPath, 'w') as file1:
                        file1.write(file1data)
                    return "file convert successful"
            except FileNotFoundError as err:
                return f"File not found error.\nError: {err}"
            except TypeError as err:
                return f"Type error. Maybe, file contains a emojis.\nError: {err}"
            except Exception as err:
                return f"Unknown Error: {err}"

        def folder(folderPath: str, resultPath: str = 'converter-result'):
            """
            Convert folder with files to .txt
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            try:
                if not os.path.exists(folderPath):
                    return "Folder not found"
                if not os.path.exists(resultPath):
                    os.mkdir(resultPath)
                for file in glob.glob(f'{folderPath}/*.pkl'):
                    if folderPath.find(".pkl") != -1:
                        with open(folderPath, 'rb') as file1:
                            file1data = pickle.load(file1)
                    elif folderPath.find(".json") != -1:
                        with open(folderPath, 'r') as file1:
                            file1data = json.load(file1)
                    else:
                        with open(folderPath, 'r') as file1:
                            file1data = file1.read()
                    file = os.path.basename(file)
                    if file1data == list(file1data):
                        file1data = str(file1data)
                    with open(f'{resultPath}/{file.replace('.pkl', '.txt')}', 'w') as file1:
                        file1.write(file1data)
                return "folder convert successful"
            except FileNotFoundError as err:
                return "Folder not found error.\nError: {err}"
            except TypeError as err:
                return f"Type error. Maybe, files contains a emojis.\nError: {err}"
            except Exception as err:
                return f"Unknown Error: {err}"

    class toPkl:
        """
        Convert Text files to Pickle format
        """
        def oneFile(filePath: str, resultPath: str = 'converter-result'):
            """
            Convert one file to .pkl format
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            try:
                if filePath.find(":") == -1:
                    with open(filePath, 'r') as file1:
                        file1data = file1.read()
                    filePath = filePath[:filePath.find('.')]
                    resultPath = resultPath + f'/{filePath}.pkl'
                    with open(resultPath, 'wb') as file1:
                        pickle.dump(file1data, file1)
                    return "file convert successful"
                elif filePath.find != -1:
                    with open(filePath, 'r') as file1:
                        file1data = file1.read()
                    if not os.path.exists(resultPath):
                        os.mkdir(resultPath)
                    filePath = os.path.basename(filePath)
                    resultPath = resultPath + f'/{filePath.replace('.txt', '.pkl')}'
                    with open(resultPath, 'wb') as file1:
                        pickle.dump(file1data, file1)
                    return "file convert successful"
            except FileNotFoundError as err:
                return f"File not found error.\nError: {err}"
            except TypeError as err:
                return f"Type error. Maybe, file contains a emojis.\nError: {err}"
            except Exception as err:
                return f"Unknown Error: {err}"

        def folder(folderPath: str, resultPath: str = 'converter-result'):
            """
            Convert folder with files to .pkl
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            try:
                if not os.path.exists(folderPath):
                    return "Folder not found"
                if not os.path.exists(resultPath):
                    os.mkdir(resultPath)
                for file in glob.glob(f'{folderPath}/*.txt'):
                    with open(file, 'r') as file1:
                        file1data = file1.read()
                    file = os.path.basename(file)
                    with open(f'{resultPath}/{file.replace('.txt', '.pkl')}', 'wb') as file1:
                        pickle.dump(file1data, file1)
                return "folder convert successful"
            except FileNotFoundError as err:
                return f"Folder not found.\nError: {err}"
            except Exception as err:
                return f"Error: {err}"

    class toJson:
        """
        Convert file to json format
        """
        def oneFile(filePath: str, resultPath: str = 'converter-result'):
            """
            Convert one file to json
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            isTxt = 0
            try:
                if filePath.find(":") == -1:
                    if filePath.find(".pkl") != -1:
                        with open(filePath, 'rb') as file1:
                            file1data = pickle.load(file1)
                    elif filePath.find(".txt") != -1:
                        isTxt = 1
                        with open(filePath, 'r') as file1:
                            file1data = file1.read()
                    filePath = filePath[:filePath.find('.')]
                    resultPath = resultPath + f'/{filePath}.json'
                    if isTxt == 1:
                        with open(resultPath, 'w') as file1:
                            file1.write(file1data)
                    else:
                        with open(resultPath, 'w') as file1:
                            json.dump(file1data, file1)
                    return "file convert successful"
                elif filePath.find(":") != -1:
                    if filePath.find(".pkl") != -1:
                        with open(filePath, 'rb') as file1:
                            file1data = pickle.load(file1)
                    elif filePath.find(".txt") != -1:
                        isTxt = 1
                        with open(filePath, 'r') as file1:
                            file1data = file1.read()
                    if not os.path.exists(resultPath):
                        os.mkdir(resultPath)
                    filePath = os.path.basename(filePath)
                    resultPath = resultPath + f'/{filePath.replace('.*', '.json')}'
                    if isTxt == 1:
                        with open(resultPath, 'w') as file1:
                            file1.write(file1data)
                    else:
                        with open(resultPath, 'w') as file1:
                            json.dump(file1data, file1)
                    return "file convert successful"
            except FileNotFoundError as err:
                return f"File not found error.\nError: {err}"
            except TypeError as err:
                return f"Type error. Maybe, file contains a emojis.\nError: {err}"
            except Exception as err:
                return f"Unknown Error: {err}"

        def folder(folderPath: str, resultPath: str = 'converter-result'):
            """
            Convert folder with files to json
            """
            if resultPath == 'converter-result':
                resultPath = os.path.abspath(__file__)
                resultPath = os.path.dirname(resultPath)
                resultPath = os.path.join(resultPath, 'converter-result')
            try:
                if not os.path.exists(folderPath):
                    return "Folder not found"
                if not os.path.exists(resultPath):
                    os.mkdir(resultPath)
                for file in glob.glob(f'{folderPath}/*.json'):
                    if file.find(".pkl") != -1:
                        with open(file, 'r') as file1:
                            file1data = pickle.load(file1)
                    elif folderPath.find(".pkl") != -1:
                        with open(folderPath, 'r') as file1:
                            file1data = {file1.read()}
                    else:
                        with open(file, 'r') as file1:
                            file1data = file1.read()
                    file = os.path.basename(file)
                    with open(f'{resultPath}/{file.replace('.*', '.pkl')}', 'w') as file1:
                        json.dump(file1data, file1)
                return "folder convert successful"
            except FileNotFoundError as err:
                return f"Folder not found.\nError: {err}"
            except Exception as err:
                return f"Error: {err}"
