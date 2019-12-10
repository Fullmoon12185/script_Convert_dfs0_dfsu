import os
import numpy as np
from datetime import datetime
from pydhi import dfs0 as dfs0
from glob import glob

inputFiles = "C:\\anhHoangKTTV\\PythonScripts_DFS0\\py-dhi-dfs-master\\py-dhi-dfs-master\\tests\\InputFiles\\"
outputFiles = ".\\OutputFiles\\"



def convertDFS02Excel():
     dfs = dfs0.dfs0()
     
     print(dfs.read_to_pandas("random12.dfs0"))
     data, t, names = dfs.read("random12.dfs0")
     print('data')
     print(data)
     print ('t')
     print(t)
     print('names')
     print(names)

def multDFS0Generating(inputFolder, outputFolder):
    relativePath = inputFolder + "*"
    print(relativePath)
    # filenames = glob.glob(relativePath)
    filenames = [os.path.relpath(x) for x in glob(relativePath)]
    print(filenames)
    for fname in filenames:
        temp = fname.split("\\") 
        dfs0Generating(fname, outputFolder + temp[2])


def dfs0Generating(inputFilename, outputFilename = 'default', titleName = "RainFall", name = 'Binh_Dinh'):
    dfs0file = outputFilename + '.dfs0'
    readData = np.loadtxt(fname = inputFilename, delimiter=',',skiprows = 0,dtype = 'str')
    print("inputfile  = " + inputFilename)
    print('outputfile = ' + outputFilename)
    if(len(readData) == 0):
        return
    newData = []
    for i in readData[2:, 1]:
        newData.append([float(i)])
    newData1 = np.asarray(newData)
    
    time_vector = []
    for i in range(len(newData)):
        time_vector.append(datetime.strptime(readData[i+1,0], '%d-%m-%Y %H:%M:%S'))
    
    title = titleName
    names = [name]
    variable_type = [100000]
    unit = [1002] #1000 meter, 1001 km, 1002 mm
    data_value_type = [0]

    dfs = dfs0.dfs0()
    dfs.create_non_equidistant_calendar(dfs0file=dfs0file, data=newData1,
                                        time_vector=time_vector,
                                        names=names, title=title,
                                        variable_type=variable_type, unit=unit,
                                        data_value_type=data_value_type)

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
    convertDFS02Excel()