import subprocess
from datetime import timedelta, datetime
import sqlite3

conn = sqlite3.connect("mon.db")
cursor = conn.cursor()

pingOff      = GET["pingOff"]
#pingOff      = "192.168.92.139 192.168.93.207 192.168.93.248 192.168.93.70"
pingOff      = pingOff.rstrip(" ")
pingOff      = pingOff.split(" ")

isFirst = True

print("[")
for i in range(len(pingOff)):
    cursor.execute("select ipadress, time_d, time_t from serv where ipadress='" + pingOff[i] + "' and id = (select max(id) from serv where ipadress='" + pingOff[i] + "')")
    r = cursor.fetchone()
    if r == None:
        break
    time_tmp1       = r[1].split(".")
    time_pc_day     = time_tmp1[0]
    time_pc_month   = time_tmp1[1]
    time_pc_year    = time_tmp1[2]
    time_tmp2       = r[2].split(":")
    time_pc_hours   = time_tmp2[0]
    time_pc_min     = time_tmp2[1]
    time_pc_sec     = time_tmp2[2]
    time_now        = datetime.now()
    time_pc         = datetime(int(time_pc_year), int(time_pc_month), int(time_pc_day), int(time_pc_hours), int(time_pc_min), int(time_pc_sec))
    result          = time_now - time_pc
    result          = int(result.total_seconds())
    if isFirst == False:
        print(', ')
    s = ('{ "IPadress":"'+ str(r[0]) + '", "sec":"' + str(result) + '" }')
    print(s)
    if isFirst == True:
        isFirst = False
print("]")

#arg = 'ping -n 3 ' + pingOff[i]
#p = subprocess.Popen(arg, stdout=subprocess.PIPE).communicate()[0].decode('cp866')
#ttl = 'TTL'
#Count = p.count(ttl)