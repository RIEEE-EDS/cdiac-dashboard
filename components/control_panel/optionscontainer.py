"""
Module/Script Name: optionscontainer.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 0

"""

# Import Dependencies
import dash.html.Div
import components.control_panel.navigationdropdown as navigationdropdown
import components.control_panel.fueltypedropdown as fueltypedropdown
import components.control_panel.sourcedropdown as sourcedropdown
import components.control_panel.nationdropdown as nationdropdown
import components.control_panel.backtodatadash as backtodatadash

# STYLES (JSON CSS)

styles = {
    'options-container': {
        'padding': '20px',
        'background-color': '#333',
        'color': '#fff',
        'overflow-y' : 'auto',
        
        #'border': '1px solid #000',

        'border-bottom-left-radius' : '10px',
        'border-bottom-right-radius' : '10px'
    }
}

# LAYOUT

layout = dash.html.Div(

    className='options-container',

    style=styles['options-container'],

    children=[

        # NAVIGATION SELECTION
        navigationdropdown.layout,

        # FUEL TYPE SELECTION
        fueltypedropdown.layout,
        
        # SOURCE SELECTION
        sourcedropdown.layout,

        # NATION SELECTION
        nationdropdown.layout,

        # INFO / BACK TO DATADASH
        backtodatadash.layout

    ]
)

# CALLBACKS (0)
