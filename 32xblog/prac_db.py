import os
import sqlite3


def create_tables(connection):
    # 커서(쿼리문을 담을 상자) 연결
    cur = connection.cursor()

    query = []

    query1 = """
            CREATE TABLE Position (
                posId INT PRIMARY KEY, 
                posName VARCHAR(100)); 
            """

    query2 = """
            CREATE TABLE Center (
                centerId INT PRIMARY KEY, 
                centerName VARCHAR(100)); 
            """

    query3 = """
            CREATE TABLE Part (
                partId INT PRIMARY KEY, 
                partName VARCHAR(100), 
                centerId INT,
                FOREIGN KEY (centerId) REFERENCES Center(centerId)
                );
            """

    query4 = """
            CREATE TABLE Employee (
                empId INT PRIMARY KEY, 
                empName VARCHAR(100), 
                birthdate TEXT,
                hiredate TEXT,
                positionId INT,
                partId INT,
                FOREIGN KEY (positionId) REFERENCES Position(posId),
                FOREIGN KEY (partId) REFERENCES Part(partId)
                );
            """

    # 쿼리를 실행
    ## table이 이미 존재할 경우 삭제 후 생성
    cur.execute("DROP TABLE IF EXISTS Position;")
    cur.execute("DROP TABLE IF EXISTS Center")
    cur.execute("DROP TABLE IF EXISTS Part")
    cur.execute("DROP TABLE IF EXISTS Employee")

    # 테이블 생성 쿼리 실행(executemany)
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)


def add_data(connection):
    # 데이터를 데이터베이스에 추가

    cur = connection.cursor()

    # 직책 데이터
    positionlist = [(1, 'CEO'),
                (2, 'CTO'),
                (3, 'manager'),
                (4,'staff')
            ]

    # 근무지 데이터
    centerlist = [(1, '서울_Sandbox'),
                (2, '성주'),
                (3, '부산'),
                (4,'해외')
            ]

    # 근무부서 데이터
    partlist = [(1, '경영전략부', 1),
                (2, '개발부', 1),
                (3, '디자인부', 1),
                (4,'마케팅부', 2)
            ]

    # 직원 데이터
    emplist = [(1, '서달미', '1993-03-26', '2020-11-01', 1, 1),
                (2, '남도산', '1993-05-07', '2020-11-01', 2, 2),
                (3, '김용산', '1993-08-23', '2020-11-01', 3, 2),
                (4, '이철산', '1994-01-09', '2020-11-01', 3, 2),
                (5, '정사하', '1992-12-28', '2020-11-01', 3, 3),
                (6, '남천호', '1991-11-11', '2020-11-01', 4, 4)
            ]

    cur.executemany("INSERT INTO Position VALUES (?, ?)"
                , positionlist)
    cur.executemany("INSERT INTO Center VALUES (?, ?)"
                , centerlist)
    cur.executemany("INSERT INTO Part VALUES (?, ?, ? )"
                , partlist)
    cur.executemany("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ? )"
                , emplist)

    connection.commit()



def select_data(connection, tablename):
# 테이블 조회
    # cursor connection
    cur = connection.cursor()

    # selection query
    sql_query = f"SELECT * FROM {tablename};"

    # 쿼리 실행
    cur.execute(sql_query)
    print(cur.fetchall())



if __name__ == "__main__":

    # sqlite(DB) 연결
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 
                                        "data", 
                                        "samsantec.sqlite"))

    # 테이블을 생성
    create_tables(conn)

    # 데이터 추가
    add_data(conn)

    # 테이블 조회(Employee table)
    select_data(conn,"Employee")