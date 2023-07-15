"""
Module/Script Name: browse.py
Author: M. W. Hefner

Created: 7/15/2023
Last Modified: 7/15/2023

Project: CDIAC at AppState

Script Description: This script defines the dash datatable and its container used for the browse page.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""
# Component ID (Should be the same as the title of this file)
component_id = "browse"

# Import Dependencies
import dash.html.Div
import dash.html.P
import dash.dash_table.DataTable
from components.staticdata import data as d

def browse_table(fuel_type, source) :

    if fuel_type == 'solids':
        df = d.df_solid
    elif fuel_type == 'liquids':
        df = d.df_liquid
    elif fuel_type == 'gases':
        df = d.df_gas
    else :
        df = d.df_total

    df = df[df[source].notnull()]

    return dash.html.Div(
        id = component_id,
        className = "table_container",
        children = [
            # TODO: Look into styling this page better.
            # Do dash.data_table/s play nice with css?
            dash.html.P('Use the sidebar dropdowns to select data.  Filter and sort below.  Inequality filters (e.g. ">2005" for Year) are supported.'),
            dash.html.P('All values are in Thousand Metric Tons of Carbon (ktC)'),
            dash.dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in ["Nation", "Year", source]],
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                page_size= 15,
            )
        ]
    )