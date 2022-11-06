#Implementacion JCI Ronald Chavez 2019

import arcpy, os

# Carpeta de los MXDs
Fuente = arcpy.GetParameterAsText(0)
MXD_list = []
MXD_list_temp = []
 
Booleano = arcpy.GetParameterAsText(1)
TextOld1= arcpy.GetParameterAsText(2)
TextNew1= arcpy.GetParameterAsText(3)
TextOld2= arcpy.GetParameterAsText(4)
TextNew2= arcpy.GetParameterAsText(5)
TextOld3= arcpy.GetParameterAsText(6)
TextNew3= arcpy.GetParameterAsText(7)
TextOld4= arcpy.GetParameterAsText(8)
TextNew4= arcpy.GetParameterAsText(9)
TextOld5= arcpy.GetParameterAsText(10)
TextNew5= arcpy.GetParameterAsText(11)

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

for mxd in MXD_list:
  MXDpath = mxd
  mapdoc = arcpy.mapping.MapDocument(MXDpath)
  for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
    if elm.text == TextOld1:
      elm.text = TextNew1
      #mapdoc.save()
      arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew1)
  #del mxd
  
  for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
    if elm.text == TextOld2:
      elm.text = TextNew2
      #mapdoc.save()
      arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew2)
  #del mxd	  

  for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
    if elm.text == TextOld3:
      elm.text = TextNew3
      #mapdoc.save()
      arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew3)
  #del mxd
  
  for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
    if elm.text == TextOld4:
      elm.text = TextNew4
      #mapdoc.save()
      arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew4)
  #del mxd
  
  for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
    if elm.text == TextOld5:
      elm.text = TextNew5
      #mapdoc.save()
      arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew5)
  mapdoc.save()
  del mapdoc

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")