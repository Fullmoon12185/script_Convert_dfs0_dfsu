import os
import gdal
from glob import glob

dir_with_csvs = r"C:/anhHoangKTTV/PythonScripts_DFS0/Project_NTB/"
os.chdir(dir_with_csvs)

def find_csv_filenames(path_to_dir, suffix=".csv"):
    relativePath = path_to_dir + "*.csv"
    print(relativePath)
    # filenames = glob.glob(relativePath)
    filenames = [os.path.relpath(x) for x in glob(relativePath)]
    return filenames
csvfiles = find_csv_filenames(dir_with_csvs)
for fn in csvfiles:
    vrt_fn = fn.replace(".csv", ".vrt")
    lyr_name = fn.replace('.csv', '')
    out_tif = fn.replace('.csv', '.tiff')
    with open(vrt_fn, 'w') as fn_vrt:
        fn_vrt.write('<OGRVRTDataSource>\n')
        fn_vrt.write('\t<OGRVRTLayer name="%s">\n' % lyr_name)
        fn_vrt.write('\t\t<SrcDataSource>%s</SrcDataSource>\n' % fn)
        fn_vrt.write('\t\t<GeometryType>wkbPoint</GeometryType>\n')
        fn_vrt.write('\t\t<GeometryField encoding="PointFromColumns" x="Lon" y="Lat" z="Ref"/>\n')
        fn_vrt.write('\t</OGRVRTLayer>\n')
        fn_vrt.write('</OGRVRTDataSource>\n')

output = gdal.Grid(out_tif,vrt_fn)
# below using your settings - I don't have sample large enough to properly test it, but it is generating file as well  
output2 = gdal.Grid('outcome2.tif','name.vrt', algorithm='invdist:power=2.0:smoothing=1.0')  