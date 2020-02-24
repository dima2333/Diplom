from socket import *
from datetime import datetime
from threading import *
import sqlite3
class Server(Thread):
    def __init__(self, ipaddr, port):
        super().__init__()
        self.__ipaddr   = ipaddr
        self.__port     = port
        self.__isRun    = True

    def run(self):
        self.__server = socket(AF_INET, SOCK_STREAM)
        self.__server.bind((self.__ipaddr, self.__port))
        self.__server.listen()

        print("\nСервер ожидает запрос на установление соединения...")
        while self.__isRun == True :
            try :
                client, address = self.__server.accept()       # кортеж из 2 элементов
            except :
                continue
            T = ClientThread(client)
            T.setDaemon(True)
            T.start()
            time_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            print('\nВремя : ' + str(time_now) + ' Соединился : ' + address[0] + " : " + str(address[1]))
    def stop(self) :
        self.__isRun    = False
        self.__server.close()

class ClientThread(Thread):
    def __init__(self, client):
        super().__init__()
        self.__client = client

    def run(self):
        while True :
            data = self.__client.recv(4096)
            if len(data) == 0 :
                break
            msg = data.decode('utf-8')
            msg = msg.split("|")
            name        = msg[0]        
            ipadress    = msg[1]   
            os          = msg[2] 
            time_d      = msg[3]
            time_t      = msg[4]
            cpu_name    = msg[5]
            cpu_percent = msg[6]
            cpu_count_l = msg[7]
            cpu_count_f = msg[8]
            ram_total   = msg[9]
            ram_percent = msg[10]
            ram_used    = msg[11]
            disk_total  = msg[12]
            disk_percent= msg[13]
            disk_used   = msg[14]
            conn = sqlite3.connect("mon.db")
            cursor = conn.cursor()
            query = "insert into serv (name, ipadress, os, time_d, time_t, cpu_name, cpu_percent, cpu_count_l, cpu_count_f, ram_total, ram_percent, ram_used, disk_total, disk_percent, disk_used) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
            cursor.execute(query, [name, ipadress, os, time_d, time_t, cpu_name, cpu_percent, cpu_count_l, cpu_count_f, ram_total, ram_percent, ram_used, disk_total, disk_percent, disk_used])
            cursor.execute("update pc set os='" + os + "' where ipadress ='" + ipadress + "'")
            conn.commit()
            conn.close()

        self.__client.close()
        return

IP      = ""
Port    = 5700
S = Server(IP, Port)
S.start()

while True :
    value = input("Нажмите <Enter> для выхода...")
    if  len(value) == 0 :
        break
S.stop()