"""
This module is responsible for reading and loading configuration settings from an external file. It
utilizes Python's configparser library to parse configuration files, enabling centralized management
of settings required throughout the Dash application.

Attributes
----------
cfg : configparser.ConfigParser
    An instance of ConfigParser that is used to read and parse the configuration files located
    at specified paths. This object stores all the configuration settings that can be accessed
    by other parts of the application.

Methods
-------
cfg.read(filenames)
    Reads and parses a list of filenames given as input, interpreting the file content as configuration data.

Examples
--------
To access a configuration value for the database connection string from within another module:

>>> import config
>>> db_connection_string = config.cfg['Database']['ConnectionString']

This allows various parts of the application to maintain consistency in configuration management and usage,
providing a robust mechanism for handling environment-specific settings such as database connections,
API keys, or custom application parameters.

Notes
-----
The module reads from a default system path '/etc/rieee/rieee.conf' and a local fallback 'rieee.conf'.
It is designed to gracefully handle missing files or settings by ignoring missing paths and using
default settings where applicable.

The use of configparser makes it easy to store and organize database credentials.

See Also
--------
configparser.ConfigParser : The class used for parsing a list of configuration files into a structured configuration object.
"""


import configparser

cfg = configparser.ConfigParser()
cfg.read('/etc/rieee/rieee.conf')
cfg.read('rieee.conf')
