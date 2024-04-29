"""
This module generates a ternary plot for analyzing the distribution of CO₂ emissions among
three different sources within various geopolitical regions, depending on user-selected filters.
The plot is dynamically adjustable based on fuel type, emission source, and theme.

Functions
---------
source_ternary(source_a, source_b, fuel_type, grouping, theme)
    Constructs a ternary plot that visualizes the proportional relationships between two primary
    CO₂ emission sources and all other sources combined. The plot's appearance and data are
    configured according to user-selected criteria such as fuel type, grouping, and color theme.

Parameters
----------
source_a : str
    The first primary source of CO₂ emissions to be analyzed (e.g., 'Fossil Fuel Energy (Consumed)').
source_b : str
    The second primary source of CO₂ emissions to be analyzed.
fuel_type : str
    The type of fuel for which emissions data is visualized (e.g., solids, liquids, gases, or total).
grouping : str
    The geopolitical grouping for the analysis (e.g., 'region', 'world', 'annex').
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the ternary plot.

Returns
-------
plotly.graph_objects.Figure
    A Plotly Figure object representing the ternary plot, configured with interactive capabilities
    and ready for display in a web or mobile interface.

Examples
--------
To generate a ternary plot for CO₂ emissions comparing 'Fossil Fuel Energy (Consumed)' and
'Electric, CHP, Heat Plants' within European countries using solid fuels with a dark theme:

>>> fig = source_ternary('Fossil Fuel Energy (Consumed)', 'Electric, CHP, Heat Plants', 'solids', 'region', 'dark')
>>> fig.show()

Notes
-----
The plot utilizes a three-dimensional representation to show the proportional contributions
of two main sources against all other sources combined. This visualization helps in understanding
the dominant emission sources and their relative significance in different geopolitical contexts.

The function handles complex data preprocessing to ensure accurate and meaningful visual output,
including dynamic adjustments for different geopolitical groupings and emission sources.

See Also
--------
plotly.graph_objects : Used for constructing complex interactive visualizations.
components.utils.constants : Provides access to global constants and data sources used in the visualization.
"""


# Import needed libraries
import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd
from components.utils import constants as d
import plotly.express as px

def source_ternary(source_a, source_b, fuel_type, grouping, theme) :

    if theme == 'light' :
        textCol = '#000'
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'

    # Assign Region Colors
    colormap = pd.DataFrame()

    # Define Colors
    colormap["REGION"] = ["NONE", "WORLD", "AFRICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "EUROPE"]
    colormap["COLOR"] = [bg, bg, "#46C6E7", "#616BB2", "#8B69AD", "#F9A05B", "#EF563C", "#F06591", "#41BB91"]

    # Set Data
    if fuel_type == 'solids':
        df = d.df_solid
        plot_title = "<b>SOLID</b> FOSSIL FUEL ENERGY USE CO₂ EMISSIONS"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        plot_title = "<b>LIQUID</b> FOSSIL FUEL ENERGY USE CO₂ EMISSIONS"
    elif fuel_type == 'gases':
        df = d.df_gas
        plot_title = "<b>GAS</b> FOSSIL FUEL ENERGY USE CO₂ EMISSIONS"
    else :
        df = d.df_total
        plot_title = "FOSSIL FUEL ENERGY USE CO₂ EMISSIONS"


    colorby = "Name"

    xanchor_ann = "left"
    align_ann = "left"
    y_ann = 0.5
    showLegend = True

    if grouping == "region" :

        # Set the regions aside for the other trace
        df = df.loc[df['Political Geography'].isin(["AFRICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "EUROPE"])]


    elif grouping == "world" :

        showLegend = False

        xanchor_ann = "right"

        align_ann = "right"

        y_ann = 1

        df = df.loc[df['Political Geography'].isin(["WORLD"])]

    elif grouping == "annex" :
        
        xanchor_ann = "center"

        align_ann = "center"

        y_ann = 0.75

        df = df.loc[df['Political Geography'].isin(['ANNEX I', 'NON-ANNEX I'])]

    else :

    # Define regions so they can be removed in the first trace
        regions_to_filter = ['ANNEX I', 'NON-ANNEX I', "WORLD", "AFRICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "EUROPE"]

        # remove regions
        df = df.loc[~df['Political Geography'].isin(regions_to_filter)]

        colorby = "Region"

    #df.loc[:,'Fossil Fuel Energy (Consumed)']

    # Replace empty records with 0
    df.loc[:, source_a] = df.loc[:, source_a].replace(np.nan, 0)
    df.loc[:, source_b] = df.loc[:, source_b].replace(np.nan, 0)

    # Join to get country region and color
    df = df.merge(d.regionLookup[["Political Geography", "REGION"]], on="Political Geography", how="left")
    df = df.merge(colormap, on="REGION", how="left")

    # Remove countries with "ANTARTICA" as their region
    df = df.loc[~df['REGION'].isin(["ANTARCTICA"])]

    # Create the ternary data frame for the countries trace
    ternary_df = pd.DataFrame()
    ternary_df['Total'] = df.loc[:,'Fossil Fuel Energy (Consumed)'].values
    ternary_df.loc[:, 'Total'] = ternary_df.loc[:, 'Total'].replace(np.nan, 0)
    ternary_df['size'] = np.sqrt(5 +  ternary_df['Total'])
    ternary_df[source_a] = df.loc[:,source_a].values
    ternary_df[source_b] = df.loc[:,source_b].values
    ternary_df['All Other Sources'] = ternary_df['Total'] - (ternary_df[source_a] + ternary_df[source_b])
    ternary_df["colors"] = df.loc[:,'COLOR']
    ternary_df['Name'] = df.loc[:,'Political Geography'].values
    ternary_df['Region'] = df.loc[:,'REGION'].values
    ternary_df['Year '] = df.loc[:,'Year'].values

    #ternary_df.to_csv('ternary_df_debug.csv', index=False)

    colormap = {
        "NONE": bg,
        "WORLD": textCol,
        "ANNEX I" : "#7570b3",
        "NON-ANNEX I" : "#1b9e77",
        "AFRICA": "#46C6E7",
        "ASIA PACIFIC": "#616BB2",
        "COMMONWEALTH OF INDEPENDENT STATES": "#8B69AD",
        "MIDDLE EAST": "#F9A05B",
        "NORTH AMERICA": "#EF563C",
        "SOUTH AND CENTRAL AMERICA": "#F06591",
        "EUROPE": "#41BB91"
    }

    def makeAxis(title, tickangle):
        return {
        'title': title,
        'titlefont': { 'size': 20 },
        'tickangle': tickangle,
        'tickfont': { 'size': 15 },
        'linecolor': textCol,
        'gridcolor': textCol,
        'ticklen': 5,
        'showline': True,
        'showgrid': True,
        #'title_standoff' : standoff
        }

    fig = go.Figure()

    fig = px.scatter_ternary(
        ternary_df, 
        a=source_a, 
        b=source_b, 
        c="All Other Sources", 
        size="size",
        color=colorby, 
        animation_frame="Year ",
        color_discrete_map=colormap,
        labels={"A": "A-axis", "B": "B-axis", "C": "C-axis"},
        title="Ternary Plot with Animation", 
        custom_data=["Name", "Total", "Region", source_a, source_b, "All Other Sources"],  # Include only these columns in hover data
        hover_data={
            'Name': True,       # Display the "Name" as is
            'Total': True,      # Display the "Total" as is
            'Region': False,     # Display the "Region" as is
            source_a: True,         # Don't display the a-axis value
            source_b: True,         # Don't display the b-axis value
            'All Other Sources': True,         # Don't display the c-axis value
            'size' : False
        }
        )

    # Show the plot
    fig.update_layout({
        'ternary': {
            'sum': 1,
            'bgcolor': 'rgba(0,0,0,0)',
            'aaxis': makeAxis(source_a, 0),
            'baxis': makeAxis('<br>' + source_b, 60),
            'caxis': makeAxis('<br>All Other Sources', -60),
        },
    })

    annotations = []

    if d.show_credit :
        annotations=[
            # Credit
            dict(
                x=1,
                y=y_ann,
                xref='paper',
                yref='paper',
                xanchor=xanchor_ann,
                yanchor='top',
                text='<b>The CDIAC at AppState Dashboard</b><br>Hefner and Marland (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                align=align_ann,
                
                font = dict(
                    size=20,
                    color = textCol
                )
            ),
        ]


    fig.update_layout(

        showlegend=showLegend,

        plot_bgcolor=bg,
        paper_bgcolor=bg,

        #margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

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

        # Subtitle
        annotations=annotations

    )

    # These lines set the last frame
    last_frame_num = len(fig.frames) -1
    fig.layout['sliders'][0]['active'] = last_frame_num
    fig = go.Figure(data=fig['frames'][-1]['data'], frames=fig['frames'], layout=fig.layout)

    fig.update_layout(
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell",
        ),
    )

    fig["layout"].pop("updatemenus") # optional, drop animation buttons

    # Define your marker customizations
    marker_settings = dict(
        line=dict(width=0),
    )

    # Update the marker settings for each frame
    for frame in fig.frames:
        for trace in frame.data:
            trace.marker = marker_settings

    # Also update the initial trace (first frame)
    fig.update_traces(marker=marker_settings)

    fig.update_traces(hovertemplate='Name: <b>%{customdata[0]}</b><br>Total: %{customdata[1]}<br>' + source_a + ': %{customdata[3]}<br>' + source_b + ': %{customdata[4]}<br>All Other Sources: %{customdata[5]}')

    return fig
