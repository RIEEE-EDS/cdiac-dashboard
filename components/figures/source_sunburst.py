"""
Module/Script Name: country_sunburst.py
Author: M. W. Hefner

Created: 9/15/2023
Last Modified: 9/15/2023

Project: CDIAC at AppState

Script Description: This script defines a source-view plotly figure.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime
import plotly.io as pio
from components.utils import constants as d

def source_sunburst(source, fuel_type, theme):

    pio.templates.default = "plotly_white"

    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    # Debug
    df = df[['Nation', source]]
    print(df[['Nation', source]])

    sunburst_parents = [
        "",
        "Total",
        "Total",
        "Total",
        "Consumption",
        "Consumption",
        "Consumption",
        "Consumption",
        "Consumption",
        "Consumption",
        "Consumption",
        "Consumption",

        "Consumption",
        "Bunkered",
        "Bunkered",
        "Consumption",
    ]

    fig = go.Figure(go.Sunburst(

        labels = [
            "Total",
            "Consumption",
            "Statistical Difference",
            "Cement",
            "Electric, CHP, Heat Plants",
            "Energy Industries' Own Use",
            "Manufact, Constr, Non-Fuel Industry",
            "Transport",
            "Household",
            "Agriculture, Forestry, Fishing",
            "Commerce and Public Services",
            "NES Other Consumption",
            
            "Bunkered",
            "Marine",
            "Aviation",
            "Flared Natural Gas",
        ],

        parents = sunburst_parents,

        values=dfl,

        branchvalues="total",

        insidetextorientation='horizontal',

        marker=dict(
            colors=[
                '#a6cee3',
                '#1f78b4',
                '#ffff00',
                "#bbbbbb",
                '#fb9a99',
                '#ff7f00',
                '#fdbf6f',
                '#e31a1c',
                '#cab2d6',
                '#33a02c',
                '#ffff99',
                '#b15928',

                "#888888",
                "#999999",
                "#aaaaaa",
                '#6a3d9a',
            ],

            line=dict(color=textCol, width=3) 
        )
    ))

    fig.update_layout(

        #uniformtext=dict(minsize=20, mode='hide'),

        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=28, 
        ),

        # Title Layout and Styling
        title = dict(
            text = nation,
            xanchor="center",
            xref = "container",
            yref = "container",
            x = 0.5,
            yanchor="top",
            y = .98,
            font = dict(
                size = 32,
            )
        ),

    )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=0.5,
        y=0,
        xref='paper',
        yref='paper',
        text='Source: CDIAC at AppState Dashboard | Hefner, M; Marland, G (' + str(datetime.date.today().year) + ')',
        showarrow=False,
        
        font = dict(
            size=20,
            color = textCol
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])
    
    return fig