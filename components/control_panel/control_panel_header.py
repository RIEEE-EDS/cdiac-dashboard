"""
This module defines the header for the control panel of the CDIAC Dashboard. It includes branding
and navigation elements such as the Appalachian State University logo and a title for the application.

Attributes
----------
layout : dash.html.Div
    The primary HTML container for the control panel header, which includes a link to the
    Appalachian State University homepage and displays the application's title as configured
    in the constants module.

component_id : str
    The identifier for the control panel header, used for targeting with callbacks and styling.

See Also
--------
components.utils.constants : Module where the application's title and other constants are defined.

Notes
-----
The header is an important part of the user interface, providing not only branding and identity to
the application but also offering a consistent and familiar navigation point for users.

Examples
--------
The layout of the control panel header is straightforward, aiming to offer a clear and
unobtrusive user experience:

>>> layout = dash.html.Div(
        id=component_id,
        children=[
            dash.html.A(
                href="https://www.appstate.edu",
                children=[
                    dash.html.Img(
                        src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",
                    )
                ]
            ),
            dash.html.H1(application_title),
        ]
    )
"""


# Component ID (Should be the same as the title of this file)
component_id = "control_panel_header"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
from components.utils.constants import application_title

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # Appstate Logo and Link

        dash.html.A(

            href = "https://www.appstate.edu",

            children=[

                dash.html.Img(

                    src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",

                )

            ]

        ),

        # Title

        dash.html.H1(application_title),

    ]
)

# CALLBACKS (0)
