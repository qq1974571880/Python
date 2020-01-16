import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="wy19961227",  # 数据库密码
    database="pythonspider"
)

tableName = "pictures"

mycursor = mydb.cursor()


def insertSQL(name, urlPath):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = (name, urlPath)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        mydb.rollback()


def insertSQLs(names, urls):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = []
    for i in range(0, len(names)):
        val.append((names[i], urls[i]))
    mycursor.executemany(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句


def selectAll():
    mycursor.execute("select * from pictures")
    myresult = mycursor.fetchall()
    return myresult


# def deleteAll():
#     sql = "truncate table " + tableName
#     mycursor.execute(sql)
#     mydb.commit()
#     print("删除完毕")
