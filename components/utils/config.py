"""
Module/Script Name: config.py

Author(s): M. W. Hefner

Initially Created: 09/01/2023

Last Modified: 10/29/2023

Script Description: This scripts reads the configuration file.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

import configparser

cfg = configparser.ConfigParser()
cfg.read('/etc/rieee/rieee.conf')
cfg.read('rieee.conf')
