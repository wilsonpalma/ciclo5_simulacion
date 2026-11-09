# Validacion Estadistica de Numeros Pseudoaleatorios - Python

## Descripcion del Problema y Proposito

Este proyecto implementa la validacion estadistica de numeros pseudoaleatorios generados mediante el metodo congruencial lineal (LCG), aplicando las pruebas de bondad de ajuste Chi-Cuadrado y Kolmogorov-Smirnov para determinar si los valores generados presentan un comportamiento compatible con una distribucion uniforme en el intervalo [0,1].

La actividad corresponde a la Practica Nro. 06 de la asignatura Simulacion (Ciclo 5, Unidad U2) de la Carrera de Ingenieria en Computacion.

## Tecnologias, Librerias y Versiones Utilizadas

- **Python**: 3.10+
- **NumPy**: >=1.24.0 (manejo de arrays numericos)
- **SciPy**: >=1.10.0 (distribuciones estadisticas chi-cuadrado y KS)
- **Matplotlib**: >=3.7.0 (generacion de graficos)
- **Pandas**: >=2.0.0 (manipulacion de datos, opcional)

## Instrucciones Paso a Paso

### 1. Clonar y Preparar el Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar la Simulacion

```bash
python main.py
```

Esto generara:
- Resultados en consola de ambas pruebas estadisticas
- Graficos guardados en la carpeta `plots/`:
  - `chi_square.png`: Barras de frecuencias observadas vs esperadas
  - `kolmogorov_smirnov.png`: CDF empirica vs teorica y diferencias D+/D-
  - `histogram.png`: Histograma de los numeros generados

### 3. Parametros Configurables

En `main.py` se pueden modificar:
- `seed`: Semilla inicial (default: 12345)
- `multiplier`: Multiplicador LCG (default: 1664525)
- `increment`: Incremento LCG (default: 1013904223)
- `modulus`: Modulo LCG (default: 2**32)
- `count`: Cantidad de numeros a generar (default: 10000)

## Estructura del Arbol de Carpetas

```
python/
├── main.py                      # Punto de entrada principal
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── model/                       # Capa de modelo (logica de negocio)
│   ├── __init__.py
│   ├── lcg.py                   # Generador Congruencial Lineal
│   ├── chi_square.py            # Prueba Chi-Cuadrado
│   └── kolmogorov_smirnov.py    # Prueba Kolmogorov-Smirnov
├── view/                        # Capa de vista (presentacion)
│   ├── __init__.py
│   ├── console_view.py          # Salida por consola
│   └── plot_view.py             # Generacion de graficos
└── controller/                  # Capa de control (orquestacion)
    ├── __init__.py
    └── simulation_controller.py # Controlador principal
```

## Declaracion Explicita del Uso de Inteligencia Artificial

### Prompt Utilizado para el Desarrollo del Codigo

> Actua como desarrollador de software educativo. Necesito implementar en Python una simulacion para validar numeros pseudoaleatorios usando el metodo congruencial lineal (LCG) y aplicar las pruebas estadisticas Chi-Cuadrado y Kolmogorov-Smirnov. La arquitectura debe seguir el patron MVC con carpetas separadas model/, view/, controller/. El codigo debe ser claro y entendible para un estudiante de 5to ciclo de computacion. Incluye generacion de graficos con matplotlib. No escribas el informe final, solo el codigo funcional.

### Herramientas de IA Utilizadas

- **Herramienta**: GitHub Copilot / ChatGPT (modelo GPT-4)
- **Alcance**: Consultas sobre estructura MVC, implementacion de pruebas estadisticas, generacion de graficos matplotlib, y organizacion del codigo
- **Responsabilidad**: El estudiante reviso, entendio y adapto todo el codigo generado segun los requisitos de la practica y las normas de la asignatura.

---

## Referencias Bibliograficas (Formato IEEE)

[1] J. Banks, J. S. Carson, B. L. Nelson, and D. M. Nicol, *Discrete-Event System Simulation*, 5th ed. Pearson, 2010.

[2] A. M. Law, *Simulation Modeling and Analysis*, 5th ed. McGraw-Hill, 2015.

[3] P. L'Ecuyer, "Tables of linear congruential generators of different sizes and good lattice structure," *Mathematics of Computation*, vol. 68, no. 225, pp. 249-260, 1999.

[4] W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, *Numerical Recipes: The Art of Scientific Computing*, 3rd ed. Cambridge University Press, 2007.

[5] M. A. Stephens, "EDF statistics for goodness of fit and some comparisons," *Journal of the American Statistical Association*, vol. 69, no. 347, pp. 730-737, 1974.