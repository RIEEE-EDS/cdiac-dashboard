"""
Module/Script Name: backtodatadash.py
Author: M. W. Hefner

Created: 6/29/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the backtodatadash link area.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "backtodatadash"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# STYLES (CSS DICT)
styles = {
    component_id : {

    }
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles[component_id],
    children= [

        dash.html.P("This dashboard is powered and supported by the Research Institute for Environment, Energy, and Economics at Appalachian State University.", style = {'text-align' : 'center'}),

        dash.html.H3(

            children = [

                dash.html.A(
                    "↖ Back to DataDash",
                    
                    href = "https://www.appstate.edu"
                )
                
            ], 
            
            style = {'text-align' : 'center'}

        ),

    ]
)

# CALLBACKS (0)
