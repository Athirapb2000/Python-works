              #  FOR INSERT

# import pymysql
# db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
# con = db.cursor()
# sqlquery = 'insert into t1 values(%s,%s,%s)'
# val = (13, 'Baby', 25)
# con.execute(sqlquery, val)
# db.commit()
# print('Inserted')

                #  OR

# import pymysql
# id = int(input('Enter the Id : '))
# na = input('Enter the Name : ')
# ag = int(input('Enter the Age : '))
# db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
# mycursor = db.cursor()
# sql = 'insert into t1 values(%s,%s,%s)'
# val = (id, na, ag)
# mycursor.execute(sql, val)
# db.commit()
# print('Inserted Successfully')

            #   FOR DELETE

# import pymysql
# id = int(input('Enter the Id : '))
# db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
# mycursor = db.cursor()
# sql = "delete from t1 where id='%d'" % (id)
# mycursor.execute(sql)
# db.commit()
# print('Deleted Successfully')

           #   FOR UPDATE

# import pymysql
# y = input('Do you want to update? ')
# if y == 'yes':
#     db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
#     id = int(input('Enter the Id : '))
#     na = input('Enter the Name : ')
#     ag = int(input('Enter the Age : '))
#     c = db.cursor()
#     sql = "update t1 set name='%s',Age='%d' where id='%d' " % (na, ag, id)
#     c.execute(sql)
#     db.commit()
#     print('Table Updated')
# elif y == 'no':
#     print('Exit')

                # FOR FETCH

# import pymysql
# id = int(input('Enter the Id : '))
# db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
# con = db.cursor()
# sql = 'select * from t1 where id=%d' %id
# con.execute(sql)
# i = con.fetchone()
# id = i[0]
# na = i[1]
# ag = i[2]
# print(f'id={i[0]}, name={na}, age={ag}')

                # OR

# import pymysql
# db = pymysql.connect(host='localhost', user='root', password='Athira123@', database='nov_test')
# con = db.cursor()
# sql = 'select * from t1'
# con.execute(sql)
# data = con.fetchall()
# for i in data:
#     id = i[0]
#     na = i[1]
#     ag = i[2]
#     print(f'id={i[0]}, name={na}, age={ag}')