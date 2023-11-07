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
        "Fossil Fuel Energy (Consumed)",
        "Electric, CHP, Heat Plants",
        "Energy Industries' Own Use",
        "Manufact, Constr, Non-Fuel Industry",
        "Transport",

        "Road Transport",
        "Rail Transport",
        "Domestic Aviation",
        "Domestic Navigation",
        "Other Transport",

        "Household",
        "Agriculture, Forestry, Fishing",
        "Commerce and Public Services",
        "NES Other Consumption",
        "Bunkered",
        "Bunkered (Marine)",
        "Bunkered (Aviation)",

    ]

    sunburst_parents = [
        "",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",

        "Transport",
        "Transport",
        "Transport",
        "Transport",
        "Transport",

        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
    ]

    if nation == "WORLD" :
        sunburst_parents.append("Fossil Fuel<br>Energy Use<br>(Consumed)")
        sunburst_parents.append("Bunkered")
        sunburst_parents.append("Bunkered")
    else :
        sunburst_parents.append("")
        sunburst_parents.append("Bunkered")
        sunburst_parents.append("Bunkered")

    sunburst_labels = [
        "Fossil Fuel<br>Energy Use<br>(Consumed)",
        "Electric, CHP,<br>Heat Plants",
        "Energy<br>Industries'<br>Own Use",
        "Manufact,<br>Constr,<br>Non-Fuel<br>Industry",
        "Transport",

        "Road<br>Transport",
        "Rail<br>Transport",
        "Domestic<br>Aviation",
        "Domestic<br>Navigation",
        "Other<br>Transport",

        "Household",
        "Agriculture,<br>Forestry,<br>Fishing",
        "Commerce and<br>Public Services",
        "NES Other<br>Consumption",
        "Bunkered",
        "Marine",
        "Aviation",

    ]
    
    sunburst_colors=[
        "rgba(0,0,0,0)",
        
        "#FF5733", 
        "#FFD700", 
        "#8A2BE2",

        "rgba(0,0,0,0)", # Transport
        
        "#00FFFF", 
        "#008000", 
        "#FF4500", 
        "#000080", 
        "#800080", 

        "#FFFF00", 
        "#228B22", 
        "#FF69B4", 
        "#FFA07A", 

        "rgba(0,0,0,0)", # Bunkered
        "#0000FF", 
        "#8B0000",

        "#A52A2A", 
        "#D2691E"]

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

        columns_to_keep.append("Flaring of Natural Gas")
        columns_to_keep.append("Manufacture of Cement")
        sunburst_labels.append("Flaring of<br>Natural Gas")
        sunburst_labels.append("Cement<br>Manufact")
        sunburst_parents.append("Fossil Fuel<br>Energy Use<br>(Consumed)")
        sunburst_parents.append("")

    # Filter the data frame for the right data
    df = df[df['Political Geography'] == nation]
    df = df[df['Year'] == 2020]

    df = df[columns_to_keep]

    df.fillna(0, inplace=True)

    # Debug
    dfl = df.values.tolist()[0]

    print(df)

    fig = go.Figure(go.Sunburst(

        labels = sunburst_labels,

        parents = sunburst_parents,

        values=dfl,

        branchvalues="total",

        insidetextorientation='horizontal',

        marker=dict(
            colors=sunburst_colors,

            line=dict(color=textCol, width=2) 
        ),

    ))

    fig.update_layout(

        #uniformtext=dict(minsize=20, mode='hide'),

        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=16, 
            color=textCol
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