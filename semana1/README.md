# APE 01 - Simulación: modelo de lluvia en Python

## Estructura

```text
simulacion_ape01_python/
├── app/
│   ├── main.py
│   └── model_factory.py
├── domain/
│   ├── entities.py
│   ├── rain_model.py
│   └── temperature.py
├── infrastructure/
│   └── data_repository.py
├── services/
│   └── simulation_service.py
├── visualization/
│   └── plotter.py
├── tests/
│   └── test_rain_model.py
├── .gitignore
└── requirements.txt
```

## Ejecución

```bash
python3 -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python -m app.main
```

Para ejecutar las pruebas:

```bash
python -m pytest
```

## Prompt de IA utilizado

> Genera la implementación en Python de la APE 01 de Simulación para construir y simular un modelo matemático de posibilidad de lluvia. Usa NumPy y Matplotlib. No uses un único script: organiza el proyecto en una pequeña arquitectura y aplica patrones de diseño. Implementa el modelo I = 0.5H + 0.3N + 0.2Tf, normaliza humedad y nubosidad, usa la tabla de factores de temperatura y las reglas de clasificación del índice. Incluye los datos horarios de la guía, salida tabular y gráficas. Deja configurable el modelo ajustado porque la guía no especifica los nuevos coeficientes. Incluye requirements.txt y .gitignore para no subir el entorno virtual.
