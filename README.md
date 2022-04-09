# PruebasDE

1. Se entregan 3 dataset en la ruta `/assets/*.csv` compuesto de ventas por tienda, tiendas y otras características, la idea es cargar estos datasets para su posterior análisis. Posterior a su cargue debe ser procesado en Python para responder las siguientes preguntas:

- Cual es la tienda con el mayor valor en ventas totales?
- Entre las 3 tiendas más grandes cuál es la que más ventas totales registra?
- Cual es la tienda con menor ventas ?
- Cual es la tienda que mas vendió en el 2 semestre del año 2012?

2. Dentro de `/assets/` se encuentra una rchivo llamado `anyclass.py`. Se debe responder lo siguiente:

- Qué hace este código?
- Si es posible, refactorizar

Nota:

Esperamos que el ejercicio sea termindo en 24 horas. Debes hacer fork de la rama y subir tus cambios. Toda la documentacion, explicaciones, print screen, debe ir en el Readme.md.
Por favor enviar correo cuando termines a pda_gobierno@avaldigitallabs.com


Buen día,

Para la resolución del problema se cargaron los archivos *.csv y con ayuda de pandas se convirtieron en DataFrames para su manipulación como tablas:
Caso 1. Se hace limpieza de los datos para poder convertirlos a float y así poder ejecutar funciones matemáticas, se trabaja con agrupación de la suma de las ventas por tienda, se ordena de forma descendente y se toma el primer resultado que seria el de la tienda con mayores ventas.
Caso2. Se toman los datos de tienda y tamaño para ordenarlos de forma descendente y se toman los tres primeros registros, la idea era ejecutar un join con el resultado ordenado del total de ventas por tienda, me salió error al ejecutar el join planeado por desconocimiento de los comandos para el cruce, trate de usar un merge per el error me mostraba que desconocía el tipo de dato, como si no los reconociera como Dataframe.
Caso 3. Este caso es muy similar al caso 1 pero en este caso el ordenamiento se hace descendente.
Caso 4. Para el caso 4 se trabajo el campo Date como un String y aplicarle un substring de forma que solo me trajera el año y el mes se realizo una agrupación de la suma total de las ventas por tienda y mes, la idea era hacer un filtro por datos donde date estuviera entre ‘2012-06’ y ‘2012-2012’, el cual no me funciono. Después se realiza un ordenamiento descendente y se toma el primer resultado para la respuesta.




Evidencia Run:
![image](https://user-images.githubusercontent.com/103300434/162577948-614b681e-00d4-4448-b8de-06ea344b727f.png)

De antemano agradezco la oportunidad, esta ha sido una experiencia muy enriquecedora.

Saludos!

Att: Diana M. Camargo
