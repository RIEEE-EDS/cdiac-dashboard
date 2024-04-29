"""
This module defines the layout and behavior of the control panel container in the CDIAC Dashboard.
The control panel container includes all user interface elements that allow user interactions for
data filtering and application control.

Functions
---------
update_source_dropdown(theme, panel_toggle_clicks)
    Updates the theme of the control panel container and manages the visibility state of the
    control panel based on user clicks on the panel toggle.

Attributes
----------
layout : dash.html.Div
    The main HTML container that holds the control panel components, including the header and
    control elements, conditionally displayed based on configuration settings.

component_id : str
    The identifier for the control panel container, used for targeting with callbacks and styling.

See Also
--------
components.control_panel.control_panel_header : Module providing the layout for the control panel header.
components.control_panel.controls_container : Module containing the interactive controls within the control panel.

Notes
-----
This module is central to user interaction, as it houses all the controls necessary for filtering
and adjusting the data visualizations displayed in the application.

Examples
--------
The layout is conditionally created based on the 'show_credit' setting from the constants module:

>>> if show_credit:
        layout = dash.html.Div(
            id=component_id,
            children=[
                control_panel_header.layout,
                controls_container.layout,
                dash.html.Div(id="control_panel_toggle")
            ]
        )
    else:
        layout = dash.html.Div(
            id=component_id,
            children=[
                controls_container.layout,
                dash.html.Div(id="control_panel_toggle")
            ]
        )
"""


# Component ID (Should be the same as the title of this file)
component_id = "panel_container"

# Import Dependencies
import dash.html.Div
import dash.exceptions
import components.control_panel.control_panel_header as control_panel_header
import components.control_panel.controls_container as controls_container
from components.utils.constants import show_credit

if show_credit :
# LAYOUT
    layout = dash.html.Div(
        id = component_id,
        children= [

            # HEADER
            control_panel_header.layout,

            # CONTROLS CONTAINER
            controls_container.layout,

            dash.html.Div(

                id = "control_panel_toggle"

            )

        ]
    )
    
else :

    layout = dash.html.Div(
        id = component_id,
        children= [

            # CONTROLS CONTAINER
            controls_container.layout,

            dash.html.Div(

                id = "control_panel_toggle"

            )

        ]
    )

# CALLBACKS (1)

# Controls Theme of component
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Output("control_panel_toggle", 'className'),
    dash.dependencies.Input('theme_toggle', 'className'),
    dash.dependencies.Input("control_panel_toggle", 'n_clicks')
)
def update_source_dropdown(theme, panel_toggle_clicks):
    """
    Toggles the CSS class of the control panel based on user interaction to expand or collapse
    the panel, while also updating the theme of the control panel.

    Parameters
    ----------
    theme : str
        The current theme setting (e.g., "light" or "dark") which affects the styling of
        the control panel.
    panel_toggle_clicks : int, optional
        The number of times the control panel toggle has been clicked by the user, which determines
        whether the panel is in an expanded or collapsed state.

    Returns
    -------
    tuple of (str, str)
        The updated class names for the panel container and the toggle element, reflecting the new
        theme and expanded/collapsed state.

    Notes
    -----
    The function checks the number of clicks on the toggle; an odd number of clicks implies a
    collapsed state, and an even number implies an expanded state. The theme is applied consistently
    regardless of the panel state.

    Examples
    --------
    >>> update_source_dropdown("light", 1)
    ('light collapsed', 'light collapsed')
    """

    if panel_toggle_clicks is None:
        return theme, theme
    elif panel_toggle_clicks % 2 == 1 :
        return theme + " collapsed", theme + " collapsed"
    else :
        return theme, theme