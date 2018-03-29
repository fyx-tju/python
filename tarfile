#tar文件解压
import os
import tarfile

file = os.path.join("/home/fyx","a")
statinfo = os.stat(file)
print statinfo.st_size
if not os.path.exists("/home/fyx/a"):
  tarfile.open("a.tar.gz",'r:gz').extractall("/home/fyx/")
