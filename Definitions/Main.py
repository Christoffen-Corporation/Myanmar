import json
import os
from pprint import pprint

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../Settings.json')

with open(filename) as data_file:    
    Settings = json.load(data_file)
OpenFrom = Settings["Files"][0]["FromLanguage"]
OpenTo = Settings["Files"][0]["ToLanguage"]

InputFile = Settings["Files"][0]["InputFileName"]
OutputFile = Settings["Files"][0]["OutputFileName"]

with open(OpenFrom) as data_file:    
    From = json.load(data_file)

FromFunctionStart = From["Function"][0]["Start"]
FromFunctionStop = From["Function"][0]["End"]

FromVariable = From["Variables"][0]["Variable"]

FromTextStart = From["Text"][0]["Start"]
FromTextStop = From["Text"][0]["End"]

FromTab = From["Characters"][0]["Tab"]

FromElseIf = From["Conditionals"][0]["ElseIf"]
FromElseIfStart = From["Conditionals"][0]["StartElseIf"]

FromQuote = From["Characters"][0]["Quote"]

with open(OpenTo) as data_file:    
    To = json.load(data_file)

ToFunctionStart = To["Function"][0]["Start"]
ToFunctionStop = To["Function"][0]["End"]

ToVariable = To["Variables"][0]["Variable"]

ToTextStart = To["Text"][0]["Start"]
ToTextStop = To["Text"][0]["End"]

ToTab = To["Characters"][0]["Tab"]

ToElseIf = To["Conditionals"][0]["ElseIf"]
ToElseIfStart = To["Conditionals"][0]["StartElseIf"]

Includes = To["Includes"][0]["STDIO"]

EntryPointStart = To["EntryPoint"][0]["MainStart"]
EntryPointStop = To["EntryPoint"][0]["MainStop"]

ToQuote = To["Characters"][0]["Quote"]















