"""
This module facilitates the creation of an upload component and Dash datatable for displaying CSV or Excel data. 
It dynamically generates a datatable based on the uploaded file and allows users to interact with the data through sorting,
filtering, and pagination functionalities.

Functions
---------
browse_table()
    Creates and returns a Div containing an empty placeholder for the datatable where uploaded data will be displayed.

parse_contents(theme, fuel_type)
    Generates a datatable based on predefined data sources filtered by fuel type. Styles the datatable according to 
    the specified theme.

update_output(theme, fuel_type)
    Callback function that updates the content of the datatable based on user interactions such as theme changes or 
    fuel type selections.

Parameters
----------
theme : str
    The theme setting (e.g., 'light', 'dark') which affects the visual styling of the datatable.
fuel_type : str
    The type of fuel (solids, liquids, gases, or total) that filters the data to be displayed in the datatable.

Returns
-------
dash.html.Div
    A Div containing the datatable for displaying data. The datatable is styled and configured to be interactive, 
    allowing users to sort, filter, and paginate through the data.

Examples
--------
To create and display a datatable within a Dash application:

>>> table_container = browse_table()
>>> app.layout = dash.html.Div(children=[table_container])

This module is designed to be used within a larger Dash application where it contributes to the user's ability to 
interactively explore data related to CO₂ emissions from various fuel sources.

Notes
-----
The module is part of a Dash application designed for environmental data analysis. It utilizes Dash's capabilities 
to render interactive data tables from CSV or Excel files uploaded by the user.

See Also
--------
dash.dash_table.DataTable : Used to create interactive tables in Dash applications.
pandas : Used for data manipulation and analysis.
components.utils.constants : Provides access to shared constants and utility functions used across the application.
"""


# Component ID (Should be the same as the title of this file)
component_id = "browse"

# Import Dependencies
import dash.html.Div
import dash.html.P
import dash.dash_table.DataTable
import pandas as pd
from components.utils import constants as d

def browse_table() :

    return dash.html.Div(
        children=[
        dash.html.Div(id='output-data-upload'),
    ])

# Callback helper function
def parse_contents(theme, fuel_type):
    # Select Color Scale depending on fuel type and theme
    if fuel_type == 'solids':
        df = d.df_solid  
        table_title = "CO₂ Emissions from the Energy Use of Solid Fossil Fuels"
        header_color = "rgba(253,180,98,0.75)"
        cell_c_1 = "rgba(253,180,98,0.5)"
        cell_c_2 = "rgba(253,180,98,0.25)"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        table_title = "CO₂ Emissions from the Energy Use of Liquid Fossil Fuels"
        header_color = "rgba(251,128,114,0.75)"
        cell_c_1 = "rgba(251,128,114,0.5)"
        cell_c_2 = "rgba(251,128,114,0.25)"
    elif fuel_type == 'gases':
        df = d.df_gas
        table_title = "CO₂ Emissions from the Energy Use of Gaseous Fossil Fuels"
        header_color = "rgba(190,186,218,0.75)"
        cell_c_1 = "rgba(190,186,218,0.5)"
        cell_c_2 = "rgba(190,186,218,0.25)"
    else :
        df = d.df_total
        table_title = "CO₂ Emissions from the Energy Use of Fossil Fuels and Cement Manufacture"
        header_color = "rgba(217,217,217,0.75)"
        cell_c_1 = "rgba(217,217,217,0.5)"
        cell_c_2 = "rgba(217,217,217,0.25)"
    
    # Set a maximum width for columns and enable word wrap
    style = {
        'maxWidth': 200,
        'whiteSpace': 'normal',
    }

    textColor = "black"
    cellsBackground = "rgba(0,0,0,0)"

    if theme == 'dark' :
        textColor = "white"

    return dash.html.Div(
        id="table-container",
        children = [
            dash.html.H1(table_title),
            dash.dash_table.DataTable(
                df.to_dict('records'),
                [{'name': i, 'id': i} for i in df.columns],
                style_table={
                    'overflowX': 'auto', 
                    },
                style_cell=style,  # Apply style to all cells
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                editable=False,
                fill_width = False,
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': cell_c_1,
                    },
                    {
                        'if': {'row_index': 'even'},
                        'backgroundColor': cell_c_2,
                    }
                ],
                style_header={
                    'font-family': 'Helvetica, sans-serif', 
                    'textAlign': 'center',
                    'font-size': '20px',
                    'backgroundColor': header_color,
                    'color': textColor,
                    'padding' : '15px'
                },
                style_data={
                    'font-family': 'Helvetica, sans-serif', 
                    'font-size': '18px',
                    'backgroundColor': cellsBackground,
                    'color': textColor
                }
            ),
        ]
    )

@dash.callback(dash.Output('output-data-upload', 'children'),
               dash.Input('theme_toggle', 'className'),
              dash.Input('fuel-type-dropdown-controler', 'value'),
              )
def update_output(theme, fuel_type):
    return parse_contents(theme, fuel_type)