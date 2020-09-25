import sqlite3

class Student:
    id: str = ''
    name: str = ''
    birth: str = ''
    regdate: str = ''

    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = conn.cursor()



class StudentDao:

    def create(self):
        # cursor(커서) : 데이터베이스 작업을 수행하고 있는 메모리 공간
        cursor = self.cursor
        try:
            # excute : sql 구문을 실행해주는 함수
            cursor.execute("drop table students")
        except sqlite3.OperationalError as err:
            print("테이블이 존재하지 않습니다.")

        cursor.execute(
            '''create table students
            (id text primary key, name text, birth text)'''
        )
        cursor.commit()

    def insert_one(self):
        cursor = self.cursor
        sql = "insert into students(id, name, birth) values ('lee', '이승기', '1989/11/11')"
        cursor.execute(sql)

    def insert_many(self):
        data = [
            ('lee', '1', '010-1111-1111'),
            ('kim', '1', '010-2222-2222'),
            ('lee', '1', '010-3333-3333')
        ]
        query = """
            INSERT INTO member(userid, password, phone) VALUES (?, ?, ?)
        """
        self.conn.executemany()

    def fetch_one(self):
        pass


    def fetch_all(self):
        cursor = self.cursor.execute('select * from students')


    def login(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

class StudentService:
    pass