"""
Module/Script Name: dashboard.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0
"""

# Import Dependencies
from dash import Dash
import components.maincontainer as mc

# Initialize Dash Application
app = Dash(
    __name__, 
)

# Set Application Title
app.title = "CDIAC at AppState"

# Define Application Layout
app.layout = mc.layout

# Main script execution
if __name__ == '__main__':
    app.run_server(debug = True)
