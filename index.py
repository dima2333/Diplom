import sqlite3
import sys
conn = sqlite3.connect("mon.db")
cursor = conn.cursor()
cursor.execute("select count(*) from pc")
countPC = cursor.fetchone()

cursor.execute("select * from pc")
print("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width = device-width, initial-scale=1, shrink-to-fit= no">
<title>Система мониторинга</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<link rel="stylesheet" href="./stmon.css">
<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
</head>

<body>""")

print("""
<nav class='navbar navbar-default navbar-dark navbar-expand-md bg-info sticky-top'>
    <div class='container'>
        <div class='navbar-header'>
            <button class='navbar-toggler' type='button' data-toggle='collapse' 
                    data-target='#colNav' 
                    aria-controls='#colNav' 
                    aria-expanded='false' 
                    aria-label='Toggle navigator'>
                    <span class='navbar-toggler-icon'></span>
            </button>
        </div>
        <h3 class='text-light'>Мониторинг серверов</h3>
        <div class='collapse navbar-collapse' id='colNav'>
            <ul class='navbar-nav ml-auto'>
                <li class='nav-item'>
                    <a class='nav-link' href='#' id='addPC'><h5>Добавить сервер</h5></a>
                </li>
                <li class='nav-item'>
                    <a class='nav-link' href="https://drive.google.com/uc?id=1eQQT2GUhIib6F19RGNmKRZKXOMdKa-pM&export=download" download><h5>Скачать клиент</h5></a>
                </li>
            </ul>
        </div>
    </div>
</nav>
""")
print("<br />")
if countPC[0] == 0:
    print("<h3 class='text-danger text-center'>Нет серверов для отображения</h3>")
else:
    print("<div class='container'>")
    print("<div class='card-columns'>")
    while True:
        r = cursor.fetchone()
        if r == None:
            break
        print("<div class='card'>")
        print("<h4 class='card-header' id='nameServ"+ str(r[0]) + "'>" + str(r[1]) + "</h4>")
        print("""<div class="card-body">
                    <table>
                        <tr>
                            <td>IP:</td>""")
        print("<td id='IP" + str(r[0]) + "'>"+ r[2] + "<td>")
        print("""<tr>
                        <tr>
                            <td>OS:</td>""")
        print("<td id='OS"+ str(r[0]) + "'>" + r[3] + "<td>")
        print("""<tr>
                        <tr>
                            <td>Stat:</td>""")
        print("<td id='status"+ str(r[0]) + "'></td>")
        print("</tr>")
        print("<tr>")
        print("<td colspan='2'><button class='btn btn-outline-info btn-block' id='sys"+ str(r[0]) +"'>Подробнее о системе...</button></td>")
        print("</tr>")
        print("""</table>
                </div>
                <div class='card-footer text-center'>""")
        print("<button class='btn btn-outline-primary btnCh' id='btnCh"+ str(r[0]) +"'>Изменить</button>")
        print("<button class='btn btn-outline-primary btnDel' id='btnDel"+ str(r[0]) +"'>Удалить</button>")
        print("</div></div>")
    print("</div>")
    print("</div>")
conn.close()
# footer
print("""
<footer class="page-footer footer fixed-bottom bg-info text-light">
    <div class="container">
        <dov class="row">
            <div class="col text-center">&#169; 2019 Seriy Dmitriy. All right reserved</div>
        </div>
    </div> 
</footer>""")

#<!--MODAL ADD PC-->
print("""
<div class='modal fade' id='myModalAdd' tabindex='-1' role='dialog' aria-labelledby='myModalAdd' aria-hidden='true'>
    <div class='modal-dialog modal-dialog-centered' role='document'>
        <div class='modal-content'>
            <div class='modal-header'>
                <h5 class='modal-title text-info' id='myModalAddH5'>Добавление нового сервера</h5>
                <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                    <span aria-hidden='true'>&times;</span>
                </button>
            </div>
            <div class='modal-body'>
                <div class='container-fluid'>
                    <div class='form-group row'>
                        <label class='col-md-5 col-form-label' for='inputName'>Имя сервера :</label>
                        <input class='col-md-7 form-control' type='text' id='inputName'/>
                    </div>
                    <div class='form-group row'>
                        <label class='col-md-5 col-form-label' for='inputIPadress'>IP адрес :</label>
                        <input class='col-md-7 form-control' type='text' id='inputIPadress'/>
                    </div>
                </div>
            </div>
            <div class='modal-footer'>
                <button type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>
                <button type='button' class='btn btn-primary' id='btnSave'>Сохранить</button>
            </div>
        </div>
    </div>
</div>
""")
#<!--MODAL CHANGE PC-->
print("""
<div class='modal fade' id='myModalCh' tabindex='-1' role='dialog' aria-labelledby='myModalCh' aria-hidden='true'>
    <div class='modal-dialog modal-dialog-centered' role='document'>
        <div class='modal-content'>
            <div class='modal-header'>
                <h5 class='modal-title text-info' id='myModalChH5'>Изменение данных сервера</h5>
                <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                    <span aria-hidden='true'>&times;</span>
                </button>
            </div>
            <div class='modal-body'>
                <div class='container-fluid'>
                    <div class='form-group row'>
                        <label class='col-md-5 col-form-label' for='inputNameCh'>Имя сервера :</label>
                        <input class='col-md-7 form-control' type='text' id='inputNameCh'/>
                    </div>
                    <div class='form-group row'>
                        <label class='col-md-5 col-form-label' for='inputIPadressCh'>IP адрес : </label>
                        <input class='col-md-7 form-control' type='text' id='inputIPadressCh'/>
                    </div>
                </div>
            </div>
            <div class='modal-footer'>
                <button type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>
                <button type='button' class='btn btn-primary' id='btnSaveCh'>Сохранить</button>
            </div>
        </div>
    </div>
</div>
""")
#<!--MODAL MONITORING PC-->
print("""
<div class='modal fade' id='myModalMon' tabindex='-1' role='dialog' aria-labelledby='myModalMon' aria-hidden='true'>
    <div class='modal-dialog modal-dialog-centered modal-lg' role='document'>
        <div class='modal-content'>
            <div class='modal-header'>
                <h5 class='modal-title text-info' id='myModalMonH5'>Информация по серверу </h5>
                <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                    <span aria-hidden='true'>&times;</span>
                </button>
            </div>
            <div class='modal-body'>
                <div class='container-fluid'>
                    <div class='row'>
                        <div class='col-3'></div>
                        <div class='col-9' id='CPUname'></div>
                    </div>
                    <div class='form-group row'>
                        <label class='col-md-2 col-form-label' for='drawingCPU'>Средняя загрузка CPU:</label>
                        <div class='nadCPU'>50%</div>
                        <canvas id="drawingCPU" width="620" height="100"></canvas>
                    </div>
                    <div class='row'>
                        <div class='col-3'></div>
                        <div class='col-9' id='RAMname'></div>
                    </div>
                    <div class='form-group row'>
                        <label class='col-md-2 col-form-label' for='drawingRAM'>Средняя загрузка RAM:</label>
                        <div class='nadRAM'>50%</div>
                        <canvas id="drawingRAM" width="620" height="100"></canvas>
                    </div>
                    <div class='row'>
                        <div class='col-3'></div>
                        <div class='col-9' id='HDDname'></div>
                    </div>
                    <div class='form-group row'>
                        <label class='col-md-2 col-form-label' for='drawingHDD'>Средняя загрузка HDD:</label>
                        <div class='nadHDD'>50%</div>
                        <canvas id="drawingHDD" width="620" height="100"></canvas>
                    </div>
                </div>
            </div>
            <div class='modal-footer'>
                <button id="CloseModal" type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>
            </div>
        </div>
    </div>
</div>
""")

print("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

<script>
$(document).ready(
    function()
    {
        // мониторинг и опрос серверов о доступности
        pingOff  = "";
        $("td[id^='IP']").each(
            function(index, element)
            {
                IPonly = $(this).text();
                pingOff = pingOff + $(this).text() + " ";
            });
            work_status(pingOff);
            intervalIDstatus = setInterval("work_status(pingOff)", 60000)
        
        // вызов модального окна отрисовки параметров мониторинга
        $('.btn[id^="sys"]').click(
            function(e)
            {
                $("#myModalMon").modal("handleUpdate");
                $("#myModalMon").modal("show");
                cnt = e.target.id.slice(3);
                work_modal(cnt);
                intervalID = setInterval("work_modal(cnt)", 10000)
            });     
        
        // кнопка удаления ПК из мониторинга
        $('.btnDel').on('click.btnDel', function(e)
            {
                cnt = e.target.id.slice(6);
                $.ajax(
                {
                    method: "POST",
                    url: "monDelPC.py",
                    data: { id: cnt },
                    success: function(data) 
                    {
                        location.href='index.py'
                    }
                });
            });

        // кнопка изменения параметров ПК в мониторинге
        $('.btnCh').on('click.btnCh', function(e)
            {
                $("#myModalCh").modal("show");
                cnt = e.target.id.slice(5);                              
                $("input#inputNameCh").val($('#nameServ' + cnt).text());
                $("input#inputIPadressCh").val($('#IP' + cnt).text());
            });           
        
        // кнопка сохранения изменений карточки ПК мониторинга
        $("#btnSaveCh").click(
            function(e)
            {
                if (($("#inputNameCh").val() != "") && ($("#inputIPadressCh").val() != ""))
                {
                    NameCh  = $("input#inputNameCh").val();
                    reg = /^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$/
                    IPadressCh = $("input#inputIPadressCh").val();          
                    if (reg.test(IPadressCh) == true)
                    {
                        $.ajax(
                        {
                            method: "POST",
                            url: "monChPC.py",
                            data: { 
                                id: cnt,
                                NameCh : NameCh,
                                IPadressCh : IPadressCh,
                                },
                            success: function(data) 
                            {
                                location.href='index.py'
                            }
                        });
                        $("#myModalCh").modal("hide");
                    }
                    else
                    {
                        alert("Введите корректное значение! Формат ввода: 255.255.255.255")
                    }    
                }
                else
                {
                    alert('Одно или несколько полей не заполненно!')
                };
            });
                
        // вызов модального окна добавления ПК в мониторинг
        $("#addPC").click(
            function()
            {
                $("#myModalAdd").modal("show");
            });
                
        // сохранение информаци после добавления ПК в мониторинг
        $("#btnSave").click(
            function()
            {
                if ($("#inputName").val() != "" && ($("#inputIPadress").val() != ""))
                {
                    var inputName  = $("#inputName").val()
                    reg = /^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$/
                    var inputIPadress = $("#inputIPadress").val()
                    if (reg.test(inputIPadress) == true)
                    {
                        $.ajax(
                        {
                            method: "POST",
                            url: "monAddPC.py",
                            data: { 
                                inputName : inputName,
                                inputIPadress : inputIPadress,
                                },
                            success: function(data) 
                            {
                                location.href='index.py'
                            }
                        });
                        $("#myModalAdd").modal("hide");
                    }
                    else
                    {
                        alert("Введите корректное значение! Формат ввода: 255.255.255.255")
                    }
                }
                else
                {
                    alert('Одно или несколько полей не заполненно!')
                };
            });
        
        //обработчик закрытия модального окна статистики, по закрытию останавливает работу функции отрисовки в интервале 
        $("button#CloseModal").click(
            function()
            {
                clearInterval(intervalID);
            });
});
// функция опроса статусов серверов
function work_status(pingOff)
{
    $.ajax("servStatus.py",
    {
        success: 
            function(data, textStatus, jqXHR)
            {
                var obj = JSON.parse(jqXHR.responseText);                        
                for (i = 0; i < obj.length; i++)
                    if (obj[i].sec <= 3600)
                    {
                        //alert("Сервер " + obj[i].IPadress + " онлайн")
                        var serv = obj[i].IPadress
                        var text = $("td[id^='IP']").filter(function(index, value)
                        {
                            if ($(this).text() == serv)
                            {
                                var s = $(this).attr('id');
                                s = s.slice(2);
                                s = "status"+s;
                                var content = document.getElementById(s);
                                content.innerHTML = "<div></div>";
                                content.innerHTML = "<div class='col-4 divON'>ON</div>";
                            }
                        });
                    }
                    else
                    {
                        //alert("Сервер " + obj[i].IPadress + " давно не выходил на связь")
                        var serv = obj[i].IPadress
                        var text = $("td[id^='IP']").filter(function(index, value)
                        {
                            if ($(this).text() == serv)
                            {
                                var s = $(this).attr('id');
                                s = s.slice(2);
                                s = "status"+s;
                                var content = document.getElementById(s);
                                content.innerHTML = "<div></div>";
                                content.innerHTML = "<div class='col-4 divOFF'>OFF</div>";
                            }
                        });
                    }
                },
        data: 
            {
                "pingOff" : pingOff
            },
    });   
}

// функция отрисовки графиков
function work_modal(cnt)
{
    $.ajax("servSelectCPU.py",
    {
        success :
            function(data, textStatus, jqXHR)
            {
                var obj = JSON.parse(jqXHR.responseText);
                // *********** CPU ***********************//
                $('#CPUname').text("");
                $('#CPUname').text("Название CPU : " + obj[0].cpu_name);
                var canvas = document.getElementById("drawingCPU");
                var context = canvas.getContext("2d"); 
                var step = 32;
                var startPX = 0;
                var startPY = 100;

                // очистка холста перед рисованием
                context.clearRect(0, 0, context.canvas.width, context.canvas.height);
                context.beginPath();
                context.strokeStyle = "#16a2b8";
                context.lineWidth = 1;
                context.setLineDash([0])
                context.moveTo(startPX, startPY - obj[0].cpu_percent);
                for (i = 1; i < obj.length; i++)
                {
                    startPX += step;
                    context.lineTo(startPX, startPY - obj[i].cpu_percent);
                }
                                context.lineWidth = 1;
                context.stroke();

                context.beginPath();
                context.strokeStyle = "#FF0000";
                context.lineWidth = 1;
                context.setLineDash([4,2])
                context.moveTo(0, 50)
                context.lineTo(620, 50)
                context.stroke();

                // *********** RAM **************************//
                $('#RAMname').text("");
                $('#RAMname').text("Общий объем памяти RAM : " + obj[0].ram_total + " Гб");
                var canvas = document.getElementById("drawingRAM");
                var context = canvas.getContext("2d"); 
                var step = 32;
                var startPX = 0;
                var startPY = 100;
                
                // очистка холста перед рисованием
                context.clearRect(0, 0, context.canvas.width, context.canvas.height);
                context.beginPath();
                context.strokeStyle = "#16a2b8";
                context.lineWidth = 1;
                context.setLineDash([0])
                context.moveTo(startPX, startPY - obj[0].ram_percent);
                for (i = 1; i < obj.length; i++)
                {
                    startPX += step;
                    context.lineTo(startPX, startPY - obj[i].ram_percent);
                }
                context.stroke();

                context.beginPath();
                context.strokeStyle = "#FF0000";
                context.lineWidth = 1;
                context.setLineDash([4,2])
                context.moveTo(0, 50)
                context.lineTo(620, 50)
                context.stroke();

                // *********** HDD **************************//
                $('#HDDname').text("");
                $('#HDDname').text("Общий объем жестких дисков HDD : " + obj[0].hdd_total + " Гб");
                var canvas = document.getElementById("drawingHDD");
                var context = canvas.getContext("2d"); 
                var step = 32;
                var startPX = 0;
                var startPY = 100;
                // очистка холста перед рисованием
                context.clearRect(0, 0, context.canvas.width, context.canvas.height);
                context.beginPath();
                context.strokeStyle = "#16a2b8";
                context.lineWidth = 1;
                context.setLineDash([0])
                context.moveTo(startPX, startPY - obj[0].hdd_percent);
                for (i = 1; i < obj.length; i++)
                {
                    startPX += step;
                    context.lineTo(startPX, startPY - obj[i].hdd_percent);
                }
                context.stroke();

                context.beginPath();
                context.strokeStyle = "#FF0000";
                context.lineWidth = 1;
                context.setLineDash([4,2])
                context.moveTo(0, 50)
                context.lineTo(620, 50)
                context.stroke();
            },
        data :
            {
                "id" : cnt
            }
    });
};
</script>
</body>
</html>""")