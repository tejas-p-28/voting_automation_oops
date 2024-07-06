import sqlite3
class Database:
    def __init__(self,dbc_in_file):
        self.dbc_in_file = sqlite3.connect('voting_db.db')
        self.db_cursor = self.dbc_in_file.cursor()
    
    def create_tables(self):
        self.db_cursor.execute('''create table if not exists conduct_election
            (id integer primary key,
            start_date date not null,
            end_date date not null,
            name text)''')
        self.db_cursor.execute('''create table if not exists admin
            (id integer primary key,
            username varchar(10) not null,
            password integer not null)''')
        self.db_cursor.execute('''create table if not exists voter
            (id integer primary key,
            username varchar(10) not null,
            password integer not null)''')
        self.db_cursor.execute('''create table if not exists voters
            (id integer primary key,
            name varchar(20),
            date_of_birth text,
            constituency varchar(20) )''')
        self.db_cursor.execute('''create table if not exists parties
            (id integer primary key,
            name text not null)''')
        self.db_cursor.execute('''create table if not exists constituency
            (id integer primary key,
            name varchar(30) not null)''')
        self.db_cursor.execute('''create table if not exists candidates
            (id integer primary key,
            name text not null,
            party_id integer not null,
            FOREIGN KEY (party_id) REFERENCES parties (id))''')
        self.db_cursor.execute('''create table if not exists votes
            (voter_id integer primary key ,
            candidate_id interger not null,
            FOREIGN KEY (voter_id) REFERENCES voters(id),
            FOREIGN KEY (candidate_id) REFERENCES candidates(id))''')
        self.dbc_in_file.commit()
        self.dbc_in_file.close()