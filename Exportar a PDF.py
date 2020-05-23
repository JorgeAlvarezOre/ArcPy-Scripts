#Importar las librerias necesarias
import arcpy, os

#Carpeta con MXDs y creacion de lista vacia mxdList
source = arcpy.GetParameterAsText(0)
mxdList = []

#Variable de texto con calidad especificada (de mejor a peor): "BEST", "BETTER", "NORMAL", "FASTER", "FASTEST"
qual = arcpy.GetParameterAsText(1)

#Variable de texto con resolusion especificada 
res = arcpy.GetParameterAsText(2)

#For para rellenar lista mxdList con ruta de cada MXD
for dirpath, subdirs, files in os.walk(source):
    for x in files:
        if x.endswith(".mxd"):
            mxdList.append(os.path.join(dirpath, x))

for mxd in mxdList:
    pdf = mxd.replace(".mxd",".pdf")
    MXDpath = mxd
    
    mapdoc = arcpy.mapping.MapDocument(MXDpath)
    PDFpath = pdf
    
    arcpy.mapping.ExportToPDF(mapdoc,PDFpath,"PAGE_LAYOUT",0,0,res,qual)
    arcpy.AddMessage("El archivo MXD fue exportado en:" + PDFpath)
    del mapdoc
