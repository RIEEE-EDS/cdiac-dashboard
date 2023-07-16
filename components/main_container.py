"""
Module/Script Name: maincontainer.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the logical layout and callback functionality of the maincontainer.

Exceptional notes about this script:

1.  dcc.Loading doesn't actually create an HTML tag of its own, so it's necessary to handle its styling in the python code.

Callback methods: 1

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "main_container"

# Import Dependencies
import dash.html.Div
import components.control_panel.panel_container as control_panel
import components.content_display.display_container as display_container

# LAYOUT
layout = dash.html.Div(

    # MAIN APPLICATION CONTAINER

    id = component_id,
    
    className = 'light',

    children= [

        # control_panel

        control_panel.layout,

        # Content Area

        dash.dcc.Loading(
            fullscreen = True,
            style = {'background-color' : 'white'},
            id = 'loading',
            type = 'graph',
            children = display_container.layout
        )

    ]
)


# CALLBACKS (1)
# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Output('loading', 'style'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    if theme == 'light' :
        return theme, {'background-color' : 'white'}
    else :
        return theme, {'background-color' : 'black'}