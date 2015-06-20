# ImageMagick-eficaz

La utilidad «convert» de ImageMagick procesa múltiples imágenes almacenándolas todas en caché antes de empezar el procesamiento. Si la memoria RAM no es suficiente para el caché, se utilizará el disco. El caché en disco genera archivos enormes que multiplican por mucho el tamaño real de las imágenes, y su procesamiento puede ser 1000% más lento. ¡1000%!

Este script usa convert para procesar múltiples imágenes de dos en dos, evitando así el caché en disco y haciéndolo 1000% más eficiente.

En mi viejo computador, convert tardaba una hora en procesar 30 imágenes. Con este script tarda una hora en procesar mil imágenes.

Este script ejecuta convert con las opciones -morph y -normalize, pudiendo elegirse la cantidad de imágenes a crear en la secuencia intermedia de morph y las imágenes origen a procesar. Debe ejecutarse en el mismo directorio donde se encuentran las imágenes a convertir.

Convert se ejecutará con estas opciones: convert *.JPG -morph 2 -monitor -normalize. (La expresión *.JPG y el número 2 de morph son elegidas por el usuario.)


Funciona con Python 3.4 en Windows.
No funciona con Python 2.7 en Linux.
