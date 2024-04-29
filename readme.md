# CDIAC at AppState Dashboard

*Author: M. W. Hefner*

This is an interactive dashboard designed to explore detailed carbon emission data from the Carbon Dioxide Information Analysis Center (CDIAC) at Appalachian State University. It uses Dash, a Python web application framework, to render the user interface in a web browser.

For more information about CDIAC at AppState, please see the [CDIAC at AppState webpage](https://energy.appstate.edu/research/work-areas/cdiac-appstate) and the "about" markdown tab of this application. For more details on contributing to this project, refer to the RIEEE environmental data scientist.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Application Structure](#application-structure)
- [Running the Application Locally](#running-the-application-locally)
- [Known Issues](#known-issues)
- [Updating the Dashboard Annually](#updating-the-dashboard-annually)

## Prerequisites

Before you start, make sure you have Python 3.11 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

### Cloning the Repository

To get started with the CDIAC Dashboard, you'll first need to clone the repository to your local machine:

```bash
git clone https://github.com/your-repository-url/cdiac-dashboard.git
cd cdiac-dashboard
```

### Setting Up the Environment

It's recommended to use a virtual environment to manage the dependencies and isolate the project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

For pip to install properly, it is necessary to have Visual Studio developer tools installed.  Otherwise, requirements can be installed effectively with conda or miniconda, **which is recommended for virtual environment management** for this very reason.

## Application Structure

The application is structured as follows:

- `application.py`: The main Python script to run the Dash app. It initializes the server and layouts.
- `components/`: Contains Python modules for different parts of the application like figures, tables, and utility functions.
- `assets/`: Stores static files like stylesheets, JavaScript files, images, and markdown files.
- `Dockerfile`: Contains commands to build a Docker image for the application.
- `requirements.txt`: Lists all Python libraries that the application depends on.

### Key Components

- `components/main_container.py`: The main container that encapsulates the entire Dash layout.
- `components/figures/`: This directory contains scripts to generate the interactive charts and figures used in the dashboard.
- `components/tables/`: Handles the table views and data interactions within the dashboard.
- `components/control_panel/`: Manages the interactive control elements like dropdowns and buttons, allowing users to filter and manipulate the data displayed in the dashboard.
- `components/content_display/`: Responsible for rendering the main content views such as graphs and data tables based on user interactions with the control panel.
- `components/utils/`: Contains application constants, links to local data, database connectivity, and other useful functionality.

## Running the Application Locally

To run the application locally, ensure you are in the project's root directory and have activated your virtual environment. Start the app by running:

```bash
python application.py
```

This will start the Dash server on `http://127.0.0.1:8050/`.

## Known Issues

- Both `assets/markdown/methodology.md` and `assets/markdown/about.md` pages need to be re-written and updated, respectively.  Until they are, these options have been commented out in the navigation dropdown options.
- There is a bug with the time series by source code when deployed onto the server - nations are not showing, only regions; consider mapping line-marker attributes differently.  Until this is fixed, the option has been commented out in the navigation dropdown options.

## Updating the Dashboard Annually

To update the dashboard data annually:

1. Modify `components/utils/constants.py` with the new year and data file name.
2. Replace the data file in `assets/data/` with the updated dataset.
3. Update `assets/markdown/download.md` with new download information.
4. After releasing on GitHub and publishing the updated application to Zonodo, update the **application's** Zonodo DOI badge in `components/utils/constants.py`.

After these steps, your application should reflect the latest data and be ready for use.
