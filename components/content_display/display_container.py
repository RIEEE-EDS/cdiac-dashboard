"""
Module/Script Name: content_display.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/15/2023

Project: CDIAC at AppState

Script Description: This script defines the logical layout and callback functionality of the content_display.

Exceptional notes about this script:
(none)

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "display_container"

# Import Dependencies
import dash.html.Div
from components.staticdata import data as d
from components.figures import figures
from components.figures.carbon_atlas import carbon_atlas
from components.tables import browse

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        dash.dcc.Graph(id='map-graph')

    ]
)

# CALLBACKS (2)
# The first callback decides, based on the state of navigation, fuel type, and source, what content should be in the display container.
@dash.callback(
    dash.dependencies.Output(component_id, 'children'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('source-dropdown-controler', 'value'),
)
def update_container(nav_opt, fuel_type, source):

    if nav_opt == "about" :
        return [
            # About page: Markdown
            dash.dcc.Markdown(children = d.about_content, mathjax=True)
        ]
    elif nav_opt == "methodology" :
        return [
            # Methodology: Markdown
            dash.dcc.Markdown(children = d.methodology_content, mathjax=True)
        ]
    elif nav_opt == "download" :
        return [
            # Downloan page: Markdown for now
            # TODO: Perhaps make this a nicer page on down the line?
            dash.dcc.Markdown(children = d.download_content, mathjax=True)
        ]
    elif nav_opt == "browse" :
        return [
            # Browse returns the browse datatable
            browse.browse_table(fuel_type, source)
        ]
    else :
        return [
            dash.dcc.Graph(id='map-graph', style = {'height' :  '100%'})
        ]
    
# Updates the graph or map displayed in the content area's map-graph
@dash.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('source-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('nation-dropdown-controler', 'value'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_map_or_graph(nav_opt, source, fuel_type, nation, theme):

    if nav_opt == 'carbon-atlas' :

        # CARBON ATLAS

        return carbon_atlas(source, fuel_type, theme)

    elif nav_opt == 'timeseries-country' :

        # TIME SERIES BY COUNTRY

        return figures.timeseries_country(fuel_type, nation)

    elif nav_opt == 'timeseries-source' :

        # TIME SERIES BY SOURCE

        return figures.timeseries_source(source, fuel_type, nation)

    else :

        # If you're going somewhere else, just keep the same figure.

        return dash.no_update
