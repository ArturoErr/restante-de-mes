# restante-de-mes

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Descripción

Este script en Python calcula:

Los días restantes para el fin de mes a partir de una fecha dada.

Los días restantes para el fin de año, así como los días transcurridos en el año.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Contenido del archivo

restante-de-mes.py: Código fuente que contiene las funciones:

fin_mes(D, M, A): Calcula e imprime la cantidad de días que faltan para terminar el mes.

fin_año(D, M, A): Calcula e imprime:

Días que faltan para el fin de año.

Días transcurridos en el año.

Validación de la fecha ingresada.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Requisitos

Python 3.x instalado en el sistema.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uso

Clona el repositorio o descarga el archivo restante-de-mes.py.

git clone <URL-del-repositorio>
cd <directorio-del-repositorio>

Ejecuta el script con Python:

python restante-de-mes.py

Ingresa la fecha en formato DD/MM/AAAA cuando se te solicite:

Introduce la fecha dia/mes/año: 05/07/2025

El programa mostrará en consola:

Días que faltan para terminar el mes.

Días que faltan para terminar el año.

Días transcurridos en el año.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Explicación del funcionamiento

fin_mes(D, M, A):

Si el mes es par, asume 31 días; si es impar, 30 días.

Resta el día actual para obtener los días restantes.

fin_año(D, M, A):

Calcula los meses restantes hasta diciembre.

Suma días por mes asumiendo alternancia par/impar (31/30 días).

Añade los días restantes del mes actual.

Imprime los días faltantes y los días transcurridos (365 - días faltantes).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
