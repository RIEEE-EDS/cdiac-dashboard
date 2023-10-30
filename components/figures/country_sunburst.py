"""
Module/Script Name: country_sunburst.py
Author: M. W. Hefner

Created: 4/12/2023
Last Modified: 10/30/2023

Project: CDIAC at AppState

Script Description: This script defines the country-view plotly figure.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.graph_objects as go
import datetime
import plotly.io as pio
from components.utils import constants as d

def country_sunburst(nation, fuel_type, theme):

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    # Take only the columns we want for the starburst chart
    columns_to_keep = [
        "Energy Supply Total",
        "Energy Consumption Total",
        "Statistical Difference (Sup-Con)",
        "Electric, CHP, Heat Plants",
        "Energy Industries' Own Use",
        "Manufact, Constr, Non-Fuel Industry",
        "Transport",
        "Household",
        "Agriculture, Forestry, Fishing",
        "Commerce and Public Services",
        "NES Other Consumption",
    ]

    if fuel_type == 'solids':

        df = d.df_solid

        plot_subtitle = str(datetime.date.today().year - 3) +" CO₂ Emissions from the Energy Use of Solid Fuels"

    elif fuel_type == 'liquids':

        df = d.df_liquid

        plot_subtitle = str(datetime.date.today().year - 3) +" CO₂ Emissions from the Energy Use of Liquid Fuels"

    elif fuel_type == 'gases':

        df = d.df_gas

        plot_subtitle = str(datetime.date.today().year - 3) +" CO₂ Emissions from the Energy Use of Gas Fuels"

    else :

        plot_subtitle = str(datetime.date.today().year - 3) +" CO₂ Emissions"

        df = d.df_total

        columns_to_keep = [
            "Fossil Fuel and Cement Production",
            "Energy Consumption Total",
            "Statistical Difference (Sup-Con)",
            "Manufacture of Cement",
            "Electric, CHP, Heat Plants",
            "Energy Industries' Own Use",
            "Manufact, Constr, Non-Fuel Industry",
            "Transport",
            "Household",
            "Agriculture, Forestry, Fishing",
            "Commerce and Public Services",
            "NES Other Consumption",
            
            "Bunkered",
            "Bunkered (Marine)",
            "Bunkered (Aviation)",
            "Flaring of Natural Gas",
        ]

    # Filter the data frame for the right data
    df = df[df['Nation'] == nation]
    df = df[df['Year'] == 2019]

    df = df[columns_to_keep]

    df.fillna(0, inplace=True)

    # Debug
    dfl = df.values.tolist()[0]

    if dfl[2] > 0 :
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
    else:
        dfl[0] = dfl[3] + dfl[1]

        dfl[2] = dfl[2] * -1

        sunburst_parents = [
            "",
            "Total",
            "Electric, CHP, Heat Plants",
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

            line=dict(color=textCol, width=0) 
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
                color = textCol,
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
                y=0,
                xref='paper',
                yref='paper',
                text='The CDIAC at AppState Dashboard (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                
                font = dict(
                    size=20,
                    color = textCol
                )
            )
        ]

    )
    
    return fig