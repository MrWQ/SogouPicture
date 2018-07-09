
import pymysql


# 查询所有
def selectUrl():
    # 打开数据库连接
    # db = pymysql.connect("localhost", "root", "431879", "wq")
    db = pymysql.connect("localhost", "root", "431879", "reptile")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM picture"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            testid = row[0]
            testurl = row[1]
            testname  = row[2]
            # 打印结果
            print("testid=%s,testname=%s,testname=%s" % \
                  (testid, testurl,testname))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
# 模糊查询name
def selectName(name):
    # 打开数据库连接
    # db = pymysql.connect("localhost", "root", "431879", "wq")
    db = pymysql.connect("localhost", "root", "431879", "reptile")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    like = '%'+str(name)+'%'
    print(like)
    # SQL 查询语句
    sql = "SELECT * FROM picture WHERE picturename LIKE"+"'"+str(like)+"'"
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            testid = row[0]
            testurl = row[1]
            testname  = row[2]
            # 打印结果
            print("testid=%s,testname=%s,testname=%s" % \
                  (testid, testurl,testname))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()




# 插入URL和name
def insertUrlName(url,name):
    # 打开数据库连接
    # db = pymysql.connect("localhost", "root", "431879", "wq")
    db = pymysql.connect("localhost", "root", "431879", "reptile")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    # sql = "SELECT * FROM test"
    # SQL 插入语句
    sql = "INSERT INTO picture(pictureurl,picturename) \
           VALUES ('%s','%s')" % \
          (url,name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

if __name__=='__main__':
    # insertUrlName()
    # selectUrl()
    selectName('炮')