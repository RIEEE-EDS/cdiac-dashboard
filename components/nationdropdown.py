"""
Module/Script Name: nationdropdown.py
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

    className='dropdown-menu',

    id='nation-selection-container',

    style=styles['dropdown-menu'],

    hidden = True,

    children=[

        dash.html.H2('Country', style={'color': '#fff'}),

        dash.dcc.Dropdown(

            id='nation-dropdown',

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
@dash.callback(
    dash.dependencies.Output('nation-selection-container', 'hidden'),
    dash.dependencies.Output('nation-dropdown', 'multi'),
    dash.dependencies.Output('nation-dropdown', 'value'),
    dash.dependencies.Input('navigation-dropdown', 'value')
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