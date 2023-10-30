"""
Module/Script Name: application.py

Author(s): M. W. Hefner

Initially Created: 6/28/2023

Last Modified: 10/29/2023

Script Description: This script initializes the dash application. It loads in needed libraries, reads the data server configuration, loads style sheets, and initializes the server.  It also contains the scripting that authorizes a user to access the application.

Exceptional notes about this script:

1. Using this script for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# !!! IMPORTANT: CHANGE TO FALSE BEFORE PUSHING !!!
LOCAL_DEVELOPMENT = False
# !!! IMPORTANT: CHANGE TO FALSE BEFORE PUSHING !!!

# Import Dependencies
import dash
import secrets
import configparser
import components.main_container as mc
import components.utils.login as login
from components.utils.constants import application_title, repo_title

# Read data server configuration
cfg = configparser.ConfigParser()
cfg.read('/etc/rieee/rieee.conf')
cfg.read('rieee.conf')

# CSS Styles
external_stylesheets = {
    'datadash_template_css' : [
        "./assets/externalstylesheets/styles.css"
    ]
}

# Initialize Dash Application
app = dash.Dash(
    __name__, 
    external_stylesheets = external_stylesheets['datadash_template_css'],
    title = application_title,
    update_title = None,
    url_base_pathname=cfg.get('app', 'url_prefix', fallback='/'),
    # / DEVELOPER NOTE
    # /
    # /  We have to supress callback exceptions
    # /  (callouts are defined to an application
    # /  app.server at start-up, on the server end,
    # /  but app.layout, sent to the client _before_ auth,
    # /  will not initially have many of the elements with IDs
    # /  in order to prevent sending unauthorized users
    # /  application information in the layout)
    # /
    # /- M W HEFNER 10/24/2023
    suppress_callback_exceptions=True
)

# Define Layout of the Dash Application
app.layout = dash.html.Div(
    children = [
        # A location object tracks the address bar url
        dash.dcc.Location(id='url'),
        # A data component stores a hash to prevent memorization
        dash.dcc.Store(data = secrets.token_hex(), id='memory'),
        # Secure container
        dash.html.Div(id='secure-div'),
        # Interval for live update data
        dash.dcc.Interval(
            id='interval-component',
            # in milliseconds
            interval=1000, # (1 second)
            n_intervals=0
        )
    ],
)

# Create a page for Shibboleth Sign-On if the user is not authorized
shibbSignOnLayout = dash.html.P(
    [
        "This application is not available. If you have authorization, please ",
        dash.html.A(
            "sign in with Shibboleth", 
            href = "/Shibboleth.sso/Login?target=/" + repo_title, 
        ),
        " to access this RIEEE DataDash application.  If you believe you are seeing this in error, please contact the RIEEE DataDash webmaster."
    ],
    style={'text-align' : 'center'}
)

@dash.callback(
    dash.Output('secure-div', 'children'),
    dash.Output('memory', 'data'),
    dash.Input('url', 'pathname'),
    dash.State('memory', 'data'),
    cache_timeout = 0
)
def authorize(pathname, hash):
    """
    Checks to see if the user is authorized and returns 
    the main container as the app layout if so.
    
    This is called any time there is a change to the url.
    
    The second input is to prevent memorization.

    Parameters
    ----------
    pathname : string
        The input used to trigger the authorization callback.

    hash : string
        State context used simply to prevent memorization.  
        There is nothing inherently sensitive about the hash.

    Returns
    -------
    dash.html.Div
        If authorized, the first return item is the layout of the application.
        If not, it returns the sign-on page.

    string
        Used to update the state to prevent memorization.

    """
    # Application Authorization Token (for preventing memorization)
    authorizationToken = secrets.token_hex()

    if login.userIsAuthorized() or LOCAL_DEVELOPMENT:
        # If the user is authorized, or this is for local development:
        return mc.layout, authorizationToken
    else :
        # If the user is not authorized, provide them with a shibboleth sign-on
        return shibbSignOnLayout, authorizationToken

# Boilerplate index HTML
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Name the app.server server
# Corresponds to application:server (thisScript:app.server) in the docker file
server = app.server

# Main script execution for (local development only)
if __name__ == '__main__' and LOCAL_DEVELOPMENT:
    # True for hot reloading (leave True)
    app.run_server(debug = True)
