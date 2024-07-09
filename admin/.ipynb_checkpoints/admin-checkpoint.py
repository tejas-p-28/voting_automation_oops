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

    def update_name(self,updated_name,name):
        self.db.db_cursor.execute('''update voters SET name = ? where name = ?''',(updated_name,name))
        self.db.dbc_in_file.commit()
    def update_dob(self,dob,updated_dob):
        self.db.db_cursor.execute('''update voters SET date_of_birth = ? where date_of_birth = ?''',[updated_dob,dob])
        self.db.dbc_in_file.commit()
    def update_const(self,const_id,updated_const_id):
        self.db.db_cursor.execute('''update voters SET const_id = ? where const_id = ?''',(updated_const_id,const_id))
        self.db.dbc_in_file.commit()
    def add_party(self,party_name):
        self.db.db_cursor.execute('''insert into parties (name) values (?)''',[party_name])
        self.db.dbc_in_file.commit()
    def add_candidate(self,candidate_name,party_id):
        self.db.db_cursor.execute('''insert into candidates (name,party_id) values (?,?)''',(candidate_name,party_id))
        self.dbc_in_file.commit()