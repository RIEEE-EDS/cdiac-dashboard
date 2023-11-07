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

def country_timeseries(fuel_type, political_geography, theme):
    
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
    df = df[df['Political Geography'] == political_geography]

    # Save a pre-melt for variables you do not want to stack
    premelt_df = df

    # melt for variables you wish to stack
    df = pd.melt(
        df, 
        id_vars=['Political Geography', 'Year'], 
        var_name='Source', 
        value_name='Carbon'
    )

    custom_order = [
        "Political Geography", 
        "Year", 

        "Electric, CHP, Heat Plants", 
        "Energy Industries' Own Use", 
        "Manufact, Constr, Non-Fuel Industry", 
        #"Transport", 
        "Road Transport", 
        "Rail Transport", 
        "Domestic Aviation", 
        "Domestic Navigation", 
        "Other Transport",
        "Household", 
        "Agriculture, Forestry, Fishing", 
        #"Public Lighting", 
        "Commerce and Public Services", 
        "NES Other Consumption", 
        #"Bunkered", 
        # Only for Totals
        "Flaring of Natural Gas", 
        "Bunkered (Marine)", 
        "Bunkered (Aviation)", 
        "Manufacture of Cement", 
    ]

    # Filter and keep only the sources you want to stack
    df = df[df['Source'].isin(custom_order) & (df.groupby('Source')['Carbon'].transform('any'))]

    # Make stacked area plot
    fig = px.area(
        df, 
        x ='Year', 
        y = 'Carbon', 
        color = 'Source', 
        color_discrete_sequence = px.colors.qualitative.Light24,
        template="plotly_dark",
        category_orders={'Source': custom_order},  # Specify the custom order
        hover_data={'Year' : False, 'Political Geography' : False},
    )

    fig.update_traces(mode="none")

    if (fuel_type == 'totals') :

        # Add Sectoral Consumption (Should stack to the same height... make dashed)
        fig.add_trace(
            go.Scatter(
                    x=premelt_df['Year'],  # X-axis: Year
                    y=premelt_df["Fossil Fuel Energy and Cement Manufacture"],  # Y-axis: Nitrogen
                    mode='lines',  # Display as a line plot
                    name="Fossil Fuel Energy and Cement Manufacture",  # Legend label
                    line=dict(color='red', dash='dash'),  # Line color
                )
        )

    # Add Reference approach
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Fossil Fuel Energy (Supplied)"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Fossil Fuel Energy (Supplied)",  # Legend label
                line=dict(color='blue', dash='dot'),  # Line color
            )
    )

    # Add sectoral total
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Fossil Fuel Energy (Consumed)"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Fossil Fuel Energy (Consumed)",  # Legend label
                line=dict(color='blue', dash='dash'),  # Line color
            )
    )

    # Add Statistical Difference "Statistical Difference (Sup-Con)",
    # Add Reference approach
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Stat Difference (Supplied - Consumed)"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Statistical Difference (Sup-Con)",  # Legend label
                line=dict(color='yellow', dash='longdashdot'),  # Line color
            )
    )

    # Figure out what the plot title will be
    if fuel_type == 'solids':
        plot_title = political_geography + " CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>SOLID</b> FOSSIL FUELS"
    elif fuel_type == 'liquids':
        plot_title = political_geography + " CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>LIQUID</b> FOSSIL FUELS"
    elif fuel_type == 'gases':
        plot_title = political_geography + " CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>GASEOUS</b> FOSSIL FUELS"
    else :
        plot_title = political_geography + " CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF FOSSIL FUELS AND CEMENT MANUFACTURE"

    # Updates the figure layout
    fig.update_layout(

        plot_bgcolor = 'rgba(0,0,0,0)',
        
        paper_bgcolor = 'rgba(0,0,0,0)',

        margin={'l': 0, 'r': 0, 't': 100, 'b': 100},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=20, 
            color = textCol  
        ),

        # Title Layout and Styling
        title = dict(
            text = plot_title,
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
                font=dict(size=20, color=textCol)
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

    fig.update_layout(
        hovermode="x",
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"
        )
    )
    
    return fig
    