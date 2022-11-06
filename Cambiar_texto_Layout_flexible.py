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
		nuevotexto1a = '' + elm.text
		if TextOld1 in nuevotexto1a:
			nuevotexto1b = nuevotexto1a.replace(TextOld1,TextNew1)
			arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew1)
			elm.text = nuevotexto1b
			#mapdoc.save()

	for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
		nuevotexto2a = '' + elm.text
		if TextOld2 in nuevotexto2a:
			nuevotexto2b = nuevotexto2a.replace(TextOld2,TextNew2)
			arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew2)
			elm.text = nuevotexto2b
			#mapdoc.save()

	for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
		nuevotexto3a = '' + elm.text
		if TextOld3 in nuevotexto3a:
			nuevotexto3b = nuevotexto3a.replace(TextOld3,TextNew3)
			arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew3)
			elm.text = nuevotexto3b
			#mapdoc.save()

	for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
		nuevotexto4a = '' + elm.text
		if TextOld4 in nuevotexto4a:
			nuevotexto4b = nuevotexto4a.replace(TextOld4,TextNew4)
			arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew4)
			elm.text = nuevotexto4b
			#mapdoc.save()

	for elm in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"):
		nuevotexto5a = '' + elm.text
		if TextOld5 in nuevotexto5a:
			nuevotexto5b = nuevotexto5a.replace(TextOld5,TextNew5)
			arcpy.AddMessage("Texto corregido y MXD guardado: "+ MXDpath + " " + TextNew5)
			elm.text = nuevotexto5b
			#mapdoc.save()
	mapdoc.save()
	del mapdoc

arcpy.AddMessage("\n")
arcpy.AddMessage("Proceso finalizado correctamente. Gracias por utilizar este script. Jorge Alvarez (2022)")
