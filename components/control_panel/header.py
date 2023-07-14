"""
Module/Script Name: header.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/29/2023
Version: 1.0

Defines the style, layout, and callback functionality of the 
compoent described by the title of this file.

Callback methods: 0

"""

# Import Dependencies
import dash.html

# STYLES (JSON CSS)

styles = {
    'header': {
        'padding': '0px',
        'background' : '#222',
        'color' : '#fff',
        'text-align' : 'center',
        'border': '1px solid #ffc900',
        'border-top-left-radius' : '10px',
        'border-top-right-radius' : '10px'
    }
}

# LAYOUT

layout = dash.html.Div(

    className='header',

    style=styles['header'],

    children=[

        # Appstate Logo and Link

        dash.html.A(
            href = "https://www.appstate.edu",

            style = {
                "text-align": "center", 
                "display": "block", 
                'border-bottom' : '1px solid #ffc900',
                'background' : '#000',
                'border-top-left-radius' : '12px',
                'border-top-right-radius' : '12px'
            },

            children=[

                dash.html.Img(
                    src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",
                    style={"height": "30px", "display": "inline-block", 'margin' : '10px'}
                )

            ]

        ),

        # Title

        dash.html.H2("Carbon Dioxide Information Analysis Center (CDIAC) at AppState")
    ]

)

# CALLBACKS (0)
