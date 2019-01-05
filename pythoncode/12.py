import sqlite3
conn=sqlite3.connect("test.db")

c=conn.cursor()
#创建数据库
#create tables
c.execute('''CREATE TABLE category(id int primary key,sort int,name text)''')
c.execute('''CREATE TABLE book
              (id int primary key,sort int,name text,price real.category int,
              FOREIGN KEY (category) REFERENCES category(id))''')

#save the changes
conn.commit()

#close the connection with the database
conn.close()

#插入数据
books=[(1,1,'Cook Recipe',3.12,1),
       (2,3,'Python Intro',17.5,2),
       (3,2,'OS Intro',13.6,2),
       ]

#execute "INSERT"
c.execute("INSERT INTO category VALUES (1,1,'kitchen')")
#execute multiple commands
c.executemany('INSERT INTO book VALUES (?,?,?,?,?)',books)

conn.commit()
conn.close()

#查询数据
#retrieve one record
c.execute('select name from category order by sort')
print(c.fetchone())
print(c.fetchone())

#retrieve all records as a list
c.execute('select * from book where book.category=1')
print(c.fetchall())

#iterate through the records
for row in c.execute('SELECT name,price FROM book ORDER BY sort'):
    print(row)
