from socket import *
import socket
import platform
import cpuinfo
import psutil

from datetime import datetime
import sqlite3

f = open("confIPserver.conf", "r")
addrServer = f.readline()
f.close()

my_ip           = socket.gethostbyname_ex(socket.gethostname())
ram = psutil.virtual_memory().total / 1000000000
ram_u = psutil.virtual_memory().used / 1000000000
disk = psutil.disk_usage('/').total / 1000000000
disk_u = psutil.disk_usage('/').used / 1000000000

name            = socket.gethostname()
ipadress        = my_ip[2][0]
os              = platform.platform()
time_d          = str(datetime.now().strftime('%d.%m.%Y'))
time_t          = str(datetime.now().strftime('%H:%M:%S'))
cpu_name        = cpuinfo.get_cpu_info()['brand']
cpu_percent     = psutil.cpu_percent(interval=1)
cpu_count_l     = psutil.cpu_count(logical=True)
cpu_count_f     = psutil.cpu_count(logical=False)
ram_total       = round(ram, 2)
ram_percent     = psutil.virtual_memory().percent
ram_used        = round(ram_u,2)
disk_total      = round(disk, 2)
disk_percent    = psutil.disk_usage('/').percent
disk_used       = round(disk_u,2)

strSend = str(name) + "|" + str(ipadress) + "|" + str(os) + "|" + str(time_d) + "|" + str(time_t) + "|" + str(cpu_name) + "|" + str(cpu_percent) + "|" + str(cpu_count_l) + "|" + str(cpu_count_f) + "|" + str(ram_total) + "|" + str(ram_percent) + "|" + str(ram_used) + "|" + str(disk_total) + "|" + str(disk_percent) + "|" + str(disk_used)

conn = sqlite3.connect("clientMon.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM client WHERE id NOT in (SELECT id FROM client ORDER BY id DESC LIMIT 100000)")
count = 0
while True:
    if count > 0 :
        break
    count += 1
    try:
        client = socket.socket(AF_INET, SOCK_STREAM)
        client.connect((addrServer, 5700))
        client.send(strSend.encode('utf-8'))
        client.close()
        query = "insert into client (name, ipadress, os, time_d, time_t, cpu_name, cpu_percent, cpu_count_l, cpu_count_f, ram_total, ram_percent, ram_used, disk_total, disk_percent, disk_used) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(query, [name, ipadress, os, time_d, time_t, cpu_name, cpu_percent, cpu_count_l, cpu_count_f, ram_total, ram_percent, ram_used, disk_total, disk_percent, disk_used])
    except ConnectionRefusedError as e:
        print(time_d + " " + time_t + "Идет установка соединения... осталось попыток : " + str(count))
        if type(e) == 'ConnectionRefusedError' :
            continue
conn.commit()
conn.close()