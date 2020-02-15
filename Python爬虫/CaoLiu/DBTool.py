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


def insertParams(params, tableName, values):
    bathSql = "INSERT INTO " + tableName
    paramSql = " ("
    for i in range(len(params)):
        if i != len(params) - 1:
            paramSql += params[i] + ", "
        else:
            paramSql += params[i] + ") "
    valueSql = "VALUES ("
    for i in range(len(params)):
        if i != len(params) - 1:
            valueSql += "%s, "
        else:
            valueSql += "%s)"
    sql = bathSql + paramSql + valueSql
    print(sql)
    val = []
    for i in range(0, len(values)):
        val.append((values[i], 0))
    print(val)
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


def getNameListByTxt(tableName: str):
    sql = "select name, urlPath from " + tableName + " where txtPath is null and picPath is null"
    cursor.execute(sql)
    results = cursor.fetchall()
    return list(results)


def deleteDBByName(tableName: str, names:list):
    sql = "delete from " + tableName + " where name = %s"
    val = []
    for i in range(0, len(names)):
        val.append((names[i],))
    cursor.executemany(sql, val)
    mydb.commit()


# def updateSQL(name):
#     sql = "UPDATE " + tableName + " SET hasDownload = 1 where name = %s"
#     try:
#         cursor.execute(sql, name)
#         mydb.commit()
#     except Exception as e:
#         print(e)
#         mydb.rollback()


def updatePicPathFromPictures(path: str, names: list, tableName: str, line: str):
    sql = "update " + tableName + " set " + line + " = %s where name = %s"
    val = []
    for i in range(0, len(names)):
        val.append((path, names[i]))
    cursor.executemany(sql, val)
    mydb.commit()


def getMinPathFromFolder(tableName: str):
    sql = "select min(path),num,id from " + tableName + " where num < 1000"
    cursor.execute(sql)
    results = cursor.fetchall()
    return list(results[0])


def updateNumFromFolder(num: int, id: str, tableName: str):
    sql = "update " + tableName + " set num = %s where id = %s"
    cursor.execute(sql, (num, id))
    mydb.commit()


def getNameListFromFolder():
    sql = "select path from folders where num > 0"
    cursor.execute(sql)
    results = cursor.fetchall()
    resultList = []
    for result in results:
        resultList.append(str(result)[2:-3])
    return resultList


def getDownloadPicInfo(tableName):
    sql = "select name, txtPath, `index` from " + tableName + " where urlPath is not null and picPath is null ORDER BY " \
                                                     "`index` DESC limit 100"
    cursor.execute(sql)
    results = cursor.fetchall()
    nameList = []
    pathList = []
    idList = []
    for result in results:
        nameList.append(result[0])
        pathList.append(result[1])
        idList.append(result[2])
    return [nameList, pathList, idList]



# def deleteAll():
#     sql = "truncate table " + tableName
#     mycursor.execute(sql)
#     mydb.commit()
#     print("删除完毕")
