import arcpy, os
from arcpy import env

#Variables de carpeta
source = arcpy.GetParameterAsText(0)
mxdList = []

RutaOld1 = arcpy.GetParameterAsText(1)
RutaNew1 = arcpy.GetParameterAsText(2)

for dirpath, subdirs, files in os.walk(source):
    for x in files:
        if x.endswith(".mxd"):
            mxdList.append(os.path.join(dirpath, x))

arcpy.AddMessage("Procesando:")

for mxd in mxdList:
    MXDpath = mxd
    mapdoc = arcpy.mapping.MapDocument(MXDpath)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld1, RutaNew1)
    mapdoc.save()
    arcpy.AddMessage("Cambios guardados correctamente")
    del mapdoc

arcpy.AddMessage("\n")
arcpy.AddMessage("Todo fue exportado!")