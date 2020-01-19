import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="wy19961227",  # 数据库密码
    database="pythonspider"
)

tableName = "pictures"

cursor = mydb.cursor()


def insertSQL(name, urlPath):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = (name, urlPath)
    try:
        cursor.execute(sql, val)
        mydb.commit()
    except:
        mydb.rollback()


def insertSQLs(names, urls):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = []
    for i in range(0, len(names)):
        val.append((names[i], urls[i]))
    cursor.executemany(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句


def selectAll():
    cursor.execute("select * from pictures")
    results = cursor.fetchall()
    return results


def getNameList():
    cursor.execute("select name from pictures")
    results = cursor.fetchall()
    listResult = []
    for result in results:
        listResult.append(str(result)[2:-3])
    return listResult


# def deleteAll():
#     sql = "truncate table " + tableName
#     mycursor.execute(sql)
#     mydb.commit()
#     print("删除完毕")
