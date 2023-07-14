"""
Module/Script Name: navigation_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the navigation_dropdown.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "navigation_dropdown"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# STYLES (CSS DICT)
styles = {
    component_id : {
        'margin-top': '20px',
        'margin-bottom': '20px',
        'color': '#000'
    },

    'h2' : {
        'color' : '#fff'
    },
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles[component_id],
    children= [

        dash.html.H2('Navigation', style = styles['h2']),

        dash.dcc.Dropdown(

            id='navigation-dropdown-controler',

            options=[

                {'label': 'About', 'value': 'about'},

                {'label': 'Carbon Emissions Atlas', 'value': 'carbon-atlas'},

                {'label': 'Time Series (by Source)', 'value': 'timeseries-source'},

                {'label': 'Time Series (by Country)', 'value': 'timeseries-country'},

                {'label': 'Browse Raw Data', 'value': 'browse'},

                {'label': 'Methodology', 'value': 'methodology'},

                {'label': 'Download', 'value': 'download'}
                
            ],

            # Default to carbon map
            value='carbon-atlas',

            clearable=False

        )

    ]
)

# CALLBACKS (0)
