import pyodbc


class Animals:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=M13369\SQLEXPRESS;'
                              'Database=Animals;'
                              'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()

    def get_pokemon(self):
        pokemon = self.cursor.execute('SELECT * FROM [Animals].[dbo].[Pokemon]')
        return pokemon.fetchall()

    def add_pokemon(self, name, type, trainer, level):
        sql = "INSERT INTO [Animals].[dbo].[Pokemon] VALUES ((SELECT MAX(Pokemonid) + 1 FROM [Animals].[dbo].[Pokemon]), '" + name + "'," + type + ", " + trainer + ", " + level + ", GETDATE())"
        self.cursor.execute(sql)
        self.cursor.commit()


