"""
This module defines the display container for the CDIAC Dashboard application,
managing the dynamic display of content based on user interactions. It integrates
Plotly graphs, markdown documents, and other interactive elements into the user interface.

Functions
---------
update_container(nav_opt, theme, source, fuel_type, nation, source_a, source_b, grouping)
    Updates the content of the display container based on user-selected navigation options,
    applying filters and themes to dynamically generate and display content.

Attributes
----------
layout : dash.html.Div
    The primary HTML container that holds the content being displayed, identified by a unique component ID.

component_id : str
    The identifier for the display container, used for targeting with callbacks and styling.

config : dict
    Configuration settings for Plotly graphs, detailing aspects like interaction options and image export settings.

sunburst_config : dict
    Special configuration for sunburst graphs to adjust visual settings and interaction behaviors.

See Also
--------
components.figures.* : Modules that generate specific Plotly graphs for the dashboard.
components.tables.browse : Module handling the data table display within the dashboard.

Notes
-----
This module plays a critical role in rendering the visual and textual content of the dashboard.
It responds to user inputs from various controls and toggles, updating the display in real time.

Examples
--------
The layout is a simple container that gets populated dynamically based on callbacks:

>>> layout = dash.html.Div(id=component_id)

Content updates are managed by a callback function that renders different components based on
navigation options selected by the user:

>>> @dash.callback(
        dash.dependencies.Output(component_id, 'children'),
        [dash.dependencies.Input('navigation-dropdown-controler', 'value')]
    )
    def update_container(nav_opt):
        # Content updating logic goes here
        pass

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
    """
    Dynamically updates the content within the display container based on user interactions
    with the dashboard's navigation controls.

    Parameters
    ----------
    nav_opt : str
        The navigation option selected by the user, which determines the type of content
        to be displayed (e.g., "about", "methodology", "download", or various data visualizations).
    theme : str
        The current theme setting (e.g., "light" or "dark") which affects the styling of
        the plotly content.
    source : str
        Selected data source filter for generating specific plots.
    fuel_type : str
        Selected fuel type filter for generating specific plots.
    nation : str
        Selected nation filter for generating specific plots involving geographic data.
    source_a : str
        Selected first source filter for ternary plot comparisons.
    source_b : str
        Selected second source filter for ternary plot comparisons.
    grouping : str
        Selected grouping option for plots that aggregate data by certain categories.

    Returns
    -------
    list of dash.development.base_component.Component
        A list containing Dash components to be rendered in the display container. This can
        include Plotly graphs, Markdown content, or other interactive elements depending on
        the navigation option selected.

    Notes
    -----
    The function leverages conditional logic to determine the appropriate content to render.
    Depending on the 'nav_opt', different functions from the figures and tables modules are
    called to generate the content. Styling and specific configurations are applied to ensure
    the content aligns with the selected theme and user preferences.

    Examples
    --------
    >>> update_container("about", "light", None, None, None, None, None, None)
    Returns a Markdown component displaying the about page content with light theme styling.
    """

    
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
