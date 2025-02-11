import json
import datetime

with open('settings.json', 'rt') as settingsFile:
            jsonData = settingsFile.read()
            settingsDictionary = json.loads(jsonData)    
            passwordSetting = settingsDictionary['password'] 

print(passwordSetting)
print(datetime.datetime.now())