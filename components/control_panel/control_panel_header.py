"""
Module/Script Name: control_panel_header.py
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
component_id = "control_panel_header"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # Appstate Logo and Link

        dash.html.A(

            href = "https://www.appstate.edu",

            children=[

                dash.html.Img(

                    src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",

                )

            ]

        ),

        # Title

        dash.html.H2("Carbon Dioxide Information Analysis Center (CDIAC) at AppState")
    ]
)

# CALLBACKS (0)
