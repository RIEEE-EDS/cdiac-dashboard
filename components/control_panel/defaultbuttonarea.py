"""
Module/Script Name: defaultbuttonarea.py

Author(s): M. W. Hefner

Initially Created: 6/29/2023

Last Modified: 10/29/2023

Script Description: this script defines the boilerplate area at the bottom of the control panel.  This includes the theme toggle, the datadash button, and the credits.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "defaultbuttonarea"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
import components.control_panel.controls.theme_toggle as theme_toggle
import components.utils.constants as constants

if constants.show_credit :
    # LAYOUT
    layout = dash.html.Div(
        id = component_id,
        children= [

            # Theme and Go-Back-To-DataDash buttons
            dash.html.Div(

                # So that the default buttons can be styled appropriately together
                id = "defaultbuttons",

                children = [

                    # THEME TOGGLE
                    theme_toggle.layout,

                    # Go-Back-To-DataDash button
                    dash.html.Div([
                        dash.html.A(
                            dash.html.Button("Go to DataDash", className="universal_button"),
                            href="/",
                            target="_blank",  # Opens the link in a new tab
                        )
                    ])

                ]
            ),

            # Statement of RIEEE support and source code link
            dash.html.P(
                [
                    "This application is made possible by the ",
                    dash.html.A(
                        "Research Institute for Environment, Energy, and Economics", 
                        href = "https://rieee.appstate.edu", 
                        style={"color" : "white"}
                    ),
                    " at Appalachian State University through the RIEEE DataDash secure research web application platform. License information and the python source code for this application is avaiable ",
                    dash.html.A(
                        "here on GitHub.", 
                        href = "https://github.com/mwhefner/cdiac-dashboard", 
                        style={"color" : "white"}
                    ),
                ]
            ),

            # Displays the RIEEE logo, which serves as a link to the RIEEE mainpage
            dash.html.A(
                dash.html.Img(
                    src='assets/images/RIEEE_LOGO.png', height=200
                ), 
                href = "https://rieee.appstate.edu",
                style={'display': 'block', 'margin': 'auto'}
            ),

            # Authorship Credit
            dash.html.P(
                [
                    "To cite this dashboard:"
                ]
            ),

            # DOI
            dash.html.A(
                dash.html.Img(
                    src='https://zenodo.org/badge/666200101.svg'
                ), 
                href = "https://zenodo.org/doi/10.5281/zenodo.10607881",
                style={'display': 'block', 'margin': 'auto'}
            ),

            # Authorship Credit
            dash.html.P(
                [
                    "Developer: ",
                    constants.developers
                ]
            ),

        ]
    )
    
else :

    layout = dash.html.Div(
        id = component_id,
        children= [

            # Theme and Go-Back-To-DataDash buttons
            dash.html.Div(

                # So that the default buttons can be styled appropriately together
                id = "defaultbuttons",

                children = [

                    # THEME TOGGLE
                    theme_toggle.layout,

                    # Go-Back-To-DataDash button
                    dash.html.Div([
                        dash.html.A(
                            dash.html.Button("Go to DataDash", className="universal_button"),
                            href="/",
                            target="_blank",  # Opens the link in a new tab
                        )
                    ])
                ]
            ),
        ]
    )

# CALLBACKS (0)
