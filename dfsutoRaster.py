"""
@file
@author  Roland Loewe <rolo@env.dtu.dk>
@version 1.0
@section LICENSE
Copyright (C) 2016 Roland Loewe
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
#######################################################################
#######################################################################
###################Convert dfsu to grid################################
#######################################################################
#########Author: Roland Loewe##########################################
#########Date: May 2016################################################
#######################################################################
#######################################################################
#read data for all time steps from a dfsu result files
#create a raster file for each time step in a subfolder in the same directory
#the result rasters have the same extent and dimension as a reference DEM grid that needs to be provided
#simulated water depths located in land or nodata areas of the reference DEM are not displayed in the result rasters

import os, shutil, gc
import sys
import numpy
from scipy.interpolate import griddata
#location of the export script
wd=os.path.dirname(os.path.realpath(__file__))
sys.path.append(wd)
#sys.path.append(r'c:\Program Files (x86)\ArcGIS\Desktop10.3\arcpy')
#sys.path.append(r'c:\Program Files (x86)\ArcGIS\Desktop10.3\bin')
sys.path.append(r'c:\Program Files (x86)\DHI\2016\MIKE SDK\bin')
#import arcpy
import clr
clr.AddReference("DHI.Generic.MikeZero.DFS")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("System")

import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *
#from DHI.Generic.Cartography import *
from DHI.Generic.MikeZero.DFS.dfsu import *
import mike_IO_dfs2 as mdfs2
import gdal
from osgeo import osr, ogr

###############Paramaters to edit######################################################################
epsg=32755
#path to dfsu result file to read
pathin=os.path.abspath(r'c:\Data\rolo\Simulations_Behzad\Sub_3\T100\Results.dfsu')
#pathin=os.path.abspath(r'c:\Data\rolo\Simulations_Behzad\Results.dfsu')
#dfsu is normally created from dfs2 file - get spatial reference from this file
pathref=os.path.abspath(r'c:\Data\rolo\Simulations_Behzad\grids\sub_3a.dfs2')
#pathref=os.path.abspath(r'c:\Data\rolo\Simulations_Behzad\dem150911_10m_landnew.dfs2')

#######################################################################################################


def array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array,epsg):
    cols = array.shape[1]
    rows = array.shape[0]
    originX = rasterOrigin[0]
    originY = rasterOrigin[1]
    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Float32)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(epsg)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


#directory where result files are created
pathout=os.path.split(pathin)[0]

#get reference info from dfs2
status,XCount,YCount,xysize,Dx,Dy,X0,Y0,Lat,Lon,Or,WKT,nanval,landval=mdfs2.get_spatial_reference(pathref)
print str(X0) + '; ' + str(Y0)
#FOR 10M grid
#if X0==0.0: X0=321372.302408058 #dirty fix for the 10m model, where origin is somehow 0 in the dfs2 file info
#if Y0==0.0: Y0=5797056.91007716
#For SUB_3
if X0==0.0: X0=321406.239610002
if Y0==0.0: Y0=5804783.59235805
[status, dfsdata] = mdfs2.read_dfs2_timestep(pathref, 1, 0)
[status, refdata] = mdfs2.dfsdata_to_numpy2D(dfsdata,XCount,YCount)
del dfsdata

########################################################
#open dfsu file
file=DfsuFile.Open(pathin)
numberOfElements = file.NumberOfElements
numberOfNodes = file.NumberOfNodes
ElementTable=file.ElementTable
NodeX = numpy.array(list(file.X))
NodeY = numpy.array(list(file.Y))
# Read dynamic item info
firstItemName = file.ItemInfo[0].Name
quantity = file.ItemInfo[0].Quantity
nitem=file.ItemInfo.Count
nstep=file.NumberOfTimeSteps

#compute coordinates for element centre points
print ("computing element coordinates")
ElementX=list()
ElementY=list()
for i in range(numberOfElements):
    ElementNodes = numpy.array(list(ElementTable[i]))
    X=0
    Y=0
    count=0
    for index in ElementNodes: #node indices are saved starting from 1 in element table
        X=X+NodeX[index-1]
        Y=Y+NodeY[index-1]
        count=count+1
    ElementX.append(X/count)
    ElementY.append(Y/count)

#combine Element coordinates into points
points=(numpy.array(ElementX),numpy.array(ElementY))
print ("element coordinates computed")
 
#get reference grid from ArcGIS, take resolution and coordinates from this, interpolate results to this grid, set them to 0 where the grid is NaN or land
minX=X0
maxX=X0+XCount*Dx
minY=Y0
maxY=Y0+YCount*Dy
dx=Dx
dy=Dy
if not dx==dy: print ("Warning: x-resolution not the same as y resolution")
grid_x, grid_y = numpy.meshgrid(numpy.arange(minX+0.5*dx,maxX,dx), numpy.arange(minY+0.5*dy,maxY,dy))

#check if folder for saving results exists - if not, create yet, if yes - delete everything in the folder
pathout=os.path.join(pathout,'ResRaster')
if os.path.exists(pathout): shutil.rmtree(pathout)
os.mkdir(pathout)

for step in range(nstep):
    #load data for the first item, 1st timestep
    itemTimeStepData = file.ReadItemTimeStep(1, step).Data
    print("data read for step: " + str(step))
    #convert results values
    values=numpy.array(list(itemTimeStepData))
    values[values<0.05]=0   
    print ("data processed")
    print ("interpolate to raster")
    grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
    grid_z0=numpy.flipud(grid_z0)
    #set values outside DEM domain to 0
    grid_z0[refdata==nanval]=0
    grid_z0[refdata>=landval]=0
    grid_z0=numpy.flipud(grid_z0)
    print ("values interpolated to grid")
    #save interpolated data as raster
    pathout2=os.path.join(pathout,'depth_'+"0"*(3-len(str(int(step))))+str(step)+'.tiff')
    array2raster(pathout2,[X0-dx/2,Y0-dy/2],dx,dy,grid_z0,epsg)
	#llcorner=arcpy.Point(minX,minY)
    #no_data=0
    #myRaster = arcpy.NumPyArrayToRaster(grid_z0,llcorner,dx,dy,no_data)
    #myRaster.save(pathout2)
    print ("raster saved")
    del itemTimeStepData
    del grid_z0
    del values
    gc.collect()

file.Close()

print ("finished")
