# Análisis del estado de los humedales 
## Introducción del trabajo
El trabajo consta con lograr determinar el estado de los humedales pricipalmente para la comuna de quilicura, este fue el lugar de aplicación donde se aplicaron las condiciones para la determinacion del estado actual y realizar una comparativa temporal entre los ultimos 10 años con el fin de poder evaluar como se encontraba el humedal en el momento de la megasequia y comparar si actualmente a empeorado su estado o mejorado con el pasar de los años.
## Herramienta NDVI y NDWI
Para el analisis temporal y determinacion del estado de los humedales, se realizaron 2 herramientas en particular, se realizo un herramienta para determinar el NDVI con el fin de poder obterner un indice del estado de salud de la vegetación en la zona, evaluar los rangos donde se encuentra la vegetacion de los humedales.
Por otra parte se complemento esta informacion con la creacion de una herramienta que mida el NDWI con el fin de poder obtener los niveles de humedad de la zona y evaluar los rangos en los que se mueve la zona para determinar si es que se encuentra en los rangos donde se encuentran los humedales.
Estas herramientas tienen la misma logica utilizan 2 bandas satelitales del satelite Landsat 8.
- NDVI: Banda infrarroja (Banda 5), Banda Roja (banda 4)
- NDWI: Banda infrarroja (Banda 5), Banda Verde (Banda 3)
## Calculadora de Raster
Este calculo se realizo con el proceso de Calculadora de Raster,
Para el calculo del NDVI y el NDWI la expresion utilizada es:
- NDVI = (b5_raster - b4_raster) / (b5_raster + b4_raster)
- NDWI = (b3_raster - b5_raster) / (b3_raster + b5_raster)

El resultado de estas expresiones, necesitamos realizar el corte del area de estudio el cual se encuentra en la Feature Dataset de la GDB, y para esto utilizamos la herramienta clip. (arcpy.management.Clip) que tiene como entrada, el resultado de la expresión del NDVI o NDWI, el area el cual cortara con la forma de los humedales y su expresión se visibiliza asi:
- arcpy.management.Clip(in_raster=NDVI, rectangle=rectangle, out_raster=ndvi_clip, in_template_dataset=area_shp, clipping_geometry="ClippingGeometry").

Esta expresion se utilizo para el calculo del NDVI como el NDWI, solo que para el NDWI se modifico el texto anterior con las variables del NDWI y la expresion de la calculadora de raster.

## Interpretacion de los resultados (NDVI y NDWI)
 Luego de aplicar estas dos herramientas se le aplico a la imagen resultante en los parametros de la tool properties en la salida resultante del NDWI y NDWI una simbologia aplicando los parametros relevantes para el estudio de estos indices.

 - NDVI: nos importan los valores desde 0 hasta el + 1
 - NDWI: nos importan los valores negativos cercanos a 0 y los positivos hasta el + 1.

Sin embargo para el analisis de humedales el NDVI nos interesan los valores entre +0.2 a +0.6 y para el NDWI nos interesan los valores positivos entre 0 y +0,2 porque aqui se encuentra el rango normal de los huemdales.

## Calculo del diferencial del NDWI y NDWI
## Interpretacion de los resultados
 por otro lado se creo otra herramienta la cual es el resultado del diferencial de los NDVI y NDWI, se utilizo la expresion de restar los resultados del NDVI_2014 y NDVI_2024, y la entrega de este resultaria en el diferencial del NDVI y los valores positivos indican la mejora de la vegetacion de la zona y los valores negativos significan que ha empeorado la vegetacion de los humedales en esos años. Para el NDWI se utilizo lo mismo pero con el resultado del NDWI_2014 y NDWI_2024, y los valores negativos representan una perdida en la humedad en los humedales y los valores positivos representan una ganancia de humedad en los humedales.

## Informacion sobre la licencia de uso para este codigo
 Es de suma importancia considerar que para poder aplicar estas herramientas se necesita que el usuario cuente con licencia de ArcGis Pro el cual realmente es un limitante, porque para un usuario con una licencia avanzada se le liberan las herramientas necesarias para este trabajo, asi que el programa igualmente se ejecutara siempre y cuando tenga la licencia activa y esta revisara primero que tengas acceso a las herramientas con esta expresion.
- arcpy.CheckOutExtension("spatial")
- arcpy.CheckOutExtension("ImageAnalyst")




