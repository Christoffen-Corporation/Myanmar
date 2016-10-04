import json
from Definitions.Settings import OpenTo

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