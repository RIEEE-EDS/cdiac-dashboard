"""
Module/Script Name: content_display.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 2

"""

# Import Dependencies
import dash
from components.staticdata import data as d
from components.content_display import figures

# STYLES (JSON CSS)

styles = {
    'content': {
        'order' : '2',
        'width' : '100%',
        'padding': '20px',
        'overflow-y' : 'auto'
    }
}

# LAYOUT

layout = dash.html.Div(
            
    className='content',

    style=styles['content'],
    
    id = "content_display",

    children=[

        dash.dcc.Graph(id='map-graph', style = {'height' :  '100%'})

    ]
)

# CALLBACKS (2)
@dash.callback(
    dash.dependencies.Output('content_display', 'children'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('source-dropdown-controler', 'value'),
)
def update_container(nav_opt, fuel_type, source):

    if nav_opt == "about" :
        return [
            dash.dcc.Markdown(children = d.about_content, mathjax=True)
        ]
    elif nav_opt == "methodology" :
        return [
            dash.dcc.Markdown(children = d.methodology_content, mathjax=True)
        ]
    elif nav_opt == "download" :
        return [
            dash.dcc.Markdown(children = d.download_content, mathjax=True)
        ]
    elif nav_opt == "browse" :
        
        if fuel_type == 'solids':
            df = d.df_solid
        elif fuel_type == 'liquids':
            df = d.df_liquid
        elif fuel_type == 'gases':
            df = d.df_gas
        else :
            df = d.df_total

        df = df[df[source].notnull()]

        return [

            # TODO: This obviously needs to be moded out

            dash.html.Div([
                dash.html.P('Use the sidebar dropdowns to select data.  Filter and sort below.  Inequality filters (e.g. ">2005" for Year) are supported.', 
                    style = {'text-align' : 'center'}),
                dash.html.P('All values are in Thousand Metric Tons of Carbon (ktC)', 
                    style = {'text-align' : 'center'}),
                dash.dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in ["Nation", "Year", source]],
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    page_action="native",
                    page_current= 0,
                    page_size= 15,
                )
            ])
        ]
    else :
        return [
            dash.dcc.Graph(id='map-graph', style = {'height' :  '100%'})
        ]
    
# Updates the graph or map displayed in the content area's map-graph
@dash.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    dash.dependencies.Input('map-graph', 'figure'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('source-dropdown-controler', 'value'),
    dash.dependencies.Input('fuel-type-dropdown-controler', 'value'),
    dash.dependencies.Input('nation-dropdown-controler', 'value')
)
def update_map_or_graph(old_figue, nav_opt, source, fuel_type, nation):

    if nav_opt == 'carbon-atlas' :

        # CARBON ATLAS

        fig = figures.carbon_atlas(source, fuel_type)

    elif nav_opt == 'timeseries-country' :

        # TIME SERIES BY COUNTRY

        fig = figures.timeseries_country(fuel_type, nation)

    elif nav_opt == 'timeseries-source' :

        # TIME SERIES BY SOURCE

        fig = figures.timeseries_source(source, fuel_type, nation)

    else :

        # If you're going somewhere else, just keep the same figure.

        fig = old_figue 
    
    
    return fig