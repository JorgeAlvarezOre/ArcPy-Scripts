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
        if elm.text == TextOld1:
                elm.text = TextNew1
                mapdoc.save()
                arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew1)
    del mapdoc
