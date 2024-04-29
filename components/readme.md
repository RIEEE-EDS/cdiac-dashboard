# Components Directory

This directory contains all the modular components of the CDIAC at AppState Dashboard. Each subdirectory and file is designed to encapsulate specific functionalities and features of the application, making the codebase more maintainable and scalable.

## Structure

The `components` directory is organized into several subdirectories, each containing Python modules related to specific aspects of the application's functionality:

- `content_display`: Modules for displaying the content of the dashboard such as graphs and data tables.
- `control_panel`: Modules for the dashboard's interactive controls like dropdowns and buttons.
- `figures`: Scripts that generate interactive charts and figures used throughout the dashboard.
- `tables`: Modules managing table views and data interactions.
- `utils`: Utility modules that include functionality such as constants, configuration settings, and database connections.

## Key Components

### Main Container

- **File**: `main_container.py`
- **Description**: This module serves as the root container of the dashboard. It integrates various components like the control panel and content display into the main application layout.

### Control Panel

- **Directory**: `control_panel`
- **Core Files**:
  - `controls_container.py`: Manages the layout of the dashboard controls.
  - `panel_container.py`: Encapsulates the entire control panel structure.

### Content Display

- **Directory**: `content_display`
- **Core Files**:
  - `display_container.py`: Handles the rendering of the main content based on user interactions from the control panel.

### Figures

- **Directory**: `figures`
- **Core Files**:
  - `carbon_atlas.py`: Generates a map visualization of carbon data.
  - `country_sunburst.py`: Provides a sunburst chart of country-level data.
  - `source_sunburst.py`: Provides a sunburst chart of source-level data.
  - `country_timeseries.py`: Provides a time series chart of country-level data.
  - `source_timeseries.py`: Provides a time series chart of source-level data.
  - `type_ternary.py`: Provides a ternary chart by fuel type.
  - `source_ternary.py`: Provides a ternary chart by source.

### Tables

- **Directory**: `tables`
- **Core Files**:
  - `browse.py`: Manages the display and interaction of data tables.

### Utilities

- **Directory**: `utils`
- **Core Files**:
  - `constants.py`: Defines constants used across the application.
  - `config.py`: Manages configuration settings read from external files.
  - `login.py` : Provides mechanisms for handling user authentication and authorization.

## Usage

To integrate a new component into the application, add the relevant Python file in the appropriate directory. Ensure that the new component is properly imported and utilized within the application's main layout or another component as necessary.

## Contributing

Contributions to the component architecture are welcome. Please ensure that all contributions maintain the modular structure of the directory and follow existing coding and documentation standards. For major changes, please open an issue first to discuss what you would like to change.

For more information on how to contribute, please review the project's main `readme.md`.

## Contact

For any specific queries regarding the components, please contact the primary developer, the RIEEE environmental data scientist, or refer to the project documentation on the repository's main page.
