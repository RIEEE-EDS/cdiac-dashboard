"""
Module/Script Name: source_timeseries.py
Author: M. W. Hefner

Created: 4/12/2023
Last Modified: 10/30/2023

Project: CDIAC at AppState

Script Description: This script defines the source-view plotly figure.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.express as px
import datetime
import plotly.io as pio
from components.utils import constants as d

def source_timeseries(source, fuel_type, nation, theme):

    pio.templates.default = "plotly_white"

    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid
        plot_title = source + " SOLID CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>SOLID</b> FOSSIL FUELS"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        plot_title = source + " LIQUID FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>LIQUID</b> FOSSIL FUELS"
    elif fuel_type == 'gases':
        df = d.df_gas
        plot_title = source + " GAS FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>GASEOUS</b> FOSSIL FUELS"
    else :
        df = d.df_total
        plot_title = source + " TOTAL CO₂ EMISSIONS"
        plot_subtitle = ""

    if theme == 'light' :
        textCol = '#000'
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'

    df = df[df['Political Geography'].isin(nation)]

    df = df.copy()

    fig = px.line(df, x='Year', y = source, color = 'Political Geography',
                  color_discrete_sequence=px.colors.qualitative.Light24_r,         
                  hover_data={'Political Geography' : True, 'Year' : False},)


    fig.update_layout(

        plot_bgcolor=bg,
        paper_bgcolor=bg,

        margin={'l': 0, 'r': 0, 't': 100, 'b': 100},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=20, 
            color = textCol  
        ),

        # Title Layout and Styling
        title = dict(
            text = plot_title.upper(),
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

        # Subtitle
        annotations=[
            # Subtitle
            dict(
                text= plot_subtitle,
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.04,
                font=dict(size=18, color=textCol)
            ),

            # Credit
            dict(
                x=0.5,
                y=-0.10,
                xref='paper',
                yref='paper',
                xanchor = 'center',
                yanchor = 'top',
                text='The CDIAC at AppState Dashboard (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                
                font = dict(
                    size=20,
                    color = textCol
                )
            )
        ]

    )
    
    fig.update_traces(mode="lines")

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"
        )
    )
    
    return fig