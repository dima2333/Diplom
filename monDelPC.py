print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width = device-width, initial-scale=1, shrink-to-fit= no">
<title>Del employee</title>
</head>
<body>
""")
id      = POST["id"]
#id      = 4
import sqlite3
id = int(id)
conn = sqlite3.connect("mon.db")
cursor = conn.cursor()
cursor.execute("select IPadress from pc where id=" + str(id))
r = cursor.fetchone()
delAll = r[0]
cursor.execute("delete from pc where id=" + str(id))
cursor.execute("delete from serv where IPadress='" + str(delAll) + "'")

conn.commit()
conn.close()

print("</body>")
print("</html>")