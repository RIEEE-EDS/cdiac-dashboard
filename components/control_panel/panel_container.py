"""
Module/Script Name: panel_container.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the logical layout and callback functionality of the panel_container.

Exceptional notes about this script:
(none)

Callback methods: 1

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "panel_container"

# Import Dependencies
import dash.html.Div
import dash.exceptions
import components.control_panel.control_panel_header as control_panel_header
import components.control_panel.controls_container as controls_container
import components.control_panel.backtodatadash as backtodatadash

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # HEADER
        control_panel_header.layout,

        # OPTIONS CONTAINER
        controls_container.layout,

        # INFO / BACK TO DATADASH
        #backtodatadash.layout,

        dash.html.Div(

            id = "control_panel_toggle"

        )

    ]
)

# CALLBACKS (1)

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Output("control_panel_toggle", 'className'),
    dash.dependencies.Input('theme_toggle', 'className'),
    dash.dependencies.Input("control_panel_toggle", 'n_clicks')
)
def update_source_dropdown(theme, panel_toggle_clicks):
    if panel_toggle_clicks is None:
        return theme, theme
    elif panel_toggle_clicks % 2 == 1 :
        return theme + " collapsed", theme + " collapsed"
    else :
        return theme, theme