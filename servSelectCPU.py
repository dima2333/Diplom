id      = GET["id"]
import sqlite3
conn = sqlite3.connect("mon.db")
cursor = conn.cursor()
cursor.execute("select ipadress from pc where id='" + str(id) + "'")
IPadress = cursor.fetchone()

cursor.execute("select cpu_percent, cpu_name, ram_total, ram_percent, disk_total, disk_percent from serv where ipadress='" + str(IPadress[0]) + "' order by id DESC LIMIT 21")
isFirst = True
print('[')
while True:
    r = cursor.fetchone()
    if r == None:
        break
    if isFirst == False:
        print(', ')
    s = ('{ "cpu_percent":"'+ str(r[0]) + '", "cpu_name":"' + str(r[1]) + '", "ram_total":"' + str(r[2]) + '", "ram_percent":"' + str(r[3]) + '", "hdd_total":"' + str(r[4]) + '", "hdd_percent":"' + str(r[5]) + '" }')
    print(s)
    if isFirst == True:
        isFirst = False
print(']')
conn.commit()
conn.close()