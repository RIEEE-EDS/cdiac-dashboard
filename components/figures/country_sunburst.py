"""
This module creates a dynamic sunburst chart visualizing the distribution of CO₂ emissions by different sectors
within a selected country, adjusted by the fuel type and displayed over a range of years.

Functions
---------
build_country_sunburst(nation, fuel_type, bg, year)
    Constructs the data structure necessary for a single snapshot of the sunburst chart,
    representing CO₂ emissions for a given year and country.

country_sunburst(nation, fuel_type, theme)
    Generates a complete sunburst chart with animation over multiple years, showing changes
    in CO₂ emissions distribution within a country.

Parameters
----------
nation : str
    The country for which the data will be visualized.
fuel_type : str
    The type of fuel (solids, liquids, gases, or total) to visualize emissions from.
bg : str
    Background color for the chart, derived from the theme.
year : int
    The year for which the data snapshot is to be visualized.
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the sunburst chart.

Returns
-------
plotly.graph_objects.Figure
    A Plotly Figure object that represents the animated sunburst chart, ready for integration
    into a web interface.

Examples
--------
To generate an animated sunburst chart for CO₂ emissions from solid fuels in the USA with a dark theme:

>>> fig = country_sunburst('USA', 'solids', 'dark')
>>> fig.show()

Notes
-----
The chart integrates complex hierarchical data that spans multiple sectors and fuel types,
providing an insightful visualization of how CO₂ emissions are distributed across different
economic activities within a country. The function dynamically adjusts colors, animations, and
data visibility based on the user-selected theme and fuel type.

See Also
--------
plotly.graph_objects : Used for constructing the sunburst chart.
datetime : Used to handle year annotations within the chart.
components.utils.constants : Provides access to global constants and data used in the visualization.
"""


# Import needed libraries
import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd
from components.utils import constants as d

def build_country_sunburst(nation, fuel_type, bg, year):

    # Take only the columns we want for the starburst chart
    columns_to_keep = [
        # "Fossil Fuel Energy and Cement Manufacture" # If Totals and SD >=0
        #                                             (step 3. insert at i=0)
        # "Fossil Fuel Energy (Supplied)",            # SD >=0 (step 2. insert at i=0)
        "Fossil Fuel Energy (Consumed)",
        # "Stat Difference (Supplied - Consumed)",    # SD >=0 (step 1. insert at i=1)
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
        # If we're looking at the world, bunkered is a child of consumption
        sunburst_parents.append("Fossil Fuel<br>Energy Use<br>(Consumed)")
        sunburst_parents.append("Bunkered")
        sunburst_parents.append("Bunkered")
    else :
        # otherwise it is just sep
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
        bg,
        
        "#6E2405", 
        "#FF9966", 
        "#B07E09",

        bg, # Transport
        
        "#FEC77C", 
        "#855914", 
        "#29AAE2", 
        "#F27AAA", 
        "#EC008C", 

        "#FDB913", 
        "#7E8959", 
        "#B25538", 
        "#662F90", 

        bg, # Bunkered
        "#0D71BA", 
        "#C1272D",
    ]

    # Set Data, Title, and Subtitle
    if fuel_type == 'solids':

        df = d.df_solid

        plot_title = nation + " <b>SOLID</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    elif fuel_type == 'liquids':

        df = d.df_liquid

        plot_title = nation + " <b>LIQUID</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    elif fuel_type == 'gases':

        df = d.df_gas

        plot_title = nation + " <b>GAS</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    else :

        plot_title = nation + " CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

        df = d.df_total

        columns_to_keep.append("Flaring of Natural Gas")
        columns_to_keep.append("Manufacture of Cement")
        sunburst_labels.append("Flaring of<br>Natural Gas")
        sunburst_labels.append("Cement<br>Manufact")
        sunburst_parents.append("Fossil Fuel<br>Energy Use<br>(Consumed)")
        sunburst_parents.append("")
        sunburst_colors.append("#3BB54A")
        sunburst_colors.append("#B0A690")

    # Filter the data frame for the right data
    df = df[df['Political Geography'] == nation]
    df = df[df['Year'] == year]

    # TODO: Later, include statistical difference here

    # stat_diff = df['Stat Difference (Supplied - Consumed)'].iloc[0]

    # if stat_diff >= 0 :

    df = df[columns_to_keep]

    # Replace zeros with NAs so it doesn't show sectors with 0
    df.replace(0, np.nan, inplace=True)

    # Transpose the DataFrame to get the values
    transposed_df = df.T

    # Reset the index to make the column names as a separate column
    transposed_df = transposed_df.reset_index()

    # Rename the columns to meaningful names if needed
    transposed_df.columns = ['Column_Name', 'Values']

    sunburst = pd.DataFrame()

    sunburst["labels"] = sunburst_labels
    sunburst["parents"] = sunburst_parents
    sunburst["values"] = transposed_df['Values']
    sunburst["colors"] = sunburst_colors
    sunburst["year"] = year

    return sunburst, plot_title, plot_subtitle

def country_sunburst(nation, fuel_type, theme):

    if theme == 'light' :
        textCol = '#000'
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'
    # Define years for the animation
    years = list(range(1995, 2021))

    # Initialize the figure with subplots
    fig = go.Figure()

    # Setup the initial sunburst chart for the first year
    sunburst, plot_title, plot_subtitle = build_country_sunburst(nation, fuel_type, bg, years[-1])

    fig.add_trace(go.Sunburst(
        labels=sunburst["labels"],
        parents=sunburst["parents"],
        values=sunburst["values"],
        branchvalues="total",
        insidetextorientation='horizontal',
        marker=dict(colors=sunburst["colors"], line=dict(color=textCol, width=0.5))
    ))

    if d.show_credit :
        annotations=[
            # Credit
            dict(
                x=0.01,
                y=0,
                xref='paper',
                yref='paper',
                xanchor="left",
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
        ]

    fig.update_layout(

        #uniformtext=dict(minsize=20, mode='hide'),

        plot_bgcolor=bg,
        paper_bgcolor=bg,

        margin={'l': 0, 'r': 0, 't': 55, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=20, 
            color=textCol
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
                color = textCol,
            )
        ),

        annotations=annotations
    )
    # Create frames for each year
    frames = []
    for year in years:
        sunburst, _, _ = build_country_sunburst(nation, fuel_type, bg, year)
        frame = go.Frame(
            data=[go.Sunburst(
                labels=sunburst["labels"],
                parents=sunburst["parents"],
                values=sunburst["values"],
                branchvalues="total",
                insidetextorientation='horizontal',
                marker=dict(colors=sunburst["colors"], line=dict(color=textCol, width=0.5))
            )],
            name=str(year)
        )
        frames.append(frame)

    fig.frames = frames

    # Add a play button and a slider for the animation
    fig.update_layout(
        updatemenus = [{ 
            'type': 'buttons',
            'direction': 'left',
            'x': 0.99,
            'y': 0,  # Position of the play button
            'xanchor': 'right',
            'yanchor': 'bottom',
            'showactive': False,
            'buttons': [{
                'label': '<br> Play Animation <br>',
                'method': 'animate',
                'args': [None, {'frame': {'duration': 600, 'redraw': True}, 'fromcurrent': True}]
            }]
        }],
        sliders = [{
            'active': years.index(years[-1]),
            'yanchor': 'top',
            'xanchor': 'center',
            'currentvalue': {
                'prefix': 'Year: ',
                'visible': True,
                'xanchor': 'center',
            },
            'transition': {'duration': 500},
            'pad': {'b': 10, 't': 10},
            'len': 0.5,
            'x': 0.5,
            'y': 0,
            'steps': [{'method': 'animate', 
                'args': [[str(year)], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}],
                'label': str(year)} for year in years]  # Label only for even years
        }]
    )

    fig.update_traces(textfont=dict(color=textCol))
    
    return fig
