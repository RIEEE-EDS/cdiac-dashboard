"""
Module/Script Name: navigation_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 9/06/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the navigation_dropdown.

Exceptional notes about this script:
(none)

Callback methods: 1

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "navigation_dropdown"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# Two IDs are used - a wrapper around the dropdown, and the controller itself.
# This allows for easier self-reference without worrying about infinite loops,
# though I love hofstadter's work, myself.

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children= [

        dash.html.H2('Navigation'),

        dash.dcc.Dropdown(

            id='navigation-dropdown-controler',

            # Provides default (and in the case of navigation, perm) options.

            # NOTE: Simply adding an option here is not sufficient to add
            # a control to the control panel.  Please see the DataDash Development
            # handbook for clarification and design guidance.

            options=[

                {'label': 'About', 'value': 'about'},

                {'label': 'Carbon Emissions Atlas', 'value': 'carbon-atlas'},

                {'label': 'Time Series (by Political Geography)', 'value': 'timeseries-country'},

                {'label': 'Sunburst Chart (by Political Geography)', 'value': 'sunburst-country'},

                {'label': 'Time Series (by Source)', 'value': 'timeseries-source'},

                {'label': 'Sunburst Chart (by Source)', 'value': 'sunburst-source'},

                {'label': 'Browse Data Table', 'value': 'browse'},

                {'label': 'How We Get Our Numbers', 'value': 'methodology'},

                {'label': 'Download Data', 'value': 'download'}
                
            ],

            # Default to the Carbon Atlas
            value = 'carbon-atlas',

            clearable=False,

            # Making this searchable will disturb the tablet experience.
            searchable=False

        )

    ]
)

# CALLBACKS (1)
# Controls the theme of the navigation dropdown
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme
