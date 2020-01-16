import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="wy19961227",  # 数据库密码
    database="pythonspider"
)
mycursor = mydb.cursor()


def insertSQL(name, urlPath, txtPath):
    sql = "INSERT INTO pictures (name, urlPath, txtPath) VALUES (%s, %s, %s)"
    val = (name, urlPath, txtPath)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        mydb.rollback()


def selectAll():
    mycursor.execute("select * from pictures")
    myresult = mycursor.fetchall()
    return myresult


print(selectAll())
