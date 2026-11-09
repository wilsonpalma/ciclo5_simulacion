# Simulación LCG - Práctica 05 Grupo 02

Implementación y análisis del Generador Congruencial Lineal (LCG) en Java siguiendo arquitectura MVC.

## Descripción del problema y propósito

Este proyecto implementa un Generador Congruencial Lineal (LCG) usando la relación recursiva:

```
X(n+1) = (a * X(n) + c) mod m
U(n) = X(n) / m
```

Con los parámetros estándar:
- **a** = 1664525
- **c** = 1013904223
- **m** = 2^32
- **semilla inicial** = 12345

El programa genera 10,000 valores pseudoaleatorios, permite comparar las primeras 20 observaciones, analiza el período del generador y permite cambiar la semilla para observar diferentes secuencias.

## Tecnologías, librerías y versiones utilizadas

- **Java**: 17+ (solo librería estándar)
- **Arquitectura**: MVC (Modelo-Vista-Controlador)
- **Paradigma**: Programación orientada a objetos

No se requieren dependencias externas.

## Instrucciones paso a paso para clonar, compilar y ejecutar

```bash
# 1. Clonar el repositorio (cuando esté disponible)
# git clone <url-del-repositorio>
# cd simulacion_practica05_grupo02_java

# 2. Compilar el código Java
javac -d bin ./controller/LCGController.java ./model/LCG.java ./view/LCGView.java ./Main.java

# 3. Ejecutar la aplicación
java -cp bin Main
```

## Estructura del árbol de carpetas

```
simulacion_practica05_grupo02_java/
├── Main.java               # Punto de entrada
├── README.md              # Este archivo
├── bin/                    # Directorio de clases compiladas
│   ├── controller/
│   │   └── LCGController.class
│   ├── model/
│   │   └── LCG.class
│   └── view/
│       └── LCGView.class
├── controller/
│   └── LCGController.java  # Controlador: Lógica de simulación
├── model/
│   └── LCG.java            # Modelo: Generador LCG
└── view/
    └── LCGView.java        # Vista: Interfaz CLI
```

## Declaración explícita del uso de Inteligencia Artificial

Se utilizó **ChatGPT (GPT-4)** como apoyo para:

- Consultar la estructura de patrones MVC en Java
- Revisar la implementación del algoritmo LCG con los parámetros dados
- Organizar el código en módulos separados (model/view/controller)
- Redactar este README.md siguiendo el formato solicitado

**Prompt principal utilizado:**

> Actúa como tutor de Simulación de Sistemas. Necesito implementar un Generador Congruencial Lineal (LCG) en Java con parámetros a=1664525, c=1013904223, m=2^32, seed=12345. El código debe usar arquitectura MVC con carpetas model/, view/, controller/. Generar 10000 valores, comparar primeros 20, analizar período, cambiar semilla. No usar librerías externas, solo java stdlib.

El estudiante es responsable de revisar, probar y corregir el código según su comprensión y las normas de la asignatura.

## Uso de la aplicación

Al ejecutar `java -cp bin Main` se muestra un menú interactivo:

```
1. Ejecutar simulación completa (10,000 valores)
2. Ver primeras N observaciones
3. Cambiar semilla y generar nueva secuencia
4. Comparar con secuencia de referencia (Python)
5. Exportar resultados a JSON
6. Mostrar resumen de resultados
0. Salir
```

### Opción 4 - Comparación con Python

Permite ingresar los primeros 20 valores generados por la implementación Python (separados por espacios o comas) y compara automáticamente con la secuencia Java para verificar que ambos algoritmos produzcan la misma salida.

## Autores

- KATHERYN MELISSA CONTENTO MALDONADO
- JUAN ALBERTO CALOPINO MARTINEZ
- WILSON PATRICIO PALMA SAMANIEGO
- BRYAN GUSTAVO TROYA VELEZ

**Grupo 2** - Simulación, Ciclo 5 - UNL
Docente: Ing. José Guamán