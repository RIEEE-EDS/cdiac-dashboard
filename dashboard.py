"""
Module/Script Name: dashboard.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script initializes the dash application for development on a local machine. 

Exceptional notes about this script:

1. This script is for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
from dash import Dash
import components.main_container as mc
import configparser

cfg = configparser.ConfigParser()
cfg.read('/etc/rieee/rieee.conf')
cfg.read('rieee.conf')

# Import Styles that _have_ to be CSS;
external_stylesheets = {
    'light_theme' : [
        "./assets/externalstylesheets/dynamic_styling.css",
        "./assets/externalstylesheets/themes.css"
    ]
}

# Initialize Dash Application
app = Dash(
    __name__, 
    external_stylesheets = external_stylesheets['light_theme'],
    title = "CDIAC at AppState",
    update_title = None,
    url_base_pathname=cfg.get('app', 'url_prefix', fallback='/')
)

# Define Application Layout
app.layout = mc.layout

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

server = app.server

# Main script execution
# if __name__ == '__main__':
    # app.run_server(debug = True)
