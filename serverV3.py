from socket import *
from threading import *
import sys
import urllib.parse

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

        while self.__isRun == True :
            #print("\nСервер ожидает запрос на установление соединения")
            try :
                client, address = self.__server.accept()       # кортеж из 2 элементов
            except :
                continue
            #print("Соединение установлено : ", client.getpeername())
            #print("address = ", address[0] + " : " + str(address[1]))

            onlinelist.append(client.getpeername())
            T = ClientThread(client)
            T.setDaemon(True)
            T.start()

    def stop(self) :
        self.__isRun    = False
        self.__server.close()

class ClientThread(Thread):
    def __init__(self, client):
        super().__init__()
        self.__client = client

    def run(self):
        while True :
        # ------------получаем и обрабатываем полученный запрос от клиента ---------------------
            data = self.__client.recv(4096)
            if len(data) == 0 :                 # если получено 0 байт, то это разрыв соединения
                break
            #print("получено от клиента : \n", data.decode("utf-8"))  #меняем 11.05.19
        # ------------обрабатываем полученный запрос ---------------------
            msg = self.handleRequest(data.decode('utf-8'))

        # ------------отправляем ответ клиенту ---------------------------
            self.__client.send(msg.encode('utf-8'))
        #print("Connection closed", self.__client.getpeername())
        onlinelist.remove(self.__client.getpeername())
        self.__client.close()
    
    def handleRequest(self, request):
        #------- получение имени запрашиваемого файла -----------
        arrFilds        = request.split("\r\n")
        arrFirstLine    = arrFilds[0].split(" ")
        #print("Имя файла : ", arrFirstLine[1])
        
        #-------- arrFirstLine[0] ===> GET или POST
# проверка наличия переменной в locals (локальной переменной) :
# if 'myVar' in locals():
#       myVar exists
# проверка наличия переменной в globals (глобальной переменной) :
# if 'myVar' in globals():
#       myVar exists
        if arrFirstLine[0] == "GET" :
            if arrFirstLine[1].find("?") != -1:
                tmp = arrFirstLine[1].split("?")
                arrFirstLine[1] = tmp[0]        # Перед знаком вопроса - имя файла
                                                # tmp[1] - строка "имя=значение&имя=значение"
                tmp = tmp[1].split("&")         # tmp - список элемнтов "имя=значение"
                globals()["GET"] = {}                   # GET пустой словарь с добавлением в глобальные переменные
                for item in tmp :
                    v = item.split("=")
                    GET[v[0]] = urllib.parse.unquote(v[1])
                    print("Key : ", v[0], ", Value : ", urllib.parse.unquote(v[1]))

        elif arrFirstLine[0] == "POST" :
            tmp = request.split("\r\n\r\n")     # tmp[0] - заголовок, tmp[1] - тело HTTP запроса
            tmp = tmp[1].split("&")             # tmp - список элементов "имя=значение"
            globals()["POST"] = {}                   # POST пустой словарь с добавлением в глобальные переменные
            for item in tmp :
                v = item.split("=")
                POST[v[0]] = urllib.parse.unquote(v[1])
                print("Key : ", v[0], ", Value : ", urllib.parse.unquote(v[1]))
        try :
            f = open("." + arrFirstLine[1], "r", encoding="utf-8" )
            allText = f.read()
            #print(allText)
            buf    = allText.encode("utf-8")
            length = str(len(buf))

            contentType = "Content-Type: text/html; charset=utf-8\r\n"

            if arrFirstLine[1].endswith(".css") :
                contentType = "Content-Type: text/css; charset=utf-8\r\n"
            elif arrFirstLine[1].endswith(".png") :
                contentType = "Content-Type: image/png; charset=utf-8\r\n"
                length = len(allText)
            elif arrFirstLine[1].endswith(".jpg") :
                contentType = "Content-Type: image/jpg; charset=utf-8\r\n"
                length = len(allText)
            elif arrFirstLine[1].endswith(".py") :               
                contentType = "Content-Type: text/html; charset=utf-8\r\n"
            #elif arrFirstLine[1].endswith(".zip") :               
            #    contentType = "Content-Type: application/zip; charset=utf-8\r\n"
            #    length = len(allText)
                # создаем экземпляр объекта 
                from io import StringIO
                codeOut = StringIO()        # буфер в который будут попадать данные, выводимые print
                sys.stdout = codeOut
                exec(allText)               # allText - файлик, который запрашивает браузер
                sys.stdout = sys.__stdout__
                allText = codeOut.getvalue()
                codeOut.close()
                mybytes = bytes(allText, 'utf-8')
            #    length = str(len(allText))
                length = str(len(mybytes))  # Считаем колличество байтов а не симоволов

            msg = "HTTP/1.1 200 OK\r\n" + contentType + "Content-Length: " + str(length) + "\r\n" + "Connection: close\r\n\r\n" + allText
            #print(allText)
            f.close()
        except Exception as e:
            print(e)
            msg = "HTTP/1.1 404 NOT FOUND\r\n" + "Content-Type: text/html; charset=utf-8\r\n" + "Content-Length: 0\r\n" + "Connection: close\r\n\r\n" 
        #------- возврат ответа --------------
        return msg 

IP = "192.168.0.102"
#IP = "192.168.92.25"
#IP = "10.3.11.11"
S = Server(IP, 80)
S.start()

onlinelist = list()
while True :
    value = input("Press <Enter> to exit or press 1 to show clients online")
    if  len(value) == 0 :
        break
    for item in onlinelist :
        print(item)
S.stop()