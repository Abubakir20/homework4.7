import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute("CREATE DATABASE IF NOT EXISTS test3")
        self.c.execute("USE test3")

    def CreateTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS Restaurants(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            adress VARCHAR(50),
            maxFoodPrice INT,
            minFoodPrice INT,
            employeesCount INT,
            experience INT
        )''')

    def InsertTB(self, name, adress, maxFoodPrice, minFoodPrice, employeesCount, experience):
        self.c.execute(f'''INSERT INTO Restaurants(name, adress, maxFoodPrice, minFoodPrice, employeesCount, experience)
        VALUES("{name}", "{adress}", {maxFoodPrice}, {minFoodPrice}, {employeesCount}, {experience})''')
        self.db.commit()

    # 1
    def FirstQuery(self):
        self.c.execute('SELECT * FROM Restaurants WHERE LOWER(name) LIKE "m%r" ORDER BY maxFoodPrice')
        return self.c.fetchall()

    # 2
    def SecondQuery(self):
        self.c.execute('SELECT name FROM Restaurants ORDER BY minFoodPrice  LIMIT 3')
        return self.c.fetchall()

    # 3
    def ThirdQuery(self):
        self.c.execute(' SELECT name, maxFoodPrice FROM Restaurants ORDER BY experience DESC, maxFoodPrice DESC LIMIT 4')
        return self.c.fetchall()


mysql = MySQL()

# INSERT:
# for i in range(10):
#     mysql.InsertTB(input("Name: "), input("Adress: "), int(input("MAX price: ")), int(input("MIN price: ")), int(input("Employees: ")), int(input("Exз: ")))

# 1
# for i in mysql.FirstQuery():
#     print(i)

# 2
# for i in mysql.SecondQuery():
#     print(i)

# 3
# for i in mysql.ThirdQuery():
#     print(i)