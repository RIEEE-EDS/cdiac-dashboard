"""
Module/Script Name: maincontainer.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the maincontainer.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "maincontainer"

# Import Dependencies
import dash.html.Div
import components.control_panel.panel_container as control_panel
import components.content_display.content_display as content_display

# STYLES (CSS DICT)
styles = {
    component_id : {
        # Flow, Size and Function
        'display': 'flex',
        'flex-flow' : 'row nowrap',
        'justify-content' : 'center',
        'align-items' : 'stretch',
        'height': '95vh',

        # Color and Fonts
        'background-color' : '#fff',
        'font-size' : '15px',
        'font-family' : '"Open Sans",sans-serif'
    }
}

# LAYOUT
layout = dash.html.Div(

    # MAIN APPLICATION CONTAINER

    id = component_id,
    
    style = styles[component_id],
    
    children= [

        # control_panel

        control_panel.layout,

        # Content Area

        content_display.layout

    ]
)

# CALLBACKS (0)
