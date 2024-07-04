from database.database import Database
class Admin:
    def __init__(self,db_name):
        self.db = Database(db_name)

    def add_admin(self,username,password):
        self.db.db_cursor.execute('''insert into admin (username,password) values(?,?)''',(username,password))
        self.db.dbc_in_file.commit()