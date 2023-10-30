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

    reverse = True

    plot_title = "CO₂ Emissions: " + source
    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid
        plot_subtitle = "From the Energy Use of Solid Fuels"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        plot_subtitle = "From the Energy Use of Liquid Fuels"
    elif fuel_type == 'gases':
        df = d.df_gas
        plot_subtitle = "From the Energy Use of Gas Fuels"
    else :
        reverse = False
        hover_data = {'Year' : False, 'Year' : False, 'Fossil Fuel and Cement Production' : False, 'Energy Supply Total' : False, 'Energy Consumption Total' : False, 'Statistical Difference (Sup-Con)' : False, 'Electric, CHP, Heat Plants' : False, "Energy Industries' Own Use" : False, 'Manufact, Constr, Non-Fuel Industry' : False, 'Transport' : False, 'Household' : False, 'Agriculture, Forestry, Fishing' : False, 'Commerce and Public Services' : False, 'NES Other Consumption' : False, 'Non-Energy Use' : False, 'Bunkered' : False, 'Bunkered (Marine)' : False, 'Bunkered (Aviation)' : False, 'Flaring of Natural Gas' : False, 'Manufacture of Cement' : False, 'Per Capita Total Emissions' : False}
        df = d.df_total
        plot_subtitle = ""

    if (reverse) :
        hover_data = {'Year' : False, 'Year' : False, 'Energy Supply Total' : False, 'Energy Consumption Total' : False, 'Statistical Difference (Sup-Con)' : False, 'Electric, CHP, Heat Plants' : False, "Energy Industries' Own Use" : False, 'Manufact, Constr, Non-Fuel Industry' : False, 'Transport' : False, 'Household' : False, 'Agriculture, Forestry, Fishing' : False, 'Commerce and Public Services' : False, 'NES Other Consumption' : False, 'Non-Energy Use' : False,}

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    df = df[df['Nation'].isin(nation)]

    df = df.copy()

    df.rename(columns={'Nation': 'Political Geography'}, inplace=True)

    fig = px.line(df, x='Year', y = source, color = 'Political Geography',
                  color_discrete_sequence=px.colors.qualitative.Light24_r,         hover_data=hover_data,)


    fig.update_layout(

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
    

    fig.update_traces(mode="markers+lines")

    fig.update_layout(
        hovermode="x",
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"
        )
    )
    
    return fig