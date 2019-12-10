import os
import numpy as np
from datetime import datetime
from pydhi import dfs0 as dfs0
from pydhi import dfsu as dfsu
from glob import glob
import shapefile

# C:\Users\VAIO\AppData\Local\Programs\Python\Python37\Lib\site-packages\pydhi
def dfsu_reading():
    dfs = dfsu.dfsu()
    (data_list, time, names) = dfs.read("kq_ngaplut_py.dfsu")
    ec = dfs.get_element_coords()
    f = open("ec", "w")
    for data in ec:
        f.write(str(data[0]) + '\t' + str(data[1]) )
        f.write("\n")
    f.close()
    
    
    print("np.shape(data_list)")
    print(np.shape(data_list))
    print(data_list)
    print(len(data_list))
    data_list = np.array(data_list)
    print(len(data_list))
    print(data_list)
    index = 0
    for i in data_list:
        # print(len(i))
        # print (i)
        # print("names[index]")
        # print(names[index])
        
        for idx in range(len(time)):
            filename = "DFSU_ouputFiles\\" + names[index] + "_" + str(idx) + ".csv"
            f = open(filename, "w")
            f.write('Element' + ',' + names[index] + ',' + 'X' + ',' + 'Y')
            f.write("\n")
            for count, data in enumerate(i[:,idx]):
                f.write(str(count) +',' + str(data) + ',' + str(ec[count, 0]) + ',' + str(ec[count, 1]))
                f.write("\n")
            f.close()   
        index = index + 1        

    #     # print ("print k")
    #     # for j in i:
    #     #     for k in j:
    #     #         print (k)
    #     #     break
    #     # print("end print k")    
            
    
    # print(len(time))
    # print (time)
    # filename = "time.txt"
    # f = open(filename, "w")        
    # for i in time:
    #     f.write(str(i))
    #     f.write("\n")
    # f.close()

    # print(len(names))
    # print (names)


def shapefile_reading():
    with shapefile.Reader("ngap_LV_PY_max_cells_0.shp") as shp:
        print(shp)

# shapefile_reading()
dfsu_reading()
#multDFS0Generating()