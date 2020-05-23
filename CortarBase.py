#Importar modulos del sistema
import arcpy
from arcpy import env

#Configurar variables
Area_Estudio = arcpy.GetParameterAsText(0)
Sistema_coordenadas_objetivo = arcpy.GetParameterAsText(1)
	#Sistema_coordenadas_objetivo = arcpy.SpatialReference(4326)
	#GCS_WGS_1984 WKID: 4326
	#WGS_1984_UTM_Zone_17S WKID: 32717 
	#WGS_1984_UTM_Zone_18S WKID: 32718
	#WGS_1984_UTM_Zone_19S WKID: 32719

#Configurar espacio de trabajo
env.workspace = arcpy.GetParameterAsText(2)

#Variables de ubicación de shapes base
in_feature_1 = r"C:\Users\jalvarez\OneDrive\Estudios\ArcGis Y QGIS\Tutoriales canal de Youtube\Geodatabase_entrada.gdb\Capital_Distrital"
in_feature_2 = r"C:\Users\jalvarez\OneDrive\Estudios\ArcGis Y QGIS\Tutoriales canal de Youtube\Geodatabase_entrada.gdb\Lim_Distrital"
in_feature_3 = r"C:\Users\jalvarez\OneDrive\Estudios\ArcGis Y QGIS\Tutoriales canal de Youtube\Geodatabase_entrada.gdb\Vias_Nacionales"

#Variable temporal con nombre del shape
out_feature_1_temp = "Capital_Distrital_temp"
out_feature_2_temp = "Lim_Distrital_temp"
out_feature_3_temp = "Vias_Nacionales_temp"

#Variable con nombre del shape
out_feature_1 = "Capital_Distrital"
out_feature_2 = "Lim_Distrital"
out_feature_3 = "Vias_Nacionales"

#Ejecutar Clip
arcpy.AddMessage("\n")
arcpy.AddMessage("Ejecutando clip...")
arcpy.Clip_analysis(in_feature_1, Area_Estudio, out_feature_1_temp)
arcpy.Clip_analysis(in_feature_2, Area_Estudio, out_feature_2_temp)
arcpy.Clip_analysis(in_feature_3, Area_Estudio, out_feature_3_temp)

#Ejecutar cambio/conversion de proyeccion
arcpy.AddMessage("\n")
arcpy.AddMessage("Convirtiendo al sistema de coordenadas seleccionado...")
arcpy.Project_management(out_feature_1_temp, out_feature_1, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_2_temp, out_feature_2, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_3_temp, out_feature_3, Sistema_coordenadas_objetivo)

#Borrar shapes temporales
	#arcpy.DeleteFeatures_management(shape) es para borrar todos los features internos
arcpy.AddMessage("\n")
arcpy.AddMessage("Borrando featureclass temporales...")
arcpy.Delete_management(out_feature_1_temp)
arcpy.Delete_management(out_feature_2_temp)
arcpy.Delete_management(out_feature_3_temp)


arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente")