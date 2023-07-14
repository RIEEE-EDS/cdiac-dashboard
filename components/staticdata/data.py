"""
Module/Script Name: data.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 6/28/2023
Version: 1.0
"""

# Import Dependencies
import pandas as pd

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

# Load TOTAL sheet
df_total = pd.read_excel('./components/staticData/National_Sectoral_2020.xlsx', sheet_name='TOTAL')

# Load SOLID FUELS sheet (also used for LIQUID FUELS sheet)
df_solid = pd.read_excel('./components/staticData/National_Sectoral_2020.xlsx', sheet_name='SOLID FUELS')

# Load LIQUID FUELS sheet (also used for LIQUID FUELS sheet)
df_liquid = pd.read_excel('./components/staticData/National_Sectoral_2020.xlsx', sheet_name='LIQUID FUELS')

# Load GAS FUELS sheet (also used for LIQUID FUELS sheet)
df_gas = pd.read_excel('./components/staticData/National_Sectoral_2020.xlsx', sheet_name='GAS FUELS')

""" CLEAN DATA -----

This section cleans the CDIAC data to be used easily by the dash application.

"""

# Which column best matches that of another sheet (TOTAL -> PHASES)
best_match = {
    2  : 2,
    3  : 3,
    4  : 5,
    5  : 6,
    6  : 7,
    7  : 8,
    8  : 9,
    9  : 10,
    10 : 11,
    11 : 12,
    12 : 13,
    13 : 4,
    14:2,
    15:2,
    16:2,
    17:2,
    18:2,
    19:2
}

# Reverse which column best matches that of another sheet (PHASES -> TOTAL)
best_match_r = {
    2: 2,
    3: 3,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    9: 10,
    10: 11,
    11: 12,
    12: 13,
    13: 4
}

# Names of the Columns in the Total sheet
df_total.columns = [
    "Nation", 
    "Year", 

    "Total CO₂ Emissions from Fossil-Fuels and Cement Production",
    "Energy Use of Fossil Fuels",

    "Tranformation of Fossil Fuels in Electricity, CHP and Heat Plants",
    "Energy Industries' Own Use of Fossil Fuels",

    "Total Non-Energy-Industry Fossil Fuel Consumption",

    "Consumption of Fossil Fuels in Manufacturing, Construction, and Non-Fuel Industry",
    "Consumption of Fossil Fuels for Transport",
    "Household Consumption of Fossil Fuels",
    "Consumption of Fossil Fuels for Agriculture, Forestry, and Fishing",
    "Consumption of Fossil Fuels for Commerce and Public Services",
    "Other Non-Energy-Industry Consumption of Fossil Fuels",

    "Non-Energy Use of Fossil Fuels",

    "Total Bunkered Fossil Fuels",
    "Bunkered Fossil Fuels (Marine)",
    "Bunkered Fossil Fuels (Aviation)"
    ,
    "Flaring of Natural Gas",
    "Manufacture of Cement",
    "Per Capita Fossil-Fuels and Cement Production"
]

# Names of the columns in the SOLID sheet
df_solid.columns = [
    "Nation", 
    "Year", 

    "Total CO₂ Emissions from Solid Fossil Fuels",
    "Energy Use of Solid Fossil Fuels",

    "Non-Energy Use of Solid Fossil Fuels",

    "Tranformation of Solid Fossil Fuels in Electricity, CHP and Heat Plants",
    "Energy Industries' Own Use of Solid Fossil Fuels",

    "Total Non-Energy-Industry Solid Fossil Fuel Consumption",

    "Consumption of Solid Fossil Fuels in Manufacturing, Construction, and Non-Fuel Industry",
    "Consumption of Solid Fossil Fuels for Transport",
    "Household Consumption of Solid Fossil Fuels",
    "Consumption of Solid Fossil Fuels for Agriculture, Forestry, and Fishing",
    "Consumption of Solid Fossil Fuels for Commerce and Public Services",
    "Other Non-Energy-Industry Consumption of Solid Fossil Fuels"
]

# Names of the columns in the LIQUID sheet
df_liquid.columns = [
    "Nation", 
    "Year", 
    "Total CO₂ Emissions from Liqiud Fossil Fuels",
    "Energy Use of Liqiud Fossil Fuels",
    "Non-Energy Use of Liqiud Fossil Fuels",
    "Tranformation of Liqiud Fossil Fuels in Electricity, CHP and Heat Plants",
    "Energy Industries' Own Use of Liqiud Fossil Fuels",
    "Total Non-Energy-Industry Liqiud Fossil Fuel Consumption",
    "Consumption of Liqiud Fossil Fuels in Manufacturing, Construction, and Non-Fuel Industry",
    "Consumption of Liqiud Fossil Fuels for Transport",
    "Household Consumption of Liqiud Fossil Fuels",
    "Consumption of Liqiud Fossil Fuels for Agriculture, Forestry, and Fishing",
    "Consumption of Liqiud Fossil Fuels for Commerce and Public Services",
    "Other Non-Energy-Industry Consumption of Liqiud Fossil Fuels"
]

# Names of the columns in the GAS sheet
df_gas.columns = [
    "Nation", 
    "Year", 
    "Total CO₂ Emissions from Gas Fossil Fuels",
    "Energy Use of Gas Fossil Fuels",
    "Non-Energy Use of Gas Fossil Fuels",
    "Tranformation of Gas Fossil Fuels in Electricity, CHP and Heat Plants",
    "Energy Industries' Own Use of Gas Fossil Fuels",
    "Total Non-Energy-Industry Gas Fossil Fuel Consumption",
    "Consumption of Gas Fossil Fuels in Manufacturing, Construction, and Non-Fuel Industry",
    "Consumption of Gas Fossil Fuels for Transport",
    "Household Consumption of Gas Fossil Fuels",
    "Consumption of Gas Fossil Fuels for Agriculture, Forestry, and Fishing",
    "Consumption of Gas Fossil Fuels for Commerce and Public Services",
    "Other Non-Energy-Industry Consumption of Gas Fossil Fuels"
]

# For mapping source to source between sheets when a different fuel type is selected
def best_match_option(value, fuel_type):

    # Are we coming from the totals sheet?  Assume first no
    from_totals = False
    # Are we going to the totals sheet?  Assume first no
    to_totals = False

    # Columns of the TO sheet
    if (fuel_type == 'totals') : 
        to_cols = df_total.columns
        to_totals = True
    elif (fuel_type == 'solids') : 
        to_cols = df_solid.columns
    elif (fuel_type == 'liquids') : 
        to_cols = df_liquid.columns
    else : 
        to_cols = df_gas.columns

    # Get FROM column index
    if (value in df_total.columns) : 
        from_index = df_total.columns.get_loc(value)
        from_totals = True

    elif (value in df_solid.columns) : 
        from_index = df_solid.columns.get_loc(value)

    elif (value in df_liquid.columns) : 
        from_index = df_liquid.columns.get_loc(value)

    elif (value in df_gas.columns) : 
        from_index = df_gas.columns.get_loc(value)

    else :
        return "Unexpected Carbon Emission Source Value.  See data.best_match_option."

    if from_totals :
        # from totals to phase; use index map
        return to_cols[best_match[from_index]]
    else :
        # coming from a phase sheet to totals; use reverse map
        if to_totals :
            return to_cols[best_match_r[from_index]]
        else :
            #phase sheet to phase sheet; index doesn't change
            return to_cols[from_index]

    




# Read Markdown Pages

# About page
with open("./assets/markdown/about.md", "r") as file:
    about_content = file.read()

# About page
with open("./assets/markdown/methodology.md", "r") as file:
    methodology_content = file.read()

# Download page
with open("./assets/markdown/download.md", "r") as file:
    download_content = file.read()
