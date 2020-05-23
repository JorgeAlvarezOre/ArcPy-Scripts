#Importar librerias a usar en el script
import arcpy, os

#Definición de variables
source = arcpy.GetParameterAsText(0) #Carpeta de Mxd
Absolute_Relative = arcpy.GetParameterAsText(1) #Para definir si se quiere con Absolote Path o Relative Path
mxdList = [] #Lista por ahora vacía donde se amacenaran las rutas de los MXD a modificar

#For para rellenar la lista mxdList con las rutas de los MXD a modificar
for dirpath, subdirs, files in os.walk(source):
	for x in files:
		if x.endswith(".mxd"):
			mxdList.append(os.path.join(dirpath, x))

arcpy.AddMessage("\n")
arcpy.AddMessage("Procesando: ")
arcpy.AddMessage("\n")

#For para establcer "Absolute Path" o "Relative Path" a cada uno de los MXD
for file in mxdList:
	mxd = arcpy.mapping.MapDocument(file) #Creacion de variable Arcpy para abrir/almacenar MXD
	arcpy.AddMessage("Procesando: " + file) #Mensaje al usuario
	if Absolute_Relative == "Absolute Path": #If para definir la propiedad Absolote Path o Relative Path
		mxd.relativePaths = False
	if Absolute_Relative == "Relative Path":
		mxd.relativePaths = True
	mxd.save() #Guardar MXD
	del mxd #Cerrar MXD

#Mensaje al usuario de exito de ejecucion
arcpy.AddMessage("\n")
arcpy.AddMessage("Todo fue configurado según lo establecido!")
