"""
Module/Script Name: panel_container.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the panel_container.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "panel_container"

# Import Dependencies
import dash.html.Div
import components.control_panel.header as header
import components.control_panel.controls_container as controls_container
import components.control_panel.backtodatadash as backtodatadash

# STYLES (CSS DICT)
styles = {
    component_id : {
        'order' : '1',
        'width' : '500px',
        'padding': '20px',
        'background-color': '#333',
        'color': '#fff',
        'border-radius' : '10px',
        'align-items' : 'stretch',
        'display' : 'flex',
        'flex-direction': 'column'
    }
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles[component_id],
    children= [

        # HEADER

        header.layout,

        # OPTIONS CONTAINER

        controls_container.layout,

        # INFO / BACK TO DATADASH

        backtodatadash.layout,

    ]
)

# CALLBACKS (0)
