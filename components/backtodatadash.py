"""
Module/Script Name: optionscontainer.py
Author: M. W. Hefner
Created: 6/29/2023
Last Modified: 6/29/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 0

"""

# Import Dependencies
import dash

styles = {
    'datadash-link' : {
        'padding': '0px',
        'background' : '#222',
        'color' : '#fff',
        'border-radius' : '10px',
        'text-align' : 'center',
        'border': '1px solid #ffc900',
    }
}

layout = dash.html.Div(

    children = [

        dash.html.P("This dashboard is powered and supported by the Research Institute for Environment, Energy, and Economics at Appalachian State University.", style = {'text-align' : 'center'}),

        dash.html.H3(

            children = [

                dash.html.A(
                    "↖ Back to DataDash",
                    
                    href = "https://www.appstate.edu"
                )
                
            ], 
            
            style = {'text-align' : 'center'}

        )

    ]
)