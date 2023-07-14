"""
Module/Script Name: nation_dropdown.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the nation_dropdown.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "nation_dropdown"

# Import Dependencies
import dash.html.Div
from components.staticdata import data as d

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

        dash.html.H2('Country', style=styles['h2']),

        dash.dcc.Dropdown(

            id='nation-dropdown-controler',

            value = [
                'CHINA (MAINLAND)', 
                'UNITED STATES OF AMERICA',
                'RUSSIAN FEDERATION',
                'INDIA'],

            options=[{'label': factor, 'value': factor} for factor in d.df_total['Nation'].unique()],

            clearable=False,

            multi=True

        )

    ]
)

# CALLBACKS (1)

# Updates whether to show the country selector, and whether it's multi- or single
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Output('nation-dropdown-controler', 'multi'),
    dash.dependencies.Output('nation-dropdown-controler', 'value'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def update_navigation_dropdown(nav_opt) :

    # Not Hidden, Not Multi Choice.  Default USA.
    if nav_opt == 'timeseries-country' : 
        return False, False, 'UNITED STATES OF AMERICA'
    
    # Not Hidden.  Multi.
    if nav_opt == 'timeseries-source' :

        return False, True, [
                'CHINA (MAINLAND)', 
                'UNITED STATES OF AMERICA',
                'RUSSIAN FEDERATION',
                'INDIA']
    
    # Hidden
    else:
        return True, True, [
                'CHINA (MAINLAND)', 
                'UNITED STATES OF AMERICA',
                'RUSSIAN FEDERATION',
                'INDIA']
