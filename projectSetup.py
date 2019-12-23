tempDataFolder = {'BD': './tempOutputFiles/Binh_Dinh/', \
                  'PY' : './tempOutputFiles/Phu_Yen/', \
                  'KH' : './tempOutputFiles/Khanh_Hoa/', \
                  'NT': './tempOutputFiles/Ninh_Thuan/',\
                  'BT': './tempOutputFiles/Binh_Thuan/'  }

BinhDinhTramNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 46, 47, 48, \
    59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 ,71, 140, 141, 142, 143]
PhuYenTramNumber = [11, 12, 13, 14, 15, 16, 17, 18, 19,\
    20, 49, 50, 51, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,\
    144, 145, 146, 147]
KhanhHoaTramNumber = [52, 53, 83, 84, 85, 86, 87, 88, 89, 90, \
    91, 92, 93, 94, 95, 96, 97, 98, 99, 148, 149, 150]
NinhThuanTramNumber = [28, 29, 30, 31, 32, 33, 34, 35, 36, \
    54, 55, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,\
    151, 152, 156]
BinhThuanTramNumber = [37, 38, 39, 40, 41, 42, 43, 44, \
    56, 57, 58, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,\
        126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, \
            153, 154, 155]
NhaTrangTramNumber = [21, 22, 23, 24, 25, 26, 27]





PROJECT_FOLDER = "C:/anhHoangKTTV/PythonScripts_DFS0/Project_NTB/"
outputFolderRainFall = {'BD' : PROJECT_FOLDER + "Project_NTB/Models/BINH_DINH/MIKE11/NAM/Boundary/Rainfall/", \
                        'PY' : PROJECT_FOLDER + "Project_NTB/Models/PHU_YEN/MIKE11/NAM/Boundary/Rainfall/", \
                        'KH' : PROJECT_FOLDER + "Project_NTB/Models/KHANH_HOA/MIKE11/NAM/Boundary/Rainfall/",\
                        'NT' : PROJECT_FOLDER + "Project_NTB/Models/NINH_THUAN/MIKE11/NAM/Boundary/Rainfall/", \
                        'BT' : PROJECT_FOLDER + "Project_NTB/Models/BINH_THUAN/MIKE11/NAM/Boundary/Rainfall/",}

url = 'http://log.achipvn.com/ntb/export/'
urlTram = 'http://log.achipvn.com/ntb/export/dstram.php?utm_source=zalo&utm_medium=zalo&utm_campaign=zalo&zarsrc=31'



inputFiles = "C:\\anhHoangKTTV\\PythonScripts_DFS0\\py-dhi-dfs-master\\py-dhi-dfs-master\\tests\\InputFiles\\"
outputFiles = ".\\OutputFiles\\"

tramThuyvanFolder = {'BD': PROJECT_FOLDER + 'Project_NTB/Models/BINH_DINH/MIKE11/MIKE11_HD/Results/Prediction_Results/stations/', \
                    'PY' : PROJECT_FOLDER + 'Project_NTB/Models/PHU_YEN/MIKE11/MIKE11_HD/Results/Prediction_Results/stations/', \
                    'KH' : PROJECT_FOLDER + 'Project_NTB/Models/KHANH_HOA/MIKE11/MIKE11_HD/Results/Prediction_Results/stations/', \
                    'NT' : PROJECT_FOLDER + 'Project_NTB/Models/NINH_THUAN/MIKE11/MIKE11_HD/Results/Prediction_Results/stations/', \
                    'BT' : PROJECT_FOLDER + 'Project_NTB/Models/BINH_THUAN/MIKE11/MIKE11_HD/Results/Prediction_Results/stations/'}

tramBaoluFolder = {'BD': PROJECT_FOLDER + 'Project_NTB/Models/BINH_DINH/MIKE11/MIKE11_HD/Results/Prediction_Results/points/', \
                    'PY' : PROJECT_FOLDER + 'Project_NTB/Models/PHU_YEN/MIKE11/MIKE11_HD/Results/Prediction_Results/points/', \
                    'KH' : PROJECT_FOLDER + 'Project_NTB/Models/KHANH_HOA/MIKE11/MIKE11_HD/Results/Prediction_Results/points/', \
                    'NT' : PROJECT_FOLDER + 'Project_NTB/Models/NINH_THUAN/MIKE11/MIKE11_HD/Results/Prediction_Results/points/', \
                    'BT' : PROJECT_FOLDER + 'Project_NTB/Models/BINH_THUAN/MIKE11/MIKE11_HD/Results/Prediction_Results/points/'}
outtxtTramThuyVan = {'BD': PROJECT_FOLDER + 'Project_NTB/txtResultsThuyVan/BINH_DINH/', \
                    'PY' : PROJECT_FOLDER + 'Project_NTB/txtResultsThuyVan/PHU_YEN/', \
                    'KH' : PROJECT_FOLDER + 'Project_NTB/txtResultsThuyVan/KHANH_HOA/', \
                    'NT' : PROJECT_FOLDER + 'Project_NTB/txtResultsThuyVan/NINH_THUAN/', \
                    'BT' : PROJECT_FOLDER + 'Project_NTB/txtResultsThuyVan/BINH_THUAN/'}
    
outtxtTramBaoLu = {'BD': PROJECT_FOLDER + 'Project_NTB/txtResultsBaoLu/BINH_DINH/', \
                    'PY' : PROJECT_FOLDER + 'Project_NTB/txtResultsBaoLu/PHU_YEN/', \
                    'KH' : PROJECT_FOLDER + 'Project_NTB/txtResultsBaoLu/KHANH_HOA/', \
                    'NT' : PROJECT_FOLDER + 'Project_NTB/txtResultsBaoLu/NINH_THUAN/', \
                    'BT' : PROJECT_FOLDER + 'Project_NTB/txtResultsBaoLu/BINH_THUAN/'}




tenTramDoMua = {59: 'My An', 60: 'An Hung', 61: 'An Quang', 62: 'An Tuong', 63: 'Vinh An', 64: 'Phu My', 65: 'Van Canh', 66: 'Phu Cat', 67: 'Đe Gi', 68: 'Đinh Binh', 69: 'Vinh Hao', 70: 'Hoai An', 71: 'Bong Son',\
        72: 'Cu Mong', 73: 'Song Cau', 74: 'Hoa Dong', 75: 'Phu Lac', 76: 'Son Thanh', 77: 'Xuan Lanh', 78: 'Xuan Son Nam', 79: 'Son Phuoc', 80: 'Ea Pa', 81: 'An Hai', 82: 'Song Hinh',\
        83: 'Ninh Son', 84: 'Ninh Diem', 85: 'Khanh Vinh', 86: 'Khanh Son', 87: 'Van Binh', 88: 'Ninh Tan', 89: 'Son Tan', 90: 'Suoi Tien', 91: 'Khanh Hiep', 92: 'Thanh Son', 93: 'Dai Lanh', 94: 'Ninh An', 95: 'Dien Lam', 96: 'Khanh Binh', 97: 'Cam Phuoc Dong', 98: 'Son Thai', 99: 'Suoi Cat', \
        100: 'Lam Son', 101: 'Nha Ho', 102: 'Ba Thap', 103: 'Phan Rang', 104: 'Nhi Ha', 105: 'Quan The', 106: 'Ca Na', 107: 'Phuoc Son', 108: 'Phuoc Huu', 109: 'Cong Hai', 110: 'Phuoc Chinh',\
        111: 'Me Pu', 112: 'Dong Giang', 113: 'La Ngau', 114: 'Vo Xu', 115: 'Ma Lam', 116: 'Song Mao', 117: 'Lien Huong', 118: 'Bau Trang', 119: 'Suoi Kiet 1', 120: 'Mui Ne', 121: 'Ke Ga', 122: 'Nga Ba 46', 123: 'Muong Man', 124: 'Phan Dung', 125: 'Phan Lam', 126: 'Phong Phu', 127: 'Binh An', 128: 'Song Luy', 129: 'Luong Son', 130: 'Thuan Hoa', 131: 'Hong Son', 132: 'La Da', 133: 'Gia Huynh', 134: 'Suoi Kiet 2', 135: 'Tan Minh', 136: 'Tan Thang', 137: 'Tan Hai', 138: 'Mang To', 139: 'Ham Kiem'
}

tenTramKhiTuong  = {45: 'Tay Thuan', 46: 'Canh Thuan', 47: 'Hoai Đuc', 48: 'Phu My',\
    49: 'Song Cau', 50: 'Son Hoi', 51: 'Song Hinh',\
    52: 'Khanh Trung', 53: 'Van Binh',\
    54: 'Ma Moi', 55: 'Phuoc Thai',\
    56: 'Hong Liem', 57: 'La Ngau'
}

tenTramThuyVan = {140: 'Bong Son', 141: 'Vinh Hiep', 142: 'Kien My', 143: 'An Hoa',\
    144: 'Song Hinh', 145: 'Song Ba', 146: 'La Hai', 147: 'Phu Hoa',\
    148: 'Dien Phu', 149: 'Duc My', 150: 'Dong Tran',\
    151: 'Quang Ninh', 152: 'Dao Long 2', 156: 'Ninh Hai',\
    58: 'Tan Lap', 153: 'Ta Pao', 154: 'Ban Chiem', 155: 'Cau Chay'
}