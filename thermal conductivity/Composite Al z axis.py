# -*- coding: utf-8 -*-
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

# 建模
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-25.0, 25.0), point2=(25.0, -25.0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=25.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(-25.0, 25.0), point2=(25.0, -25.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidExtrude(sketch=s1, depth=25.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
del mdb.models['Model-1'].sketches['__profile__']

# 属性
mdb.models['Model-1'].Material(name='Al')
mdb.models['Model-1'].materials['Al'].Density(table=((2.7e-17, ), ))
mdb.models['Model-1'].materials['Al'].Elastic(table=((69.0, 0.35), ))
mdb.models['Model-1'].materials['Al'].SpecificHeat(table=((8.8e14,),))
mdb.models['Model-1'].materials['Al'].Expansion(table=((2.31e-05, ), ))
mdb.models['Model-1'].materials['Al'].Conductivity(table=((237.0, ), ))
mdb.models['Model-1'].Material(name='Cu')
mdb.models['Model-1'].materials['Cu'].Density(table=((8.96e-17, ), ))
mdb.models['Model-1'].materials['Cu'].Elastic(table=((110.0, 0.34), ))
mdb.models['Model-1'].materials['Cu'].SpecificHeat(table=((3.9e14,),))
mdb.models['Model-1'].materials['Cu'].Expansion(table=((1.7e-05, ), ))
mdb.models['Model-1'].materials['Cu'].Conductivity(table=((401.0, ), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Al', material='Al',
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Cu', material='Cu',
    thickness=None)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-2']
p.SectionAssignment(region=region, sectionName='Cu', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

#网格
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]',), )
p.setMeshControls(regions=pickedRegions, technique=BOTTOM_UP)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#10 ]',), )
p.generateMesh(regions=pickedRegions, boundaryPreview=ON)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#10 ]',), )
pickedGeomSourceSide = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#20 ]',), )
pickedGeomTargetSide = regionToolset.Region(faces=faces)
v = p.vertices
v1 = p.vertices
vector = (v[0], v1[3])
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
p.generateBottomUpExtrudedMesh(cell=c[0],
    geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector,
    targetSide=pickedGeomTargetSide, numberOfLayers=10)
elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD,
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]',), )
pickedRegions = (cells,)
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
    elemType3))

p = mdb.models['Model-1'].parts['Part-2']
p.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]',), )
p.setMeshControls(regions=pickedRegions, technique=BOTTOM_UP)
p = mdb.models['Model-1'].parts['Part-2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#20 ]',), )
p.generateMesh(regions=pickedRegions, boundaryPreview=ON)
p = mdb.models['Model-1'].parts['Part-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#20 ]',), )
pickedGeomSourceSide = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#10 ]',), )
pickedGeomTargetSide = regionToolset.Region(faces=faces)
v = p.vertices
v1 = p.vertices
vector = (v[3], v1[0])
p = mdb.models['Model-1'].parts['Part-2']
c1 = p.cells
p.generateBottomUpExtrudedMesh(cell=c1[0],
    geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector,
    targetSide=pickedGeomTargetSide, numberOfLayers=10)
elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD,
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]',), )
pickedRegions = (cells,)
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
    elemType3))

p = mdb.models['Model-1'].parts['Part-1']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5',
    ' #0:95 #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 #0:95',
    ' #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 ]',), )
f = p.faces
p.associateMeshWithGeometry(geometricEntity=f[0], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=('[#0:900 #2020202:100 ]',), )
f1 = p.faces
p.associateMeshWithGeometry(geometricEntity=f1[5], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 #0:95',
    ' #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5',
    ' #0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 ]',), )
f = p.faces
p.associateMeshWithGeometry(geometricEntity=f[2], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4', ' #10000000 ]',
), )
f1 = p.faces
p.associateMeshWithGeometry(geometricEntity=f1[3], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=('[#4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4 ]',), )
f = p.faces
p.associateMeshWithGeometry(geometricEntity=f[1], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-2']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=('[#0:900 #2020202:100 ]',), )
f1 = p.faces
p.associateMeshWithGeometry(geometricEntity=f1[4], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-2']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4',
    ' #10000000 #0:4 #10000000 #0:4 #10000000 #0:4 #10000000',
    ' #0:4 #10000000 #0:4 #10000000 #0:4 #10000000 #0:4', ' #10000000 ]',
), )
f = p.faces
p.associateMeshWithGeometry(geometricEntity=f[0], elemFaces=pickedElemFaces)
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=('[#4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4',
    ' #0:4 #4 #0:4 #4 #0:4 #4 #0:4', ' #4 #0:4 #4 #0:4 #4 #0:4 #4 ]',), )
f1 = p.faces
p.associateMeshWithGeometry(geometricEntity=f1[2], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-2']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5',
    ' #0:95 #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 #0:95',
    ' #20202020:5 #0:95 #20202020:5 #0:95 #20202020:5 ]',), )
f = p.faces
p.associateMeshWithGeometry(geometricEntity=f[3], elemFaces=pickedElemFaces)
p = mdb.models['Model-1'].parts['Part-2']
e = p.elementFaces
pickedElemFaces = e.getSequenceFromMask(mask=(
    '[#0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 #0:95',
    ' #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5',
    ' #0:95 #8080808:5 #0:95 #8080808:5 #0:95 #8080808:5 ]',), )
f1 = p.faces
p.associateMeshWithGeometry(geometricEntity=f1[1], elemFaces=pickedElemFaces)

# 装配
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a1.Instance(name='Part-1-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-2']
a1.Instance(name='Part-2-1', part=p, dependent=ON)
p1 = a1.instances['Part-2-1']
p1.translate(vector=(55.0, 0.0, 0.0))

a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Part-1-1'].faces
f2 = a1.instances['Part-2-1'].faces
a1.FaceToFace(movablePlane=f1[5], fixedPlane=f2[4], flip=ON, clearance=0.0)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Part-1-1'].edges
e2 = a1.instances['Part-2-1'].edges
a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[0], flip=ON)

# 分析步
mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1',
    previous='Initial', response=STEADY_STATE, deltmx=None, cetol=None,
    creepIntegration=None, amplitude=RAMP)

# 相互作用
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]',), )
region1 = a.Surface(side1Faces=side1Faces1, name='m_Surf-1')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]',), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON,
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)

mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].ThermalConductance(
    definition=TABULAR, clearanceDependency=ON, pressureDependency=OFF,
    temperatureDependencyC=OFF, massFlowRateDependencyC=OFF,
    dependenciesC=0, clearanceDepTable=((2159.0, 0.0), (0.0, 5.0)))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]',), )
region1 = a.Surface(side1Faces=side1Faces1, name='m_Surf-3')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]',), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-3')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1',
    createStepName='Step-1', master=region1, slave=region2,
    sliding=FINITE, thickness=ON, interactionProperty='IntProp-1',
    adjustMethod=NONE, initialClearance=OMIT, datumAxis=None,
    clearanceRegion=None)

# 边界条件
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]',), )
region = a.Set(faces=faces1, name='Set-1')
mdb.models['Model-1'].TemperatureBC(name='BC-1', createStepName='Step-1',
    region=region, fixed=OFF, distributionType=UNIFORM, fieldName='',
    magnitude=1000.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-2-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]',), )
region = a.Set(faces=faces1, name='Set-2')
mdb.models['Model-1'].TemperatureBC(name='BC-2', createStepName='Step-1',
    region=region, fixed=OFF, distributionType=UNIFORM, fieldName='',
    magnitude=20.0, amplitude=UNSET)

# 作业
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=6,
    numDomains=6, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)