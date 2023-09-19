"""
Module/Script Name: fuel_type_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 9/06/2023

Project: CDIAC at AppState

Script Description: The fuel type selector allows for the selection of fossil fuel by solid, liquid, gaseous, or total.

Exceptional notes about this script:
(none)

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "fuel_type_dropdown"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children=[

        dash.html.H2('Fuel Type'),

        dash.dcc.Dropdown(

            id='fuel-type-dropdown-controler',

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

# CALLBACKS (2)

# Updates whether or not to show the fuel type dropdown selector.
@dash.callback(
    # OUT controls visibility of component (HIDDEN == VARIABLE -> FALSE == VISIBLE)
    dash.dependencies.Output(component_id, 'hidden'),
    # IN from navigation dropdown
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def update_fuel_dropdown(nav_opt) :
    # Navigat options that have a fuel type dropdown menu
    if nav_opt in [
        'carbon-atlas', 
        'timeseries-source', 
        'timeseries-country', 
        'sunburst-country', 
        'sunburst-source', 
        'browse'] :
        return False # IS visible
    else:
        return True # is NOT visible

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme