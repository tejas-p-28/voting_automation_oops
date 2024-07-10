from database.database import Database
class Voter:
    def __init__(self,db_name):
        self.db = Database(db_name)

    def add_voter(self,username,password):
        self.db.db_cursor.execute('''insert into voter (username,password) values(?,?)''',(username,password))
        self.db.dbc_in_file.commit()
    def cast_vote(self,voter_id,candidate_id):
        self.db.db_cursor.execute('''insert into votes (voter_id,candidate_id) values (?,?)''',(voter_id,candidate_id))
        self.db.db_cursor.execute('''update voters SET voted = 1 where id = ?''',[voter_id])
        self.db.dbc_in_file.commit()