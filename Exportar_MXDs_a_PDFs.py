#Implementacion JCI Ronald Chavez 2019

# Importar modulos del sistema
import arcpy, os

#Cambiar a carpetas donde se encuentran los MXDs
Fuente = arcpy.GetParameterAsText(0)
MXD_list = []
MXD_list_temp = []

Booleano = arcpy.GetParameterAsText(1)

#change qual to desired level, choose: "BEST", "BETTER", "NORMAL", "FASTER", "FASTEST"
qual = arcpy.GetParameterAsText(2)

#change res to desired value
res = arcpy.GetParameterAsText(3)

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
arcpy.AddMessage("Procesando: ")
arcpy.AddMessage("\n")

for mxd in MXD_list:
	pdf = mxd.replace(".mxd",".pdf")
	MXDpath = mxd
	
	mapdoc = arcpy.mapping.MapDocument(MXDpath)
	PDFpath = pdf
	
	arcpy.mapping.ExportToPDF(mapdoc,PDFpath,"PAGE_LAYOUT",0,0,res,qual)
	arcpy.AddMessage("El archivo MXD fue exportado en:" + PDFpath)
	del mapdoc
  
arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
