"""
This module defines the main container of the application which serves as the central
layout component that includes the control panel and the content display areas.

Functions
---------
sunburst_no_loading(nav_opt)
    Dynamically loads content into the main container based on navigation options
    without displaying a loading spinner for certain views.

theme_toggle(theme)
    Changes the theme of the main container and its child components based on
    user interaction with the theme toggle control.

Attributes
----------
layout : dash.html.Div
    Defines the layout of the main container which includes the control panel and
    areas for loading and non-loading content.

component_id : str
    The identifier for the main container, used for targeting with callbacks and styling.

See Also
--------
components.control_panel.panel_container : Module containing the layout and functionality of the control panel.
components.content_display.display_container : Module containing the layout and functionality of the content display.

Notes
-----
This module is crucial for integrating the control and display components into a single
cohesive unit. Proper functioning of callbacks in this module ensures that user interactions
are effectively translated into visual changes on the dashboard.

Examples
--------
The layout is structured to include both a control panel and a dynamic content display area,
which updates based on the user's navigation choices. Here's how the layout is defined:

>>> layout = dash.html.Div(
        id=component_id,
        className='light',
        children=[
            control_panel.layout,
            dash.dcc.Loading(
                fullscreen=True,
                style={'background-color': 'white'},
                id='loading-content',
                type='graph',
                children=[]
            ),
            dash.html.Div(
                id='non-loading-content',
                children=[]
            )
        ]
    )

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
    """
    Handles dynamic loading of content based on the selected navigation option without
    showing a loading spinner for specified views.

    This function is responsible for managing the visibility of content in the
    `loading-content` and `non-loading-content` areas of the application's main container.
    It selectively disables the loading spinner for views that include elements like year sliders
    where immediate feedback is required without the obstruction of a loading indicator.

    Parameters
    ----------
    nav_opt : str
        The current value of the navigation dropdown that determines which content
        should be displayed in the main container.

    Returns
    -------
    tuple of (list, dash component)
        The first element of the tuple is the content for the 'loading-content' Div,
        which will be an empty list when the loading spinner should be hidden.
        The second element is either the layout from `display_container` if content is to be
        displayed without a loader, or an empty list otherwise.

    Examples
    --------
    When a navigation option that does not require a loading spinner is selected, the function
    returns an empty list for the `loading-content` and the respective display layout for the
    `non-loading-content`:

    >>> sunburst_no_loading('year_slider_view')
    ([], display_container.layout)

    If the navigation option requires a loading spinner, the function returns the display layout
    for the `loading-content` and an empty list for the `non-loading-content`:

    >>> sunburst_no_loading('default_view')
    (display_container.layout, [])

    """

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