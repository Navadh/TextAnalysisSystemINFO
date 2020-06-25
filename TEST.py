import pymysql

# tasdb=pymysql.connect('localhost', 'root', 'NavINFO5717TX','tasdb')
#
# cursor=tasdb.cursor()
# sql="select ttasname, count(*) as total from ttasys group by ttasname having total>0 order by total asc"
# # sql="select ttasname, count(*) as total from ttasys group by ttasname having total>0"
#
# # sql="select ttasname, count(*) from ttasys group by ttasname"
# # sql="select * from ttasys where ttasname='xyz'"
# command=cursor.execute(sql)
# results=cursor.fetchall()
# # cursor.execute('select version()')
# # data=cursor.fetchone()
#
# #print('Database version:%s'%data)
# # print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# print("ttasname \t\t total")
# # print("ttasname \t\t count")
# print('-----------------------------------------------------------------------------')
#
# for row in results:
#     print(str(row[0])+"\t\t\t" + str(row[1]))
# cursor.close()
# results=""
# tasdb.close()



# tasdb=pymysql.connect('localhost', 'root', 'NavINFO5717TX','tasdb')
#
# cursor=tasdb.cursor()
# sql="select * from ttasys where ttasname like %s"
# values="%n%"
# command=cursor.execute(sql, values)
# results=cursor.fetchall()
# # cursor.execute('select version()')
# #data=cursor.fetchone()
#
# #print('Database version:%s'%data)
# print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# print('-----------------------------------------------------------------------------')
#
# for row in results:
#     print(str(row[0])+"\t\t"+row[1]+"\t\t\t"+row[2]+"\t\t"+str(row[3])+"\t\t"+str(row[4]))
# cursor.close()
# results=""
# # tasdb.commit()
# tasdb.close()

tasdb=pymysql.connect('localhost', 'root', 'NavINFO5717TX','tasdb')

cursor=tasdb.cursor()
sql="delete from ttasys where ttasid=%s"
values=int(input("Please input an id you wnat to delete: "))

# sql="update ttasys set ttasname=%s where ttasid=%s"
# values=("BIG", 8)

# sql="insert into ttasys(ttasname, ttasmemo, ttasdate, ttasnum) values(%s, %s, %s, %s)"
# values=("ABC", "Visitor", "2020-06-23", 5717)
command=cursor.execute(sql, values)
# results=cursor.fetchall()
# cursor.execute('select version()')
#data=cursor.fetchone()

#print('Database version:%s'%data)
# print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# print('-----------------------------------------------------------------------------')

#for row in results:
#    print(str(row[0])+"\t\t"+row[1]+"\t\t\t"+row[2]+"\t\t"+str(row[3])+"\t\t"+str(row[4]))

# results=""

cursor.close()
tasdb.commit()

tasdb.close()