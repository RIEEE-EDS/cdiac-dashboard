"""
Module/Script Name: carbon_atlas.py
Author: M. W. Hefner

Created: 4/12/2023
Last Modified: 7/15/2023

Project: CDIAC at AppState

Script Description: This script defines the carbon atlas choropleth figure.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
import plotly.io as pio
from components.staticdata import data as d

# Carbon Atlas
def carbon_atlas(source, fuel_type, theme) :

    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid
        if (theme == 'light'):
            c_scale = "turbid"
        else :
            c_scale = "turbid_r"    
    elif fuel_type == 'liquids':
        df = d.df_liquid
        if (theme == 'light'):
            c_scale = "Hot_r"
        else :
            c_scale = "Hot"
    elif fuel_type == 'gases':
        df = d.df_gas
        if (theme == 'light'):
            c_scale = "dense"
        else :
            c_scale = "dense_r"
    else :
        df = d.df_total
        if (theme == 'light'):
            c_scale = "electric_r"
        else :
            c_scale = "electric"

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

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

        # set color scale
        color_continuous_scale = c_scale,
        
        # set color range
        range_color = [0, maxValue]
    )
    
    fig.update_geos(fitbounds="locations", visible=False)
    
    fig.update_layout(
            geo=dict(bgcolor= 'rgba(0,0,0,0)'),
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin={'l': 0, 'r': 0, 't': 60, 'b': 0},
            coloraxis_colorbar_title="CO₂ Emissions<br>kilotonnes C",
            title=source,
            title_font_color=textCol,  # Set the font color of the title
            font=dict(
                size=15, # Set the font size for the entire plot, excluding the title
                color = textCol  
            ),
            title_x=0.5,  # Set the horizontal alignment of the title (0-1)
            title_y=0.95,  # Set the vertical alignment of the title (0-1)
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
            size=15,
            color = textCol
        )
    )

    fig.update_layout(annotations=[subtitle_annotation])
    
    # These lines set the a last frame
    last_frame_num = len(fig.frames) -1

    fig.layout['sliders'][0]['active'] = last_frame_num

    fig = go.Figure(data=fig['frames'][-1]['data'], frames=fig['frames'], layout=fig.layout)

    return fig