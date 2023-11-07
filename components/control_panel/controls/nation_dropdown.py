"""
Module/Script Name: nation_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 9/22/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the nation_dropdown.

Exceptional notes about this script:
This script is titled using the old "nation" terminology; as of September 2023, this is officially outdated language (in favor of the use of the term "political geography").  Eventually, it would be nice to eliminate vestiges of the previous standard language so that the language in the scripts are consistent with the language in the literature it is used to produce.

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "nation_dropdown"

# Import Dependencies
import dash.html.Div
from components.utils import constants as d

# STYLES (CSS DICT)

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children= [

        dash.html.H2('Political Geography'),

        dash.dcc.Dropdown(

            id='nation-dropdown-controler',

            value = 'WORLD',

            options=[{'label': factor, 'value': factor} for factor in d.df_total['Political Geography'].unique()],

            clearable=False,

            multi=True

        )

    ]
)

# CALLBACKS (2)

# Updates whether to show the country selector, and whether it's multi- or single
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Output('nation-dropdown-controler', 'multi'),
    dash.dependencies.Output('nation-dropdown-controler', 'value'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def update_nation_dropdown(nav_opt) :

    # Not Hidden, Not Multi Choice.  Default USA.
    if nav_opt == 'political-geography-time-series' : 
        return False, False, 'WORLD'
    
    if nav_opt == 'political-geography-sunburst' : 
            return False, False, 'WORLD'

    # Not Hidden.  Multi.
    if nav_opt == 'source-time-series' :

        return False, True, ['ANNEX I', 'NON-ANNEX I', 'AFRICA', 'ASIA PACIFIC', 'COMMONWEALTH OF INDEPENDENT STATES', 'EUROPE', 'NORTH AMERICA', 'MIDDLE EAST', 'SOUTH AND CENTRAL AMERICA', 'CHINA (MAINLAND)',  'UNITED STATES OF AMERICA', 'RUSSIAN FEDERATION', 'INDIA']
    
    # Hidden
    else:
        return True, False, []

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme