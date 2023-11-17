"""
Module/Script Name: nation_group_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 9/06/2023

Project: CDIAC at AppState

Script Description: The nation group selector allows for the selection of different groupings on the ternary analysis pages.

Exceptional notes about this script:
(none)

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "nation_group_dropdown"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children=[

        dash.html.H2('Aggregation Level'),

        dash.dcc.Dropdown(

            id='nation-group-dropdown-controler',

            options=[

                {'label': 'Individual (No Aggregates)', 'value': 'individual'},

                {'label': 'BP World Region Aggregates', 'value': 'region'},

                {'label': 'UNFCCC Party Type Aggregates', 'value': 'annex'},

                {'label': 'Global Aggregate', 'value': 'world'}

            ],

            searchable=False,

            value='individual',

            clearable=False

        )
    ]
)

# CALLBACKS (2)

# Updates whether or not to show the nation group dropdown selector.
@dash.callback(
    # OUT controls visibility of component (HIDDEN == VARIABLE -> FALSE == VISIBLE)
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Output('nation-group-dropdown-controler', 'hidden'),
    # IN from navigation dropdown
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def update_fuel_dropdown(nav_opt) :
    # Navigat options that have a nation group dropdown menu
    if nav_opt in [
        'type-ternary', 'source-ternary'] :
        return False, False # IS visible
    else:
        return True, True # is NOT visible

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme