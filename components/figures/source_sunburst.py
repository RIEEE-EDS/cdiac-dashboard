"""
This module generates a sunburst chart visualizing CO₂ emissions by region and fuel type,
highlighting global distributions and emphasizing specific source contributions within a year.

Functions
---------
build_sunburst_data(source, fuel_type, year, bg)
    Prepares the necessary data structure for a single year sunburst visualization, including
    adjustments based on the fuel type and geographical aggregation.

source_sunburst(source, fuel_type, theme)
    Constructs a full sunburst chart animated over multiple years, reflecting changes in
    CO₂ emissions distribution worldwide according to a specified source and fuel type.

Parameters
----------
source : str
    The specific source of CO₂ emissions to visualize (e.g., "Total Emissions").
fuel_type : str
    The type of fuel (solids, liquids, gases, or total) to filter data by for the visualization.
year : int
    The year for which the data snapshot is to be visualized.
bg : str
    Background color for the chart, derived from the theme, influencing visibility and aesthetics.
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the sunburst chart.

Returns
-------
plotly.graph_objects.Figure
    A Plotly Figure object that represents the sunburst chart with animation capabilities,
    configured according to the specified parameters and ready for display.

Examples
--------
To generate a sunburst chart for total CO₂ emissions from solid fuels with a dark theme:

>>> fig = source_sunburst('Total Emissions', 'solids', 'dark')
>>> fig.show()

Notes
-----
The visualization is particularly effective in illustrating the contribution of different regions
to global CO₂ emissions, with interactive elements allowing users to explore trends over time.
The chart leverages detailed hierarchical data that connects regional emissions data to global
aggregates, providing an insightful visualization of how emissions are distributed across different
geopolitical regions.

The function dynamically adjusts colors, animations, and data visibility based on user-selected
theme and fuel type, incorporating detailed data preparation steps to ensure accurate and meaningful
visualizations.

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

def build_sunburst_data(source, fuel_type, year, bg) :
    # Assign Region Colors
    colormap = pd.DataFrame()

    colormap["REGION"] = ["NONE", "WORLD", "AFRICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "EUROPE"]
    colormap["COLOR"] = [bg, bg, "#46C6E7", "#616BB2", "#8B69AD", "#F9A05B", "#EF563C", "#F06591", "#41BB91"]

    # Set Data, Title, and Subtitle
    if fuel_type == 'solids':

        df = d.df_solid

        plot_title = source + " <b>SOLID</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    elif fuel_type == 'liquids':

        df = d.df_liquid

        plot_title = source + " <b>LIQUID</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    elif fuel_type == 'gases':

        df = d.df_gas

        plot_title = source + " <b>GAS</b> FUEL CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

    else :

        plot_title = source + " CO₂ EMISSIONS"

        plot_subtitle = "<b>" + str(year) +"</b>"

        df = d.df_total

    # Filter the DataFrame to include only rows where Year is year
    df = df[df['Year'] == year]

    world_bunkered = df.loc[df['Political Geography'] == "WORLD", "Bunkered"].values[0]
    world_bunkered_marine = df.loc[df['Political Geography'] == "WORLD", "Bunkered (Marine)"].values[0]
    world_bunkered_aviation = df.loc[df['Political Geography'] == "WORLD", "Bunkered (Aviation)"].values[0]

    # Replace zeros with NaN values using .loc
    df.loc[df['Year'] == year, source] = df.loc[df['Year'] == year, source].replace(0, np.nan)

    # Left join to get the 'REGION' column
    df = df.merge(d.regionLookup[["Political Geography", "REGION"]], on="Political Geography", how="left")

    df = df.merge(colormap, on="REGION", how="left")

    # Clean the 'REGION' values
    df.loc[df['REGION'] == "NONE", 'REGION'] = ""

    # List of region values to filter
    regions_to_filter = ["", "WORLD", "AFRICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "EUROPE"]

    # Filter out rows with specified 'REGION' values
    df = df.loc[df['REGION'].isin(regions_to_filter),]

    # Filter out rows for annex division using .loc
    df = df.loc[~df['Political Geography'].isin(['ANNEX I', 'NON-ANNEX I'])]

    # Select only the columns you need
    df = df.loc[:,['Political Geography', 'REGION', source, 'COLOR', 'Year']]

    # Create the 'sunburst' DataFrame
    sunburst = pd.DataFrame()

    # Assign columns from 'df' to 'sunburst'
    sunburst["labels"] = df.loc[:,'Political Geography']
    sunburst["parents"] = df.loc[:,'REGION']
    sunburst["values"] = df.loc[:,source]
    sunburst["colors"] = df.loc[:,'COLOR']
    sunburst["year"] = df.loc[:,'Year']

    # Fix Region Colors

    sunburst.loc[sunburst["labels"] == "WORLD", "colors"] = bg
    sunburst.loc[sunburst["labels"] == "AFRICA", "colors"] = "#46C6E7"
    sunburst.loc[sunburst["labels"] == "ASIA PACIFIC", "colors"] = "#616BB2"
    sunburst.loc[sunburst["labels"] == "COMMONWEALTH OF INDEPENDENT STATES", "colors"] = "#8B69AD"
    sunburst.loc[sunburst["labels"] == "MIDDLE EAST", "colors"] = "#F9A05B"
    sunburst.loc[sunburst["labels"] == "NORTH AMERICA", "colors"] = "#EF563C"
    sunburst.loc[sunburst["labels"] == "SOUTH AND CENTRAL AMERICA", "colors"] = "#F06591"
    sunburst.loc[sunburst["labels"] == "EUROPE", "colors"] = "#41BB91"

    # Perform specific replacements based on the 'source' column using .loc
    if source in ["Fossil Fuel Energy and Cement Manufacture", "Fossil Fuel Energy (Supplied)", "Fossil Fuel Energy (Consumed)"]:
        # add bunkers
        bunkers = [
            {'labels' : 'Bunkered<br>Fuels', 'parents' : 'WORLD', 'values' : world_bunkered, 'colors' : "blue"},
            {'labels' : 'Bunkered<br>(Marine)<br>Fuels', 'parents' : 'Bunkered<br>Fuels', 'values' : world_bunkered_marine, 'colors' : "blue"},
            {'labels' : 'Bunkered<br>(Aviation)<br>Fuels', 'parents' : 'Bunkered<br>Fuels', 'values' : world_bunkered_aviation, 'colors' : "blue"},
            ]

        bunkers_df = pd.DataFrame(bunkers)

        sunburst = pd.concat([sunburst, bunkers_df], ignore_index=True)

        # Change region titles
        sunburst.loc[sunburst["labels"] == "WORLD", "labels"] = "<b>WORLD</b><br>(INCLUDES<br>INTERNATIONALLY<br>BUNKERED FUELS)"
        sunburst.loc[sunburst["parents"] == "WORLD", "parents"] = "<b>WORLD</b><br>(INCLUDES<br>INTERNATIONALLY<br>BUNKERED FUELS)"

    sunburst.loc[sunburst["labels"] == "COMMONWEALTH OF INDEPENDENT STATES", "labels"] = "COMMONWEALTH OF<br>INDEPENDENT STATES"
    sunburst.loc[sunburst["parents"] == "COMMONWEALTH OF INDEPENDENT STATES", "parents"] = "COMMONWEALTH OF<br>INDEPENDENT STATES"
    sunburst.loc[sunburst["labels"] == "SOUTH AND CENTRAL AMERICA", "labels"] = "SOUTH AND<br>CENTRAL AMERICA"
    sunburst.loc[sunburst["parents"] == "SOUTH AND CENTRAL AMERICA", "parents"] = "SOUTH AND<br>CENTRAL AMERICA"

    # change country titles
    sunburst.loc[sunburst["labels"] == "UNITED STATES OF AMERICA", "labels"] = "UNITED STATES<br>OF AMERICA"
    sunburst.loc[sunburst["labels"] == "RUSSIAN FEDERATION", "labels"] = "RUSSIAN<br>FEDERATION"
    sunburst.loc[sunburst["labels"] == "ISLAMIC REPUBLIC OF IRAN", "labels"] = "ISLAMIC REPUBLIC<br>OF IRAN"

    return sunburst, plot_title, plot_subtitle

def source_sunburst(source, fuel_type, theme):

    # Define color and background based on the theme
    if theme == 'light':
        textCol = '#000'
        bg = '#fff'
    elif theme == 'dark':
        textCol = '#fff'
        bg = '#000'

    # Define years for the animation
    years = list(range(1995, 2021))

    # Initialize the figure with subplots
    fig = go.Figure()

    # Setup the initial sunburst chart for the first year
    sunburst, plot_title, plot_subtitle = build_sunburst_data(source, fuel_type, years[-1], bg)
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
        sunburst, _, _ = build_sunburst_data(source, fuel_type, year, bg)
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