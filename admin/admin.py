from database.database import Database
class Admin:
    def __init__(self,db_name):
        self.db = Database(db_name)

    def add_admin(self,username,password):
        self.db.db_cursor.execute('''insert into admin (username,password) values(?,?)''',(username,password))
        self.db.dbc_in_file.commit()

    def add_constituency(self,name):
        self.db.db_cursor.execute('''insert into constituency (name) values(?)''',[name])
        self.db.dbc_in_file.commit()

    def add_conduct_election(self,name,start_date,ending_date):
        self.db.db_cursor.execute('''insert into conduct_election (name,start_date,end_date) values (?,?,?)''',(name,start_date,ending_date))
        self.db.dbc_in_file.commit()

    def update_name(self,name):
        self.db.db_cursor.execute('''update voters SET name = ?''',[name])
        self.db.dbc_in_file.commit()