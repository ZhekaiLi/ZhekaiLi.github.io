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

**Simplest Example**:
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

### Ex.1: Create table, insert rows and read rows
**Create table and insert rows**
```py
db = sqlite3.connect("test.db")
cur = db.cursor()

cur.execute("Create table if not exists tb (a Text, b Text)")
cur.execute("Insert into tb values ('one', 'two')")
cur.execute("Insert into tb values ('three', 'four')")
db.commit() # commit the change
```

**Two methods to read rows**
```py
cur.execute("Select * from tb")

# Read rows one by one
row = cur.fetchone()
while row: # 每执行一次，便往下读一行，直到读完
    print(row)
    row = cur.fetchone()

# Read all rows and iterrate
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
db.close()
```

## Execute 
### 执行单条 SQL 语句
`cur.execute()`

Examples:

```py
cur.execute("Select * from tb")

query = "Select * from tb where a = ?"
cur.execute(query, ('one',))
```
### 批量执行
`cur.executemany()`

常用于批量插入数据

```py
cur.execute("Create table if not exists tb (a Text, b Text)")
values = (
    ('one', 'two'),
    ('three', 'four')
)
insert_statement = "Insert into tb VALUES (?, ?)"
cur.executemany(insert_statement, values)
```
