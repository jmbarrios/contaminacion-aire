# 🚀 Tu Proyecto de Datos

## 📁 Estructura del Proyecto
```
your_project/
├── ⚙️ .devcontainer/        # 🐳 configuración de contenedor
├── 📊 00-data/              # datos crudos, intermedios y procesados
│   ├── interim/             # 🔄 datos transformados
│   ├── processed/           # ✅ datos finales listos para análisis
│   └── raw/                 # 🗄️ datos originales (inmutables)
├── 📜 01-scripts/           # 🏃 scripts ejecutables
├── 📚 02-docs/              # 📖 documentación
├── 📄 03-reports/           # 📊 informes y figuras
│   ├── data_quality/        # ✅ informes de calidad de datos
│   └── figures/             # 🖼️ gráficos generados
├── 🧪 98-tests/             # 🧪 pruebas unitarias
├── 📓 99-notebooks/         # 📝 notebooks de Jupyter para exploración
├── 📦 pyproject.toml        # 📋 dependencias y configuración
└── 🧠 src/your_project/     # 🎯 paquete principal de Python
```

## Características del Dev Container
- Entorno reproducible con Python 3.11
- Gestor de paquetes `uv` para instalaciones rápidas
- Herramientas de calidad: `ruff` (linting/formateo)
- Integración con Jupyter notebooks

## 🛠️ Configuración Manual (usando uv)

### Prerrequisitos
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Instalación
```bash
# Crear entorno virtual
uv venv
# Activar entorno virtual
source .venv/bin/activate      # 🐧 Linux/Mac
# .venv\Scripts\activate.ps1   # 🪟 Windows

# Instalar el proyecto y dependencias
uv pip install -e .[dev]

```

## 🎯 Uso del Proyecto

### Organización del Código
Una recomendación de como organizar el código de tu proyectopodría ser 
`src/your_project/`:

| Módulo | Descripción |
|--------|-------------|
| `utils/` | Funciones utilitarias reutilizables |
| `data/` | Carga y preprocesamiento de datos |
| `features/` | Ingeniería de características |
| `models/` | Entrenamiento y evaluación de modelos |
| `visualization/` | Funciones de visualización |

### Scripts

```bash
# 📊 Generar informe de calidad de datos
python scripts/generate_data_quality_report.py --input 00-data/raw/mydata.csv

# 🔄 Preprocesamiento de datos
python scripts/preprocess_data.py --input 00-data/raw/mydata.csv --output 00-data/processed/

# 🎓 Entrenamiento de modelos
python scripts/train_model.py --config configs/model_config.yaml
```

### Jupyter Notebooks
```bash
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser
```
💡 *Los notebooks deben guardarse en la carpeta `99-notebooks/`*

## ✨ Calidad de Código

### Ruff (Linting y Formateo)
```bash
# Ejecutar linting
ruff check .

# Corregir automáticamente problemas
ruff check --fix .

# Formatear código
ruff format .
```

### Ty (Type Checking)
```bash
# Verificar errores de tipos
ty src/
```

## 🧪 Pruebas

### ▶️ Ejecutar pruebas
```bash
# Ejecutar todas las pruebas
pytest tests/

# Con cobertura
pytest --cov=src tests/
```

### Posible estructura de Pruebas
- `tests/test_data.py` - pruebas para carga y procesamiento de datos
- `tests/test_features.py` - pruebas para ingeniería de características  
- `tests/test_models.py` - pruebas para modelos
- `tests/test_utils.py` - pruebas para utilidades

## 📊 Informes de Calidad de Datos

Los informes se generan en `reports/data_quality/` y proporcionan:

| Característica | Descripción |
|----------------|-------------|
| Estadísticas | Descriptivas completas |
| Distribuciones | Visualización de variables |
| Valores faltantes | Análisis de missing values |
| Correlaciones | Matriz de correlaciones |
| Valores atípicos | Detección de outliers |
| Recomendaciones | Sugerencias de limpieza |

## 👥 Trabajo en Equipo

### 🤝 Colaboración
1. Crear rama: `git checkout -b feature/nombre-feature`
2. Commits descriptivos
3. Ejecutar pruebas localmente
4. Crear Pull Request para revisión

## 📦 Dependencias Principales

### Producción
| Paquete | Versión | Uso |
|---------|---------|-------|-----|
| pandas | ≥2.0 | Manipulación de datos |
| numpy | ≥1.24 | Operaciones numéricas |
| scikit-learn | ≥1.3 | Machine learning |
| matplotlib | ≥3.7 | Visualización |
| seaborn | ≥0.12 | Visualización estadística |
| ydata-profiling | ≥4.0 | Informes de calidad |

### Desarrollo
| Paquete | Versión | Uso |
|---------|---------|-----|
| pytest | ≥7.0 | Pruebas unitarias |
| ruff | ≥0.1 | Linting y formateo |
| mypy | ≥1.0 | Type checking |
| pre-commit | ≥3.0 | Hooks de git |

## 🎨 Personalización

### Cambiar el Nombre del Proyecto
1. Renombrar `src/your_project/` a `src/tu_nuevo_nombre/`
2. Actualizar `pyproject.toml`:
   ```toml
   [project]
   name = "tu_nuevo_nombre"
   ```
3. Actualizar importaciones en todos los archivos

### Agregar Nuevas Dependencias
```bash
# Agregar dependencia de producción
uv add nombre-paquete

# Agregar dependencia de desarrollo
uv add --dev nombre-paquete

# Actualizar archivo de dependencias e instalar
uv sync
```
