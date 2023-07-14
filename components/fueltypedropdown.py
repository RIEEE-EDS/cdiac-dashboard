"""
Module/Script Name: fueltypedropdown.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 1

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

    id = 'fuel-type-dropdown-container',

    style=styles['dropdown-menu'],

    hidden = False,

    children=[

        dash.html.H2('Fuel Type', style = {'color' : '#fff'}),

        dash.dcc.Dropdown(

            id='fuel-type-dropdown',

            options=[

                {'label': 'Totals', 'value': 'totals'},

                {'label': 'Solids', 'value': 'solids'},

                {'label': 'Liquids', 'value': 'liquids'},

                {'label': 'Gases', 'value': 'gases'}

            ],

            searchable=False,

            value='totals',

            clearable=False

        )
    ]
)

# CALLBACKS (1)
@dash.callback(
    dash.dependencies.Output('fuel-type-dropdown-container', 'hidden'),
    dash.dependencies.Input('navigation-dropdown', 'value')
)
def update_fuel_dropdown(nav_opt) :
    if nav_opt in ['carbon-atlas', 'timeseries-source', 'timeseries-country', 'browse'] :
        return False
    else:
        return True