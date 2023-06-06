---
layout: wiki
title: sqlite3
cate1: Python
cate2: -libs
description: 
keywords: Python
---

```py
import sqlite3
```

# 1. Quick Start
```py
# Connect Database (Create an instance of database interface)
db = sqlite3.connect(":memory:")

# Create a cursor for Query
cur = db.cursor()
# Execute a query
cur.execute("SELECT sqlite_version()")
# Read the query results
# cur.fetchone can fetch the first row of results
version = cur.fetchone()[0]
print(f"SQLite version {version}")

# Close curor and database
cur.close()
db.close()
```

## Ex.1: Create table, Insert rows and Read rows
- Create table and insert rows
- Read rows (three ways)
- <span style="background-color: yellow; color: black;">Read into pd.DataFrame</span>

### Create table and insert rows
```py
db = sqlite3.connect("test.db")
cur = db.cursor()

cur.execute('''
Create table if not exists tb (
    id Integer Primary Key,
    a Text, 
    b Text
)
''')
cur.execute("Insert into tb (a, b) values ('one', 'two')")
cur.execute("Insert into tb (a, b) values ('three', 'four')")
db.commit() # commit the change
```

### Read rows (three ways)
`cur.fetchone()`
`cur.fetchmany(n)`
`cur.fetchall()`

```py
cur.execute("Select * from tb")

# 1. Read rows one by one
row = cur.fetchone()
while row: # 每执行一次，便往下读一行，直到读完
    print(row)
    row = cur.fetchone()

# 2. Read exact number of rows
rows = cur.fetchmany(3)
print(rows)

# 3. Read all rows and iterrate
rows = cur.fetchall()
print(rows)

>>> 
[(1, 'one', 'two'), (2, 'three', 'four')]
```

### Read into pd.DataFrame
未经证实?

```py
query = "Select * from tb"
df = pd.read_sql(query, db)
```



# 2. Execute 
## 2.1 Single line
`cur.execute()`

Examples:

```py
cur.execute("Select * from tb")

query = "Select * from tb where a = ?"
cur.execute(query, ('one',)) # 这里小括号内有个逗号是因为 python 本身的机制: 单个元素的 tuple 如果不带逗号就不会被当作一个 tuple
```

## 2.2 Multiple lines
`cur.executemany()`

常用于批量插入数据

```py
cur.execute('''
Create table if not exists tb (
    id Integer Primary Key,
    a Text, 
    b Text
)
''')
values = [
    ['one', 'two'],
    ['three', 'four']
]
insert_statement = "Insert into tb (a, b) values (?, ?)"
cur.executemany(insert_statement, values)
```


