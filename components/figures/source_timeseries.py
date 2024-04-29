"""
This module generates a time-series line chart for analyzing CO₂ emissions from a specified source
across multiple geopolitical regions. The plot can dynamically adjust based on user-selected criteria
such as fuel type, region, and visual theme.

Functions
---------
source_timeseries(source, fuel_type, nation, theme)
    Constructs a line chart that visualizes the trends of CO₂ emissions from a particular source,
    filtered by fuel type and region, and styled according to the specified theme.

Parameters
----------
source : str
    The specific source of CO₂ emissions to be analyzed (e.g., 'Total Emissions').
fuel_type : str
    The type of fuel for which emissions data is visualized (e.g., solids, liquids, gases, or total).
nation : list
    A list of countries or regions for which the emissions data is being visualized.
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the color scheme of the chart.

Returns
-------
plotly.graph_objects.Figure
    A Plotly Figure object representing the time-series chart, configured with interactive capabilities
    and ready for display in a web or mobile interface.

Examples
--------
To generate a time-series chart for CO₂ emissions from 'Total Emissions' using total fuels in Germany
with a dark theme:

>>> fig = source_timeseries('Total Emissions', 'total', ['Germany'], 'dark')
>>> fig.show()

Notes
-----
The visualization provides a comprehensive view of emission trends, emphasizing changes over time
within selected regions. The chart uses custom color and line styles to distinguish between regions,
enhancing readability and user engagement.

The function handles complex data preprocessing to ensure accurate and meaningful visual output,
including dynamic adjustments for different geopolitical regions and emission sources.

See Also
--------
plotly.express : High-level interface for creating expressive data visualizations.
plotly.graph_objects : For lower-level interface for creating complex visualizations.
components.utils.constants : Module where global constants and data sources are defined.
"""


# Import needed libraries
import plotly.express as px
import datetime
import plotly.io as pio
from components.utils import constants as d

def source_timeseries(source, fuel_type, nation, theme):

    pio.templates.default = "plotly_white"

    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid
        plot_title = source + " <b>SOLID</b> CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>SOLID</b> FOSSIL FUELS"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        plot_title = source + " <b>LIQUID</b> FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>LIQUID</b> FOSSIL FUELS"
    elif fuel_type == 'gases':
        df = d.df_gas
        plot_title = source + " <b>GAS</b> FUEL CO₂ EMISSIONS"
        plot_subtitle = "FROM ENERGY USE OF <b>GASEOUS</b> FOSSIL FUELS"
    else :
        df = d.df_total
        plot_title = source + " TOTAL CO₂ EMISSIONS"
        plot_subtitle = ""

    if theme == 'light' :
        textCol = '#000'
        bg = '#fff'
    if theme == 'dark' :
        textCol = '#fff'
        bg = '#000'

    df = df[df['Political Geography'].isin(nation)]

    df = df.copy()

    # Define your custom color map for specific political geographies
    custom_color_map = {
        'WORLD': textCol,
        'AFRICA': '#46C6E7',
        'ASIA PACIFIC': '#616BB2',
        'COMMONWEALTH OF INDEPENDENT STATES': '#8B69AD',
        'MIDDLE EAST': '#F9A05B',
        'NORTH AMERICA': '#EF563C',
        'SOUTH AND CENTRAL AMERICA': '#F06591',
        'EUROPE': '#41BB91',
        # Add more specific mappings as needed
    }

    # Default color sequence for other categories
    if theme == "dark" :
        default_color_sequence = px.colors.qualitative.Light24_r
    else :
        default_color_sequence = px.colors.qualitative.Dark24_r

    # Combine custom colors with the default sequence
    # Make sure the custom colors take precedence
    for category in df['Political Geography'].unique():
        if category not in custom_color_map:
            # Use the next color in the default sequence for this category
            custom_color_map[category] = default_color_sequence.pop(0)

    fig = px.line(df, x='Year', y=source, color='Political Geography',
                color_discrete_map=custom_color_map,  # Use the combined color map
                hover_data={'Political Geography': True, 'Year': False})
    
    if d.show_credit :
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
                y=-0.10,
                xref='paper',
                yref='paper',
                xanchor = 'center',
                yanchor = 'top',
                text='The CDIAC at AppState Dashboard (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                
                font = dict(
                    size=20,
                    color = textCol
                )
            )
        ]
    else :
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
        ]

    # Define your custom line styles for specific political geographies
    line_styles = {
        "WORLD" : "longdashdot",
        "AFRICA" : "dash",
        "ASIA PACIFIC" : "dash", 
        "COMMONWEALTH OF INDEPENDENT STATES" : "dash", 
        "MIDDLE EAST" : "dash", 
        "NORTH AMERICA" : "dash", 
        "SOUTH AND CENTRAL AMERICA" : "dash", 
        "EUROPE" : "dash", 
        "ANNEX I" : "dot", 
        "NON-ANNEX I" : "dot", 
        # Add more mappings as needed
    }

    # Update traces
    for trace in fig.data:
        if trace.name in line_styles:
            fig.update_traces(selector=dict(name=trace.name),
                            line=dict(dash=line_styles[trace.name]))


    fig.update_layout(

        plot_bgcolor=bg,
        paper_bgcolor=bg,

        margin={'l': 0, 'r': 0, 't': 100, 'b': 100},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=20, 
            color = textCol  
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
                color = textCol
            )
        ),

        # Subtitle
        annotations=annotations

    )
    
    fig.update_traces(mode="lines")

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"
        )
    )
    
    return fig