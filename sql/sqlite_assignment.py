from ast import Add
import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

# cur.execute("""create table student(stu_id integer,stu_name text,stu_age integer,stu_course text,stu_marks integer)""")

# cur.execute("""
# insert into student values(101,'rupa',20,'python',100)""")

# cur.execute("""
# insert into student values(102,'sri',22,'java',80)""")

# cur.execute("""
# insert into student values(103,'sai',21,'java',90)""")

# cur.execute("""
# insert into student values(104,'latha',23,'python',100),(105,'mahii',24,'java',110)""")


conn.commit()

#PART-A BASIC QUERIES

cur.execute("select * from student")
print(cur.fetchall())

cur.execute("select stu_name from student")
print(cur.fetchall())

cur.execute("select stu_name from student where stu_marks>=75")
print(cur.fetchall())

cur.execute("select stu_name from student where stu_course='python'")
print(cur.fetchall())

cur.execute("select *from student where stu_id=102")
print(cur.fetchall())

cur.execute("update student set stu_marks=85 where stu_id=102")
conn.commit()
print(cur.fetchall())

cur.execute("delete from student where stu_id=105")
conn.commit()
print(cur.fetchall())

cur.execute("select *from student")
print(cur.fetchall())

#PART-B ADVANCED QUERIES


# cur.executemany("""insert into student values(?,?,?,?,?)""",[(106,'greesh',25,'python',70),(107,'bharu',26,'java',80),(108,'laxmi',27,'python',90),(109,'sindhu',28,'java',100),(110,'mahalatha',29,'python',110),(111,'bhanu',30,'java',120),(112,'kalyan',31,'python',130),(113,'bhavya',32,'java',140),(114,'thanmayee',33,'python',150),(115,'greeshma',34,'java',160)])
conn.commit()

cur.execute("select stu_name,stu_marks from student order by stu_marks desc")              
print(cur.fetchall())

cur.execute("select stu_name,stu_marks from student order by stu_marks limit 3")
print(cur.fetchall())

cur.execute("select count(*) from student")
print(cur.fetchall())

cur.execute("select avg(stu_marks) from student")
print(cur.fetchone())

cur.execute("select max(stu_marks) from student")
print(cur.fetchone())

cur.execute("select min(stu_marks) from student")
print(cur.fetchone())

cur.execute("select stu_name from student where stu_name like 's%'")
print(cur.fetchall())

cur.execute("select stu_course,count(*) from student group by stu_course")
print(cur.fetchall())

cur.execute("select stu_course,avg(stu_marks) from student group by stu_course")
print(cur.fetchall())

cur.execute("select stu_name,stu_marks from student where stu_marks between 60 and 90")
print(cur.fetchall())

try:
    cur.execute("select * from students")
    print(cur.fetchall())
except sqlite3.Error as e:
    print("An error occurred: ",e)
finally:
    conn.close()

    




 
