"""
Module/Script Name: browse.py

Author(s): M. W. Hefner

Initially Created: 7/15/2023

Last Modified: 10/29/2023

Script Description: This script defines the upload csv/excel component and dash datatable.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

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
        header_color = "rgba(217,95,2,0.75)"
        cell_c_1 = "rgba(217,95,2,0.5)"
        cell_c_2 = "rgba(217,95,2,0.25)"
    elif fuel_type == 'liquids':
        df = d.df_liquid
        table_title = "CO₂ Emissions from the Energy Use of Liquid Fossil Fuels"
        header_color = "rgba(117,112,179,0.75)"
        cell_c_1 = "rgba(117,112,179,0.5)"
        cell_c_2 = "rgba(117,112,179,0.25)"
    elif fuel_type == 'gases':
        df = d.df_gas
        table_title = "CO₂ Emissions from the Energy Use of Gaseous Fossil Fuels"
        header_color = "rgba(27,158,119,0.75)"
        cell_c_1 = "rgba(27,158,119,0.5)"
        cell_c_2 = "rgba(27,158,119,0.25)"
    else :
        df = d.df_total
        table_title = "CO₂ Emissions from the Energy Use of Fossil Fuels and Cement Manufacture"
        header_color = "rgba(231,41,138,0.75)"
        cell_c_1 = "rgba(231,41,138,0.5)"
        cell_c_2 = "rgba(231,41,138,0.25)"
    
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