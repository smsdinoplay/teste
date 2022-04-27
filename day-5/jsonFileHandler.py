"""
Insulin Functions
"""

import json

def readJsonFile(fileName):
    data=""
    try:
        with open('day-5/files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print('Não foi possivel ler o arquivo.')
    return data
        