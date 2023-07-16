"""
Module/Script Name: figures.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the interactive plotly figures used in this application.

Callback methods: 0

"""

# Import needed libraries
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
import plotly.io as pio
from components.staticdata import data as d


# Time Series by Country
def timeseries_country(fuel_type, nation) :

    pio.templates.default = "plotly_white"

    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    df = df[df['Nation'] == nation]

    df = pd.melt(
        df, 
        id_vars=['Nation', 'Year'], 
        var_name='Source', 
        value_name='Carbon'
    )

    fig = px.line(df, x='Year', y = 'Carbon', color = 'Source', 
                  color_discrete_sequence=px.colors.qualitative.Alphabet)

    fig.update_layout(

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        title = nation,

        title_font_color="black",  # Set the font color of the title

        font=dict(

            size=15  # Set the font size for the entire plot, excluding the title

        ),

        title_x=0.5,  # Set the horizontal alignment of the title (0-1)

        title_y=0.95,  # Set the vertical alignment of the title (0-1)

        title_xanchor="center",  # Set the horizontal anchor point of the title

        title_yanchor="top",  # Set the vertical anchor point of the title

        )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=1,
        y=1,
        xref='paper',
        yref='paper',
        text='CDIAC at AppState, ' + str(datetime.date.today().year),
        showarrow=False,

        font = dict(
            size=15
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])
    
    return fig


# Time Series by Source
def timeseries_source(source, fuel_type, nation) :

    pio.templates.default = "plotly_white"

    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    df = df[df['Nation'].isin(nation)]

    fig = px.line(df, x='Year', y = source, color = 'Nation', 
                  color_discrete_sequence=px.colors.qualitative.Light24_r)

    fig.update_layout(

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title="CO₂ Emissions (kilotonnes C)",

        title = source,

        legend_title = "Source",

        title_font_color="black",  # Set the font color of the title

        font=dict(

            size=15  # Set the font size for the entire plot, excluding the title

        ),

        title_x=0.5,  # Set the horizontal alignment of the title (0-1)

        title_y=0.95,  # Set the vertical alignment of the title (0-1)

        title_xanchor="center",  # Set the horizontal anchor point of the title

        title_yanchor="top",  # Set the vertical anchor point of the title

        )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=1,
        y=1,
        xref='paper',
        yref='paper',
        text='CDIAC at AppState, ' + str(datetime.date.today().year),
        showarrow=False,

        font = dict(
            size=15
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])

    return fig