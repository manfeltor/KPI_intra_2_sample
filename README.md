## Project Overview

### Project Name
*KPI intra_2*

### Description
*KPI intra_2 is a custom KPI reports tool under development designed to facilitate the operations KPI analysis both for inner and external client upper management. Includes features like central measurement statistics for delivery, wharehousing, relevant events details (seassonality) and predicitions.*

### Key Features

- **User Authentication:**
  - Secure login and registration system.
  - General overview of KPIs for inner client management.
  - Specific metrics and analysis for external companies.
     
- **Deliveries KPI Dashboard:**
  - View key metrics to understand the delivery performance by region.
  - Analize the deliveries cumulative behavior to adjust delivery promise for your costumers for each region and anticipate to special events.

- **Warehouse Analysis (under development):**
  - See the wharehouse ocupation and daily rates on real time.
  - Understand the wharehousing behavior by periods with the main metrics dashboards.
  - Predict your storage costs with the predictions sections, specially for season events
 
- **Pattern recognition Analysis (under development):**
  - See the insights returned by the multidisciplinary analysis to make more precisse descitions.
  - Nurture the perspectives of your decisions with projections based on previous data.
 
- **Relevant dates (under development):**
  - Understand the changes on statistical behavior of the normal operation on special events that trigger a rise in demand and affect main metrics.
  - Get ready and prepare your customer service team and campaign with the custom suggestions for seassonality.
 
  For more information regarding the development of features, please refer to the status section.

### Tech Stack

- **Python**: The primary programming language used for backend development.
- **Django**: The web framework used for building the backend and handling the MVC structure.
- **SQLite**: The database system used for development and testing (will be replaced with PostgreSQL MSQLS in production, still under evaluation).
- **HTML/CSS**: For building the frontend structure and styling.
  - **Bootstrap styles**: A framework used for styling and responsive design.
- **JavaScript**: Used for adding interactivity to the frontend.
  - **Vanilla JS**: For basic DOM manipulation and event handling.
- **Git**: Version control system used to manage code and collaboration.
- **GitHub**: Hosting service for version control using Git, where the project's repository is stored.
- **Django REST Framework**: For building APIs.
- **Celery**: Task queue used for handling asynchronous tasks (under development).
- **Docker**: Containerization tool used to create and manage containers (to be containerized once ready for deployment).
- **Gunicorn**: WSGI HTTP server for running Django applications in production (to be implemented once containerization ready).

### Development Tools

- **VS Code**: Preferred code editor for development.
- **SQLite Browser**: For managing the SQLite database during development.

### Deployment

- **on premise**: To be deployed on local VM server partition.

### Status
- **Current Status:** *KPI intra_2 is currently under development, waiting for upper management deffinitions for further development.*
- **Planned Features:**
  - *Warehouse Analysis:* *This functionality has already the origin DB shcema and self DB configuration plan for FACT table, and is waiting a local server migration for data population testing between VM partitions.*
  - *Relevant dates:* *This functionality is still under planning, mainly on the client setting of the relevant dates and events for its operation.*
  - *Pattern recognition Analysis:* *The planning of the logic roadmap for this functionality depends mainly on the completion of the other main functionalities.*
 
### Roadmap

### In Progress
- Reconfiguration of main FACT table population API protocol due changes on the server side possibilities.

### Planned Features
- **Q3 2024:** Reconfigured FACT table population and linking and polishing of deliveries dashboard to meet upper management requeriments.
- **Q4 2024:** Configured data generation for WH metrics.
- **Q1 2025:** WH metrics dashboard and data configuration for pattern recognition.
- **Q2/3 2025:** Full patter recognition board with multidisciplinary analysis.

### Contributors
- **Lead Developer:** *Felipe Torres*
- For colaboration please contact me at manfeltor@live.com

### Project Links
- **Repository:** [KPI intra_2_sample](https://github.com/manfeltor/KPI_intra_2_sample)
- **Live Demo:** comming soon.*

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.8+**
- **Django 4.0+**
- **SQLite** (or another database if you're using one)
- **Git**

### Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/manfeltor/KPI_intra_2_sample
cd KPI_intra_2_sample
```

### Setup virtual environment (recommended)

```bash
python -m venv env
source env/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Apply migrations

To setup your database

```bash
python manage.py migrate
```
### Sample Database for Execution

Since this is a demonstration repo and the full database is too large for GitHub, please download the sample database:

- **[Download Sample Database](https://intralogargentinasa-my.sharepoint.com/:u:/g/personal/ftorres_intralog_com_ar/EYwLC4NJOvZOrjYge3F8VWEBq1YpI_hUglQAjPHWD2u-ow?e=Fbux0M)** (password: sampledb1234)
- the download password is: sampledb1234
- copy the database to root directory of the project

**Note:** The sample database contains a subset of anonymized data that simulates the real environment. The original database and API credentials are proprietary. If you require a demonstration or further access, please contact me at manfeltor@live.com.

### Run development server

Start the Django development server:

```bash
python manage.py runserver
```

### License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for more details.
