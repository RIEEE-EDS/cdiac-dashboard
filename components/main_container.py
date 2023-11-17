"""
Module/Script Name: maincontainer.py

Author(s): M. W. Hefner

Initially Created: 6/28/2023

Last Modified: 10/29/2023

Script Description: This script defines the logical layout and callback functionality of the main container of the application.  This container holds all the other html tags and is the child of the secure-container Div tag in the app.layout if and only if the user is authorized.

Exceptional notes about this script:
1.  dcc.Loading doesn't actually create an HTML tag of its own, so it's necessary to handle its styling in the python code.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same or similar as the title of this file)
# This is used for css styling and callbacks.
component_id = "main_container"

# Import Dependencies
import dash.html.Div
import components.control_panel.panel_container as control_panel
import components.content_display.display_container as display_container

# LAYOUT
layout = dash.html.Div(

    id = component_id,
    
    className = 'light',

    children= [

        # control_panel

        control_panel.layout,

        # content_display

        dash.dcc.Loading(
            fullscreen = True,
            style = {'background-color' : 'white'},
            id = 'loading-content',
            type = 'graph',
            children = []
        ),

        dash.html.Div(
            id='non-loading-content',
            children = []
        )

    ]
)


# CALLBACKS (2)
@dash.callback(
    dash.dependencies.Output("loading-content", "children"),
    dash.dependencies.Output("non-loading-content", "children"),
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def sunburst_no_loading(nav_opt):
    # Handles situations where we do not want a dcc.loading screen to pop up
    # such as pages with year sliders
    if nav_opt in [] :
        return [], display_container.layout
    else :
        return display_container.layout, []

        
# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Output('loading-content', 'style'),
    dash.dependencies.Output('non-loading-content', 'style'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def theme_toggle(theme):
    """
    Updates this component's theme when the theme toggle is updated.

    Parameters
    ----------
    
    theme : string
        The input used to trigger the callback (when the theme's class changes).

    Returns
    -------

    string
        Used to update the url's hash state to prevent memorization.

    json
        directly returns what the dcc.Loading's CSS should be since it must be defined with Python.

    """
    if theme == 'light' :
        return theme, {'background-color' : 'white'}, {'background-color' : 'white'}
    else :
        return theme, {'background-color' : 'black'}, {'background-color' : 'black'}