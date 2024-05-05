# Romagnoli-Salmain-TP2
 
Trabajo Práctico 2 Romagnoli y Salmain notas: Uint_8 es el tipo de valor que va de 0 a 255 Cada pixel es una tupla con los tres valores RGB.

PARTE 1 HACER EL FILTRO

Paso 1: Agregarle un margen de 2 pixeles a la matriz. Cada pixel del margen tiene el mismo valor que el valor mas cercano de la matriz, para los que no corresponden a las puntas, copian el de su fila o columna, las esquinas cambia. (chequear cuadro en la consigna) Ejemplo --> si la imagen es de 3x3, post padding queda de 7x7 -dos funciones:

una que agrege valores
una que va adentro de la que agrega valores que decida cual es el valor que le tiene que poner (segun el que está más cerca en la original)
paso 2:hacer la separacion de cuadrantes. Tomo un valor y separo en cuadrantes alrededor(mirar cuadro en la consigna). Aclaracion: los que dicen por ejemplo a/b significa que estan en a y b, no que se divide.\ 
(HECHO, era una sola linea jajaja)

paso3: funciones sobre esos cuadrantes. 1-La varianza es un kilombo pero dijo que nos fijemos como calcularla con numpy.var Hay que calcular varianza muchas veces, hacer una funcion que calcule la varianza y lo haga con parametro n y no solo para 3x3, porque mas adelante se hace para 2x2. 2- comparo las varianzas (son ifs eso es medio boludo) 3- calculo el promedio para cada canal de color en el cuadrante. Dijo que es más fácil / rápido hacerlo al mismo tiempo que la varianza. 4- reemplazo el pixel por ese promedio. Este va en la foto SIN EL PADDING. pero se calcula con el padding entonces el pixel va a quedar así: suponiendo que uso el cuadrante A: (promedio rojos de A, promedio azules de A, promedio verdes de A)

como recorrer la matriz original ya teniendo el padding: for i in range(2, len(img) + 2) for j in range(2, len(img) + 2)

PARTE 2 COMPARAR IMAGENES punto 6 y 7 de la consigna en la parte del mensaje

PARTE 3 LEER EL MENSAJE Hay que hacer el lector de mensaje siguiendo las reglas en la consigna.

