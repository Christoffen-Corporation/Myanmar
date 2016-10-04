import json
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../Settings.json')

with open(filename) as data_file:    
    Settings = json.load(data_file)
OpenFrom = Settings["Files"][0]["FromLanguage"]
OpenTo = Settings["Files"][0]["ToLanguage"]

CheckHeaders = Settings["Options"][0]["Headers"]
OpenHeaders = Settings["Files"][0]["Headers"]

CheckEntry = Settings["Options"][0]["EntryPoint"]
OpenEntry = Settings["Files"][0]["EntryPoint"]
EndEntry = Settings["Options"][0]["EntryPointEnd"]

InputFile = Settings["Files"][0]["InputFileName"]
OutputFile = Settings["Files"][0]["OutputFileName"]