"""
Module/Script Name: source_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 9/06/2023

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

            optionHeight=50,

            searchable=False

        )

    ]
)

# CALLBACKS (2)

# Determines whether or not to show the source dropdown menu
# and what the options are.
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Output('source-dropdown-controler', 'options'),
    dash.dependencies.Output('source-dropdown-controler', 'value'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.State('source-dropdown-controler', 'options'),
    dash.dependencies.Input('source-dropdown-controler', 'value')
)
def update_source_dropdown(nav_opt, fuel_type, options, value):
    
    #print(nav_opt, fuel_type, options, value)

    # Defaults
    hidden = True

    if fuel_type == "totals" :
        options = [
            {'label': col, 'value': col} for col in d.df_total.columns[2:] 
            if col not in ['Nation', 'Year'] and 
            (nav_opt not in ['source-sunburst', 'type-ternary', 'carbon-atlas'] or col != "Stat Difference (Supplied - Consumed)")
        ]
    else :
        options = [
            {'label': col, 'value': col} for col in d.df_total.columns[2:] 
            if col not in ['Nation', 'Year', 'Flaring of Natural Gas', 'Manufacture of Cement', 'Per Capita Total Emissions'] and 
            (nav_opt not in ['source-sunburst', 'type-ternary', 'carbon-atlas'] or col != "Stat Difference (Supplied - Consumed)")
        ]

    if nav_opt in [
            'carbon-atlas',

            'source-time-series',

            'source-sunburst',

            'type-ternary',
        ] :

        hidden = False

        if nav_opt != 'source-time-series' and value == "Stat Difference (Supplied - Consumed)":
            return hidden, options, "Fossil Fuel Energy (Supplied)"

        if fuel_type == 'totals' and nav_opt != 'type-ternary':

            # If coming from a different fueltype, change to best match source
            if value not in d.df_total.columns :
                value = d.best_match_option(value, fuel_type)

        else :
            
            if nav_opt == 'type-ternary':
                value = d.best_match_option(value, "solids")
            elif value not in d.df_gas.columns :
                value = d.best_match_option(value, fuel_type)

    return hidden, options, value

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme