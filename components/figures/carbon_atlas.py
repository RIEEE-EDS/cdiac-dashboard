"""
This module provides a function to create a choropleth map visualizing CO₂ emissions
from various fuel types across different nations, based on user-selected filters for
data source, fuel type, and UI theme.

Functions
---------
carbon_atlas(source, fuel_type, theme)
    Generates a choropleth map for CO₂ emissions using the specified source, fuel type,
    and theme. The color scale and other visual elements of the map adjust according to the theme.

Parameters
----------
source : str
    The specific data source for CO₂ emission values (e.g., total emissions, per capita).
fuel_type : str
    The type of fuel for which emissions data is visualized (e.g., solids, liquids, gases).
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the choropleth map.

Returns
-------
plotly.graph_objs._figure.Figure
    A Plotly Figure object representing the choropleth map, configured according to the specified
    parameters and ready for display in a Dash application.

Examples
--------
To generate a choropleth map for solid fuel CO₂ emissions with a dark theme:

>>> fig = carbon_atlas('Total Emissions', 'solids', 'dark')
>>> fig.show()

Notes
-----
The function first filters the dataset based on the `fuel_type` to get the relevant subset of the data.
It then applies a color scale based on the `theme`, where each theme inverses the colors for better
visibility depending on the background. The function also dynamically adjusts the maximum value
on the color scale to match the highest emission value present in the filtered dataset.

The map differentiates between various geopolitical regions using a color scale that reflects
the magnitude of emissions. The function dynamically filters data to exclude certain global
aggregations like 'WORLD' or 'EUROPE' to provide a more detailed view at the national level.

The layout includes a subtitle annotation that dynamically updates with the current year, providing
a watermark styled as a citation to the CDIAC at AppState Dashboard.

See Also
--------
plotly.graph_objects : Plotly's graph object module for constructing figures.
plotly.express : Plotly's high-level interface for building figures.
components.utils.constants : Module where various constants like data frames and mappings are defined.
"""


# Import needed libraries
import plotly.graph_objects as go
import plotly.express as px
import datetime
from components.utils import constants as d

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
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'


    # List of Nation values to filter
    nations_to_filter = ["AFRICA", "ANTARCTICA", "ASIA PACIFIC", "COMMONWEALTH OF INDEPENDENT STATES", "EUROPE", "MIDDLE EAST", "NORTH AMERICA", "SOUTH AND CENTRAL AMERICA", "ANNEX I", "NON-ANNEX I", "WORLD"]

    # Filter out rows with specified Nation values
    df = df.copy()[~df['Political Geography'].isin(nations_to_filter)]

    # Top of the scale should be the max value for the entire range of years
    maxValue = df[source].max()

    # Map each observation to their nation ISO for plotly
    df['Nation_ISO'] = df['Political Geography'].map(d.location_mapping)

    df['Year '] = df['Year']

    # Create the choropleth figure
    fig = px.choropleth(

        # Our Dataframe
        df, 

        # Base locations of ISO
        locations = "Nation_ISO",

        # The color of a nation depends on the carbon emissions value from the given source
        color = source,

        # Hovering over a country should give you the nation name
        hover_name = "Political Geography",

        hover_data= {"Nation_ISO" : False},

        # Animate based on year
        animation_frame = "Year ",

        # set color scale
        color_continuous_scale = c_scale,
        
        # set color range
        range_color = [0, maxValue]
    )
    
    fig.update_geos(fitbounds="locations", visible=False)
    
    # Give it the CDIAC Watermark with overkill year code lol
    subtitle_annotation = dict(
        x=0.5,
        y=0,
        xref='paper',
        yref='paper',
        xanchor="center",
        text='<b>The CDIAC at AppState Dashboard</b><br>Hefner and Marland (' + str(datetime.date.today().year) + ')',
        showarrow=False,
        align="center",
        
        font = dict(
            size=20,
            color = textCol
        )
    )

    # Figure out what the plot title will be
    if fuel_type == 'solids':
        plot_title = " <b>Solid</b> Fuel CO₂ Emissions"
    elif fuel_type == 'liquids':
        plot_title = " <b>Liquid</b> Fuel CO₂ Emissions"
    elif fuel_type == 'gases':
        plot_title = " <b>Gas</b> Fuel CO₂ Emissions"
    else :
        plot_title = " CO₂ Emissions"

    if source == "Per Capita Total Emissions" :
        plot_title = "PER CAPITA CO₂ EMISSIONS"
    else:
        plot_title = (source + plot_title).upper()

    fig.update_layout(

            geo=dict(bgcolor= 'rgba(0,0,0,0)'),
            plot_bgcolor=bg,
            paper_bgcolor=bg,

            margin={'l': 0, 'r': 0, 't': 50, 'b': 0},

            coloraxis_colorbar_title="CO₂ Emissions<br>kilotonnes C".upper(),

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

            sliders = [dict(
                font=dict(size=20, color = textCol),
                pad=dict(t=0,b=10,l=20)
            )],
        )
    

    if d.show_credit :
        fig.update_layout(
                # Apply CDIAC Watermark
                annotations=[subtitle_annotation]
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

    return fig