print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width = device-width, initial-scale=1, shrink-to-fit= no">
<title>Change employee</title>
</head>
<body>
""")
id          = POST["id"]
NameCh      = POST["NameCh"]
IPadressCh  = POST["IPadressCh"]

import sqlite3

conn = sqlite3.connect("mon.db")
cursor = conn.cursor()
query = "update pc set name=?, ipadress=? where id=?"
cursor.execute(query, [NameCh, IPadressCh, id])
conn.commit()
conn.close()

print("</body>")
print("</html>")