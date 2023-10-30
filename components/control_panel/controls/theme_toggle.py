"""
Module/Script Name: theme_toggle.py

Author(s): M. W. Hefner

Initially Created: 7/01/2023

Last Modified: 10/29/2023

Script Description: This script defines the functionality of the theme toggle.  When toggled (clicked), the theme toggle's class changes between "dark" and "light".  This is used in callbacks throughout the application to update components to the correct theme.

Exceptional notes about this script:
(none)

Callback methods: 1

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "theme_toggle"

# Import Dependencies
import dash.html

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [
        dash.html.Button(
            dash.html.P('Switch to Dark Theme'), 
            id = 'theme_toggle_switch',  
            className = "universal_button", 
            n_clicks=0
        )
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
        return 'light', dash.html.P('Switch to Dark Theme')
    else :
        return 'dark', dash.html.P('Switch to Light Theme')