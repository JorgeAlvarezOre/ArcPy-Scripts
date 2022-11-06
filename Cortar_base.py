# Importar modulos del sistema. En Python 2 evitar SIEMPRE tildes, ñ y caracteres raros.
import arcpy
from arcpy import env
import os

# Establecer variables locales
Area_corte = arcpy.GetParameterAsText(0)
Sistema_coordenadas_objetivo = arcpy.GetParameterAsText(1)
	#Sistema_coordenadas_objetivo = arcpy.SpatialReference("WGS 1984 UTM Zone 18S")
	#GCS_WGS_1984 WKID: 4326
	#WGS_1984_UTM_Zone_17S WKID: 32717 
	#WGS_1984_UTM_Zone_18S WKID: 32718
	#WGS_1984_UTM_Zone_19S WKID: 32719

# Configurar workspace (espacio de trabajo) y Geodatabase base
env.workspace = arcpy.GetParameterAsText(2)

Ruta_GDB_maestro = r"G:\Jorge\Utilitarios ArcGIS\Geodatabase_Peru.gdb"

in_feature_1 = os.path.join(Ruta_GDB_maestro,"AguajalesBofedales")
# in_feature_1 = r"G:\Jorge\Onedrive\Estudios\ArcGis y QGIS\Curso Arcpy\GIS\Base.gdb\Aguajales_Bofedales"
in_feature_2 = os.path.join(Ruta_GDB_maestro,"ANP_Nacional")
in_feature_3 = os.path.join(Ruta_GDB_maestro,"ANP_Privada")
in_feature_4 = os.path.join(Ruta_GDB_maestro,"ANP_Regional")
in_feature_5 = os.path.join(Ruta_GDB_maestro,"ANP_Zona_Amortiguamiento")
in_feature_6 = os.path.join(Ruta_GDB_maestro,"Capital_Departamental")
in_feature_7 = os.path.join(Ruta_GDB_maestro,"Capital_Distrital")
in_feature_8 = os.path.join(Ruta_GDB_maestro,"Capital_Provincial")
in_feature_9 = os.path.join(Ruta_GDB_maestro,"Centros_Poblados")
in_feature_10 = os.path.join(Ruta_GDB_maestro,"Comunidades_Campesinas")
in_feature_11 = os.path.join(Ruta_GDB_maestro,"Comunidades_Nativas")
in_feature_12 = os.path.join(Ruta_GDB_maestro,"Concesiones_Mineras")
in_feature_13 = os.path.join(Ruta_GDB_maestro,"Cotas")
in_feature_14 = os.path.join(Ruta_GDB_maestro,"Curvas")
in_feature_15 = os.path.join(Ruta_GDB_maestro,"Estaciones_Meteorologicas")
in_feature_16 = os.path.join(Ruta_GDB_maestro,"Islas")
in_feature_17 = os.path.join(Ruta_GDB_maestro,"Lagos")
in_feature_18 = os.path.join(Ruta_GDB_maestro,"Lim_Departamental")
in_feature_19 = os.path.join(Ruta_GDB_maestro,"Lim_Distrital")
in_feature_20 = os.path.join(Ruta_GDB_maestro,"Lim_Provincial")
in_feature_21 = os.path.join(Ruta_GDB_maestro,"Lineas_ferreas")
in_feature_22 = os.path.join(Ruta_GDB_maestro,"MAPs")
in_feature_23 = os.path.join(Ruta_GDB_maestro,"Ncerros")
in_feature_24 = os.path.join(Ruta_GDB_maestro,"Nevados")
in_feature_25 = os.path.join(Ruta_GDB_maestro,"Nlagos")
in_feature_26 = os.path.join(Ruta_GDB_maestro,"Nrios")
in_feature_27 = os.path.join(Ruta_GDB_maestro,"Oceano_Pacifico")
in_feature_28 = os.path.join(Ruta_GDB_maestro,"Polurb")
in_feature_29 = os.path.join(Ruta_GDB_maestro,"Puentes")
in_feature_30 = os.path.join(Ruta_GDB_maestro,"Rios")
in_feature_31 = os.path.join(Ruta_GDB_maestro,"Rios_Area")
in_feature_32 = os.path.join(Ruta_GDB_maestro,"Senales")
in_feature_33 = os.path.join(Ruta_GDB_maestro,"Vias_departamentales")
in_feature_34 = os.path.join(Ruta_GDB_maestro,"Vias_Nacionales")
in_feature_35 = os.path.join(Ruta_GDB_maestro,"Vias_Vecinales")

out_feature_1_temp = "AGUAJALES_BOFEDALES_temp"
out_feature_2_temp = "ANP_NACIONAL_temp"
out_feature_3_temp = "ANP_PRIVADA_temp"
out_feature_4_temp = "ANP_REGIONAL_temp"
out_feature_5_temp = "ANP_ZONA_AMORTIGUAMIENTO_temp"
out_feature_6_temp = "CAPITAL_DEPARTAMENTAL_temp"
out_feature_7_temp = "CAPITAL_DISTRITAL_temp"
out_feature_8_temp = "CAPITAL_PROVINCIAL_temp"
out_feature_9_temp = "CENTROS_POBLADOS_temp"
out_feature_10_temp = "COMUNIDADES_CAMPESINAS_temp"
out_feature_11_temp = "COMUNIDADES_NATIVAS_temp"
out_feature_12_temp = "CONCESIONES_MINERAS_temp"
out_feature_13_temp = "COTAS_temp"
out_feature_14_temp = "CURVAS_temp"
out_feature_15_temp = "ESTACIONES_METEOROLOGICAS_temp"
out_feature_16_temp = "ISLAS_temp"
out_feature_17_temp = "LAGOS_temp"
out_feature_18_temp = "LIM_DEPARTAMENTAL_temp"
out_feature_19_temp = "LIM_DISTRITAL_temp"
out_feature_20_temp = "LIM_PROVINCIAL_temp"
out_feature_21_temp = "VIAS_FERREAS_temp"
out_feature_22_temp = "MAPs_temp"
out_feature_23_temp = "NCERROS_temp"
out_feature_24_temp = "NEVADOS_temp"
out_feature_25_temp = "NLAGOS_temp"
out_feature_26_temp = "NRIOS_temp"
out_feature_27_temp = "OCEANO_PACIFICO_temp"
out_feature_28_temp = "CASCO_URBANO_temp"
out_feature_29_temp = "PUENTES_temp"
out_feature_30_temp = "RIOS_temp"
out_feature_31_temp = "RIOS_AREA_temp"
out_feature_32_temp = "SENHALES_temp"
out_feature_33_temp = "VIAS_DEPARTAMENTALES_temp"
out_feature_34_temp = "VIAS_NACIONALES_temp"
out_feature_35_temp = "VIAS_VECINALES_temp"

out_feature_1 = "AGUAJALES_BOFEDALES"
out_feature_2 = "ANP_NACIONAL"
out_feature_3 = "ANP_PRIVADA"
out_feature_4 = "ANP_REGIONAL"
out_feature_5 = "ANP_ZONA_AMORTIGUAMIENTO"
out_feature_6 = "CAPITAL_DEPARTAMENTAL"
out_feature_7 = "CAPITAL_DISTRITAL"
out_feature_8 = "CAPITAL_PROVINCIAL"
out_feature_9 = "CENTROS_POBLADOS"
out_feature_10 = "COMUNIDADES_CAMPESINAS"
out_feature_11 = "COMUNIDADES_NATIVAS"
out_feature_12 = "CONCESIONES_MINERAS"
out_feature_13 = "COTAS"
out_feature_14 = "CURVAS"
out_feature_15 = "ESTACIONES_METEOROLOGICAS"
out_feature_16 = "ISLAS"
out_feature_17 = "LAGOS"
out_feature_18 = "LIM_DEPARTAMENTAL"
out_feature_19 = "LIM_DISTRITAL"
out_feature_20 = "LIM_PROVINCIAL"
out_feature_21 = "VIAS_FERREAS"
out_feature_22 = "MAPs"
out_feature_23 = "NCERROS"
out_feature_24 = "NEVADOS"
out_feature_25 = "NLAGOS"
out_feature_26 = "NRIOS"
out_feature_27 = "OCEANO_PACIFICO"
out_feature_28 = "CASCO_URBANO"
out_feature_29 = "PUENTES"
out_feature_30 = "RIOS"
out_feature_31 = "RIOS_AREA"
out_feature_32 = "SENHALES"
out_feature_33 = "VIAS_DEPARTAMENTALES"
out_feature_34 = "VIAS_NACIONALES"
out_feature_35 = "VIAS_VECINALES"

#Ejecutar clip
arcpy.AddMessage("\n") #print("\n") en Geoprocessing > Python
arcpy.AddMessage("Ejecutando clip...") #print("Ejecutando clip...") en Geoprocessing > Python
arcpy.Clip_analysis(in_feature_1, Area_corte, out_feature_1_temp)
arcpy.Clip_analysis(in_feature_2, Area_corte, out_feature_2_temp)
arcpy.Clip_analysis(in_feature_3, Area_corte, out_feature_3_temp)
arcpy.Clip_analysis(in_feature_4, Area_corte, out_feature_4_temp)
arcpy.Clip_analysis(in_feature_5, Area_corte, out_feature_5_temp)
arcpy.Clip_analysis(in_feature_6, Area_corte, out_feature_6_temp)
arcpy.Clip_analysis(in_feature_7, Area_corte, out_feature_7_temp)
arcpy.Clip_analysis(in_feature_8, Area_corte, out_feature_8_temp)
arcpy.Clip_analysis(in_feature_9, Area_corte, out_feature_9_temp)
arcpy.Clip_analysis(in_feature_10, Area_corte, out_feature_10_temp)
arcpy.Clip_analysis(in_feature_11, Area_corte, out_feature_11_temp)
arcpy.Clip_analysis(in_feature_12, Area_corte, out_feature_12_temp)
arcpy.Clip_analysis(in_feature_13, Area_corte, out_feature_13_temp)
arcpy.Clip_analysis(in_feature_14, Area_corte, out_feature_14_temp)
arcpy.Clip_analysis(in_feature_15, Area_corte, out_feature_15_temp)
arcpy.Clip_analysis(in_feature_16, Area_corte, out_feature_16_temp)
arcpy.Clip_analysis(in_feature_17, Area_corte, out_feature_17_temp)
arcpy.Clip_analysis(in_feature_18, Area_corte, out_feature_18_temp)
arcpy.Clip_analysis(in_feature_19, Area_corte, out_feature_19_temp)
arcpy.Clip_analysis(in_feature_20, Area_corte, out_feature_20_temp)
arcpy.Clip_analysis(in_feature_21, Area_corte, out_feature_21_temp)
arcpy.Clip_analysis(in_feature_22, Area_corte, out_feature_22_temp)
arcpy.Clip_analysis(in_feature_23, Area_corte, out_feature_23_temp)
arcpy.Clip_analysis(in_feature_24, Area_corte, out_feature_24_temp)
arcpy.Clip_analysis(in_feature_25, Area_corte, out_feature_25_temp)
arcpy.Clip_analysis(in_feature_26, Area_corte, out_feature_26_temp)
arcpy.Clip_analysis(in_feature_27, Area_corte, out_feature_27_temp)
arcpy.Clip_analysis(in_feature_28, Area_corte, out_feature_28_temp)
arcpy.Clip_analysis(in_feature_29, Area_corte, out_feature_29_temp)
arcpy.Clip_analysis(in_feature_30, Area_corte, out_feature_30_temp)
arcpy.Clip_analysis(in_feature_31, Area_corte, out_feature_31_temp)
arcpy.Clip_analysis(in_feature_32, Area_corte, out_feature_32_temp)
arcpy.Clip_analysis(in_feature_33, Area_corte, out_feature_33_temp)
arcpy.Clip_analysis(in_feature_34, Area_corte, out_feature_34_temp)
arcpy.Clip_analysis(in_feature_35, Area_corte, out_feature_35_temp)

#Ejecutar cambio/conversion de proyeccion
arcpy.AddMessage("\n")
arcpy.AddMessage("Convirtiendo al sistema de coordenadas seleccionado...")
#arcpy.Project_management(r"G:\Jorge\Onedrive\Estudios\ArcGis y QGIS\Curso Arcpy\GIS\Salida_temp.gdb\AGUAJALES_BOFEDALES_temp", out_feature_1, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_1_temp, out_feature_1, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_2_temp, out_feature_2, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_3_temp, out_feature_3, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_4_temp, out_feature_4, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_5_temp, out_feature_5, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_6_temp, out_feature_6, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_7_temp, out_feature_7, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_8_temp, out_feature_8, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_9_temp, out_feature_9, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_10_temp, out_feature_10, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_11_temp, out_feature_11, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_12_temp, out_feature_12, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_13_temp, out_feature_13, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_14_temp, out_feature_14, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_15_temp, out_feature_15, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_16_temp, out_feature_16, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_17_temp, out_feature_17, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_18_temp, out_feature_18, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_19_temp, out_feature_19, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_20_temp, out_feature_20, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_21_temp, out_feature_21, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_22_temp, out_feature_22, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_23_temp, out_feature_23, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_24_temp, out_feature_24, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_25_temp, out_feature_25, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_26_temp, out_feature_26, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_27_temp, out_feature_27, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_28_temp, out_feature_28, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_29_temp, out_feature_29, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_30_temp, out_feature_30, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_31_temp, out_feature_31, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_32_temp, out_feature_32, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_33_temp, out_feature_33, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_34_temp, out_feature_34, Sistema_coordenadas_objetivo)
arcpy.Project_management(out_feature_35_temp, out_feature_35, Sistema_coordenadas_objetivo)

#Borrar shapes temporales
	#arcpy.DeleteFeatures_management(shape) es para borrar todos los features internos
arcpy.AddMessage("\n")
arcpy.AddMessage("Borrando featureclass temporales...")
arcpy.Delete_management(out_feature_1_temp)
arcpy.Delete_management(out_feature_2_temp)
arcpy.Delete_management(out_feature_3_temp)
arcpy.Delete_management(out_feature_4_temp)
arcpy.Delete_management(out_feature_5_temp)
arcpy.Delete_management(out_feature_6_temp)
arcpy.Delete_management(out_feature_7_temp)
arcpy.Delete_management(out_feature_8_temp)
arcpy.Delete_management(out_feature_9_temp)
arcpy.Delete_management(out_feature_10_temp)
arcpy.Delete_management(out_feature_11_temp)
arcpy.Delete_management(out_feature_12_temp)
arcpy.Delete_management(out_feature_13_temp)
arcpy.Delete_management(out_feature_14_temp)
arcpy.Delete_management(out_feature_15_temp)
arcpy.Delete_management(out_feature_16_temp)
arcpy.Delete_management(out_feature_17_temp)
arcpy.Delete_management(out_feature_18_temp)
arcpy.Delete_management(out_feature_19_temp)
arcpy.Delete_management(out_feature_20_temp)
arcpy.Delete_management(out_feature_21_temp)
arcpy.Delete_management(out_feature_22_temp)
arcpy.Delete_management(out_feature_23_temp)
arcpy.Delete_management(out_feature_24_temp)
arcpy.Delete_management(out_feature_25_temp)
arcpy.Delete_management(out_feature_26_temp)
arcpy.Delete_management(out_feature_27_temp)
arcpy.Delete_management(out_feature_28_temp)
arcpy.Delete_management(out_feature_29_temp)
arcpy.Delete_management(out_feature_30_temp)
arcpy.Delete_management(out_feature_31_temp)
arcpy.Delete_management(out_feature_32_temp)
arcpy.Delete_management(out_feature_33_temp)
arcpy.Delete_management(out_feature_34_temp)
arcpy.Delete_management(out_feature_35_temp)

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
