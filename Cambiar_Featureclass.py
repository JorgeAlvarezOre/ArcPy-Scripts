#Implementacion JCI Ronald Chavez y Jorge Alvarez 2019

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

#Cambiar a carpetas donde se encuentran los MXDs
Fuente = arcpy.GetParameterAsText(0)
MXD_list = []
MXD_list_temp = []
 
Booleano = arcpy.GetParameterAsText(1) #false sin subdirectorios, true con subdirectorios

RutaOld1 = arcpy.GetParameterAsText(2)
RutaNew1 = arcpy.GetParameterAsText(3)
TipArch1 = arcpy.GetParameterAsText(4)
Archivo1 = arcpy.GetParameterAsText(5)
RutaOld2 = arcpy.GetParameterAsText(6)
RutaNew2 = arcpy.GetParameterAsText(7)
TipArch2 = arcpy.GetParameterAsText(8)
Archivo2 = arcpy.GetParameterAsText(9)
RutaOld3 = arcpy.GetParameterAsText(10)
RutaNew3 = arcpy.GetParameterAsText(11)
TipArch3 = arcpy.GetParameterAsText(12)
Archivo3 = arcpy.GetParameterAsText(13)
RutaOld4 = arcpy.GetParameterAsText(14)
RutaNew4 = arcpy.GetParameterAsText(15)
TipArch4 = arcpy.GetParameterAsText(16)
Archivo4 = arcpy.GetParameterAsText(17)
RutaOld5 = arcpy.GetParameterAsText(18)
RutaNew5 = arcpy.GetParameterAsText(19)
TipArch5 = arcpy.GetParameterAsText(20)
Archivo5 = arcpy.GetParameterAsText(21)

# Recorrer carpeta de los MXDs y enlistar los *.mxd, considerando o no las subcarpetas
if Booleano == "true":
    for dirpath, subdirs, files in os.walk(Fuente):
        for x in files:
            if x.endswith(".mxd"):
                MXD_list.append(os.path.join(dirpath, x))
else:
    for fname in os.listdir(Fuente):
        MXD_list_temp.append(os.path.join(Fuente, fname))
    for x in MXD_list_temp:
        if x.endswith(".mxd"):
            MXD_list.append(x)

arcpy.AddMessage("\n")
arcpy.AddMessage('Procesando')
arcpy.AddMessage("\n")

for mxd in MXD_list:
	MXDpath = mxd
	mapdoc = arcpy.mapping.MapDocument(MXDpath)
	for lyr in arcpy.mapping.ListLayers(mapdoc):
		if lyr.supports("DATASOURCE"):
			if lyr.dataSource == RutaOld1:
				lyr.replaceDataSource(RutaNew1, TipArch1, Archivo1)
				arcpy.AddMessage(MXDpath+': '+RutaOld1+' camdiado por '+RutaNew1+'\''+Archivo1)
			if lyr.dataSource == RutaOld2:
				lyr.replaceDataSource(RutaNew2, TipArch2, Archivo2)
				arcpy.AddMessage(MXDpath+': '+RutaOld2+' camdiado por '+RutaNew2+'\''+Archivo2)
			if lyr.dataSource == RutaOld3:
				lyr.replaceDataSource(RutaNew3, TipArch3, Archivo3)
				arcpy.AddMessage(MXDpath+': '+RutaOld3+' camdiado por '+RutaNew3+'\''+Archivo3)
			if lyr.dataSource == RutaOld4:
				lyr.replaceDataSource(RutaNew4, TipArch4, Archivo4)
				arcpy.AddMessage(MXDpath+': '+RutaOld4+' camdiado por '+RutaNew4+'\''+Archivo4)
			if lyr.dataSource == RutaOld5:
				lyr.replaceDataSource(RutaNew5, TipArch5, Archivo5)
				arcpy.AddMessage(MXDpath+': '+RutaOld5+' camdiado por '+RutaNew5+'\''+Archivo5)
	mapdoc.save()
	del mapdoc
  
arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
