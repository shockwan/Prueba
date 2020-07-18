import os

shutdown = input("Quieres apagar tu computador Si/No: ")
if shutdown == 'No':
    exit()
else:
    os.system("systemctl poweroff")   