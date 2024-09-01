
## Resumen del Proyecto

### Nombre del Proyecto
*KPI intra_2*

### Descripción
*KPI intra_2 es una herramienta de informes KPI personalizada en desarrollo, diseñada para facilitar el análisis de KPI de operaciones tanto para la alta dirección interna como para la de clientes externos. Incluye características como estadísticas de medición central para la entrega, almacenamiento, detalles de eventos relevantes (estacionalidad) y predicciones.*

### Características Principales

- **Autenticación de Usuarios:**
  - Sistema de inicio de sesión y registro seguro.
  - Vista general de los KPIs para la gestión interna del cliente.
  - Métricas y análisis específicos para empresas externas.

- **Panel de Control de KPI de Entregas:**
  - Ver métricas clave para comprender el rendimiento de las entregas por región.
  - Analizar el comportamiento acumulativo de las entregas para ajustar la promesa de entrega a sus clientes en cada región y anticiparse a eventos especiales.

- **Análisis de Almacenamiento (en desarrollo):**
  - Ver la ocupación del almacén y las tasas diarias en tiempo real.
  - Comprender el comportamiento del almacenamiento por períodos con los paneles de métricas principales.
  - Predecir sus costos de almacenamiento con la sección de predicciones, especialmente para eventos estacionales.

- **Análisis de Reconocimiento de Patrones (en desarrollo):**
  - Ver las ideas proporcionadas por el análisis multidisciplinario para tomar decisiones más precisas.
  - Nutrir las perspectivas de sus decisiones con proyecciones basadas en datos anteriores.

- **Fechas Relevantes (en desarrollo):**
  - Comprender los cambios en el comportamiento estadístico de la operación normal en eventos especiales que desencadenan un aumento en la demanda y afectan las métricas principales.
  - Prepararse y preparar su equipo de servicio al cliente y campañas con las sugerencias personalizadas para la estacionalidad.

Para obtener más información sobre el desarrollo de características, consulte la sección de estado.

### Stack Tecnológico

- **Python**: El lenguaje de programación principal utilizado para el desarrollo del backend.
- **Django**: El framework web utilizado para construir el backend y manejar la estructura MVC.
- **SQLite**: El sistema de base de datos utilizado para desarrollo y pruebas (se reemplazará por PostgreSQL o MSSQL en producción, aún en evaluación).
- **HTML/CSS**: Para construir la estructura del frontend y el estilo.
  - **Estilos Bootstrap**: Un framework utilizado para el estilo y diseño responsivo.
- **JavaScript**: Utilizado para agregar interactividad al frontend.
  - **Vanilla JS**: Para la manipulación básica del DOM y manejo de eventos.
- **Git**: Sistema de control de versiones utilizado para gestionar el código y la colaboración.
- **GitHub**: Servicio de hosting para control de versiones usando Git, donde se almacena el repositorio del proyecto.
- **Django REST Framework**: Para construir APIs.
- **Celery**: Cola de tareas utilizada para manejar tareas asincrónicas (en desarrollo).
- **Docker**: Herramienta de contenedorización utilizada para crear y gestionar contenedores (se contenedizará una vez esté listo para despliegue).
- **Gunicorn**: Servidor HTTP WSGI para ejecutar aplicaciones Django en producción (se implementará una vez que esté lista la contenedorización).

### Herramientas de Desarrollo

- **VS Code**: Editor de código preferido para el desarrollo.
- **SQLite Browser**: Para gestionar la base de datos SQLite durante el desarrollo.

### Despliegue

- **on premise**: Se desplegará en una partición del servidor virtual local.

### Estado
- **Estado Actual:** *KPI intra_2 está actualmente en desarrollo, esperando definiciones de la alta dirección para el desarrollo adicional.*
- **Características Planeadas:**
  - *Análisis de Almacenamiento:* *Esta funcionalidad ya tiene el esquema de origen de la base de datos y el plan de configuración de la base de datos para la tabla FACT, y está esperando una migración del servidor local para pruebas de población de datos entre particiones del servidor virtual.*
  - *Fechas Relevantes:* *Esta funcionalidad está todavía en planificación, principalmente en la configuración por parte del cliente de las fechas y eventos relevantes para su operación.*
  - *Análisis de Reconocimiento de Patrones:* *La planificación de la hoja de ruta lógica para esta funcionalidad depende principalmente de la finalización de las otras funcionalidades principales.*

### Hoja de Ruta

### En Progreso
- Reconfiguración del protocolo API de población de la tabla FACT principal debido a cambios en las posibilidades del lado del servidor.

### Características Planeadas
- **Q3 2024:** Población reconfigurada de la tabla FACT y enlace y pulido del panel de control de entregas para cumplir con los requisitos de la alta dirección.
- **Q4 2024:** Generación de datos configurados para métricas de almacenamiento.
- **Q1 2025:** Panel de métricas de almacenamiento y configuración de datos para el reconocimiento de patrones.
- **Q2/3 2025:** Tablero completo de reconocimiento de patrones con análisis multidisciplinario.

### Contribuyentes
- **Desarrollador Principal:** *Felipe Torres*
- Para colaboración, por favor contáctame en manfeltor@live.com

### Enlaces del Proyecto
- **Repositorio:** [KPI intra_2_sample](https://github.com/manfeltor/KPI_intra_2_sample)
- **Demo en Vivo:** [Demo en Vivo](#) *Enlace a una demostración en vivo si está disponible.*

## Instalación

Siga estos pasos para configurar el proyecto en su máquina local.

### Requisitos Previos

Asegúrese de tener lo siguiente instalado en su máquina:

- **Python 3.8+**
- **Django 4.0+**
- **SQLite** (u otra base de datos si usa una diferente)
- **Git**

### Clonar el Repositorio

Primero, clone el repositorio en su máquina local usando Git:

```bash
git clone https://github.com/manfeltor/KPI_intra_2_sample
cd KPI_intra_2_sample
```

### Configurar entorno virtual (recomendado)

```bash
python -m venv env
source env/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Aplicar migraciones

Para configurar su base de datos

```bash
python manage.py migrate
```
### Base de Datos de Ejemplo para Ejecución

Dado que este es un repositorio de demostración y la base de datos completa es demasiado grande para GitHub, descargue la base de datos de ejemplo:

- **[Descargar Base de Datos de Ejemplo](https://intralogargentinasa-my.sharepoint.com/:u:/g/personal/ftorres_intralog_com_ar/EYwLC4NJOvZOrjYge3F8VWEBq1YpI_hUglQAjPHWD2u-ow?e=Fbux0M)** (contraseña: sampledb1234)
- La contraseña de descarga es: sampledb1234
- Copie la base de datos en el directorio raíz del proyecto.

**Nota:** La base de datos de ejemplo contiene un subconjunto de datos anonimizados que simulan el entorno real. La base de datos original y las credenciales de API son propiedad de la empresa. Si necesita una demostración o acceso adicional, por favor contácteme en manfeltor@live.com.

### Ejecutar el servidor de desarrollo

Inicie el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

### Licencia
Este proyecto está licenciado bajo la Licencia Pública General de GNU v3.0. Consulte el archivo [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) para más detalles.
