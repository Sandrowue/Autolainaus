import json
# Tiedoston käsittely: avaaminen ja sulkeminen

# Avataan tiedosto lukua varten
readSettingsFile = open('settings.txt', 'rt')
readFileContent = readSettingsFile.read()
print(readFileContent)

# Avataan sama tiedosto toisen kerran lukua varten
readSettingsFile2 = open('settings.txt', 'rt')
readFileContent2 = readSettingsFile2.read()
print(readFileContent2)

# Avataan tiedosto kirjoiutusta varten

writeNewSettingsFile = open('newSettings.txt', 'wt')
writeFileContent = writeNewSettingsFile.write('Alustetaan uudet tietokanta asetukset')
writeNewSettingsFile.close()

readNewSettingsFile = open('newSettings.txt', 'rt')
readNewFileContent = readNewSettingsFile.read()
print(readNewFileContent)

# Luetaan tiedosto with-rakenteen avulla. Tiedosto suljetaan ja muisti tyhjennetään operaattorin päätteeksi

with open('settings.txt', 'rt') as withReadSettingsFile:
    readFileContent3 = withReadSettingsFile.read()
    print(readFileContent3)

with open ('newSettings.txt', 'at') as withNewSettingsFile2:
    withNewSettingsFile2.write('\nPalevelin: 127.0.0.2')

with open('newSettings.txt', 'rt') as withReadSettingsFile2:
    readFileContent4 = withReadSettingsFile2.read()
    print(readFileContent4)


asetukset = {}

with open('settings.json', 'rt') as jsonReadSettingsFile:
    readFileContent5 = jsonReadSettingsFile.read()
    asetukset  = json.loads(readFileContent5) # Muunnetaan json muotoinen teksti Python-sanakirjaksi

print(asetukset)

asetuksetDict = {
    'server': 'autolainea.raseko.fi',
    'port': 5432,
    'database': 'autolainaus',
    'userName': 'postgres',
    'password': 'helenium'
        }

asetuksetJson = json.dumps(asetuksetDict)
# Luodaan uusi tiedosto
with open('asetukset.json', 'wt') as jsonAsetukset:
    jsonAsetukset.write(asetuksetJson)