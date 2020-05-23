#ACCESS_WORKSPACE — A personal geodatabase or Access workspace
#ARCINFO_WORKSPACE — An ArcInfo coverage workspace
#CAD_WORKSPACE —A CAD file workspace
#EXCEL_WORKSPACE —An Excel file workspace
#FILEGDB_WORKSPACE —A file geodatabase workspace
#OLEDB_WORKSPACE —An OLE database workspace
#PCCOVERAGE_WORKSPACE —A PC ARC/INFO Coverage workspace
#RASTER_WORKSPACE —A raster workspace
#SDE_WORKSPACE —An SDE geodatabase workspace
#SHAPEFILE_WORKSPACE —A shapefile workspace
#TEXT_WORKSPACE —A text file workspace
#TIN_WORKSPACE —A TIN workspace
#VPF_WORKSPACE —A VPF workspace

import arcpy, os
from arcpy import env

#Cambiar a carpetas donde se encuentran los MXDs
source = arcpy.GetParameterAsText(0)
mxdList = []

outLoc = source

RutaOld1 = arcpy.GetParameterAsText(1)
RutaNew1 = arcpy.GetParameterAsText(2)
TipArch1 = arcpy.GetParameterAsText(3)
Archivo1 = arcpy.GetParameterAsText(4)

for dirpath, subdirs, files in os.walk(source):
    for x in files:
        if x.endswith(".mxd"):
            mxdList.append(os.path.join(dirpath, x))

arcpy.AddMessage("\n")
arcpy.AddMessage('Procesando')
arcpy.AddMessage("\n")

for mxd in mxdList:
	MXDpath = mxd
	mapdoc = arcpy.mapping.MapDocument(MXDpath)
	for lyr in arcpy.mapping.ListLayers(mapdoc):
		if lyr.supports("DATASOURCE"):
			if lyr.dataSource == RutaOld1:
				lyr.replaceDataSource(RutaNew1, TipArch1, Archivo1)
				arcpy.AddMessage(MXDpath+': '+RutaOld1+' camdiado por '+RutaNew1+'\''+Archivo1)
	mapdoc.save()
	del mapdoc

arcpy.AddMessage("\n")
arcpy.AddMessage("¡Todo fue un éxito!")
