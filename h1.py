import pymysql
class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()
        
    
    def ConnectDB(self):
        self.db = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "1234"
            )
        self.c = self.db.cursor()
    
    def CreateDB(self):
        self.c.execute("Create database IF NOT EXISTs test2")
        self.c.execute("USE test2")

    def CreateTB(self):
        self.c.execute('''Create table IF NOT EXISTS Company(
                                                    name VARCHAR(50) NOT NULL,
                                                    location VARCHAR(50) NOT NULL,
                                                    capital INT NOT NULL,
                                                    employees_count INT NOT NULL,
                                                    establishedAT INT NOT NULL,
                                                    monthly_expences INT NOT NULL
                                        )''')
        
    def InsertTB(self, name, location, capital, employees_count, establishedAT, monthly_expences):
        self.c.execute(f'''INSERT INTO Company VALUES(
                       "{name}", "{location}", {capital}, {employees_count}, {establishedAT}, {monthly_expences})''')
        self.db.commit()

    def FistQuery(self):
        self.c.execute("SELECT * FROM Company ORDER BY name")
        return self.c.fetchall()
    
    def SecondQuery(self):
        self.c.execute("SELECT * FROM Company ORDER BY capital DESC")
        return self.c.fetchall()
    
    def ThirdQuery(self):
        self.c.execute("SELECT * FROM Company ORDER BY employees_count")
        return self.c.fetchone()
    
    def FourthQuery(self):
        self.c.execute('SELECT * FROM Company WHERE location = "Toshkent" ')
        return self.c.fetchall()
    
    def FifthQuery(self):
        self.c.execute("SELECT location, COUNT(*) FROM Company GROUP BY location")
        return self.c.fetchall()
    
    def SixthQuery(self):
        self.c.execute('SELECT name, (YEAR(CURDATE()) - establishedAT) * (12 * monthly_expences) FROM Company')
        return self.c.fetchall()

mysql = MySQL()
# INSERT:
# for i in range(3):
#     mysql.InsertTB(input("Name: "), input("Location: "), int(input("Capital: ")), int(input("e_count: ")), int(input("EstablishedAT: ")), int(input("Monthly expences: ")))

# 1: First_Query
# for i in mysql.FistQuery():
#     print(i)

# 2: Second_Query
# for i in mysql.SecondQuery():
#     print(i)

# 3: Third_Query
# print(mysql.ThirdQuery())

# 4: Fourth_Query
# for i in mysql.FourthQuery():
#     print(i)


# 5: Fifth_Query
# for i in mysql.FifthQuery():
#     print(i)

# 6: Sixth_Query
# for i in mysql.SixthQuery():
#     print(i)