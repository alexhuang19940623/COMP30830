import platform
import socket
import multiprocessing
import psutil
from setuptools import setup, find_packages
 
setup(
    name='pip_setup',
    version='0.1.0',
    description='just for test',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='bin381',
    url='https://github.com',
    author_email='',
    license='MIT',
    packages=find_packages(),#需要处理哪里packages，当然也可以手动填，例如['pip_setup', 'pip_setup.ext']
    include_package_data=False,
    zip_safe=True,
)

def showinfo(tip, info):
    print("{}:{}".format(tip,info))


showinfo('Machine name', platform.node())
showinfo('OS version',platform.version())
showinfo('OS name', platform.system())
showinfo('OS bit', platform.architecture())
showinfo('CPU version', platform.processor())
showinfo('CPU numbers', multiprocessing.cpu_count())
showinfo('Amount of memories', psutil.virtual_memory().total)
showinfo('IP address', socket.gethostbyname(socket.gethostname()))