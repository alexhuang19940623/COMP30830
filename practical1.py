import os
import commands
import string
import socket
import json
def base_info():
    """
    :return HOSTNAME, IPADDR, CPU, CPUIDLE, MEM, AVAI_MEM, VERSION(6/7), MACHINE(64/32)
    """
    ifname='eth0'
    osinfo = os.uname()
    HOSTNAME = osinfo[1]
    VERSION  = osinfo[2].split('.')[-2]
    MACHINE  = osinfo[-1]
    mem_cmd = "awk '/MemTotal/{printf(\"%0.2f\",$2/1000/1000)}' /proc/meminfo"
    MEM = int(round(float(commands.getoutput(mem_cmd))))
 
    cpu_cmd = "awk '/processor/{cpu+=1}END{print cpu}' /proc/cpuinfo"
    CPU = commands.getoutput(cpu_cmd)
    if VERSION == 'el7':
        avai_mem_cmd = "awk '/MemAvailable/ {printf(\"%0.2f\",$2/1000/1000)}' /proc/meminfo"
        AVAI_MEM =  commands.getoutput(avai_mem_cmd)
        cpuidle_cmd = "top -bcn 1 | head |awk '/Cpu/ {print $8}'"
        CPUIDLE = commands.getoutput(cpuidle_cmd)
    if VERSION == 'el6':
        ##centos6 可用内存计算方法:MemFree+Buffers+Cached
        avai_mem_cmd = "sed -n '2,4p' /proc/meminfo |awk '{sum+=$2}END{printf(\"%.2f\",sum/1000/1000)}'"
        AVAI_MEM =  commands.getoutput(avai_mem_cmd)
        cpuidle_cmd = "top -bcn 1 | sed -n 's/ //g;3p' | awk -F\"%|,\" '{print $7}'"
        CPUIDLE = commands.getoutput(cpuidle_cmd)
    unix_socker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IPADDR = socket.inet_ntoa(fcntl.ioctl(
        unix_socker.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
 
    return HOSTNAME, IPADDR, CPU, CPUIDLE, MEM, AVAI_MEM, VERSION, MACHINE