print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width = device-width, initial-scale=1, shrink-to-fit= no">
<title>Add employee</title>
</head>
<body>
""")
inputName     = POST["inputName"]
inputIPadress = POST["inputIPadress"]

import sqlite3

conn = sqlite3.connect("mon.db")
cursor = conn.cursor()

query = "insert into pc (name, ipadress, os) values(?, ?, ?);"
cursor.execute(query, [inputName, inputIPadress, ''])
conn.commit()
conn.close()
print("</body>")
print("</html>")