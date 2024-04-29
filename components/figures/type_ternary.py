"""
This module generates a ternary plot for visualizing the proportional distribution of CO₂ emissions
from solid, liquid, and gas fossil fuels within various geopolitical regions. It allows exploration
of fuel usage patterns and their environmental impact based on user-selected criteria such as source,
geopolitical grouping, and theme.

Functions
---------
type_ternary(source, grouping, theme)
    Constructs a ternary plot that visualizes the relative contributions of solid, liquid, and gas
    fuels to total CO₂ emissions, filtered by geopolitical grouping and styled according to the
    specified theme.

Parameters
----------
source : str
    The specific source of CO₂ emissions to be analyzed (e.g., 'Total Emissions', 'Fossil Fuel Energy (Consumed)').
grouping : str
    The geopolitical grouping for the analysis (e.g., 'region', 'world', 'annex'), which determines
    the scope of the data included in the plot.
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the ternary plot.

Returns
-------
plotly.graph_objects.Figure
    A Plotly Figure object representing the ternary plot, configured with interactive capabilities
    and ready for display in a web or mobile interface.

Examples
--------
To generate a ternary plot for CO₂ emissions from total fossil fuels within European countries using
a light theme:

>>> fig = type_ternary('Total Emissions', 'region', 'light')
>>> fig.show()

Notes
-----
The ternary plot provides a unique visual representation of how different types of fossil fuels contribute
to total emissions in selected regions or globally. This visualization helps stakeholders and policymakers
to understand the impact of various energy sources on carbon outputs.

The visualization dynamically adjusts based on the user-selected theme, enhancing readability and user
engagement. Each geopolitical region or group is represented in the plot, allowing for comparisons and
deeper analysis of regional differences in fuel consumption patterns.

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

def type_ternary(source, grouping, theme) :

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

    # Create copies and rename the 'source' column in each copy
    df_solid_copy = d.df_solid[['Political Geography', 'Year', source]].copy()
    df_liquid_copy = d.df_liquid[['Political Geography', 'Year', source]].copy()
    df_gas_copy = d.df_gas[['Political Geography', 'Year', source]].copy()
    df_total_copy = d.df_total[['Political Geography', 'Year', source]].copy()

    df_solid_copy = df_solid_copy.rename(columns={source: 'Solid'})
    df_liquid_copy = df_liquid_copy.rename(columns={source: 'Liquid'})
    df_gas_copy = df_gas_copy.rename(columns={source: 'Gas'})
    df_total_copy = df_total_copy.rename(columns={source: 'Total'})

    # Merge the copies of the DataFrames
    df_merged = pd.merge(df_total_copy, df_solid_copy, on=['Political Geography', 'Year'], how='outer')
    df_merged = pd.merge(df_merged, df_liquid_copy, on=['Political Geography', 'Year'], how='outer')
    df_merged = pd.merge(df_merged, df_gas_copy, on=['Political Geography', 'Year'], how='outer')

    df = df_merged


    # Set Title and credit properties
    plot_title = source
    plot_subtitle = "CO₂ EMISSIONS SOURCE FUEL TYPE PROPORTIONS"

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
    df.loc[:, 'Total'] = df.loc[:, 'Total'].replace(np.nan, 0)
    df.loc[:, 'Solid'] = df.loc[:, 'Solid'].replace(np.nan, 0)
    df.loc[:, 'Liquid'] = df.loc[:, 'Liquid'].replace(np.nan, 0)
    df.loc[:, 'Gas'] = df.loc[:, 'Gas'].replace(np.nan, 0)

    # Join to get country region and color
    df = df.merge(d.regionLookup[["Political Geography", "REGION"]], on="Political Geography", how="left")
    df = df.merge(colormap, on="REGION", how="left")

    # Remove countries with "ANTARTICA" as their region
    df = df.loc[~df['REGION'].isin(["ANTARCTICA"])]

    # Create the ternary data frame for the countries trace
    ternary_df = pd.DataFrame()
    ternary_df['Total'] = df.loc[:,'Total'].values
    ternary_df.loc[:, 'Total'] = ternary_df.loc[:, 'Total'].replace(np.nan, 0)
    ternary_df['size'] = np.sqrt(5 +  ternary_df['Total'])
    ternary_df['Solid'] = df.loc[:,'Solid'].values
    ternary_df['Liquid'] = df.loc[:,'Liquid'].values
    ternary_df['Gas'] = df.loc[:,'Gas'].values
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
        }

    fig = go.Figure()

    fig = px.scatter_ternary(
        ternary_df, 
        b='Solid', 
        c='Liquid', 
        a='Gas', 
        size="size",
        color=colorby, 
        animation_frame="Year ",
        color_discrete_map=colormap,
        labels={"A": "A-axis", "B": "B-axis", "C": "C-axis"},
        title="Ternary Plot with Animation", 
        custom_data=["Name", "Total", "Region", "Solid", "Liquid", "Gas"],
        hover_data={
            'Name': True,       # Display the "Name" as is
            'Total': True,      # Display the "Total" as is
            'Region': False,     # Display the "Region" as is
            'Solid': True,         # Don't display the a-axis value
            'Liquid': True,         # Don't display the b-axis value
            'Gas': True,         # Don't display the c-axis value
            'size' : False
        }
        )

    # Show the plot
    fig.update_layout({
        'ternary': {
            'sum': 1,
            'bgcolor': 'rgba(0,0,0,0)',
            'aaxis': makeAxis("Gas", 0),
            'baxis': makeAxis('<br>' + "Solid", 60),
            'caxis': makeAxis('<br>Liquid', -60),
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
        )
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

    fig.update_traces(hovertemplate='Name: <b>%{customdata[0]}</b><br>Total: %{customdata[1]}<br> Solid Fuel: %{customdata[3]}<br>Liquid Fuel: %{customdata[4]}<br>Gas Fuel: %{customdata[5]}')

    return fig
