"""
Module/Script Name: source_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/16/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the source_dropdown.

Exceptional notes about this script:
(none)

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "source_dropdown"

# Import Dependencies
import dash.html.Div
from components.utils import constants as d

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children= [

        dash.html.H2('Source'),

        dash.dcc.Dropdown(

            id='source-dropdown-controler',

            value = d.df_total.columns[2],

            options = [{'label': col, 'value': col} for col in d.df_total.columns[2:] if col not in ['Nation', 'Year']],

            clearable=False,

            optionHeight=50

        )

    ]
)

# CALLBACKS (2)

# Determines whether or not to show the source dropdown menu
# and what the options are.
# TODO: This is messy.  Clean it up once the SQL connection is established.
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Output('source-dropdown-controler', 'options'),
    dash.dependencies.Output('source-dropdown-controler', 'value'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('source-dropdown-controler', 'value')
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

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme