import arcpy
from arcpy.sa import *

def calcular_diferencia_ndwi(rNdwi_24, rNdwi_14, outNDWI):

    arcpy.env.overwriteOutput = True

    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    ndwi_24 = arcpy.Raster(rNdwi_24)
    ndwi_14 = arcpy.Raster(rNdwi_14)

    # Proceso: Calculadora de rasters (Raster Calculator)
    diferencia_ndwi = ndwi_24 - ndwi_14
    diferencia_ndwi.save(outNDWI)

    return outNDWI

if __name__ == "__main__":
    # Parametros de entrada
    rNdwi_24 = arcpy.GetParameterAsText(0)
    rNdwi_14 = arcpy.GetParameterAsText(1)
    outNDWI = arcpy.GetParameterAsText(2)

    # Llamar a la funcion principal con los parametros proporcionados
    resultado = calcular_diferencia_ndwi(rNdwi_24, rNdwi_14, outNDWI)
