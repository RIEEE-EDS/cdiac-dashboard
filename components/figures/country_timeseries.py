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
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'

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
        "Domestic Navigation", 
        "Domestic Aviation", 
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

    custom_color_map = {
        "Electric, CHP, Heat Plants" : "#6E2405", 
        "Energy Industries' Own Use" : "#FF9966", 
        "Manufact, Constr, Non-Fuel Industry" : "#B07E09", 
        "Road Transport" : "#FEC77C", 
        "Rail Transport" : "#855914", 
        "Domestic Aviation" : "#F27AAA", 
        "Domestic Navigation" : "#29AAE2", 
        "Other Transport" : "#EC008C", 
        "Household" : "#FDB913", 
        "Agriculture, Forestry, Fishing" : "#7E8959", 
        "Commerce and Public Services" : "#B25538", 
        "NES Other Consumption" : "#662F90", 
        "Flaring of Natural Gas" : "#3BB54A", 
        "Bunkered (Marine)" : "#0D71BA", 
        "Bunkered (Aviation)" : "#C1272D", 
        "Manufacture of Cement" : "#B0A690",  
    }

    # Filter and keep only the sources you want to stack
    df = df[df['Source'].isin(custom_order) & (df.groupby('Source')['Carbon'].transform('any'))]

    # Make stacked area plot
    fig = px.area(
        df, 
        x ='Year', 
        y = 'Carbon', 
        color = 'Source', 
        #color_discrete_sequence=px.colors.qualitative.Alphabet,
        color_discrete_map=custom_color_map,
        template="plotly_dark",
        hover_data={'Year' : False, 'Political Geography' : False},
    )

    #fig.update_traces(mode="none")

    fig.update_traces(mode="lines",line=dict(width=0))

    # Add Statistical Difference "Statistical Difference (Sup-Con)",
    fig.add_trace(
        go.Scatter(
                x=premelt_df['Year'],  # X-axis: Year
                y=premelt_df["Stat Difference (Supplied - Consumed)"],  # Y-axis: Nitrogen
                mode='lines',  # Display as a line plot
                name="Statistical Difference (Sup-Con)",  # Legend label
                line=dict(color='orange', dash='longdashdot'),  # Line color
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



    # Figure out what the plot title will be
    if fuel_type == 'solids':
        plot_title = political_geography + " <b>SOLID</b> FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE"
    elif fuel_type == 'liquids':
        plot_title = political_geography + " <b>LIQUID</b> FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE"
    elif fuel_type == 'gases':
        plot_title = political_geography + " <b>GAS</b> FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE"
    else :
        plot_title = political_geography + " CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF FOSSIL FUELS AND CEMENT MANUFACTURE"

    if d.show_credit :
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
                x=0,
                y=-0.05,
                xref='paper',
                yref='paper',
                xanchor="left",
                yanchor="top",
                text='<b>The CDIAC at AppState Dashboard</b><br>Hefner and Marland (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                align="left",
                
                font = dict(
                    size=20,
                    color = textCol
                )
            ),
        ]
    else :
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
        ]

    # Updates the figure layout
    fig.update_layout(

        legend={'traceorder': 'reversed'},

        plot_bgcolor=bg,
        paper_bgcolor=bg,

        margin={'l': 0, 'r': 0, 't': 100, 'b': 100},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # everyone knows what a year is
        xaxis_title = "",

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
        annotations=annotations
    )

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"
        )
    )
    
    return fig
    