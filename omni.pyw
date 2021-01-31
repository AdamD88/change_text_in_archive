import shutil
import os
import tkinter as tk
from tkinter import *
import subprocess
import time

global path_1
global path_2
global file_in
global file_out


#okno informujące o tym ze zostanie zamkniety thunderbird
def okienko():
    def countdown(time):
        if time == -1:
            window.destroy()
        else:
            if time == 0:
                label.configure(text="Dziękuję", font=("Arial Bold", 15))
            else:
                label.configure(text="Okno zamknie się za: %d seconds" % time,  font=("Arial Bold", 15))

            window.after(1000, countdown, time-1)
    window = tk.Tk()

    label = tk.Label(window, width=30)
    label.pack(padx=30, pady=30)
    countdown(15)
    window.geometry('700x200')
    window.title("Informacja")
    lbl = Label(window, text="System za 15 sekund zamknie program pocztowy,\n"
                             " po czym uruchomi go ponownie. Proszę zapisać swoją pracę.", font=("Arial Bold", 18))
    lbl.pack(padx=20, pady=20)

    window.mainloop()


okienko()


# ubicie programu thunderbird
try:
    os.system("TASKKILL /F /IM thunderbird.exe")
except:
    pass
time.sleep(1)
# sprawdzanie lokalizacji thunderbirda

if os.path.isdir("C:/Program Files (x86)/Mozilla Thunderbird"):
    path_1 = "Program Files (x86)"
    path_2 = "Program Files (x86)"
else:
    path_1 = "Program Files"
    path_2 = "Program Files"
print(path_2,path_1)
file_in = "C:/{}/Mozilla Thunderbird/omni.ja".format(path_1)
file_out = "C:/{}/Mozilla Thunderbird/omni2.ja".format(path_2)

with open(file_in, 'rb') as f:
    data = f.read()
    f.close()

data = data.replace(b'imapSubscribePrompt', b'imapSubscribePromtt')


with open(file_out, 'wb') as f:
    f.write(data)
    f.close()

# usunięcie pliku
os.remove("C:\{}\Mozilla Thunderbird\omni.ja".format(path_1))
# zmiana nazwy pliku
shutil.move("C:\{}\Mozilla Thunderbird\omni2.ja".format(path_2),
                "C:\{}\Mozilla Thunderbird\omni.ja".format(path_2))
subprocess.call("C:\{}\Mozilla Thunderbird\{}".format(path_1, "thunderbird.exe"))





