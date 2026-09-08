# Análisis de cancelación y propagación de error con el Dólar Observado (SII 2022-2025)

# Descripción del Proyecto
Este repositorio contiene la resolución del Laboratorio Evaluado 1 de Computación Numérica. El objetivo principal es analizar el comportamiento del error numérico (error absoluto, relativo y propagación) y las limitaciones de la representación en punto flotante mediante un caso práctico: la compra y venta de dólares utilizando el promedio mensual publicado por el Servicio de Impuestos Internos (SII) de Chile entre los años 2022 y 2025.

El proyecto demuestra cómo las operaciones matemáticas básicas (especialmente la resta de números de magnitud similar) en sistemas computacionales de precisión limitada pueden inducir a una cancelación catastrófica, eliminando la confiabilidad de las ganancias o variaciones calculadas.

# Estructura del Repositorio

El proyecto sigue la estructura requerida:

problema2-dolar-sii/
│
├── README.md                  #descripción y resultados del proyecto
├── INFORME.md                 #conclusiones finales y análisis detallado de compra/venta
├── requirements.txt           #dependencias del proyecto (numpy, matplotlib)
│
├── data/
│   └── dolar_observado_sii_2022_2025.csv  #dataset oficial del SII
│
├── cargar_datos.py            #módulo de carga del CSV con numpy
├── errores.py                 #funciones vectorizadas para cálculo de cifras significativas y errores
├── anualidad.py               #script de variación y error año a año
├── punto_flotante.py          #pruebas de float32/float64 y cancelación en máquina
├── exportar_csv.py                #genera csv de salida con, para cada par de puntos evaluado y para cada año, el error absoluto, el error relativo y el error propagado. 
│
└── graficos/                  #graficos generados
    ├── 1_serie_mensual.png
    ├── 2_variacion_mensual.png
    ├── 3_error_representacion.png
    ├── 4_rentabilidad.png
    └── 5_deriva_flotante.png