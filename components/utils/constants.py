"""
Module/Script Name: constants.py

Author(s): M. W. Hefner

Initially Created: 06/28/2023

Last Modified: 10/29/2023

Script Description: this script contains constants and calls for locally stored (on the application server) data.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
import pandas as pd
import math

# IN-LINE APPLICATION METADATA----------------------------------------

# SETS THE TITLE OF THE APPLICATION
application_title = "The CDIAC at AppState Dashboard"

# SET THE APPLICATION ID (APPLICATION METADATA USED FOR AUTHORIZATION)
app_id = 4

# SET THE REPO TITLE (APPLICATION METADATA USED FOR AUTHORIZATION)
repo_title = "cdiac"

app_doi = "NONE_FOR_TEMPLATE"

developers = "Matt Hefner, RIEEE Environmental Data Scientist"

version = "2023"

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
df_total = pd.read_excel('assets/data/National_Sectoral_2020.xlsx', sheet_name='TOTAL')

# Round down
#df_total = df_total.applymap(round_down)

# Load SOLID FUELS sheet (also used for LIQUID FUELS sheet)
df_solid = pd.read_excel('assets/data/National_Sectoral_2020.xlsx', sheet_name='SOLID FUELS')

# Round down
#df_solid = df_solid.applymap(round_down)

# Load LIQUID FUELS sheet (also used for LIQUID FUELS sheet)
df_liquid = pd.read_excel('assets/data/National_Sectoral_2020.xlsx', sheet_name='LIQUID FUELS')

# Round down
#df_liquid = df_liquid.applymap(round_down)

# Load GAS FUELS sheet (also used for LIQUID FUELS sheet)
df_gas = pd.read_excel('assets/data/National_Sectoral_2020.xlsx', sheet_name='GAS FUELS')

""" CLEAN DATA -----

This section cleans the CDIAC data to be used easily by the dash application.

"""

# Names of the Columns in the Total sheet
df_total.columns = [
    "Nation", 
    "Year", 

    "Fossil Fuel and Cement Production",

    "Energy Supply Total",

    "Energy Consumption Total",

    "Statistical Difference (Sup-Con)",

    "Electric, CHP, Heat Plants",
    
    "Energy Industries' Own Use",

    # Subsectors

    "Manufact, Constr, Non-Fuel Industry",

    # Subsectors

    "Transport",

    # Subsectors

    "Household",
    "Agriculture, Forestry, Fishing",
    "Commerce and Public Services",
    "NES Other Consumption",
    "Non-Energy Use",

    # Only for Totals-----------------
    "Bunkered",

    "Bunkered (Marine)",
    "Bunkered (Aviation)",

    "Flaring of Natural Gas",

    "Manufacture of Cement",

    "Per Capita Total Emissions"
]

# Names of the columns in the SOLID sheet
df_solid.columns = [
    "Nation", 
    "Year", 

    "Energy Supply Total",

    "Energy Consumption Total",

    "Statistical Difference (Sup-Con)",

    "Electric, CHP, Heat Plants",

    "Energy Industries' Own Use",

    # Subsectors

    "Manufact, Constr, Non-Fuel Industry",

    # Subsectors

    "Transport",

    # Subsectors

    "Household",
    "Agriculture, Forestry, Fishing",
    "Commerce and Public Services",
    "NES Other Consumption",
    "Non-Energy Use",
]

df_liquid.columns = df_solid.columns

df_gas.columns = df_solid.columns

# For mapping source to source between sheets when a different fuel type is selected
def best_match_option(value, fuel_type):

    # Are we coming from the totals sheet?  Assume first no
    from_totals = False
    
    if (value in df_solid.columns) : 
        from_index = df_solid.columns.get_loc(value)
    else :
        from_index = df_total.columns.get_loc(value)
        from_totals = True

    if (from_totals and fuel_type == 'totals') :
        return value
    
    if (from_totals and fuel_type != 'totals') :
        if (from_index >= 3 and from_index <= 14):
            return df_solid.columns[from_index - 1]
        else:
            return df_solid.columns[2]

    if (not from_totals and fuel_type == 'totals') :
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

