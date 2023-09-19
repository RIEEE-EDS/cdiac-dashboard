"""
Module/Script Name: backtodatadash.py
Author: M. W. Hefner

Created: 6/29/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the backtodatadash link area.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "backtodatadash"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [
        dash.html.A(dash.html.Img(
                src='/assets/images/RIEEE_LOGO.svg'
            ), href = "https://rieee.appstate.edu",
                style={"color" : "white", 'width': '65%', 'height': '65%', 'display': 'block', 'margin': 'auto'}),
        dash.html.P(["This dashboard is powered and supported by the ",
                     dash.html.A("Research Institute for Environment, Energy, and Economics", href = "https://datadash-dev.appstate.edu", style={"color" : "white"}),
                       " at Appalachian State University."]),
        dash.html.H3(
            children = [
                dash.html.A("Go to DataDash", href = "https://datadash-dev.appstate.edu", style={"color" : "white", 'text-decoration': 'none'}, className = 'universal_button')
            ]
        ),
    ]
)

# CALLBACKS (0)
