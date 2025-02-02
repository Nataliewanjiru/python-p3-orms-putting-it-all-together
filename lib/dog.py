import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
   
    @classmethod
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS dogs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.breed))
        self.id = CURSOR.lastrowid  

        CONN.commit()

    @classmethod
    def create(cls,name,breed):
        dog = cls(name,breed)
        dog.save()
        return dog
    
    @classmethod
    def new_from_db(cls, row):
        id, name, breed = row
        return cls(id, name, breed)