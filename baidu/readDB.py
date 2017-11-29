
import sqlite3
import logging
conn = sqlite3.connect('C:\\Users\\Boss\\baidu\\data\\cnblogs.db')
c = conn.cursor()
# data = c.execute("select * from blogs where title =:title",{"title":'Webpack实战'}) #working
data = c.execute("select Id, title,titleLink,publishDate from blogs")
# totalCount = c.execute("select count(1) from blogs")
# data = c.execute("select count(*) from blogs where titleLink =:title",{"title":'http://www.cnblogs.com/csonezp/p/7868127.html'})
# alldata=c.fetchall()
# print(len(alldata))
# print(c.fetchone())
# print(data.get)
# print(totalCount)
for d in data:
    # logging.warning(d)
    print(d)
conn.close()



# insert_str=""
# c.execute()

# str = "insert into blogs(name,link) values(?,?)"