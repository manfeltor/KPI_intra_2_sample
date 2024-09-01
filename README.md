## Project Overview

### Project Name
*INTRALOG leads manager*

### Description
*This Leads Manager is a custom tailored CRM tool under development designed to streamline the management of leads for a sales team. It includes features like lead assignment, status tracking, management metrics and campaign analysis, all integrated into a user-friendly web interface.*

### Key Features

- **Lead Management:**
  - Pull from WP custom plugins, view, and manage leads with detailed information making a first classification.
  - Assign leads to specific users and track progress.
 
- **Custom User Generation:**
  - Create and edit users with specific roles and relevant fields.
  - Manage users (for management), and edit your own for better personalization and security.
  
- **User Role Management:**
  - Define user roles such as Admin, Manager, and Employee.
  - Manage user permissions based on roles.

- **Custom CRM Forms:**
  - Dynamic form generation for different lead types.
  - Store and manage form submissions with detailed logs for behavior analysis.
 
- **User Authentication:**
  - Secure login and registration system.
  - Profile management including password change and role assignment.

- **Analytics Dashboard:**
  - View key metrics and performance indicators (under development).
  - Filter data by date, status, and assigned user.

- **Campaign Analysis (under development):**
  - Associate leads with marketing campaigns.
  - Track the effectiveness of each campaign with upper management analysis dashboards.
 
  For more planned features see the status section.

### Tech Stack

- **Python**: The primary programming language used for backend development.
- **Django**: The web framework used for building the backend and handling the MVC structure.
- **SQLite**: The database system used for development and testing (will be replaced with PostgreSQL MSQLS in production, still under evaluation).
- **HTML/CSS**: For building the frontend structure and styling.
  - **W3.CSS**: A CSS framework used for styling and responsive design.
  - **FontAwesome**: Icon library used for enhancing the UI.
- **JavaScript**: Used for adding interactivity to the frontend.
  - **Vanilla JS**: For basic DOM manipulation and event handling.
- **Git**: Version control system used to manage code and collaboration.
- **GitHub**: Hosting service for version control using Git, where the project's repository is stored.
- **Django REST Framework**: For building APIs (if applicable).
- **Celery**: Task queue used for handling asynchronous tasks (under development).
- **Docker**: Containerization tool used to create and manage containers (to be containerized once ready for deployment).
- **Gunicorn**: WSGI HTTP server for running Django applications in production (to be implemented once containerization ready).

### Development Tools

- **VS Code**: Preferred code editor for development.
- **SQLite Browser**: For managing the SQLite database during development.

### Deployment

- **on premise**: To be deployed on local server as internal client tool.


### Status
- **Current Status:** *INTRALOG CRM leads Manager is currently under development, waiting for upper management deffinitions for the last functionalities.*
- **Planned Features:**
  - *Campaign Analysis:* *This feature will associate mkt campaign source with each lead, to study each campaign config and combinations efficiency.*
  - *Commercial Performance:* *Management will be able to track the team's perfomance as a whole and for each member with the event log functionality, that will have real time analysis for improvement areas leverage and identify best skills and practices to replicate in the rest of the team.*
  - *Real time alerts:* *This feature will give personalized alerts via mail and whatsapp about relevant potential leads.*

### Contributors
- **Lead Developer:** *Felipe Torres*

### Project Links
- **Repository:** [Leads manager](https://github.com/manfeltor/leadsmanager)
- **Live Demo:** [Live Demo](#) *Link to a live demo if available.*

### License
*State the license under which the project is released (e.g., MIT License).*
