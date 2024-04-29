"""
Initializes the Dash application, manages user authorization, and defines the application layout.
This script loads necessary libraries, reads data server configuration, initializes the server,
and handles user authentication and authorization.

Functions
---------
authorize(pathname: str, hash: str) -> Tuple[dash.html.Div, str]
    Checks if the user is authorized to access the application based on the current pathname.
    Returns the main container layout if authorized; otherwise, redirects to the Shibboleth sign-on page.
    Updates the state to prevent memorization.

Notes
-----
- This script serves as the entry point for the Dash application, defining the application layout
  and managing user authorization.
- Local development mode is enabled if the `REDIS_URL` environment variable is not present,
  allowing the application to run on localhost for development purposes.
- The `authorize` function is used as a callback to dynamically update the application layout
  based on the user's authorization status.
- The application layout is updated dynamically without page reloads, providing a seamless user experience.
- The index HTML template includes JavaScript code to adjust the height of the application layout
  dynamically based on the window size.  You can find accomp. javascript over in assets/js
- Error handling for database connections, user authorization, and server initialization is essential
  for ensuring the reliability and security of the application.

Dependencies
------------
dash : The main web application framework used for building the Dash application.
secrets : Provides access to cryptographically secure random numbers for generating authorization tokens.
configparser : Parses configuration files to read data server configuration settings.
components.main_container : Provides the layout for the main content container of the Dash application.
components.utils.login : Contains functions for user authorization and authentication.
components.utils.constants : Contains application-specific constants such as application_title and repo_title.
os : Provides access to operating system functionalities, used for environment variable detection.

See Also
--------
dash : The official Dash documentation for more information on building web applications with Dash.
secrets : Python documentation on the secrets module for generating secure random numbers.
configparser : Python documentation on the configparser module for reading configuration files.
"""


import os 

if 'REDIS_URL' in os.environ:

    # RUNNING ON SERVER

    LOCAL_DEVELOPMENT = False

else:

    # RUNNING ON A LOCAL MACHINE FOR DEVELOPMENT

    # NOTE: MUST BE CONNECTED TO APP'S VPN FOR THIS TO ACTUALLY DELIVER
    # THE APPLICATION'S CONTENTS TO THE BROWSER.

    LOCAL_DEVELOPMENT = True

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
    id='main-content'  # Ensure this matches the ID used in js/adjust_height.js
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <script>
        // JavaScript function to adjust the height of the application layout
        function adjustHeight() {
            const viewHeight = window.innerHeight + 'px';
            // The application layout must have the ID 'main-content'
            document.getElementById('main-content').style.height = viewHeight;
        }

        // Add event listeners to adjust height on page load and on window resize
        window.addEventListener('resize', adjustHeight);
        window.addEventListener('load', adjustHeight);
        </script>
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

# Main script execution (for local development)
if __name__ == '__main__' and LOCAL_DEVELOPMENT:
    # True for hot reloading (leave True)
    app.run_server(debug = True)
