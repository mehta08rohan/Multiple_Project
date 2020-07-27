import sqlite3
from Employee import employee

a=employee('Ron','Coleman',42)


conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute(""" create table emp (fname text , lname text , age int )""")

c.execute("insert into emp values('Rohan','Mehta',25)")
c.execute("insert into emp values(:f,:l,:a)",{"f":a.fname,"l":a.lname,"a":a.age})

c.execute("select * from emp")
print(c.fetchall())

conn.commit()
conn.close()

