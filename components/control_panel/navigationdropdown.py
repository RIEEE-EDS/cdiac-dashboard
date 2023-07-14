"""
Module/Script Name: navigationdropdown.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 0

"""

# Import Dependencies
import dash


# STYLES (JSON CSS)

styles = {
    'dropdown-menu': {
        'margin-top': '20px',
        'margin-bottom': '20px',
        'color': '#000'
    }
}

# LAYOUT

layout = dash.html.Div(

    className='dropdown-menu',
    
    style=styles['dropdown-menu'],

    children=[

        dash.html.H2('Navigation', style = {'color' : '#fff'}),

        dash.dcc.Dropdown(

            id='navigation-dropdown',

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
