

# Connect to Oracle

<center>

Author: Zhekai Li
Date: May 30, 2023
</center>

## 1. Download Oracle Client

(1) Download the client from the link: [https://www.oracle.com/database/technologies/instant-client.html](https://www.oracle.com/database/technologies/instant-client.html)

<img src="/images/2023-05/Snipaste_2023-05-30_13-38-27.png" width="70%">

(2) Extract the .zip file downloaded and open it, there should be a folder called <u>"instantclient_XX_XX"</u> (XX could be a number)

(3) Move that folder to any location you want, for example, I moved it to my C disk so that the path became <u>"C:\instantclient_21_10"</u>

## 2. Initialize Oracle Client

```py
import cx_Oracle
import pandas as pd

try:
    cx_Oracle.init_oracle_client(lib_dir= r"C:\instantclient_21_10")
except:
    print("Oracle is initialized before.")
```

## 3. Connect to Database

```py
dsn = cx_Oracle.makedsn(
    host="ivdwhdev.ad.skynet",
    port="1521", 
    service_name="IVDWHDEV.ad.skynet"
)

connection = cx_Oracle.connect('username', 'password', dsn)
```

You can try the following query for test

```py
query = "SELECT * FROM FPSINPUT.CAL_SHIFTS"
pd.read_sql(query, connection)
```




