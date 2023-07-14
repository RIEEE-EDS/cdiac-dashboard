"""
Module/Script Name: header.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the control_panel header.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "header"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# STYLES (CSS DICT)
styles = {
    component_id : {
        'padding': '0px',
        'background' : '#222',
        'color' : '#fff',
        'text-align' : 'center',
        'border': '1px solid #ffc900',
        'border-top-left-radius' : '10px',
        'border-top-right-radius' : '10px'
    },

    'a' : {
        "text-align": "center", 
        "display": "block", 
        'border-bottom' : '1px solid #ffc900',
        'background' : '#000',
        'border-top-left-radius' : '12px',
        'border-top-right-radius' : '12px'
    },
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles[component_id],
    children= [

        # Appstate Logo and Link

        dash.html.A(

            href = "https://www.appstate.edu",

            style = styles['a'],

            children=[

                dash.html.Img(
                    src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",
                    
                    style={"height": "30px", "display": "inline-block", 'margin' : '10px'}
                )

            ]

        ),

        # Title

        dash.html.H2("Carbon Dioxide Information Analysis Center (CDIAC) at AppState")
    ]
)

# CALLBACKS (0)
