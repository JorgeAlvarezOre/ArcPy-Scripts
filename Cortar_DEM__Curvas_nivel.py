# -*- coding: utf-8 -*-

#DEM Alos Palsar RTC ~ 12.5 m/pixel (© JAXA/METI, 2015)
#DEM Aster Global DEM V003 ~ 30 m/pixel (NASA/METI, 2013)
#DEM MERIT DEM ~ 90m/pixel (Yamazaki D. et al, 2017)

#Set the necessary product code
#Import system modules
#import arceditor
import arcpy
from arcpy import env

#Set local variables
Area_corte = arcpy.GetParameterAsText(0)
Sistema_coordenadas_objetivo = arcpy.GetParameterAsText(1)
	#Sistema_coordenadas_objetivo = arcpy.SpatialReference(4326)
	#GCS_WGS_1984 WKID: 4326
	#WGS_1984_UTM_Zone_17S WKID: 32717 
	#WGS_1984_UTM_Zone_18S WKID: 32718
	#WGS_1984_UTM_Zone_19S WKID: 32719
Espaciado_vertical_curvas_nivel = arcpy.GetParameterAsText(2)
env.workspace = arcpy.GetParameterAsText(3) # Set workspace
Booleano_DEM_Hillshade_Alos_Palsar_Peru = arcpy.GetParameterAsText(4)
Booleano_DEM_Hillshade_Aster_Global_Peru_V003 = arcpy.GetParameterAsText(5)
Booleano_DEM_Hillshade_MERIT_Peru = arcpy.GetParameterAsText(6)
Booleano_Curvas_nivel_Alos_Palsar_Peru = arcpy.GetParameterAsText(7)
Booleano_Curvas_nivel_Aster_Global_Peru_V003 = arcpy.GetParameterAsText(8)
Booleano_Curvas_nivel_MERIT_Peru = arcpy.GetParameterAsText(9)

#Ruta DEMs base
DEM_Alos_Palsar = r"G:\Jorge\Utilitarios ArcGIS\Geodatabase_Peru_DEM.gdb\DEM_Alos_Palsar_Peru"
DEM_Aster_Global = r"G:\Jorge\Utilitarios ArcGIS\Geodatabase_Peru_DEM.gdb\DEM_Aster_Global_Peru_V003"
DEM_MERIT = r"G:\Jorge\Utilitarios ArcGIS\Geodatabase_Peru_DEM.gdb\DEM_MERIT_Peru"

if Booleano_DEM_Hillshade_Alos_Palsar_Peru == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando DEM y Hillshade desde Alos Palsar")
	arcpy.gp.ExtractByMask_sa(DEM_Alos_Palsar, Area_corte, "DEM_Alos_Palsar_Clip_Temp")
	arcpy.ProjectRaster_management("DEM_Alos_Palsar_Clip_Temp", "DEM_ALOS_PALSAR", Sistema_coordenadas_objetivo)
	arcpy.HillShade_3d("DEM_Alos_Palsar_Clip_Temp", "HILLSHADE_Alos_Palsar_Clip_Temp", "315", "45", "NO_SHADOWS", "1")
	arcpy.ProjectRaster_management("HILLSHADE_Alos_Palsar_Clip_Temp", "HILLSHADE_ALOS_PALSAR", Sistema_coordenadas_objetivo)
	arcpy.Delete_management("DEM_Alos_Palsar_Clip_Temp")
	arcpy.Delete_management("HILLSHADE_Alos_Palsar_Clip_Temp")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("DEM y Hillshade desde Alos Palsar creado")

if Booleano_Curvas_nivel_Alos_Palsar_Peru == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando Curvas de nivel desde Alos Palsar")
	arcpy.gp.Contour_sa("DEM_ALOS_PALSAR", "CURVAS_AP_TSS", Espaciado_vertical_curvas_nivel, "0", "1")
	Smoothing_Tolerance_Alos_Palsar = str(Espaciado_vertical_curvas_nivel) + " Meters"
	arcpy.SmoothLine_cartography("CURVAS_AP_TSS", "CURVAS_ALOS_PALSAR", "PAEK", Smoothing_Tolerance_Alos_Palsar, "FIXED_CLOSED_ENDPOINT", "FLAG_ERRORS")
	arcpy.Delete_management("CURVAS_AP_TSS")
	arcpy.AddField_management("CURVAS_ALOS_PALSAR", "Tipo", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ALOS_PALSAR", "ALTITUD", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ALOS_PALSAR", "FUENTE", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ALOS_PALSAR", "ACTUALIZADO", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.CalculateField_management("CURVAS_ALOS_PALSAR", "ALTITUD", "[Contour]", "VB", "")
	arcpy.MakeFeatureLayer_management("CURVAS_ALOS_PALSAR", "CURVAS_ALOS_PALSAR_FeatureLayer")
	MOD_Curvas_Principales_Alos_Palsar = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") = 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_ALOS_PALSAR_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Principales_Alos_Palsar)
	arcpy.CalculateField_management("CURVAS_ALOS_PALSAR_FeatureLayer", "Tipo", "\"CURVAS PRINCIPALES\"", "VB", "")
	MOD_Curvas_Secundarias_Alos_Palsar = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") <> 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_ALOS_PALSAR_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Secundarias_Alos_Palsar)
	arcpy.CalculateField_management("CURVAS_ALOS_PALSAR_FeatureLayer", "Tipo", "\"CURVAS SECUNDARIAS\"", "VB", "")
	arcpy.SelectLayerByAttribute_management("CURVAS_ALOS_PALSAR_FeatureLayer", "CLEAR_SELECTION")
	arcpy.DeleteField_management("CURVAS_ALOS_PALSAR_FeatureLayer", "Id;InLine_FID;SmoLnFLag;Contour")
	arcpy.CalculateField_management("CURVAS_ALOS_PALSAR_FeatureLayer", "FUENTE", "\"JAXA/METI\"", "VB", "")
	arcpy.CalculateField_management("CURVAS_ALOS_PALSAR_FeatureLayer", "ACTUALIZADO", "2015", "VB", "")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Curvas de nivel desde Alos Palsar creado")

if Booleano_DEM_Hillshade_Aster_Global_Peru_V003 == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando DEM y Hillshade desde Aster Global V003")
	arcpy.gp.ExtractByMask_sa(DEM_Aster_Global, Area_corte, "DEM_Aster_Global_Clip_Temp")
	arcpy.ProjectRaster_management("DEM_Aster_Global_Clip_Temp", "DEM_ASTER_GLOBAL", Sistema_coordenadas_objetivo)
	arcpy.HillShade_3d("DEM_Aster_Global_Clip_Temp", "HILLSHADE_DEM_Aster_Global_Clip_Temp", "315", "45", "NO_SHADOWS", "1")
	arcpy.ProjectRaster_management("HILLSHADE_DEM_Aster_Global_Clip_Temp", "HILLSHADE_ASTER_GLOBAL", Sistema_coordenadas_objetivo)
	arcpy.Delete_management("DEM_Aster_Global_Clip_Temp")
	arcpy.Delete_management("HILLSHADE_DEM_Aster_Global_Clip_Temp")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("DEM y Hillshade desde Aster Global V003 creado")

if Booleano_Curvas_nivel_Aster_Global_Peru_V003 == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando Curvas de nivel desde Aster Global V003")
	arcpy.gp.Contour_sa("DEM_ASTER_GLOBAL", "CURVAS_AG_TSS", Espaciado_vertical_curvas_nivel, "0", "1")
	Smoothing_Tolerance_Aster_Global = str(Espaciado_vertical_curvas_nivel) + " Meters"
	arcpy.SmoothLine_cartography("CURVAS_AG_TSS", "CURVAS_ASTER_GLOBAL", "PAEK", Smoothing_Tolerance_Aster_Global, "FIXED_CLOSED_ENDPOINT", "FLAG_ERRORS")
	arcpy.Delete_management("CURVAS_AG_TSS")
	arcpy.AddField_management("CURVAS_ASTER_GLOBAL", "Tipo", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ASTER_GLOBAL", "ALTITUD", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ASTER_GLOBAL", "FUENTE", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_ASTER_GLOBAL", "ACTUALIZADO", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.CalculateField_management("CURVAS_ASTER_GLOBAL", "ALTITUD", "[Contour]", "VB", "")
	arcpy.MakeFeatureLayer_management("CURVAS_ASTER_GLOBAL", "CURVAS_ASTER_GLOBAL_FeatureLayer")
	MOD_Curvas_Principales_Aster_Global = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") = 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Principales_Aster_Global)
	arcpy.CalculateField_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "Tipo", "\"CURVAS PRINCIPALES\"", "VB", "")
	MOD_Curvas_Secundarias_Aster_Global = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") <> 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Secundarias_Aster_Global)
	arcpy.CalculateField_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "Tipo", "\"CURVAS SECUNDARIAS\"", "VB", "")
	arcpy.SelectLayerByAttribute_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "CLEAR_SELECTION")
	arcpy.DeleteField_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "Id;InLine_FID;SmoLnFLag;Contour")
	arcpy.CalculateField_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "FUENTE", "\"NASA/METI\"", "VB", "")
	arcpy.CalculateField_management("CURVAS_ASTER_GLOBAL_FeatureLayer", "ACTUALIZADO", "2013", "VB", "")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Curvas de nivel desde Aster Global V003 creado")

if Booleano_DEM_Hillshade_MERIT_Peru == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando DEM y Hillshade desde MERIT")
	arcpy.gp.ExtractByMask_sa(DEM_MERIT, Area_corte, "DEM_MERIT_Clip_Temp")
	arcpy.ProjectRaster_management("DEM_MERIT_Clip_Temp", "DEM_MERIT", Sistema_coordenadas_objetivo)
	arcpy.HillShade_3d("DEM_MERIT_Clip_Temp", "HILLSHADE_DEM_MERIT_Clip_Temp", "315", "45", "NO_SHADOWS", "1")
	arcpy.ProjectRaster_management("HILLSHADE_DEM_MERIT_Clip_Temp", "HILLSHADE_MERIT", Sistema_coordenadas_objetivo)
	arcpy.Delete_management("DEM_MERIT_Clip_Temp")
	arcpy.Delete_management("HILLSHADE_DEM_MERIT_Clip_Temp")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("DEM y Hillshade desde MERIT creado")

if Booleano_Curvas_nivel_MERIT_Peru == "true":
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Creando Curvas de nivel desde MERIT")
	arcpy.gp.Contour_sa("DEM_MERIT", "CURVAS_M_TSS", Espaciado_vertical_curvas_nivel, "0", "1")
	Smoothing_Tolerance_MERIT = str(Espaciado_vertical_curvas_nivel) + " Meters"
	arcpy.SmoothLine_cartography("CURVAS_M_TSS", "CURVAS_MERIT", "PAEK", Smoothing_Tolerance_MERIT, "FIXED_CLOSED_ENDPOINT", "FLAG_ERRORS")
	arcpy.Delete_management("CURVAS_M_TSS")
	arcpy.AddField_management("CURVAS_MERIT", "Tipo", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_MERIT", "ALTITUD", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_MERIT", "FUENTE", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.AddField_management("CURVAS_MERIT", "ACTUALIZADO", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
	arcpy.CalculateField_management("CURVAS_MERIT", "ALTITUD", "[Contour]", "VB", "")
	arcpy.MakeFeatureLayer_management("CURVAS_MERIT", "CURVAS_MERIT_FeatureLayer")
	MOD_Curvas_Principales_MERIT = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") = 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_MERIT_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Principales_MERIT)
	arcpy.CalculateField_management("CURVAS_MERIT_FeatureLayer", "Tipo", "\"CURVAS PRINCIPALES\"", "VB", "")
	MOD_Curvas_Secundarias_MERIT = "MOD( Contour , " + str(int(Espaciado_vertical_curvas_nivel) * 5) + ") <> 0"
	arcpy.SelectLayerByAttribute_management("CURVAS_MERIT_FeatureLayer", "NEW_SELECTION", MOD_Curvas_Secundarias_MERIT)
	arcpy.CalculateField_management("CURVAS_MERIT_FeatureLayer", "Tipo", "\"CURVAS SECUNDARIAS\"", "VB", "")
	arcpy.SelectLayerByAttribute_management("CURVAS_MERIT_FeatureLayer", "CLEAR_SELECTION")
	arcpy.DeleteField_management("CURVAS_MERIT_FeatureLayer", "Id;InLine_FID;SmoLnFLag;Contour")
	arcpy.CalculateField_management("CURVAS_MERIT_FeatureLayer", "FUENTE", "\"Yamazaki D. et al\"", "VB", "")
	arcpy.CalculateField_management("CURVAS_MERIT_FeatureLayer", "ACTUALIZADO", "2017", "VB", "")
	arcpy.AddMessage("\n")
	arcpy.AddMessage("Curvas de nivel desde MERIT creado")

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")

# def initializeParameters(self)
#	self.params[10].value = True
#	self.params[10].enabled = 0

# updateParameters(self)
# if self.params[4].value == True:
# 	self.params[7].enabled = 1
# else:
# 	self.params[7].enabled = 0
# 	self.params[7].value = False
# 
# if self.params[5].value == True:
# 	self.params[8].enabled = 1
# else:
# 	self.params[8].enabled = 0
# 	self.params[8].value = False
# 
# if self.params[6].value == True:
# 	self.params[9].enabled = 1
# else:
# 	self.params[9].enabled = 0
# 	self.params[9].value = False