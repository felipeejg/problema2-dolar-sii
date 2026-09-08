# INFORME: Laboratorio Evaluado 1 - Análisis de Error y Punto Flotante
# Nombre: Felipe Jara Guzmán

# Descripción: 
Este repositorio contiene el análisis numérico de la variación del dólar observado (promedio mensual del SII, 2022-2025) aplicando conceptos de error absoluto, error relativo, propagación de error y el efecto de la cancelación catastrófica en operaciones de punto flotante.

# Sección 6: Preguntas del error a contestar

## A1. Error de representación mes a mes
Al simular un almacenamiento de baja precisión (2 cifras significativas), el mes que quedó con el mayor error relativo al redondear fue Abril de 2022. 
* Valor real: 815.12 CLP
* Valor aproximado (2 cs): 820 CLP
* Error absoluto: |815.12 - 820| = 4.88 CLP
* Error relativo: (4.88 / 815.12) * 100 = aprox. 0.6%
Este mes encabeza el error porque su magnitud original dejó una fracción grande que la máquina "recortó" para ajustarse a las dos cifras.

# A2. Evaluación entre dos puntos (una compra-venta)
Simulando una inversión inicial de M = 1.000.000 CLP:
* Compra: Febrero 2023 (Real: 798.26 | Aprox 2 cs: 800)
* Venta: Enero 2025 (Real: 1000.76 | Aprox 2 cs: 1000)
* Operaciones: 
  * USD comprados: 1.000.000 / 800 = 1250 USD.
  * Pesos finales: 1250 * 1000 = 1.250.000 CLP.
  * Ganancia = 1.250.000 - 1.000.000 = 250.000 CLP.
* Propagación del error: En la multiplicación y la división, los errores relativos se suman. El error relativo total de las tasas es de aproximadamente 1.47%. Al aplicar este porcentaje a la ganancia, el error absoluto arrastrado es de 3675 CLP. 
* Resultado: La ganancia final es de 250.000 +/- 3675 CLP (Error porcentual: 1.47%).

# A3. Cancelación (dos meses casi iguales)
Se calculó la variación entre Diciembre de 2022 y Diciembre de 2023 utilizando 3 cifras significativas:
* Diciembre 2022: Real 875.66 -> Aprox: 876 (Ea: 0.34)
* Diciembre 2023: Real 874.67 -> Aprox: 875 (Ea: 0.33)
* Variación aproximada: 875 - 876 = -1.0 CLP.
* Error propagado: En la resta, los errores absolutos se suman. Ea propagado = 0.34 + 0.33 = 0.67 CLP.
* Resultado: Variación = -1.0 +/- 0.67 CLP (Error relativo: ~67%).
* Conclusión: Con un margen de error tan gigante frente al resultado, no se puede afirmar con seguridad si el dólar subió o bajó. La incertidumbre casi iguala a la variación, produciéndose una cancelación catastrófica.

# A4. Anualidad (variación enero - diciembre)
Propagando los errores absolutos al restar Diciembre y Enero de cada año con 3 cifras significativas, el orden de los años del más confiable al menos confiable es:
1. Año 2024: Variación aprox 74.00 +/- 0.31 CLP | Error Porcentual: 0.42%
2. Año 2022: Variación aprox 54.00 +/- 0.39 CLP | Error Porcentual: 0.73%
3. Año 2025: Variación aprox -84.00 +/- 0.92 CLP | Error Porcentual: 1.09%
4. Año 2023: Variación aprox 49.00 +/- 0.67 CLP | Error Porcentual: 1.39%
* ¿Qué tienen en común los años poco confiables? Los años con mayor error relativo (como 2023 y 2025) comparten la característica de tener una variación neta más pequeña en comparación con sus magnitudes absolutas. Cuando la diferencia real es pequeña, el error acumulado por los redondeos toma un peso porcentual enorme, restándole validez matemática al cálculo.

# A5. Mejor compra y mejor venta
* Mes más barato (Mínimo): Febrero de 2023 (798.26 CLP).
* Mes más caro (Máximo): Enero de 2025 (1000.76 CLP).
* Rentabilidad: Comprar en el mínimo y vender en el máximo entrega una rentabilidad bruta de casi 25%.
* ¿Sobrevive al error? Sí. La diferencia entre ambos meses es superior a 200 pesos. Nuestro error propagado ronda los ~3.6 pesos. La diferencia es abismalmente mayor que la incertidumbre, por lo que la conclusión no queda en duda.


# Sección 7: Preguntas del punto flotante

# B1. Cifras significativas = mantisa corta
Restringir un precio a 2 cifras significativas equivale lógicamente a guardarlo en un sistema con una mantisa de muy pocos bits. La mantisa es la parte de la memoria que guarda los dígitos reales del número. Si hay pocos bits, las fracciones menos significativas se truncan o redondean (pérdida de información).
* Ejemplo con 1000.76: Si forzamos la máquina a usar solo 3 cifras significativas, el número se convierte en 1.00 x 10^3 = 1000. El error de representación es directo: 1000.76 - 1000 = 0.76 pesos que la máquina "olvidó" por falta de espacio en la mantisa.

# B2. La ida y vuelta que no vuelve
Al ejecutar el ciclo de tomar pesos, comprar dólares, y volver a venderlos por pesos utilizando el mismo tipo de cambio forzado a precisión simple (float32), no se recupera el millón exacto. 
Esto ocurre porque la división y multiplicación sucesivas generan fracciones que exceden la capacidad de la mantisa de 32 bits (que solo almacena ~7 cifras decimales útiles). Los bits sobrantes se descartan en cada operación, acumulando un "residuo" que deriva en pérdidas o ganancias microscópicas fantasmas.

# B4. Cancelación en la máquina
Al ejecutar la operación 874.67 - 875.66:
* En float32 el resultado arrojó -0.98999023.
* En float64 el resultado arrojó -0.9899999999998954.
* Análisis: El resultado real exacto es -0.99. Al usar float32, solo las primeras 3 cifras significativas (-0.989) retienen algo de validez. El resto (99023) es ruido o "basura" numérica inventada por la máquina. Esto conecta con lo demostrado en A3: al restar números flotantes parecidos, las cifras significativas principales se aniquilan entre sí y el resultado queda dominado por los errores de representación arrastrados en los últimos bits.

# Sección 9: Documento de entrega y conclusión final

Basado estrictamente en los cálculos de propagación de error y la certidumbre matemática de los datos, se concluye lo siguiente para un plan de inversión:

1. ¿Cuándo conviene comprar?
El escenario óptimo se presentó en Febrero de 2023, marcando el mínimo del período analizado (798.26 CLP). Este mínimo es completamente seguro frente a meses vecinos (como Junio 2023 con 799.87 CLP), ya que la diferencia real supera el umbral del error de representación de máquina.

2. ¿Cuándo conviene vender?
El momento óptimo de venta es Enero de 2025 (1000.76 CLP). La confianza es absoluta, pues la brecha de casi 18 pesos respecto a su predecesor (Diciembre 2024) es órdenes de magnitud superior a los errores de cálculo propagados.

3. La mejor jugada completa
Comprar en Febrero de 2023 y vender en Enero de 2025. La rentabilidad de esta jugada arroja un 25% de ganancia. Al propagar los errores asumiendo baja precisión computacional, se obtiene una ganancia de 250.000 +/- 3675 CLP. Como el margen de error es mínimo (~1.47%), la recomendación es numéricamente sólida.

4. Los tramos donde NO se puede recomendar
Es numéricamente irresponsable hacer afirmaciones sobre el tramo Diciembre de 2022 a Diciembre de 2023. En este periodo de doce meses, la variación absoluta del valor del dólar fue de tan solo ~1 peso. Bajo nuestro análisis, el margen de error absoluto propagado fue de 0.67 CLP, lo que implica una incertidumbre del 67%. Con este nivel de ruido, cualquier recomendación sobre tendencia al alza o a la baja carece de rigor.

5. La lección de método
Aprendí que al restar dos números grandes y de magnitud casi idéntica, las cifras verdaderamente significativas se cancelan mutuamente, evaporando la precisión y dejando el resultado a decisión del error de redondeo acumulado.
