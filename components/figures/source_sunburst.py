"""
Module/Script Name: country_sunburst.py
Author: M. W. Hefner

Created: 9/15/2023
Last Modified: 10/30/2023

Project: CDIAC at AppState

Script Description: This script defines a source-view plotly figure.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.graph_objects as go
import datetime
import plotly.io as pio
from components.utils import constants as d

def source_sunburst(source, fuel_type, theme):

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    if fuel_type == 'solids':

        df = d.df_solid

        plot_subtitle = "CO₂ Emissionsfrom the Energy Use of Solid Fuels"

    elif fuel_type == 'liquids':

        df = d.df_liquid

        plot_subtitle = "CO₂ Emissions from the Energy Use of Liquid Fuels"

    elif fuel_type == 'gases':

        df = d.df_gas

        plot_subtitle = "CO₂ Emissions from the Energy Use of Gas Fuels"

    else :

        plot_subtitle = "CO₂ Emissions"

        df = d.df_total

    # Filter the data frame for the right data
    df = df[df['Year'] == 2020]
    df = df[[source, 'Nation']]
    df = df.transpose()

    keys = d.location_mapping.keys()
    # Convert the keys to a list if needed
    key_list = list(keys)

    sunburst_labels = ['WORLD', 'AFRICA', 'NORTH AMERICA', 'AFGHANISTAN', 'SOUTH AMERICA', 'ASIA', 'EUROPE', 'ALBANIA', 'OCEANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA', 'ANTIGUA & BARBUDA', 'AZERBAIJAN', 'ARGENTINA', 'AUSTRALIA', 'AUSTRIA', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'ARMENIA', 'BARBADOS', 'BELGIUM', 'BERMUDA', 'BHUTAN', 'PLURINATIONAL STATE OF BOLIVIA', 'BOSNIA & HERZEGOVINA', 'BOTSWANA', 'BRAZIL', 'ANTARCTIC FISHERIES', 'BELIZE', 'BRITISH INDIAN OCEAN TERRITORIES', 'SOLOMON ISLANDS', 'BRITISH VIRGIN ISLANDS', 'BRUNEI (DARUSSALAM)', 'BULGARIA', 'MYANMAR (FORMERLY BURMA)', 'BURUNDI', 'BELARUS', 'CAMBODIA', 'REPUBLIC OF CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'SRI LANKA', 'CHAD', 'CHILE', 'CHINA (MAINLAND)', 'TAIWAN', 'CHRISTMAS ISLAND', 'COLOMBIA', 'COMMONWEALTH OF INDEPENDENT STATES (CIS)', 'COMOROS', 'MAYOTTE', 'CONGO', 'DEMOCRATIC REPUBLIC OF THE CONGO (FORMERLY ZAIRE)', 'COOK ISLANDS', 'COSTA RICA', 'CROATIA', 'CUBA', 'CYPRUS', 'CZECHOSLOVAKIA', 'CZECH REPUBLIC', 'BENIN', 'DENMARK', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ETHIOPIA', 'ERITREA', 'ESTONIA', 'FAEROE ISLANDS', 'FALKLAND ISLANDS (MALVINAS)', 'FIJI', 'FINLAND', 'ALAND ISLANDS', 'FRANCE', 'FRANCE (INCLUDING MONACO)', 'FRENCH GUIANA', 'FRENCH POLYNESIA', 'DJIBOUTI', 'FRENCH EQUATORIAL AFRICA', 'FRENCH INDO-CHINA', 'GABON', 'FRENCH WEST AFRICA', 'GEORGIA', 'GAMBIA', 'OCCUPIED PALESTINIAN TERRITORY', 'GERMANY', 'FORMER GERMAN DEMOCRATIC REPUBLIC', 'FEDERAL REPUBLIC OF GERMANY', 'GHANA', 'GIBRALTAR', 'KIRIBATI', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA', 'GUYANA', 'HAITI', 'HONDURAS', 'HONG KONG SPECIAL ADMINSTRATIVE REGION OF CHINA', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'ISLAMIC REPUBLIC OF IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'ITALY (INCLUDING SAN MARINO)', 'COTE D IVOIRE', 'JAMAICA', 'JAPAN', 'JAPAN (EXCLUDING THE RUYUKU ISLANDS)', 'KAZAKHSTAN', 'JORDAN', 'KENYA', 'DEMOCRATIC PEOPLE S REPUBLIC OF KOREA', 'UNITED KOREA', 'REPUBLIC OF KOREA', 'KOSOVO', 'KUWAIT', 'KUWAITI OIL FIRES', 'KYRGYZSTAN', 'LAO PEOPLE S DEMOCRATIC REPUBLIC', 'LEBANON', 'LEEWARD ISLANDS', 'LESOTHO', 'LATVIA', 'LIBERIA', 'LIBYAN ARAB JAMAHIRIYAH', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAU SPECIAL ADMINSTRATIVE REGION OF CHINA', 'MADAGASCAR', 'MALAWI', 'FEDERATION OF MALAYA-SINGAPORE', 'SARAWAK', 'MALAYSIA', 'PENINSULAR MALAYSIA', 'SABAH', 'MALDIVES', 'MALI', 'MALTA', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MEXICO', 'MONACO', 'MONGOLIA', 'REPUBLIC OF MOLDOVA', 'MONTENEGRO', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'OMAN', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLAND ANTILLES', 'CURACAO', 'NETHERLAND ANTILLES AND ARUBA', 'ARUBA', 'SAINT MARTIN (DUTCH PORTION)', 'BONAIRE, SAINT EUSTATIUS, AND SABA', 'NEW CALEDONIA', 'VANUATU', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORWAY', 'NORTHERN MARIANA ISLANDS', 'PACIFIC ISLANDS (PALAU)', 'FEDERATED STATES OF MICRONESIA', 'MARSHALL ISLANDS', 'PALAU', 'PAKISTAN', 'EAST & WEST PAKISTAN', 'PANAMA', 'PANAMA', 'FORMER PANAMA CANAL ZONE', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'GUINEA BISSAU', 'TIMOR-LESTE (FORMERLY EAST TIMOR)', 'PUERTO RICO', 'QATAR', 'REUNION', 'ROMANIA', 'RUSSIAN FEDERATION', 'RWANDA-URUNDI', 'RWANDA', 'RYUKYU ISLANDS', 'SAINT BARTHELEMY', 'SAINT HELENA', 'ST. KITTS-NEVIS-ANGUILLA', 'ST. KITTS-NEVIS', 'ANGUILLA', 'SAINT LUCIA', 'SAINT MARTIN (French part)', 'ST. PIERRE & MIQUELON', 'ST. VINCENT & THE GRENADINES', 'SAN MARINO', 'SAO TOME & PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'VIET NAM', 'SLOVENIA', 'SOMALIA', 'SOUTH AFRICA', 'CUSTOMS UNION OF SOUTH AFRICA', 'ZIMBABWE', 'RHODESIA-NYASALAND', 'FORMER DEMOCRATIC YEMEN', 'SPAIN', 'REPUBLIC OF SOUTH SUDAN', 'REPUBLIC OF SUDAN', 'WESTERN SAHARA', 'SUDAN', 'SURINAME', 'SVALBARD & JAN MAYEN ISLANDS', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SWITZERLAND', 'SYRIAN ARAB REPUBLIC', 'TAJIKISTAN', 'THAILAND', 'TOGO', 'TONGA', 'TRINIDAD AND TOBAGO', 'UNITED ARAB EMIRATES', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE', 'MACEDONIA', 'USSR', 'EGYPT', 'UNITED KINGDOM', 'CHANNEL ISLANDS', 'GUERNSEY', 'JERSEY', 'ISLE OF MAN', 'UNITED REPUBLIC OF TANZANIA', 'TANGANYIKA', 'ZANZIBAR', 'UNITED STATES OF AMERICA', 'U.S. VIRGIN ISLANDS', 'BURKINA FASO', 'URUGUAY', 'UZBEKISTAN', 'VENEZUELA', 'DEMOCRATIC REPUBLIC OF VIETNAM', 'REPUBLIC OF SOUTH VIETNAM', 'WAKE ISLAND', 'WALLIS AND FUTUNA ISLANDS', 'SAMOA', 'FORMER YEMEN', 'YEMEN', 'YUGOSLAVIA (FORMER SOCIALIST FEDERAL REPUBLIC)', 'YUGOSLAVIA (MONTENEGRO & SERBIA)', 'ZAMBIA']
    sunburst_parents = ['', 'World', 'World', 'World', 'World', 'World', 'World', 'Europe', 'Oceania', 'Africa', 'Asia Pacific', 'Europe', 'Africa', 'South and Central America', 'Commonwealth of Independent States', 'South and Central America', 'Asia Pacific', 'Europe', 'South and Central America', 'Middle East', 'Asia Pacific', 'Commonwealth of Independent States', 'South and Central America', 'Europe', 'South and Central America', 'Asia Pacific', 'South and Central America', 'Europe', 'Africa', 'South and Central America', 'Antarctica', 'South and Central America', 'Asia Pacific', 'Asia Pacific', 'South and Central America', 'Asia Pacific', 'Europe', 'Asia Pacific', 'Africa', 'Commonwealth of Independent States', 'Asia Pacific', 'Africa', 'North America', 'Africa', 'South and Central America', 'Africa', 'Asia Pacific', 'Africa', 'South and Central America', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'South and Central America', 'Commonwealth of Independent States', 'Africa', 'Africa', 'Africa', 'Africa', 'Asia Pacific', 'South and Central America', 'Europe', 'South and Central America', 'Europe', 'Europe', 'Europe', 'Africa', 'Europe', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'Africa', 'Africa', 'Africa', 'Europe', 'Europe', 'South and Central America', 'Asia Pacific', 'Europe', 'Europe', 'Europe', 'Europe', 'South and Central America', 'Asia Pacific', 'Africa', 'Africa', 'Asia Pacific', 'Africa', 'Africa', 'Europe', 'Africa', 'Middle East', 'Europe', 'Europe', 'Europe', 'Africa', 'Europe', 'Asia Pacific', 'Europe', 'North America', 'South and Central America', 'South and Central America', 'Asia Pacific', 'South and Central America', 'Africa', 'South and Central America', 'South and Central America', 'South and Central America', 'Asia Pacific', 'Europe', 'Europe', 'Asia Pacific', 'Asia Pacific', 'Middle East', 'Middle East', 'Europe', 'Middle East', 'Europe', 'Europe', 'Africa', 'South and Central America', 'Asia Pacific', 'Asia Pacific', 'Commonwealth of Independent States', 'Middle East', 'Africa', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Europe', 'Middle East', 'Middle East', 'Commonwealth of Independent States', 'Asia Pacific', 'Middle East', 'South and Central America', 'Africa', 'Europe', 'Africa', 'Africa', 'Europe', 'Europe', 'Europe', 'Asia Pacific', 'Africa', 'Africa', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Africa', 'Europe', 'South and Central America', 'Africa', 'Africa', 'North America', 'Europe', 'Asia Pacific', 'Commonwealth of Independent States', 'Europe', 'South and Central America', 'Africa', 'Africa', 'Middle East', 'Africa', 'Asia Pacific', 'Asia Pacific', 'Europe', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'South and Central America', 'Africa', 'Africa', 'Asia Pacific', 'Europe', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'South and Central America', 'South and Central America', 'South and Central America', 'Asia Pacific', 'South and Central America', 'South and Central America', 'Asia Pacific', 'Europe', 'Europe', 'Africa', 'Asia Pacific', 'South and Central America', 'Middle East', 'Africa', 'Europe', 'Commonwealth of Independent States', 'Africa', 'Africa', 'Asia Pacific', 'South and Central America', 'Africa', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'South and Central America', 'North America', 'South and Central America', 'Europe', 'Africa', 'Middle East', 'Africa', 'Europe', 'Africa', 'Africa', 'Asia Pacific', 'Europe', 'Asia Pacific', 'Europe', 'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Middle East', 'Europe', 'Africa', 'Africa', 'Africa', 'Africa', 'South and Central America', 'Europe', 'Africa', 'Europe', 'Europe', 'Europe', 'Middle East', 'Commonwealth of Independent States', 'Asia Pacific', 'Africa', 'Asia Pacific', 'South and Central America', 'Middle East', 'Africa', 'Europe', 'Commonwealth of Independent States', 'South and Central America', 'Asia Pacific', 'Africa', 'Europe', 'Europe', 'USSR', 'Africa', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa', 'North America', 'South and Central America', 'Africa', 'South and Central America', 'Commonwealth of Independent States', 'South and Central America', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Middle East', 'Middle East', 'Europe', 'Europe', 'Africa']

    df = df.copy()
    df.fillna(0, inplace=True)

    # Debug
    dfl = df.values.tolist()[0]

    fig = go.Figure(go.Sunburst(

        labels = sunburst_labels,

        parents = sunburst_parents,

        values=dfl,

        branchvalues="total",

        insidetextorientation='horizontal',

        marker=dict(
            colors=[

            ],

            line=dict(color=textCol, width=0) 
        )
    ))

    fig.update_layout(

        #uniformtext=dict(minsize=20, mode='hide'),

        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin={'l': 0, 'r': 0, 't': 100, 'b': 0},

        yaxis_title = "CO₂ Emissions (kilotonnes C)",

        # Set the font size for the entire plot, excluding the title
        font=dict(
            size=28, 
        ),

        # Title Layout and Styling
        title = dict(
            text = source,
            xanchor="center",
            xref = "container",
            yref = "container",
            x = 0.5,
            yanchor="top",
            y = .98,
            font = dict(
                size = 32,
                color = textCol,
            )
        ),

                # Subtitle
        annotations=[
            # Subtitle
            dict(
                text= plot_subtitle,
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.04,
                font=dict(size=18, color=textCol)
            ),

            # Credit
            dict(
                x=0.5,
                y=0,
                xref='paper',
                yref='paper',
                text='The CDIAC at AppState Dashboard (' + str(datetime.date.today().year) + ')',
                showarrow=False,
                
                font = dict(
                    size=20,
                    color = textCol
                )
            )
        ]

    )
    
    return fig