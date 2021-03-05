**Principales Diferencias entre Fortran y Python**

**Sismología**

**ENES, Morelia**

**Luis A. Dominguez**

Fortran es un lenguaje de programación de alto nivel que es muy utilizado principalmente en el área de ciencias, y cuyas siglas significan traductor de formulas ( **FOR** mula **TRA** nslator). La siguiente tabla muestra una de las principales diferencias entre **Python** uno de los lenguajes más populares actualmente y **Fortran**.

| **FORTRAN** | **PYTHON** |
| --- | --- |
|
- No requiere indentación (aunque es recomendable)
- Requiere compilarse
- El primer elemento de un arreglo es 1
- No hay diferencia entre mayúsculas y minúsculas
- Tipos de datos:
  - Integer type
  - Real type
  - Complex type
  - Logical type
  - Character type
 |
- No requiere compilarse
- El primer elemento de un arreglo es 0
- No es necesario declarar el tipo de datos o la declaración es implícita.
- Por default las variables son de doble precisión.
- Tipos de datos:
  - Dobles
  - Strings
  - Lista
  - Tuples
  - Dictionarios
  - Etc.

 |

**Nombres del programa:**

**No esta permitido utilizar espacios, acentos, caracteres especial o empezar con un número el nombre del archivo. Todos los archivos con código deberán de tener extensión .f90 aunque existen otras extensiones como .f, .f77, .for por ejemplo.**

**Compilación:**

Existe una extensa gama de opciones de compilación. Sin embargo, en este curso no será necesario utilizarlas. Los programas que elaboremos en este curso se pueden compilar utilizando las opciones por defecto.

Si tu programa consiste en un solo archivo se puede compilar de la siguiente forma:

\&gt;\&gt; gfortran programa.f90 -o programa.exe

La opción -o indica cual es el nombre del archivo de salida que será un ejecutable. En este caso utilice la extensión .exe para el nombre del archivo de salida. Pero puedes asignar la opción que tu prefieras incluso no utilizar ninguna extensión.

Si tu programa consiste en múltiples archivos y/o librerías deberás de especificarlos todos dentro de línea de compilación.

\&gt;\&gt; gfortran programa.f90 librerias.f90 -o programa.exe

**Programas de prueba:**

- **hola\_mundo.f90**

El programa clásico que simplemente muestra el mensaje &quot;Hola mundo&quot; en pantalla.

\&gt;\&gt; gfortran hola\_mundo.f90 -o hola\_mundo.exe

- **mayor\_de\_edad.f90 – Condición IF, entrada y salida de datos**

Este programa muestra como se usa la condición **if,** y como se puede interactuar con el programa.

\&gt;\&gt; gfortran mayor\_de\_edad.f90 -o mayor\_de\_edad.exe

- **ejemplo\_ciclo\_for.f90 – Ciclos FOR**

Este programa cuenta del 1 al 100. Muestra como se utiliza el ciclo for.

\&gt;\&gt; gfortan ejemplo\_ciclo\_for.f90 -o ejemplo\_ciclo\_for.exe

- **area\_main.f90 y rutina\_area.f90. Subrutinas**

Este programa calcula el área de un círculo de radio r. Este código muestra como se pueden escribir subrutinas en un archivo separado, y como llamarlas desde el programa principal.

\&gt;\&gt; gfrotran area\_main.f90 rutina\_area.f90 -o área.exe

- **arreglos.f90 – Arreglos de números (vectores y matrices)**

Este programa muestra como se pueden declarar arreglos de números los cuales vamos a usar en este curso para resolver problemas de sismología.

\&gt;\&gt; gfortran arreglos.f90 -o arreglos.exe

3
