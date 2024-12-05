import json

with open('settings.json', 'rt') as settingsFile:
            jsonData = settingsFile.read()
            settingsDictionary = json.loads(jsonData)    
            passwordSetting = settingsDictionary['password'] 

print(passwordSetting)