# Moduuli Postgresql tietokantapalvelimen käyttämiseen

import psycopg2
import json

# Luokat
class DbConnection():
    def __init__(self, settings: dict):
        self.settings = settings
        self.server = settings['server']
        self.port = settings['port']
        self.databaseName = settings['database']
        self.userName = settings['userName']
        self.password = settings['password']