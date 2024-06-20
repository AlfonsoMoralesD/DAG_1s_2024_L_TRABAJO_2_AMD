import arcpy
from arcpy.sa import *

def calcular_diferencia_ndvi(rNdvi_24, rNdvi_14, outNDVI):
   
    arcpy.env.overwriteOutput = True

    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    ndvi_24 = arcpy.Raster(rNdvi_24)
    ndvi_14 = arcpy.Raster(rNdvi_14)

    # Proceso: Calculadora de rasters (Raster Calculator)
    diferencia_ndvi = ndvi_24 - ndvi_14
    diferencia_ndvi.save(outNDVI)

    return outNDVI

if __name__ == "__main__":
    # Parametros de entrada
    rNdvi_24 = arcpy.GetParameterAsText(0)
    rNdvi_14 = arcpy.GetParameterAsText(1)
    outNDVI = arcpy.GetParameterAsText(2)

    # Llamar a la funcion principal con los parametros proporcionados
    resultado = calcular_diferencia_ndvi(rNdvi_24, rNdvi_14, outNDVI)
    
