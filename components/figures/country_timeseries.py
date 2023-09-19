"""
Module/Script Name: country_timeseries.py
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
import pandas as pd
import datetime
import plotly.io as pio
from components.utils import constants as d
import plotly.graph_objects as go

def country_timeseries(fuel_type, nation, theme):

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

    # Filter to proper political geography
    df = df[df['Nation'] == nation]

    # Save a pre-melt for variables you do not want to stack
    premelt_df = df

    # melt for variables you wish to stack
    df = pd.melt(
        df, 
        id_vars=['Nation', 'Year'], 
        var_name='Source', 
        value_name='Carbon'
    )

    # Filter and keep only the sources you want to stack
    df = df[df['Source'].isin([
        "Nation", 
        "Year", 

        "Electric, CHP, Heat Plants",

        "Energy Industries' Own Use",

        # Subsectors

        "Manufact, Constr, Non-Fuel Industry",

        # Subsectors

        "Transport",

        # Subsectors

        "Household",
        "Agriculture, Forestry, Fishing",
        "Commerce and Public Services",
        "NES Other Consumption",
        "Non-Energy Use",]
    )]

    # Make stacked area plot
    fig = px.area(
        df, 
        x ='Year', 
        y = 'Carbon', 
        color = 'Source', 
        color_discrete_sequence = px.colors.qualitative.Alphabet
    )

    # Add Sectoral Consumption (Should stack to the same height... make dashed)
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Sectoral (Consumption) Total"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Sectoral (Consumption) Total",  # Legend label
                line=dict(color='red', dash='dash'),  # Line color
            )
    )

    # Add Reference approach
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Reference (Supply) Total"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Reference (Supply) Total",  # Legend label
                line=dict(color='blue', dash='dot'),  # Line color
            )
    )

    fig.update_layout(

        plot_bgcolor = 'rgba(0,0,0,0)',
        
        paper_bgcolor = 'rgba(0,0,0,0)',

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