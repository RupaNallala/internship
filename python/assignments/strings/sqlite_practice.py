import sqlite3

a=sqlite3.connect("emp.db")

c=a.cursor()

c.execute("""create table employee(emp_id integer,emp_name text,emp_sal integer)""")

c.execute("""
insert into employee values(101,'rupa',70000)
""")

c.execute("""
insert into employee values(102,'sri',80000),(103,'sai',90000)
""")

data=[(104,'latha',100000),(105,'mahii',110000)]

c.executemany("""insert into employee values(?, ?, ?)""",data)

c.execute("""insert into employee values(?,?,?)""",(106,'greesh',20000))

a.commit()

p=c.execute("select * from employee")
for x in p:
    print(x)
    #or
#for x in c.execute("select * from employee"):
# print(x)

#without using of for loop to print
c.execute('select *from employee')
print(c.fetchone())                 #it returns one row of table
print(c.fetchmany(3))               #it returns a range of rows like 3            
print(c.fetchall())                 #it returs all the rows 

#where clause
c.execute("select * from employee where emp_sal>=80000 and emp_name='sri'")
print(c.fetchall())

#update clause
c.execute("update employee set emp_sal=85000 where emp_name='sri'")
print(c.fetchall())
c.commit()

#between clause
c.execute("select * from employee where emp_sal between 80000 and 100000")
print(c.fetchall())

#in clause
c.execute("select * from employee where emp_id in (101,102,103)")
print(c.fetchall())

#like clause
c.execute("select * from employee where emp_name like 's%'")
print(c.fetchall())

#limit clause
c.execute("select * from employee limit 3")
print(c.fetchall())

#not in clause
c.execute("select * from employee where emp_id not in (101,102,103)")
print(c.fetchall())
c.commit()
 








