import arcpy, os

# Cambiar a carpeta con los MXD
Fuente = arcpy.GetParameterAsText(0)
MXD_list = []
MXD_list_temp = []

Booleano = arcpy.GetParameterAsText(1)
RutaOld1 = arcpy.GetParameterAsText(2)
RutaNew1 = arcpy.GetParameterAsText(3)
RutaOld2 = arcpy.GetParameterAsText(4)
RutaNew2 = arcpy.GetParameterAsText(5)
RutaOld3 = arcpy.GetParameterAsText(6)
RutaNew3 = arcpy.GetParameterAsText(7)
RutaOld4 = arcpy.GetParameterAsText(8)
RutaNew4 = arcpy.GetParameterAsText(9)
RutaOld5 = arcpy.GetParameterAsText(10)
RutaNew5 = arcpy.GetParameterAsText(11)

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

arcpy.AddMessage("Procesando:")

for mxd in MXD_list:
    MXDpath = mxd
    mapdoc = arcpy.mapping.MapDocument(MXDpath)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld1, RutaNew1)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld2, RutaNew2)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld3, RutaNew3)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld4, RutaNew4)
    mapdoc.findAndReplaceWorkspacePaths(RutaOld5, RutaNew5)
    mapdoc.save()
    del mapdoc
    arcpy.AddMessage("El MXD fue sobreescrito correctamente")

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
