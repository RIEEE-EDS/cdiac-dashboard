"""
Module/Script Name: sidebar.py
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
import components.header as header
import components.optionscontainer as optionscontainer


# STYLES (JSON CSS)

styles = {
    'sidebar': {
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

    className='sidebar',

    style=styles['sidebar'],

    children=[

        # HEADER

        header.layout,

        # OPTIONS CONTAINER

        optionscontainer.layout

    ]
)

# CALLBACKS (0)
