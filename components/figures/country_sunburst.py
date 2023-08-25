"""
Module/Script Name: country_sunburst.py
Author: M. W. Hefner

Created: 4/12/2023
Last Modified: 7/16/2023

Project: CDIAC at AppState

Script Description: This script defines the country-view plotly figure.

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

def country_sunburst(nation, theme):

    pio.templates.default = "plotly_white"

    # Select Color Scale depending on fuel type and theme
    df = d.df_total

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    df = df[df['Nation'] == nation]
    df = df[df['Year'] == 2020]
    df = df.values.tolist()[0][2:-1]

    #print(d.df_total.columns[2:-1])
    #print(df)

    fig = go.Figure(go.Sunburst(

        labels = d.df_total.columns[2:-1],

        parents = [
            "",
            "Total CO₂ Emissions from Fossil-Fuels and Cement Production",

            "Energy Use of Fossil Fuels",
            "Energy Use of Fossil Fuels",

            "Energy Use of Fossil Fuels",

            "Total Non-Energy-Industry Fossil Fuel Consumption",
            "Total Non-Energy-Industry Fossil Fuel Consumption",
            "Total Non-Energy-Industry Fossil Fuel Consumption",
            "Total Non-Energy-Industry Fossil Fuel Consumption",
            "Total Non-Energy-Industry Fossil Fuel Consumption",
            "Total Non-Energy-Industry Fossil Fuel Consumption",

            "Total CO₂ Emissions from Fossil-Fuels and Cement Production",

            "Total CO₂ Emissions from Fossil-Fuels and Cement Production",
            "Total Bunkered Fossil Fuels",
            "Total Bunkered Fossil Fuels",
            
            "Total CO₂ Emissions from Fossil-Fuels and Cement Production",
            "Total CO₂ Emissions from Fossil-Fuels and Cement Production"
        ],

        values=df,

        branchvalues="total"

    ))

    fig.update_layout(

        uniformtext=dict(minsize=10, mode='hide'),

        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=20, 
            color = textCol  
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
                color = textCol
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