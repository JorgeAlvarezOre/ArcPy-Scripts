#Importar las librerias necesarias
import arcpy, os

#Carpeta con MXDs y creacion de lista vacia mxdList
source = arcpy.GetParameterAsText(0)
mxdList = []

#Creacion de variables de texto
TextOld1= arcpy.GetParameterAsText(1)
TextNew1= arcpy.GetParameterAsText(2)

#For para rellenar lista mxdList con ruta de cada MXD
for dirpath, subdirs, files in os.walk(source):
    for x in files:
        if x.endswith(".mxd"):
            mxdList.append(os.path.join(dirpath, x))

#For para modificar MXDs si encuentra el texto especificado
for mxd in mxdList:
    MXDpath = mxd
    mapdoc = arcpy.mapping.MapDocument(MXDpath)
    for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
        nuevotexto1a = '' + elm.text
        if TextOld1 in nuevotexto1a:
            nuevotexto1b = nuevotexto1a.replace(TextOld1,TextNew1)
            arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew1)
            elm.text = nuevotexto1b
            mapdoc.save()
    del mapdoc
