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
import components.control_panel.controls.nation_dropdown as nation_dropdown

# LAYOUT
layout = dash.html.Div(

    id = component_id,

    children = [
        
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
                
            ],

            color = "#ffcc00"

        ),

        # INFO / DEFAULT BUTTON AREA
        defaultbuttonarea.layout,

    ]
)

# CALLBACKS (0)
