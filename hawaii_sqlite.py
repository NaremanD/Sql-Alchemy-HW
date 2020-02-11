import os
import sqlite3

db_path = os.path.join("Resources", "hawaii.sqlite")

conn = sqlite3.connect(db_path)
csr = conn.cursor()

cmd = "SELECT name FROM sqlite_master WHERE type = 'table'"
csr.execute(cmd)
tables = csr.fetchall()
print(tables)

cmd = "select * from measurement "
csr.execute(cmd)
data = csr.fetchall()
print(data)

cmd = "select * from station "
csr.execute(cmd)
data = csr.fetchall()
print(data)
