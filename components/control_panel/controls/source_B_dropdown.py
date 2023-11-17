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
component_id = "source_b_dropdown"

# Import Dependencies
import dash.html.Div
from components.utils import constants as d

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children= [

        dash.html.H2('Source B (Bottom Left)'),

        dash.dcc.Dropdown(

            id='source-b-dropdown-controler',

            value = "Road Transport",

            options = [
                "Electric, CHP, Heat Plants",
                "Energy Industries' Own Use",
                "Manufact, Constr, Non-Fuel Industry",
                "Transport",
                "Road Transport",
                "Rail Transport",
                "Domestic Aviation",
                "Domestic Navigation",
                "Other Transport",
                "Household",
                "Agriculture, Forestry, Fishing",
                "Commerce and Public Services",
                "NES Other Consumption",
                "Bunkered",
                "Bunkered (Marine)",
                "Bunkered (Aviation)",
            ],

            clearable=False,

            optionHeight=50,

            searchable=True

        )

    ]
)

# CALLBACKS (2)

# Determines whether or not to show the source dropdown menu
# and what the options are.
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
)
def update_sourceb_dropdown(nav_opt):
    if nav_opt == 'source-ternary' : return False
    else : return True

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme