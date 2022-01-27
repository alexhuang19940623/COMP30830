import platform
import socket
import multiprocessing
import psutil

def showinfo(tip, info):
    print("{}:{}".format(tip,info))


showinfo('Machine name', platform.node())
showinfo('OS version',platform.version())
showinfo('OS name', platform.system())
showinfo('OS bit', platform.architecture())
showinfo('CPU version', platform.processor())
showinfo('CPU numbers', multiprocessing.cpu_count())
showinfo('Amount of memories', psutil.virtual_memory().total)
showinfo('IP Address', socket.gethostbyname(socket.gethostname()))