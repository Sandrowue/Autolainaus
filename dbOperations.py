# Moduuli Postgresql tietokantapalvelimen käyttämiseen
import psycopg2

import json

import cipher

# Luokat
class DbConnection():
    def __init__(self, settings: dict):
        self.settings = settings
        self.server = settings['server']
        self.port = settings['port']
        self.databaseName = settings['database']
        self.userName = settings['userName']
        self.password = settings['password']
        
        # Yhteysmerkkijono
        self.connectionString = f'dbname={self.databaseName} user={self.userName} password={self.password} host={self.server} port={self.port}'
        print('Yhteysmerkkijono on:', self.connectionString)

    # Metodi tietojen lisäämiseen (INSERT)
    def addToTable(self, table: str, data: dict) -> str:
        message = ""

        # Muodostetaan lista sarakkeiden (kenttien) nimistä ja arvoista SQL lausetta varten
        keys = data.keys() # Luetaan sanakirjan avaimet
        columns = ''
        values = ''

        for column in keys:
            columns += column + ', '
            rawValue = data[column]

            # Lisätään puolilainausmerkit, jos kyseessä on merkkijono
            if isinstance(rawValue, str):
                value = f'\'{rawValue}\'' # \' mahdollistaa puolilainausmerkin lisääminen
            else:
                value = f'{rawValue}'

            values += value + ', ' # Lisätään arvo sekä pilkku ja välilyönti

        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursori suorittamaan tietokantaoperaatiota
            cursor = currentConnection.cursor()

            # Poistetaan viimeinen pilkku
            columns = columns[:-2]
            values = values[:-2]

            sqlClause = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            print(sqlClause)
            # Suoritetaan SQL-lause
            cursor.execute(sqlClause)

            # Vahvistetaan tapahtuman (transaction)
            currentConnection.commit()


        except(Exception, psycopg2.Error) as e:
            raise e
        
        finally:
            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuhotaan yhteys

        
if __name__ == '__main__':

    testiasetukset = {"server": "127.0.0.1", "port": "5432", "database": "autolainaus", "userName": "autolainaus", "password": "helenium"}
   
    testidata = {'ryhma': 'Mopo Jopo',
                 'vastuuhenkilo': 'Hannu'}

    dbConnection = DbConnection(testiasetukset)
    dbConnection.addToTable('ryhma', testidata)

