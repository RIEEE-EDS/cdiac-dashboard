"""
Module/Script Name: controls_container.py

Author(s): M. W. Hefner

Initially Created: 6/28/2023

Last Modified: 10/29/2023

Script Description: contains the controls of the application, including navigation, and user controls, and the boilerplate credits at the bottom of the control panel.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "controls_container"

# Import Dependencies
import dash.html.Div
import components.control_panel.controls.navigation_dropdown as navigation_dropdown
import components.control_panel.controls.theme_toggle as theme_toggle
import components.control_panel.defaultbuttonarea as defaultbuttonarea
import components.control_panel.controls.fuel_type_dropdown as fuel_type_dropdown
import components.control_panel.controls.source_dropdown as source_dropdown
import components.control_panel.controls.source_A_dropdown as source_A_dropdown
import components.control_panel.controls.source_B_dropdown as source_B_dropdown
import components.control_panel.controls.nation_dropdown as nation_dropdown
import components.control_panel.controls.nation_group_selection as nation_group_selection

# LAYOUT
layout = dash.html.Div(

    id = component_id,

    children = [

        dash.html.P(
            [
                dash.html.A(
                    "Click here", 
                    href = "https://energy.appstate.edu/research/work-areas/cdiac-appstate", 
                    style={"color" : "white"}
                ),

                " to read more about the Carbon Dioxide Information Analysis Center at Appalachian State University."
            ],
            style={"textAlign": "center"}
        ),
        
        # NAVIGATION SELECTION
        navigation_dropdown.layout,

        # CONTROLS GO HERE
        dash.dcc.Loading(

            children = [
                # FUEL TYPE SELECTION
                fuel_type_dropdown.layout,
                
                # SOURCE SELECTION
                source_dropdown.layout,

                # NATION SELECTION
                nation_dropdown.layout,

                # Ternary Source Selections
                source_A_dropdown.layout,
                source_B_dropdown.layout,
                # Ternary Group Selection
                nation_group_selection.layout

            ],

            color = "#ffcc00"

        ),

        # INFO / DEFAULT BUTTON AREA
        defaultbuttonarea.layout,

    ]
)

# CALLBACKS (0)
