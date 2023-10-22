# encoding: utf-8
import odbAccess
import numpy as np

myOdb = odbAccess.openOdb(r"D:\temp\Job-1.odb", readOnly=False)
myFrames = myOdb.steps["Step-1"].frames
myField = myFrames[-1].fieldOutputs
HFL = myField["HFL"].values
U = myField["U"].values
temp3 = []
temp4 = []
temp5 = []
while len(temp4) < 441:
    temp4.append(U[len(temp4)].data[2])
while len(temp5) < 441:
    temp5.append(U[len(U)/2+len(temp5)].data[2])
for value in HFL:
    temp3.append(value.data[2])
data_u = np.mean(temp4) + np.mean(temp5)
data3 = np.mean(temp3)
K_z = abs(data3*(50+data_u)/980)
#result = [str(K_x)+'\n',str(K_y)+'\n',str(K_z)+'\n']
with open(r"D:\temp\material analysis\material analysis.txt",'w') as f:
   f.write(str(K_z))
#   f.writelines(result)