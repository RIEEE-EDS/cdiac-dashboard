"""
This module provides centralized management of constants used across the Dash application,
including predefined paths, data file names, application metadata, and utility functions for data processing.
It facilitates consistent access to these constants throughout the application, ensuring that changes in one place
reflect across all components that use them.

Attributes
----------
application_title : str
    The title of the application displayed in the browser's title bar and possibly within the app.
app_id : int
    A unique identifier for the application, used for internal management and possibly for authorization checks.
repo_title : str
    A short identifier or name for the repository or project associated with this application.
app_doi : str
    Digital Object Identifier (DOI) for referencing the application, often used for citation or version control.
developers : str
    Names of the developers or contributors to the application, used for credits or debug information.
version : str
    Version identifier of the application, helpful for tracking updates and changes.
data_file : str
    Name of the primary data file containing CO₂ emissions data, used throughout the application to load data.
zonodo_doi_badge : dash.html.A
    An HTML component displaying a DOI badge linking to the application's DOI page, providing citation information.
show_credit : bool
    A flag determining whether to show developer credits in the application, useful for presentations or anonymous usage.
location_mapping : dict
    A dictionary mapping geographical locations to their short codes, facilitating data handling and visualization.
df_total : pandas.DataFrame
    DataFrame loaded with total CO₂ emissions data from the specified Excel sheet.
df_solid : pandas.DataFrame
    DataFrame loaded with solid fuel CO₂ emissions data.
df_liquid : pandas.DataFrame
    DataFrame loaded with liquid fuel CO₂ emissions data.
df_gas : pandas.DataFrame
    DataFrame loaded with gas fuel CO₂ emissions data.
regionLookup : pandas.DataFrame
    DataFrame containing mappings of countries to their respective regions, used for regional analysis and filtering.
about_content : str
    Content of the 'About' page, loaded from a markdown file.
methodology_content : str
    Content of the 'Methodology' page, detailing the methods used in the application, loaded from a markdown file.
download_content : str
    Content of the 'Download' page, providing download options and information, loaded from a markdown file.

Examples
--------
To access the application title within another module of the application:

>>> from constants import application_title
>>> print(application_title)

This module plays a crucial role in maintaining the integrity and consistency of application-wide settings and data,
thereby reducing redundancy and potential errors from mismanaged constants or repeated code segments.

See Also
--------
pandas : For managing data in DataFrame formats.
dash.html : For creating HTML components in the Dash application.
"""


# Import Dependencies
import pandas as pd
import math
import dash.html

# IN-LINE APPLICATION METADATA----------------------------------------

# SETS THE TITLE OF THE APPLICATION
application_title = "The CDIAC at AppState Dashboard"

# SET THE APPLICATION ID (APPLICATION METADATA USED FOR AUTHORIZATION)
app_id = 4

# SET THE REPO TITLE (APPLICATION METADATA USED FOR AUTHORIZATION)
repo_title = "cdiac"

app_doi = "FINAL PRE-PUBLICATION"

developers = "Matt Hefner"

# 1. Update the version
version = "2023"

# 2. Update the data file name
data_file = "CDIAC_Sectoral_Inventory_1995_2020.xlsx"

zonodo_doi_badge = dash.html.A(
    dash.html.Img(

        # 4. a) Update the badge SVG

        src='https://zenodo.org/badge/666200101.svg'
    ), 

    # 4. b) Update the badge DOI
    href = "https://zenodo.org/doi/10.5281/zenodo.10607881",

    style={'display': 'block', 'margin': 'auto'}
)

# For showing in conexts where you do not wish to be doxed
# i.e. presentations in anonymous contexts
show_credit = True

# Location map for carbon atlas
location_mapping = {
    'WORLD': 'World',
    'AFRICA': 'AFR',
    'NORTH AMERICA': 'NAM',
    'AFGHANISTAN': 'AFG',
    'SOUTH AMERICA': 'SAM',
    'ASIA': 'ASI',
    'EUROPE': 'EUR',
    'ALBANIA': 'ALB',
    'OCEANIA': 'OCE',
    'ALGERIA': 'DZA',
    'AMERICAN SAMOA': 'ASM',
    'ANDORRA': 'AND',
    'ANGOLA': 'AGO',
    'ANTIGUA & BARBUDA': 'ATG',
    'AZERBAIJAN': 'AZE',
    'ARGENTINA': 'ARG',
    'AUSTRALIA': 'AUS',
    'AUSTRIA': 'AUT',
    'BAHAMAS': 'BHS',
    'BAHRAIN': 'BHR',
    'BANGLADESH': 'BGD',
    'ARMENIA': 'ARM',
    'BARBADOS': 'BRB',
    'BELGIUM': 'BEL',
    'BERMUDA': 'BMU',
    'BHUTAN': 'BTN',
    'PLURINATIONAL STATE OF BOLIVIA': 'BOL',
    'BOSNIA & HERZEGOVINA': 'BIH',
    'BOTSWANA': 'BWA',
    'BRAZIL': 'BRA',
    #'ANTARCTIC FISHERIES': 'ATA', # Excluded for now
    'BELIZE': 'BLZ',
    'BRITISH INDIAN OCEAN TERRITORIES': 'IOT',
    'SOLOMON ISLANDS': 'SLB',
    'BRITISH VIRGIN ISLANDS': 'VGB',
    'BRUNEI (DARUSSALAM)': 'BRN',
    'BULGARIA': 'BGR',
    'MYANMAR (FORMERLY BURMA)': 'MMR',
    'BURUNDI': 'BDI',
    'BELARUS': 'BLR',
    'CAMBODIA': 'KHM',
    'REPUBLIC OF CAMEROON': 'CMR',
    'CANADA': 'CAN',
    'CAPE VERDE': 'CPV',
    'CAYMAN ISLANDS': 'CYM',
    'CENTRAL AFRICAN REPUBLIC': 'CAF',
    'SRI LANKA': 'LKA',
    'CHAD': 'TCD',
    'CHILE': 'CHL',
    'CHINA (MAINLAND)': 'CHN',
    'TAIWAN': 'TWN',
    'CHRISTMAS ISLAND': 'CXR',
    'COLOMBIA': 'COL',
    'COMMONWEALTH OF INDEPENDENT STATES (CIS)': 'CIS',
    'COMOROS': 'COM',
    'MAYOTTE': 'MYT',
    'CONGO': 'COG',
    'DEMOCRATIC REPUBLIC OF THE CONGO (FORMERLY ZAIRE)': 'COD',
    'COOK ISLANDS': 'COK',
    'COSTA RICA': 'CRI',
    'CROATIA': 'HRV',
    'CUBA': 'CUB',
    'CYPRUS': 'CYP',
    'CZECHOSLOVAKIA': 'CZE',
    'CZECH REPUBLIC': 'CZE',
    'BENIN': 'BEN',
    'DENMARK': 'DNK',
    'DOMINICA': 'DMA',
    'DOMINICAN REPUBLIC': 'DOM',
    'ECUADOR': 'ECU',
    'EL SALVADOR': 'SLV',
    'EQUATORIAL GUINEA': 'GNQ',
    'ETHIOPIA': 'ETH',
    'ERITREA': 'ERI',
    'ESTONIA': 'EST',
    'FAEROE ISLANDS': 'FRO',
    'FALKLAND ISLANDS (MALVINAS)': 'FLK',
    'FIJI': 'FJI',
    'FINLAND': 'FIN',
    'ALAND ISLANDS': 'ALA',
    'FRANCE': 'FRA',
    'FRANCE (INCLUDING MONACO)': 'FRA',
    'FRENCH GUIANA': 'GUF',
    'FRENCH POLYNESIA': 'PYF',
    'DJIBOUTI': 'DJI',
    'FRENCH EQUATORIAL AFRICA': 'ATF',
    'FRENCH INDO-CHINA': 'ATF',
    'GABON': 'GAB',
    'FRENCH WEST AFRICA': 'ATF',
    'GEORGIA': 'GEO',
    'GAMBIA': 'GMB',
    'OCCUPIED PALESTINIAN TERRITORY': 'PSE',
    'GERMANY': 'DEU',
    'FORMER GERMAN DEMOCRATIC REPUBLIC': 'DEU',
    'FEDERAL REPUBLIC OF GERMANY': 'DEU',
    'GHANA': 'GHA',
    'GIBRALTAR': 'GIB',
    'KIRIBATI': 'KIR',
    'GREECE': 'GRC',
    'GREENLAND': 'GRL',
    'GRENADA': 'GRD',
    'GUADELOUPE': 'GLP',
    'GUAM': 'GUM',
    'GUATEMALA': 'GTM',
    'GUINEA': 'GIN',
    'GUYANA': 'GUY',
    'HAITI': 'HTI',
    'HONDURAS': 'HND',
    'HONG KONG SPECIAL ADMINSTRATIVE REGION OF CHINA': 'HKG',
    'HUNGARY': 'HUN',
    'ICELAND': 'ISL',
    'INDIA': 'IND',
    'INDONESIA': 'IDN',
    'ISLAMIC REPUBLIC OF IRAN': 'IRN',
    'IRAQ': 'IRQ',
    'IRELAND': 'IRL',
    'ISRAEL': 'ISR',
    'ITALY': 'ITA',
    'ITALY (INCLUDING SAN MARINO)': 'ITA',
    'COTE D IVOIRE': 'CIV',
    'JAMAICA': 'JAM',
    'JAPAN': 'JPN',
    'JAPAN (INCLUDING OKINAWA)': 'JPN',
    'KAZAKHSTAN': 'KAZ',
    'JORDAN': 'JOR',
    'KENYA': 'KEN',
    'KOREA, NORTH': 'PRK',
    'KOREA, SOUTH': 'KOR',
    'KUWAIT': 'KWT',
    'KYRGYZSTAN': 'KGZ',
    'LAO PEOPLE S DEMOCRATIC REPUBLIC': 'LAO',
    'LEBANON': 'LBN',
    'LESOTHO': 'LSO',
    'LATVIA': 'LVA',
    'LIBERIA': 'LBR',
    'LIBYAN ARAB JAMAHIRIYA': 'LBY',
    'LIECHTENSTEIN': 'LIE',
    'LITHUANIA': 'LTU',
    'LUXEMBOURG': 'LUX',
    'MACAO': 'MAC',
    'MADAGASCAR': 'MDG',
    'MALAWI': 'MWI',
    'MALAYSIA': 'MYS',
    'MALDIVES': 'MDV',
    'MALI': 'MLI',
    'MALTA': 'MLT',
    'MARTINIQUE': 'MTQ',
    'MAURITANIA': 'MRT',
    'MAURITIUS': 'MUS',
    'MEXICO': 'MEX',
    'MOLDOVA': 'MDA',
    'MONACO': 'MCO',
    'MONGOLIA': 'MNG',
    'MONTENEGRO': 'MNE',
    'MOROCCO': 'MAR',
    'MOZAMBIQUE': 'MOZ',
    'OMAN': 'OMN',
    'NAMIBIA': 'NAM',
    'NAURU': 'NRU',
    'NEPAL': 'NPL',
    'NETHERLANDS': 'NLD',
    'NETHERLANDS ANTILLES': 'ANT',
    'ARUBA': 'ABW',
    'NEW CALEDONIA': 'NCL',
    'VANUATU': 'VUT',
    'NEW ZEALAND': 'NZL',
    'NICARAGUA': 'NIC',
    'NIGER': 'NER',
    'NIGERIA': 'NGA',
    'NIUE': 'NIU',
    'NORTHERN MARIANA ISLANDS': 'MNP',
    'NORWAY': 'NOR',
    'FORMER YUGOSLAV REPUBLIC OF MACEDONIA': 'MKD',
    'MALAYA': 'MYS',
    'MICRONESIA, FEDERATED STATES OF': 'FSM',
    'MARIANA ISLANDS': 'MNP',
    'PAKISTAN': 'PAK',
    'PALAU': 'PLW',
    'PANAMA': 'PAN',
    'PAPUA NEW GUINEA': 'PNG',
    'PARAGUAY': 'PRY',
    'PERU': 'PER',
    'PHILIPPINES': 'PHL',
    'PITCAIRN': 'PCN',
    'POLAND': 'POL',
    'PORTUGAL': 'PRT',
    'GUINEA-BISSAU': 'GNB',
    'TIMOR-LESTE': 'TLS',
    'PUERTO RICO': 'PRI',
    'QATAR': 'QAT',
    'REUNION': 'REU',
    'ROMANIA': 'ROU',
    'RUSSIAN FEDERATION': 'RUS',
    'RWANDA': 'RWA',
    'SAINT HELENA': 'SHN',
    'SAINT KITTS & NEVIS': 'KNA',
    'ANGUILLA': 'AIA',
    'SAINT LUCIA': 'LCA',
    'SAINT PIERRE & MIQUELON': 'SPM',
    'SAINT VINCENT & THE GRENADINES': 'VCT',
    'SAN MARINO': 'SMR',
    'SAO TOME & PRINCIPE': 'STP',
    'SAUDI ARABIA': 'SAU',
    'SENEGAL': 'SEN',
    'SERBIA': 'SRB',
    'SEYCHELLES': 'SYC',
    'SIERRA LEONE': 'SLE',
    'SINGAPORE': 'SGP',
    'SLOVAKIA': 'SVK',
    'VIET NAM': 'VNM',
    'SLOVENIA': 'SVN',
    'SOMALIA': 'SOM',
    'REPUBLIC OF YEMEN': 'YEM',
    'SOUTH AFRICA': 'ZAF',
    'ZIMBABWE': 'ZWE',
    'SPAIN': 'ESP',
    'SPANISH NORTH AFRICA': 'ESP',
    'WESTERN SAHARA': 'ESH',
    'SUDAN': 'SDN',
    'SURINAME': 'SUR',
    'SWAZILAND': 'SWZ',
    'SWEDEN': 'SWE',
    'SWITZERLAND': 'CHE',
    'SYRIAN ARAB REPUBLIC': 'SYR',
    'TAJIKISTAN': 'TJK',
    'THAILAND': 'THA',
    'TOGO': 'TGO',
    'TONGA': 'TON',
    'TRINIDAD & TOBAGO': 'TTO',
    'UNITED ARAB EMIRATES': 'ARE',
    'TUNISIA': 'TUN',
    'TURKEY': 'TUR',
    'TURKMENISTAN': 'TKM',
    'TURKS & CAICOS ISLANDS': 'TCA',
    'TUVALU': 'TUV',
    'UGANDA': 'UGA',
    'UKRAINE': 'UKR',
    'SOVIET UNION': 'SUN',
    'THE FORMER YUGOSLAV REPUBLIC OF MACEDONIA': 'MKD',
    'EGYPT': 'EGY',
    'UNITED KINGDOM': 'GBR',
    'GUERNSEY': 'GGY',
    'JERSEY': 'JEY',
    'ISLE OF MAN': 'IMN',
    'TANZANIA': 'TZA',
    'UNITED STATES OF AMERICA': 'USA',
    'VIRGIN ISLANDS OF THE UNITED STATES': 'VIR',
    'BURKINA FASO': 'BFA',
    'URUGUAY': 'URY',
    'UZBEKISTAN': 'UZB',
    'VANUATU': 'VUT',
    'VATICAN CITY': 'VAT',
    'VENEZUELA': 'VEN',
    'WALLIS & FUTUNA ISLANDS': 'WLF',
    'SAMOA': 'WSM',
    'YEMEN': 'YEM',
    'SERBIA & MONTENEGRO': 'SCG',
    'ZAMBIA': 'ZMB',
    'ZANZIBAR': 'TZA'
}

def round_down(x):
    if isinstance(x, (int, float)) and not math.isnan(x):
        return round(x)
    else:
        return x
    
# Load TOTAL sheet
df_total = pd.read_excel('assets/data/' + data_file, sheet_name='TOTALS')

# Rounding Down
#
# Something that was briefly considered during development. Still unsure.
#
# Round down
#df_total = df_total.applymap(round_down)

# Load SOLID FUELS sheet (also used for LIQUID FUELS sheet)
df_solid = pd.read_excel('assets/data/' + data_file, sheet_name='SOLID FUELS')

# Round down
#df_solid = df_solid.applymap(round_down)

# Load LIQUID FUELS sheet (also used for LIQUID FUELS sheet)
df_liquid = pd.read_excel('assets/data/' + data_file, sheet_name='LIQUID FUELS')

# Round down
#df_liquid = df_liquid.applymap(round_down)

# Load GAS FUELS sheet (also used for LIQUID FUELS sheet)
df_gas = pd.read_excel('assets/data/' + data_file, sheet_name='GAS FUELS')

# Load region lookup
regionLookup = pd.read_excel('assets/data/Region_Lookup.xlsx')

""" CLEAN DATA -----

This section cleans the CDIAC data to be used easily by the dash application.

"""

# For mapping source to source between sheets when a different fuel type is selected
def best_match_option(value, fuel_type):

    # Are we coming from the totals sheet?  Assume first no
    from_totals = False
    
    # If the value of the source is in the solid df's columns,
    if (value in df_solid.columns) : 
        # Then see where that's at (index of the column)
        from_index = df_solid.columns.get_loc(value)
    else :
        # Then we're coming from totals.  Get its index
        from_index = df_total.columns.get_loc(value)
        from_totals = True

    # If we're coming from totals and we want to go to totals,
    # return the value
    if (from_totals and fuel_type == 'totals') :
        return value
    
    # If we're coming from totals and we want to go somewhere else,
    if (from_totals and fuel_type != 'totals') :
        # If you're between indexes 3 ("Fossil Fuel Energy (Supplied)") 
        # and 21 ("Bunkered (Aviation)")
        # (index starting at zero)
        if (from_index >= 3 and from_index <= 20):
            # Return one below since totals has an extra
            return df_solid.columns[from_index - 1]
        else:
            # Just return the main total
            return df_solid.columns[2]

    # if you're coming from s/l/g and going to totals
    if (not from_totals and fuel_type == 'totals') :
        # return one over since totals has an extra
        return df_total.columns[from_index + 1]

    return value


# Read Markdown Pages-------------------------------

# About page
with open("./assets/markdown/about.md", "r") as file:
    about_content = file.read()

# About page
with open("./assets/markdown/methodology.md", "r") as file:
    methodology_content = file.read()

# Download page
with open("./assets/markdown/download.md", "r") as file:
    download_content = file.read()

