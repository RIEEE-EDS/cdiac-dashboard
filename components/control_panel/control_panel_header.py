"""
Module/Script Name: control_panel_header.py

Author(s): M. W. Hefner

Initially Created: 6/28/2023

Last Modified: 10/29/2023

Script Description: This is the control panel header.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "control_panel_header"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
from components.utils.constants import application_title

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

        dash.html.H1(application_title)

    ]
)

# CALLBACKS (0)
