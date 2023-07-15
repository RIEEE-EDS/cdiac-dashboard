"""
Module/Script Name: figures.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the interactive plotly figures used in this application.

Callback methods: 0

"""

# Import needed libraries
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
import plotly.io as pio
from components.staticdata import data as d

# Carbon Atlas
def carbon_atlas(source, fuel_type) :

    # Select Color Scale depending on fuel type
    if fuel_type == 'solids':
        df = d.df_solid
        c_scale = "turbid"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        c_scale = "Hot_r"
    elif fuel_type == 'gases':
        df = d.df_gas
        c_scale = "dense"
    else :
        df = d.df_total
        c_scale = "electric_r"

    # Top of the scale should be the max value for the entire range of years
    maxValue = df[source].max()

    # Map each observation to their nation ISO for plotly
    df['Nation_ISO'] = df['Nation'].map(d.location_mapping)

    # Create the choropleth figure
    fig = px.choropleth(

        # Our Dataframe
        df, 

        # Base locations of ISO
        locations = "Nation_ISO",

        # The color of a nation depends on the carbon emissions value from the given source
        color = source,

        # Hovering over a country should give you the nation name
        hover_name = "Nation",

        # Animate based on year
        animation_frame = "Year",

        # Keep "nation" as a distinct group
        # TODO: Something is off about this.  Countries do no remain selected over years within plotly.
        animation_group = "Nation",

        color_continuous_scale = c_scale,
        
        range_color = [0, maxValue]
    )
    
    fig.update_geos(fitbounds="locations", visible=False)
    
    fig.update_layout(
            margin={'l': 0, 'r': 0, 't': 60, 'b': 0},
            coloraxis_colorbar_title="CO₂ Emissions<br>kilotonnes C",
            title=source,
            title_font_color="black",  # Set the font color of the title
            font=dict(
                size=15  # Set the font size for the entire plot, excluding the title
            ),
            title_x=0.5,  # Set the horizontal alignment of the title (0-1)
            title_y=0.99,  # Set the vertical alignment of the title (0-1)
            title_xanchor="center",  # Set the horizontal anchor point of the title
            title_yanchor="top"  # Set the vertical anchor point of the title
        )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=0.5,
        y=-0.10,
        xref='paper',
        yref='paper',
        text='Source: CDIAC at AppState, ' + str(datetime.date.today().year),
        showarrow=False,

        font = dict(
            size=15
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])
    
    # These lines set the a last frame
    last_frame_num = len(fig.frames) -1

    fig.layout['sliders'][0]['active'] = last_frame_num

    fig = go.Figure(data=fig['frames'][-1]['data'], frames=fig['frames'], layout=fig.layout)

    return fig


# Time Series by Country
def timeseries_country(fuel_type, nation) :

    pio.templates.default = "plotly_white"

    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    df = df[df['Nation'] == nation]

    df = pd.melt(
        df, 
        id_vars=['Nation', 'Year'], 
        var_name='Source', 
        value_name='Carbon'
    )

    fig = px.line(df, x='Year', y = 'Carbon', color = 'Source', 
                  color_discrete_sequence=px.colors.qualitative.Alphabet)

    fig.update_layout(

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        title = nation,

        title_font_color="black",  # Set the font color of the title

        font=dict(

            size=15  # Set the font size for the entire plot, excluding the title

        ),

        title_x=0.5,  # Set the horizontal alignment of the title (0-1)

        title_y=0.95,  # Set the vertical alignment of the title (0-1)

        title_xanchor="center",  # Set the horizontal anchor point of the title

        title_yanchor="top",  # Set the vertical anchor point of the title

        )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=1,
        y=1,
        xref='paper',
        yref='paper',
        text='CDIAC at AppState, ' + str(datetime.date.today().year),
        showarrow=False,

        font = dict(
            size=15
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])
    
    return fig


# Time Series by Source
def timeseries_source(source, fuel_type, nation) :

    pio.templates.default = "plotly_white"

    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    df = df[df['Nation'].isin(nation)]

    fig = px.line(df, x='Year', y = source, color = 'Nation', 
                  color_discrete_sequence=px.colors.qualitative.Light24_r)

    fig.update_layout(

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title="CO₂ Emissions (kilotonnes C)",

        title = source,

        legend_title = "Source",

        title_font_color="black",  # Set the font color of the title

        font=dict(

            size=15  # Set the font size for the entire plot, excluding the title

        ),

        title_x=0.5,  # Set the horizontal alignment of the title (0-1)

        title_y=0.95,  # Set the vertical alignment of the title (0-1)

        title_xanchor="center",  # Set the horizontal anchor point of the title

        title_yanchor="top",  # Set the vertical anchor point of the title

        )
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=1,
        y=1,
        xref='paper',
        yref='paper',
        text='CDIAC at AppState, ' + str(datetime.date.today().year),
        showarrow=False,

        font = dict(
            size=15
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])

    return fig