"""
Module/Script Name: theme_toggle.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/15/2023

Project: CDIAC at AppState

Script Description: This script defines the logical layout and callback functionality of the theme_toggle.

Exceptional notes about this script:
(none)

Callback methods: 1

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "theme_toggle"

# Import Dependencies
import dash.html

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # TODO: Make Look nice
        dash.html.Button('Switch to Dark Theme', id = 'theme_toggle_switch', n_clicks=0)

    ]
)

# CALLBACKS (1)
# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Output('theme_toggle_switch', 'children'),
    dash.dependencies.Input('theme_toggle_switch', 'n_clicks')
)
def update_source_dropdown(n_clicks):
    if n_clicks % 2 == 0 :
        return 'light', "Switch to Dark Theme"
    else :
        return 'dark', "Switch to Light Theme"