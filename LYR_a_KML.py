#Importar modulo arcpy
import arcpy

#Configurar espacio de trabajo (Workspace)
arcpy.env.workspace = arcpy.GetParameterAsText(0)

if len(arcpy.ListFiles("*.lyr")) > 0:
    for layer in arcpy.ListFiles("*.lyr"):
        #Configurar variable
        outKML = layer[:-4] + ".kmz"
        #Ejecutar LayerToKML
        arcpy.LayerToKML_conversion(layer, outKML)
        arcpy.AddMessage('Se convirtio el archivo: '+outKML+'.')
else:
    arcpy.AddMessage('No se econtraron archivos *.lyr en '+arcpy.env.workspace+'.')
