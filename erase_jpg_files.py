import os 
import re

direc =  "D:\SASS\colisions"

for filename in os.listdir(direc):
    f = str(os.path.join(direc,filename))
    reguala = re.search(r".jpg$", f)
    if reguala:
        os.remove(os.path.join(direc,filename))
