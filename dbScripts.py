import sqlite3
from datetime import datetime
conn = sqlite3.connect('Dodhia.db')
cursor=conn.cursor()
#cursor.execute("INSERT INTO requestTable VALUES ('1410','Sickness','Mercy','254','Paul','202','Pending')")
cursor.execute("SELECT * FROM managerTable")
#cursor.execute('ALTER TABLE requestTable ADD COLUMN status text')


print("done")
print(cursor.fetchall())

conn.commit()
#Close Database connection
conn.close()
