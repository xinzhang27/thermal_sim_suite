# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-25.0, 25.0), point2=(25.0, -25.0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=50.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].sketches['__profile__']



p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
p.DatumPlaneByOffset(plane=f[3], flip=SIDE2, offset=25.0)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d1 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d1[2], cells=pickedCells)




mdb.models['Model-1'].Material(name='Al')
mdb.models['Model-1'].materials['Al'].Density(table=((2.7e-17, ), ))
mdb.models['Model-1'].materials['Al'].Elastic(table=((69.0, 0.35), ))
mdb.models['Model-1'].materials['Al'].Expansion(table=((2.31e-05, ), ))
mdb.models['Model-1'].materials['Al'].Conductivity(table=((237.0, ), ))
mdb.models['Model-1'].Material(name='Cu')
mdb.models['Model-1'].materials['Cu'].Density(table=((8.96e-17, ), ))
mdb.models['Model-1'].materials['Cu'].Elastic(table=((110.0, 0.34), ))
mdb.models['Model-1'].materials['Cu'].Expansion(table=((1.7e-05, ), ))
mdb.models['Model-1'].materials['Cu'].Conductivity(table=((401.0, ), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Al', material='Al',
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Cu', material='Cu',
    thickness=None)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(cells=cells, name='Set-2')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Cu', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)




p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD,
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
    elemType3))



a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)


mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1',
    previous='Initial', response=STEADY_STATE, deltmx=None, cetol=None,
    creepIntegration=None, amplitude=RAMP)




a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#3 ]', ), )
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#7ff ]', ), )
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#fffff ]', ), )
v1 = a.instances['Part-1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#fef ]', ), )
region = a.Set(vertices=verts1, edges=edges1, faces=faces1, cells=cells1,
    name='Set-1')
mdb.models['Model-1'].Temperature(name='Predefined Field-1',
    createStepName='Initial', region=region, distributionType=UNIFORM,
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(20.0,
    ))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#100 ]', ), )
region = a.Set(faces=faces1, name='Set-2')
mdb.models['Model-1'].TemperatureBC(name='BC-1', createStepName='Step-1',
    region=region, fixed=OFF, distributionType=UNIFORM, fieldName='',
    magnitude=1000.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#40 ]',), )
region = a.Set(faces=faces1, name='Set-3')
mdb.models['Model-1'].TemperatureBC(name='BC-2', createStepName='Step-1',
    region=region, fixed=OFF, distributionType=UNIFORM, fieldName='',
    magnitude=20.0, amplitude=UNSET)



mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8,
    numDomains=8, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)


