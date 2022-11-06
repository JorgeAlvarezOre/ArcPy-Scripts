# Importar modulos del sistema
import arcpy, os
from datetime import date

# Declaracion de variables
Fuente = arcpy.GetParameterAsText(0) #Carpetas donde se encuentran los MXDs
MXD_list = [] # Lista para los MXD
MXD_list_temp = [] # Lista para los MXD temporal
Booleano1 = arcpy.GetParameterAsText(1) #Con o sin subcarpetas
Booleano2 = arcpy.GetParameterAsText(2) #Autorrellenar
Titulo = arcpy.GetParameterAsText(3) #Variable para el título
Resumen = arcpy.GetParameterAsText(4) #Variable para el resumen
Descripcion = arcpy.GetParameterAsText(5) #Variable para la descripción
#Etiqueta = arcpy.GetParameterAsText(6) #Variable para las etiquetas. Las etiquetas se separan por comas (,)

# Recorrer carpeta de los MXDs y enlistar los *.mxd, considerando o no las subcarpetas
if Booleano1 == "true":
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
arcpy.AddMessage("Procesando: ")

for mxd in MXD_list:
    mpk = mxd.replace(".mxd",".mpk")
    MPKpath = mpk
    
    MXDpath = mxd
    mapdoc = arcpy.mapping.MapDocument(MXDpath)
    
    if Booleano2 == "true":
        mapdoc.title = Titulo #mapdoc.filePath Cambiar despues a nombre del MXD
        mapdoc.summary = Resumen
        mapdoc.description = Descripcion
        Hoy = date.today()
        mapdoc.tags = "Mapas, Jorge Alavrez ("+str(Hoy.year)+")"
        mapdoc.save()
    
    arcpy.PackageMap_management(MXDpath, MPKpath)
    arcpy.AddMessage("El archivo MXD fue exportado en:" + MPKpath)
    
    del mapdoc

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
#os.system('shutdown -s -t 0') #Sin advertencia?