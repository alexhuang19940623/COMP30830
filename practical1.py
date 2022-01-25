import platform
def showinfo(tip, info):
    print("{}:{}".format(tip,info))
 
 
showinfo("OS",platform.platform())
showinfo('OS version',platform.version())
showinfo('OS name', platform.system())
showinfo('OS bit', platform.architecture())
showinfo('Computer type', platform.machine())
showinfo('Computer name', platform.node())
showinfo('CPU version', platform.processor())
showinfo('Computer infomation', platform.uname())