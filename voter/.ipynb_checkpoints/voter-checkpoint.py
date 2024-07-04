from database.database import Database
class Voter:
    def __init__(self,db_name):
        self.db = Database(db_name)

    def add_voter(self,username,password):
        self.db.db_cursor.execute('''insert into voter (username,password) values(?,?)''',(username,password))
        self.db.dbc_in_file.commit()