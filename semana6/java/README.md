# Validacion Estadistica de Numeros Pseudoaleatorios - Java

## Descripcion del Problema y Proposito

Este proyecto implementa la validacion estadistica de numeros pseudoaleatorios generados mediante el metodo congruencial lineal (LCG), aplicando las pruebas de bondad de ajuste Chi-Cuadrado y Kolmogorov-Smirnov para determinar si los valores generados presentan un comportamiento compatible con una distribucion uniforme en el intervalo [0,1].

La actividad corresponde a la Practica Nro. 06 de la asignatura Simulacion (Ciclo 5, Unidad U2) de la Carrera de Ingenieria en Computacion.

## Tecnologias, Librerias y Versiones Utilizadas

- **Java**: JDK 17+ (compatible con JDK 8+)
- **IDE**: IntelliJ IDEA, Eclipse, NetBeans o VS Code
- **Librerias**: Solo libreria estandar de Java (sin dependencias externas)

## Instrucciones Paso a Paso

### 1. Compilar y Ejecutar

#### Desde linea de comandos:
```bash
# Navegar a la carpeta java
cd java

# Compilar
javac -d out "src/Main.java" "src/model/*.java" "src/view/*.java" "src/controller/*.java"

# Ejecutar
java -cp out Main
```

#### Desde IDE (IntelliJ IDEA / Eclipse / NetBeans / VS Code):
1. Abrir la carpeta `java` como proyecto
2. Configurar JDK 17+ si no se detecta automaticamente
3. Ejecutar la clase `Main` (clic derecho -> Run)

### 2. Parametros Configurables

En `src/Main.java` se pueden modificar:
- `seed`: Semilla inicial (default: 12345)
- `multiplier`: Multiplicador LCG (default: 1664525)
- `increment`: Incremento LCG (default: 1013904223)
- `modulus`: Modulo LCG (default: 2^32)
- Tamano de muestra en `runSimulation()` y `runComparison()`

## Estructura del Arbol de Carpetas

```
java/
├── src/
│   ├── Main.java                           # Punto de entrada principal
│   ├── model/                              # Capa de modelo (logica de negocio)
│   │   ├── LCG.java                        # Generador Congruencial Lineal
│   │   ├── ChiSquareTest.java              # Prueba Chi-Cuadrado
│   │   └── KolmogorovSmirnovTest.java      # Prueba Kolmogorov-Smirnov
│   ├── view/                               # Capa de vista (presentacion)
│   │   ├── ConsoleView.java                # Salida por consola
│   │   └── PlotView.java                   # Graficos textuales
│   └── controller/                         # Capa de control (orquestacion)
│       └── SimulationController.java       # Controlador principal
└── README.md                               # Este archivo
```

## Declaracion Explicita del Uso de Inteligencia Artificial

### Prompt Utilizado para el Desarrollo del Codigo

> Actua como desarrollador de software educativo. Necesito implementar en Java una simulacion para validar numeros pseudoaleatorios usando el metodo congruencial lineal (LCG) y aplicar las pruebas estadisticas Chi-Cuadrado y Kolmogorov-Smirnov. La arquitectura debe seguir el patron MVC con carpetas separadas model/, view/, controller/. El codigo debe ser claro y entendible para un estudiante de 5to ciclo de computacion. Usa solo la libreria estandar de Java, sin dependencias externas. Incluye representacion textual de graficos. No escribas el informe final, solo el codigo funcional.

### Herramientas de IA Utilizadas

- **Herramienta**: GitHub Copilot / ChatGPT (modelo GPT-4)
- **Alcance**: Consultas sobre estructura MVC en Java, implementacion de pruebas estadisticas sin librerias externas, representacion textual de graficos, y organizacion del codigo
- **Responsabilidad**: El estudiante reviso, entendio y adapto todo el codigo generado segun los requisitos de la practica y las normas de la asignatura.

---

## Referencias Bibliograficas (Formato IEEE)

[1] J. Banks, J. S. Carson, B. L. Nelson, and D. M. Nicol, *Discrete-Event System Simulation*, 5th ed. Pearson, 2010.

[2] A. M. Law, *Simulation Modeling and Analysis*, 5th ed. McGraw-Hill, 2015.

[3] P. L'Ecuyer, "Tables of linear congruential generators of different sizes and good lattice structure," *Mathematics of Computation*, vol. 68, no. 225, pp. 249-260, 1999.

[4] W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, *Numerical Recipes: The Art of Scientific Computing*, 3rd ed. Cambridge University Press, 2007.

[5] M. A. Stephens, "EDF statistics for goodness of fit and some comparisons," *Journal of the American Statistical Association*, vol. 69, no. 347, pp. 730-737, 1974.