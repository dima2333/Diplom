help ('modules')
#Для подобных целей я использовал psutil библиотеку. Некоторые подсказки:
#
#перечислить процессы с помощью psutil.pids() (ссылка)
#проверить информацию процесса с помощью process = psutil.Process(pid) (ссылка)
#do process.kill или process.terminate()
#Установка на windows - pip будет выполнять установку из исходного кода (что означает компиляцию), 
# поэтому вы, вероятно, захотите загрузить двоичную установку из 

#psutil.process_iter()

#, если вам нужен список имен процессов, вы можете сделать что-то вроде:
#
#Например, если вам нужен список имен процессов, вы можете сделать что-то вроде:

#[p.name() for p in psutil.process_iter()]) for p in psutil.process_iter()]

#Большое спасибо за помощь. Получившийся работающий код:
#
#def ipconf_cmd():
#   text = subprocess.check_output('ipconfig')
#   decoded = text.decode('cp866')
#   Path('~/output.txt').expanduser().write_text(decoded)