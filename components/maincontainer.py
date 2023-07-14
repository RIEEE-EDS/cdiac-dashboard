"""
Module/Script Name: maincontainer.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0

Defines the style, layout, and callback functionality of the main container of the application.

Callback methods: 0

"""

# Import Dependencies
import dash.html.Div
import components.sidebar as sidebar
import components.contentarea as contentarea

# STYLES (JSON CSS)

styles = {
    'main-container': {
        # Flow, Size and Function
        'display': 'flex',
        'flex-flow' : 'row nowrap',
        'justify-content' : 'center',
        'align-items' : 'stretch',
        'height': '95vh',

        # Color and Fonts
        'background-color' : '#fff',
        'font-size' : '15px',
        'font-family' : '"Open Sans",sans-serif'
    }
}

# LAYOUT

layout = dash.html.Div(

    # MAIN APPLICATION CONTAINER

    className = 'main-container',
    
    style = styles['main-container'],
    
    children= [

        # SIDEBAR

        sidebar.layout,

        # Content Area

        contentarea.layout

    ]
)

# CALLBACKS (0)
