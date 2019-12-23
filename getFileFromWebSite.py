import requests
import numpy as np
import os
import subprocess
from DFS0_Generating import *
from projectSetup import *
from glob import glob

# tempDataFolder = {'BD': './tempOutputFiles/Binh_Dinh/', \
#                   'PY' : './tempOutputFiles/Phu_Yen/', \
#                   'KH' : './tempOutputFiles/Khanh_Hoa/', \
#                   'NT': './tempOutputFiles/Ninh_Thuan/',\
#                   'BT': './tempOutputFiles/Binh_Thuan/'  }

# BinhDinhTramNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 46, 47, 48, \
#     59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 ,71, 140, 141, 142, 143]
# PhuYenTramNumber = [11, 12, 13, 14, 15, 16, 17, 18, 19,\
#     20, 49, 50, 51, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,\
#     144, 145, 146, 147]
# KhanhHoaTramNumber = [52, 53, 83, 84, 85, 86, 87, 88, 89, 90, \
#     91, 92, 93, 94, 95, 96, 97, 98, 99, 148, 149, 150]
# NinhThuanTramNumber = [28, 29, 30, 31, 32, 33, 34, 35, 36, \
#     54, 55, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,\
#     151, 152, 156]
# BinhThuanTramNumber = [37, 38, 39, 40, 41, 42, 43, 44, \
#     56, 57, 58, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,\
#         126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, \
#             153, 154, 155]
# NhaTrangTramNumber = [21, 22, 23, 24, 25, 26, 27]



# PROJECT_FOLDER = "C:/anhHoangKTTV/PythonScripts_DFS0/Project_NTB/"
# outputFolderRainFall = {'BD' : PROJECT_FOLDER + "Project_NTB/Models/BINH_DINH/MIKE11/NAM/Boundary/Rainfall/", \
#                         'PY' : PROJECT_FOLDER + "Project_NTB/Models/PHU_YEN/MIKE11/NAM/Boundary/Rainfall/", \
#                         'KH' : PROJECT_FOLDER + "Project_NTB/Models/KHANH_HOA/MIKE11/NAM/Boundary/Rainfall/",\
#                         'NT' : PROJECT_FOLDER + "Project_NTB/Models/NINH_THUAN/MIKE11/NAM/Boundary/Rainfall/", \
#                         'BT' : PROJECT_FOLDER + "Project_NTB/Models/BINH_THUAN/MIKE11/NAM/Boundary/Rainfall/",}

# url = 'http://log.achipvn.com/ntb/export/'
# urlTram = 'http://log.achipvn.com/ntb/export/dstram.php?utm_source=zalo&utm_medium=zalo&utm_campaign=zalo&zarsrc=31'



def createDirectory(dirName, isRemoveFile = False):
    if(os.path.isdir(dirName) == False):
        try:
            cmd = 'mkdir -p ' + dirName
            print(cmd)
            subprocess.call(cmd, shell=True)
        except ValueError:
            print("Cannot create folder!")
    else:
        if(isRemoveFile == True):
            fn = [os.path.relpath(x) for x in glob( dirName + '*.*')]
            if(len(fn) > 0):
                try:
                    cmd = 'rm ' + dirName + '*.*'
                    print(cmd)
                    subprocess.call(cmd, shell=True)
                except ValueError:
                    print("Cannot remove files")
            else:
                print("Folder is empty!")
def createAllNeccessaryDirectories():
    createDirectory(tempDataFolder['BD'], isRemoveFile= True)
    createDirectory(tempDataFolder['PY'], isRemoveFile= True)
    createDirectory(tempDataFolder['KH'], isRemoveFile= True)
    createDirectory(tempDataFolder['NT'], isRemoveFile= True)
    createDirectory(tempDataFolder['BT'], isRemoveFile= True)
    

def getDataFromWebSite(url, filename):
    try:
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    except ValueError:
        print("Oops! Cannot get data from the " + url)


def getAlldataFromWebSite():    
    createDirectory('./DataFromWebsite')
    getDataFromWebSite(url, "./DataFromWebsite/luongmua.txt")
    getDataFromWebSite(urlTram, "./DataFromWebsite/DanhsachTram.txt")

def convertRawDataToTxtFormat():
    temp = np.loadtxt(fname='./DataFromWebsite/luongmua.txt', delimiter=';',skiprows = 1,dtype = 'str')
    temptram = 0
    filename = ""
    fileHandle = 0
    listOfData = []
    createAllNeccessaryDirectories()
    for i in temp:
        if(temptram != int(i[0])):
            temptram = int(i[0])
            if(temptram in BinhDinhTramNumber):
                filename = tempDataFolder['BD'] + i[0]
            elif(temptram in PhuYenTramNumber):
                filename = tempDataFolder['PY'] + i[0]
            elif(temptram in KhanhHoaTramNumber):
                filename = tempDataFolder['KH'] + i[0]
            elif(temptram in NhaTrangTramNumber):
                filename = tempDataFolder['KH'] + i[0]
            elif(temptram in NinhThuanTramNumber):
                filename = tempDataFolder['NT'] + i[0]
            elif(temptram in BinhThuanTramNumber):
                filename = tempDataFolder['BT'] + i[0]
            if(fileHandle != 0):
                if(len(listOfData) > 0):
                    for lineindex in listOfData:
                        fileHandle.write(lineindex)
                fileHandle.close()
            listOfData = []
            fileHandle = open(filename, "w")
            
            line = i[2] + "," + i[1] + '\n'
            listOfData.insert(0, line)
        else:
            line = i[2] + "," + i[1] + '\n'
            listOfData.insert(0, line)
    #For last place
    if(fileHandle != 0):
        if(len(listOfData) > 0):
            for lineindex in listOfData:
                fileHandle.write(lineindex)
        fileHandle.close()        

def convertTxtDataToDFS0():
    multDFS0Generating(tempDataFolder['BD'], outputFolderRainFall['BD'])   
    multDFS0Generating(tempDataFolder['PY'], outputFolderRainFall['PY'])   
    multDFS0Generating(tempDataFolder['KH'], outputFolderRainFall['KH'])   
    multDFS0Generating(tempDataFolder['NT'], outputFolderRainFall['NT'])   
    multDFS0Generating(tempDataFolder['BT'], outputFolderRainFall['BT'])   
        