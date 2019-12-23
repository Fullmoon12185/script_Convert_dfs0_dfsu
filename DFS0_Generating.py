import os
import numpy as np
from datetime import datetime
from pydhi import dfs0 as dfs0
from glob import glob
from projectSetup import *
import subprocess


def convertDFS02ExcelAll():
    convertMultipleDFS02Excel(tramThuyvanFolder['BD'], outtxtTramThuyVan['BD'])
    convertMultipleDFS02Excel(tramBaoluFolder['BD'], outtxtTramBaoLu['BD'])
    
    convertMultipleDFS02Excel(tramThuyvanFolder['PY'], outtxtTramThuyVan['PY'])
    convertMultipleDFS02Excel(tramBaoluFolder['PY'], outtxtTramBaoLu['PY'])
    
    convertMultipleDFS02Excel(tramThuyvanFolder['KH'], outtxtTramThuyVan['KH'])
    convertMultipleDFS02Excel(tramBaoluFolder['KH'], outtxtTramBaoLu['KH'])
    
    convertMultipleDFS02Excel(tramThuyvanFolder['NT'], outtxtTramThuyVan['NT'])
    convertMultipleDFS02Excel(tramBaoluFolder['NT'], outtxtTramBaoLu['NT'])
    
    convertMultipleDFS02Excel(tramThuyvanFolder['BT'], outtxtTramThuyVan['BT'])
    convertMultipleDFS02Excel(tramBaoluFolder['BT'], outtxtTramBaoLu['BT'])

def convertMultipleDFS02Excel(dfs0Folder, outputFolder):
    if(os.path.isdir(outputFolder)):
        fn = [os.path.relpath(x) for x in glob( outputFolder + '*.*')]
        if(len(fn) > 0):
            try:
                cmd = 'rm ' + outputFolder + '*.*'
                print(cmd)
                subprocess.call(cmd, shell=True)
            except ValueError:
                print("Cannot remove files")
        else:
            print("Folder is empty!")
    relativePath = dfs0Folder + "*.dfs0"
    print(relativePath)
    filenames = [os.path.relpath(x) for x in glob(relativePath)]
    print(filenames)
    for fname in filenames:
        temp = fname.split("\\") 
        convertDFS02Excel(fname, outputFolder + temp[-1][:-5] + '.csv')

def convertDFS02Excel(dfs0Filename, outputFilename = "out.csv"):
    dfs = dfs0.dfs0()
    data, t, names = dfs.read(dfs0Filename)
    print("outputfilename = " + outputFilename)
    fileHandle = open(outputFilename, "w")
    fileHandle.write(names[0] + "\n")
    for i in range(len(data)):
        line = str(t[i]) + ',' + str(data[i][0]) + '\n'
        fileHandle.write(line)
    fileHandle.close()
    print('data')
    print(data[0])
    print ('t')
    print(t[0])
    print('names')
    print(names)

def multDFS0Generating(inputFolder, outputFolder):
    if(os.path.isdir(outputFolder)):
        fn = [os.path.relpath(x) for x in glob( outputFolder + '*.*')]
        if(len(fn) > 0):
            try:
                cmd = 'rm ' + outputFolder + '*.*'
                print(cmd)
                subprocess.call(cmd, shell=True)
            except ValueError:
                print("Cannot remove files")
        else:
            print("Folder is empty!")
    
    relativePath = inputFolder + "*"
    print(relativePath)
    # filenames = glob.glob(relativePath)
    filenames = [os.path.relpath(x) for x in glob(relativePath)]
    print(filenames)
    name = ''
    titleName = ''
    for fname in filenames:
        temp = fname.split("\\") 
        if(int(temp[2]) in tenTramDoMua):
            name = tenTramDoMua[int(temp[2])]
            titleName = 'Rainfall'
            outputFilename = outputFolder + temp[2] + '_' + titleName + '_' + name
        elif(int(temp[2]) in tenTramKhiTuong):
            name = tenTramKhiTuong[int(temp[2])]
            titleName = 'Evaporation'
            outputFilename = outputFolder  + temp[2] + '_' + titleName + '_' + name
        elif(int(temp[2]) in tenTramThuyVan):
            name = tenTramThuyVan[int(temp[2])]
            titleName = 'WaterLevel'
            outputFilename = outputFolder  + temp[2] + '_' + titleName + '_' + name
        else:
            outputFilename = outputFolder + temp[2]
        
        
        if(name == ''):
            dfs0Generating(fname, outputFilename)        
        else:
            dfs0Generating(fname, outputFilename, name = name, titleName = titleName)


def dfs0Generating(inputFilename, outputFilename = 'default', titleName = "Rainfall", name = 'Binh_Dinh'):
    dfs0file = outputFilename + '.dfs0'
    # dfs0file_1 = outputFilename + 'bis.dfs0'
    readData = np.loadtxt(fname = inputFilename, delimiter=',',skiprows = 0,dtype = 'str')
    print("inputfile  = " + inputFilename)
    print('outputfile = ' + outputFilename)
    if(len(readData) == 0):
        return
    newData = []
    for i in readData[:, 1]:
        newData.append([float(i)])
    newData1 = np.asarray(newData)
    
    time_vector = []
    for i in range(len(newData)):
        time_vector.append(datetime.strptime(readData[i,0], '%d-%m-%Y %H:%M:%S'))
    
    title = titleName
    names = [name]
    if(titleName == 'Rainfall'):
        variable_type = [100004]
        unit = [1002] #1000 meter, 1001 km, 1002 mm
        data_value_type = [2]
    elif(titleName == 'Evaporation'):
        variable_type = [100005]
        unit = [1002] #1000 meter, 1001 km, 1002 mm
        data_value_type = [2]
    elif(titleName == 'WaterLevel'):
        variable_type = [100000]
        unit = [1000] #1000 meter, 1001 km, 1002 mm
        data_value_type = [0]
    else:
        variable_type = [100004]
        unit = [1002] #1000 meter, 1001 km, 1002 mm
        data_value_type = [2]
    dfs = dfs0.dfs0()
    dfs.create_non_equidistant_calendar(dfs0file=dfs0file, data=newData1,
                                        time_vector=time_vector,
                                        names=names, title=title,
                                        variable_type=variable_type, unit=unit,
                                        data_value_type=data_value_type)

    start_time = time_vector[0]
    #1400 = 5s
    #1401 = 5m
    #1402 = 5h
    #1403 =
    #1404 = 5h
    # timeseries_unit = 1403
    # dt = 5
    # dfs.create_equidistant_calendar(dfs0file=dfs0file_1, data=newData1,
    #                                 start_time=start_time,
    #                                 timeseries_unit=timeseries_unit, dt=dt,
    #                                 names=names, title=title,
    #                                 variable_type=variable_type,
    #                                 unit=unit, data_value_type=data_value_type)
    assert True

def test_create_equidistant_calendar():

    dfs0file = r'random11.dfs0'
    data = np.random.random([1000, 2])
    data[2, :] = np.nan
    start_time = datetime.datetime(2017, 1, 1)
    timeseries_unit = 1402
    title = 'Hello Test'
    names = ['VarFun01', 'NotFun']
    variable_type = [100000, 100000]
    unit = [1000, 1000]
    data_value_type = [0, 1]
    dt = 5
    dfs = dfs0.dfs0()
    dfs.create_equidistant_calendar(dfs0file=dfs0file, data=data,
                                    start_time=start_time,
                                    timeseries_unit=timeseries_unit, dt=dt,
                                    names=names, title=title,
                                    variable_type=variable_type,
                                    unit=unit, data_value_type=data_value_type)

    #os.remove(dfs0file)
    assert True

def test_create_non_equidistant_calendar():
    dfs0file = r'random12.dfs0'
    data = np.random.random([1000, 2])
    data[2, :] = np.nan
    start_time = datetime.datetime(2017, 1, 1)
    time_vector = []
    for i in range(1000):
        time_vector.append(start_time + datetime.timedelta(hours=i*0.1))
    title = 'Hello Test'
    names = ['VarFun01', 'NotFun']
    variable_type = [100000, 100000]
    unit = [1000, 1000]
    data_value_type = [0, 1]

    dfs = dfs0.dfs0()
    dfs.create_non_equidistant_calendar(dfs0file=dfs0file, data=data,
                                        time_vector=time_vector,
                                        names=names, title=title,
                                        variable_type=variable_type, unit=unit,
                                        data_value_type=data_value_type)

    assert True
    #os.remove(dfs0file)



# multDFS0Generating()
if __name__ == '__main__':
    convertDFS02ExcelAll()