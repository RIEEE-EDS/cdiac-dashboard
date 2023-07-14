"""
Module/Script Name: sourcedropdown.py
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
from components.staticdata import data as d

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

    className = 'dropdown-menu',

    id = 'source-dropdown-container',

    style=styles['dropdown-menu'],

    hidden = False,

    children=[

        dash.html.H2('Source', style = {'color' : '#fff'}),

        dash.dcc.Dropdown(

            id='source-dropdown',

            value = d.df_total.columns[2],

            options = [{'label': col, 'value': col} for col in d.df_total.columns[2:] if col not in ['Nation', 'Year']],

            clearable=False,

            optionHeight=50

        )
    ]
)

# CALLBACKS (1)
@dash.callback(
    dash.dependencies.Output('source-dropdown-container', 'hidden'),
    dash.dependencies.Output('source-dropdown', 'options'),
    dash.dependencies.Output('source-dropdown', 'value'),
    dash.dependencies.Input('navigation-dropdown', 'value'),
    dash.dependencies.Input('fuel-type-dropdown', 'value'),
    dash.dependencies.Input('source-dropdown', 'value')
)
def update_source_dropdown(nav_opt, fuel_type, value):

    # Defaults
    hidden = False
    options = []

    if nav_opt not in ['about', 'timeseries-country', 'methodology', 'download'] :

        if fuel_type == 'totals':

            options = [{'label': col, 'value': col} for col in d.df_total.columns[2:]]  # Exclude the first two columns
            
            # TODO: Exclude last col (NATION_ISO)

            # If coming from a different fueltype, change to best match source
            if value not in d.df_total.columns :
                value = d.best_match_option(value, fuel_type)

        elif fuel_type == 'solids':

            options = [{'label': col, 'value': col} for col in d.df_solid.columns[2:]]  # Exclude the first two columns
            
            if value not in d.df_solid.columns :
                value = d.best_match_option(value, fuel_type)

        elif fuel_type == 'liquids':

            options = [{'label': col, 'value': col} for col in d.df_liquid.columns[2:]]  # Exclude the first two columns
            
            if value not in d.df_liquid.columns :
                value = d.best_match_option(value, fuel_type)

        elif fuel_type == 'gases':
            
            options = [{'label': col, 'value': col} for col in d.df_gas.columns[2:]]  # Exclude the first two columns
            
            if value not in d.df_gas.columns :
                value = d.best_match_option(value, fuel_type)

    else :
        hidden = True
    
    return hidden, options, value