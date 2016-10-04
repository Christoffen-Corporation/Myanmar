import json
from Definitions.Settings import OpenFrom

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