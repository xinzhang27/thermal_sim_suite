# encoding: utf-8
import odbAccess
import numpy as np

myOdb = odbAccess.openOdb(r"D:\temp\Job-1.odb", readOnly=False)
myFrames = myOdb.steps["Step-1"].frames
myField = myFrames[-1].fieldOutputs
myValues = myField["HFL"].values
data = []
n = 0
temp = []
for value in myValues:
    n += 1
    temp.append(value.data[1])
    if n == 8:
        data.append(np.mean(temp))
        n = 0
        temp = []


data = np.mean(data)
K = abs(data*50/980)
with open(r"D:\temp\material analysis\material analysis.txt",'w') as f:
   f.write(str(K))