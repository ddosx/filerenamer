import os
import sys
from colorama import Fore, Back, Style
import subprocess
from rich.console import Console
from rich.progress import track
from tqdm import tqdm
import tkinter.messagebox

if sys.platform == 'win32':
    mvcom = 'move'
else:
    mvcom = 'mv'

args = sys.argv[1:]
if len(args) != 3:
    # print(Fore.RED + 'Ошибка в ввдении аргментов командной строки')
    # print(Fore.WHITE + 'python3' + Fore.CYAN + ' app.py ' + Fore.GREEN + ' директория '+Fore.MAGENTA + 'старое-расширение новое-расширение'+Style.RESET_ALL)
    tkinter.messagebox.showerror('Ошибка', 'Ошибка в ввдении аргментов командной строки \n python3 app.py  директория старое-расширение новое-расширение')
    exit()

console = Console()
dirarg = [args[0],args[0].split('/')]

originex = args[1]
newex = args[2]
dir = dirarg[0]

files = os.listdir(dir)
filecount = len(files)
filepercent = 100/filecount
completepercent = 0
i = 0

with console.status("[bold green]Отдумка...") as status:
    for file in tqdm(files):
        completepercent += filepercent
        i += 1
        if '.'+str(file.split('.')[-1]) == originex:
            filex = dirarg[0]+'/'+file
            fileq = '.'.join((file.split('.')[0:-1]))
            if newex == '.zero':
                files = dirarg[0]+'/'+fileq
            else:
                files = dirarg[0]+'/'+fileq+newex
            subprocess.run(['mv', filex, files])

        completeq  = str(completepercent).split('.')[1]
        completew = completeq[0:1]
        completee = str(completepercent).split('.')[0]
        complete = str(completee) + '.' +str(completew)
        task = str(i) + '/' +str(filecount) + str(' ')+str(complete)+'%/100%'

tkinter.messagebox.showinfo('Успех', 'Переименование прошло успешно!')