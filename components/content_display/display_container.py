"""
Module/Script Name: display_container.py

Author(s): M. W. Hefner

Initially Created: 7/01/2023

Last Modified: 10/29/2023

Script Description: This is the display container that holds the content being displayed by the application.  It calls different plotly figures, markdowns and tables as selected by the navigation dropdown menu.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "display_container"

# Import Dependencies
import dash.html.Div
import plotly.graph_objs as go
from components.utils import constants as d
from components.figures.carbon_atlas import carbon_atlas
from components.figures.country_sunburst import country_sunburst
from components.figures.country_timeseries import country_timeseries
from components.figures.source_sunburst import source_sunburst
from components.figures.source_timeseries import source_timeseries
from components.figures.source_ternary import source_ternary
from components.figures.type_ternary import type_ternary
from components.tables.browse import browse_table
from dash import Patch
import numpy as np

# LAYOUT
layout = dash.html.Div(
    id = component_id,
)



config = {
    'doubleClickDelay': 500,
      'toImageButtonOptions': {
        'format': 'jpeg', # one of png, svg, jpeg, webp
        'filename': 'CDIAC_APPSTATE_DASHBOARD',
        'height': 1080,
        'width': 1920,
    }
    }

sunburst_config = {
    'doubleClickDelay': 500,
      'toImageButtonOptions': {
        'format': 'jpeg', # one of png, svg, jpeg, webp
        'filename': 'CDIAC_APPSTATE_DASHBOARD',
        'height': 1050,
        'width': 1400,
    }
    }

# CALLBACKS (2)
# The first callback decides what content should be in the display container.
@dash.callback(
    dash.dependencies.Output(component_id, 'children'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('theme_toggle', 'className'),
    dash.dependencies.Input('source-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('nation-dropdown-controler', 'value'),
    dash.dependencies.Input('source-a-dropdown-controler', 'value'),
    dash.dependencies.Input('source-b-dropdown-controler', 'value'),
    dash.dependencies.Input('nation-group-dropdown-controler', 'value'),
)
def update_container(nav_opt, theme, source, fuel_type, nation, source_a, source_b, grouping):
    
    # for displaying all non-plotly figure navigation options
    if nav_opt == "about" :
        return [
            # About page: Markdown
            dash.dcc.Markdown(children = d.about_content, className = "markdown", mathjax=True)
        ]
    elif nav_opt == "methodology" :
        return [
            # Methodology: Markdown
            dash.dcc.Markdown(children = d.methodology_content, className = "markdown", mathjax=True)
        ]
    elif nav_opt == "download" :
        return [
            # Downloan page: Markdown for now
            # TODO: Perhaps make this a nicer page on down the line?
            dash.dcc.Markdown(children = d.download_content, className = "markdown", mathjax=True)
        ]
    if nav_opt == "table" :
        return [
            dash.dcc.Loading(
                children=browse_table(),
                )
        ]
    
    else :

        if nav_opt == 'carbon-atlas' :

            # Carbon Atlas
            return dash.dcc.Loading(
                id = "carbon-atlas-loading",
                children= dash.dcc.Graph(
                    figure=carbon_atlas(source, fuel_type, theme) , 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'})
            )

        if nav_opt == 'political-geography-sunburst' :

            # Political Geography sunburst
            return dash.dcc.Loading(
                id="political-geography-sunburst-loading",
                children=dash.dcc.Graph(
                    figure=country_sunburst(nation, fuel_type, theme),
                    className='plotly-figure',
                    style={
                        'height': '100vh',
                        'background': 'radial-gradient(circle at center, #999 10%, transparent 70%)',
                        'background-size': '100% 100%',
                        'background-repeat': 'no-repeat'
                    },
                    config=sunburst_config
                )
            )


        if nav_opt == 'political-geography-time-series' :

            # Surface Demo
            return dash.dcc.Loading(
                id = "political-geography-time-series-loading",
                children=dash.dcc.Graph(
                    figure=country_timeseries(fuel_type, nation, theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'},
                    config=config)
            )
        
        if nav_opt == 'source-sunburst' :

            # Animation Demo
            return dash.dcc.Graph(
                    figure=source_sunburst(source, fuel_type, theme), 
                    className='plotly-figure', 
                    id="plot-figure-with-year",
                    style = {'height' :  '100vh'},
                    config=sunburst_config)
            

        if nav_opt == 'source-time-series' :

            # Animation Demo
            return dash.dcc.Loading(
                id = "source-time-series-loading",
                children=dash.dcc.Graph(
                    figure=source_timeseries(source, fuel_type, nation, theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'},
                    config=config)
            )
        
        if nav_opt == 'source-ternary' :

            # Animation Demo
            return dash.dcc.Loading(
                id = "ternary-loading",
                children=dash.dcc.Graph(
                    figure=source_ternary(source_a, source_b, fuel_type, grouping, theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'},
                    config=config)
            )
        
        if nav_opt == 'type-ternary' :

            # Animation Demo
            return dash.dcc.Loading(
                id = "ternary-loading",
                children=dash.dcc.Graph(
                    figure=type_ternary(source, grouping, theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'},
                    config=config)
            )

        else :
            return dash.dcc.Loading(
                children=dash.dcc.Graph(
                    figure=go.Figure(), 
                    className='plotly-figure', 
                    id="plot-figure-with-year",
                    style = {'height' :  '100vh'},
                    config=config))
