#Importar modulos requeridos
import arcpy, os

#Declaracion de variables
source = arcpy.GetParameterAsText(0) #Carpetas donde se encuentran los MXDs
mxdList = [] #Lista para los MXD
Booleano = arcpy.GetParameterAsText(1) #Autorrellenar
Titulo = arcpy.GetParameterAsText(2) #Variable para el título
Resumen = arcpy.GetParameterAsText(3) #Variable para el resumen
Descripcion = arcpy.GetParameterAsText(4) #Variable para la descripción
#Etiqueta = arcpy.GetParameterAsText(5) #Variable para las etiquetas. Las etiquetas se separan por comas (,)

for dirpath, subdirs, files in os.walk(source):
    for x in files:
        if x.endswith(".mxd"):
            mxdList.append(os.path.join(dirpath, x))

arcpy.AddMessage("\n")
arcpy.AddMessage("Procesando: ")

for mxd in mxdList:
	mpk = mxd.replace(".mxd",".mpk")
	MXDpath = mxd
	
	mapdoc = arcpy.mapping.MapDocument(MXDpath)
	MPKpath = mpk
	
	if Booleano == "true":
		mapdoc.title = Titulo #mapdoc.filePath Cambiar despues a nombre del MXD
		mapdoc.summary = Resumen
		mapdoc.description = Descripcion
		mapdoc.tags = "Mapas"
		mapdoc.save()
	
	arcpy.PackageMap_management(MXDpath, MPKpath)
	arcpy.AddMessage("El archivo MXD fue exportado en:" + MPKpath)
	
	del mapdoc
