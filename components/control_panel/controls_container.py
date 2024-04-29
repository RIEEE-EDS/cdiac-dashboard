"""
This module defines the controls container for the CDIAC Dashboard, organizing and displaying
all user interactive elements such as dropdowns and links for navigation within the application.

Attributes
----------
layout : dash.html.Div
    The main HTML container that holds all control elements, including navigation dropdowns,
    user interaction controls like theme toggles, and various data selection options. Also includes
    a descriptive paragraph with a link to more information about CDIAC at Appalachian State University.

component_id : str
    The identifier for the controls container, used for targeting with callbacks and styling.

See Also
--------
components.control_panel.controls.* : Modules that define individual controls like dropdowns for
fuel type, source selection, and navigation within the dashboard.

Notes
-----
This module plays a critical role in user interaction, facilitating the selection and filtering
of data visualized in the dashboard. It ensures that all controls are accessible and functional,
allowing for dynamic updates to the data displays based on user input.

Examples
--------
The layout of the controls container is structured to provide a user-friendly interface with all
necessary controls neatly organized. Here's how the layout is defined:

>>> layout = dash.html.Div(
        id=component_id,
        children=[
            dash.html.P(
                [
                    dash.html.A(
                        "Click here", 
                        href="https://energy.appstate.edu/research/work-areas/cdiac-appstate", 
                        style={"color": "white"}
                    ),
                    " to read more about the Carbon Dioxide Information Analysis Center at Appalachian State University."
                ],
                style={"textAlign": "center"}
            ),
            navigation_dropdown.layout,
            dash.dcc.Loading(
                children=[
                    fuel_type_dropdown.layout,
                    source_dropdown.layout,
                    nation_dropdown.layout,
                    source_A_dropdown.layout,
                    source_B_dropdown.layout,
                    nation_group_selection.layout
                ],
                color="#ffcc00"
            ),
            defaultbuttonarea.layout,
        ]
    )
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
                "To collapse or expand this control panel, touch or left-click the far right edge. ⇨"
            ],
            style={"textAlign": "center", 'fontSize' : '20px', "fontStyle": "italic"}
        ),

        dash.html.P(
            [
                dash.html.A(
                    "Click here", 
                    href = "https://energy.appstate.edu/research/work-areas/cdiac-appstate", 
                    style={"color" : "white"}
                ),

                " to read more about the Carbon Dioxide Information Analysis Center at Appalachian State University.",

                "Collapse or expand this control panel"
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
