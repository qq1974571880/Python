import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="wy19961227",  # 数据库密码
    database="pythonspider"
)

cursor = mydb.cursor()


def insertSQL(name, urlPath, tableName):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = (name, urlPath)
    try:
        cursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print(e)
        mydb.rollback()


def insertSQLs(names, urls, tableName):
    sql = "INSERT INTO " + tableName + " (name, urlPath) VALUES (%s, %s)"
    val = []
    for i in range(0, len(names)):
        val.append((names[i], urls[i]))
    cursor.executemany(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句


def selectAll(tableName):
    cursor.execute("select * from " + tableName)
    results = cursor.fetchall()
    return results


def getNameList(tableName):
    cursor.execute("select name from " + tableName)
    results = cursor.fetchall()
    listResult = []
    for result in results:
        listResult.append(str(result)[2:-3])
    return listResult


# def updateSQL(name):
#     sql = "UPDATE " + tableName + " SET hasDownload = 1 where name = %s"
#     try:
#         cursor.execute(sql, name)
#         mydb.commit()
#     except Exception as e:
#         print(e)
#         mydb.rollback()


def updateSQLs(names, tableName):
    try:
        sql = "UPDATE " + tableName + " SET hasDownload = %s where name = %s"
        val = []
        for i in range(0, len(names)):
            val.append((1, names[i]))
        cursor.executemany(sql, val)
        mydb.commit()  # 数据表内容有更新，必须使用到该语句
    except Exception as e:
        print(e)
        mydb.rollback()

# def deleteAll():
#     sql = "truncate table " + tableName
#     mycursor.execute(sql)
#     mydb.commit()
#     print("删除完毕")
