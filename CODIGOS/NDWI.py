import arcpy
from arcpy.sa import *

def calcular_ndwi(b3, b5, area, ndwi_clip):
    # Permite sobrescribir sobre archivos de salidas ya creados asi en caso de crear otro con el mismo nombre
    # no hay necesidad de borrar el otro ya que este lo hace
    arcpy.env.overwriteOutput = True

     # Confirmacion de que el usuario tiene habilitado el uso de las extensiones
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    b3_raster = arcpy.Raster(b3)
    b5_raster = arcpy.Raster(b5)
    area_shp = area

    # Definicion del Poligono o Shape
    desc = arcpy.Describe(area_shp)
    rectangle = f"{desc.extent.XMin} {desc.extent.YMin} {desc.extent.XMax} {desc.extent.YMax}"

    # Expresion utilizada en la calculadora de raster
    # no hay necesidad de utilzar el Float pero sirve para la entender la expresion
    NDWI = Float(b3_raster - b5_raster) / Float(b3_raster + b5_raster)

    arcpy.management.Clip(in_raster=NDWI, rectangle=rectangle, out_raster=ndwi_clip, in_template_dataset=area_shp, clipping_geometry="ClippingGeometry")
    return ndwi_clip

if __name__ == "__main__":
    b3 = arcpy.GetParameterAsText(0)  # Ruta al archivo de la banda 3
    b5 = arcpy.GetParameterAsText(1)  # Ruta al archivo de la banda 5
    area = arcpy.GetParameterAsText(2)  # Ruta al Area de estudio de los humedales
    ndwi_clip = arcpy.GetParameterAsText(3)  # Nombre para el archivo de salida

    resultado = calcular_ndwi(b3, b5, area, ndwi_clip)