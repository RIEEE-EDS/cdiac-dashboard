# RIEEE DataDash Application Template

**Author: M. W. Hefner**

**Version 1.0.0**

This web application and associated documentation is the RIEEE DataDash Python/Dash framework application template. Demonstrating by highly documented example, It securely connects to the RIEEE data server in real-time, displaying $\LaTeX$-supporting markdown pages, rendering data tables, and utilizing the Dash and Plotly libraries for highly interactive data visualizations. Put a description and introduction to your application here.  

$\LaTeX$ example: 

The **First Fundamental Theorem of Calculus** states:

Let $f$ be a continuous function on the closed interval $[a, b]$, and let $F(x)$ be an antiderivative of $f$ on $[a, b]$. Then:

$$\int_a^b f(x) \, dx = F(b) - F(a).$$

## Table of Contents

- Before You Begin Developing
- Installation and Getting Started
- Usage
- Features
- Contributing
- License

## Before You Begin Developing

Ensure that you have access to the open access documentation, such as the RIEEE DataDash development guide, and have studied those materials first.

Make sure that the RIEEE DataDash administrator has given you the permissions necessary to create a new DataDash application.  For now, this includes the necessary data server permissions and corresponding config file to include in your development directory.  The RIEEE data server can only be connected to directly through a secure connection; off-campus development requires the use of AppState's secure VPN software.

## Installation and Getting Started

1. First, clone the repository:

```shell
git clone https://github.com/mwhefner/datadash-application-template.git
```

2. Navigate to the project directory:

```shell
cd datadash-application-template
```

4. Create a python virtual environment (named "venv" in this case, but you can name it whatever you would like):

For windows:

```shell
python -m venv venv
```

For macOS and linux:

```shell
python3 -m venv venv
```

5. Activate the virtual environment:

For windows:

```shell
.\venv\Scripts\activate.bat 
```

For macOS and linux:

```shell
source venv/bin/activate
```

6. Install the required dependencies into the virtual environment:

```shell
pip install -r requirements.txt
```

Note: this step may take a considerable amount of time.

7. Place the config file obtained from the RIEEE DataDash administrator in the application's root directory.

## Running for Local Development

1. Activate the virtual environment:

For windows:

```shell
.\venv\Scripts\activate.bat 
```

For macOS and linux:

```shell
source myenv/bin/activate
```

2. To run the application for local development, execute the following command:

```shell
python application.py
```

Once the application is running, open your web browser and visit `http://localhost:8050` to access the application's interface webpage.

3. Closing the application:

When you're done, exit the virtual environment by using the deactivate command:

```shell
deactivate
```

## Features

Give a detailed description of the application's features here.

For the template, there are five navigation pages:

- The first is a demonstration of a markdown page display, which display's the project's readme.md (other markdown files should be included in the assets' markdown folder.)  It is good practice to make this about page available in the applicaiton to encourage others to learn and contribute.
- The second page securely connects to the RIEEE data server and creates example plotly figures.  
- The third displays a straightforward example of interactive image analysis / animation.
- The fourth page gives a sample of Dash controls in the control panel and an interactive choropleth map.
- The fifth displays 3 dimensional data.

## Contributing

RIEEE welcomes community involvement in the development of the DataDash platform and data science competency expanding resources! If you would like to contribute, please get in touch with [RIEEE's Environmental Data Scientist Matt Hefner](mailto:hefnermw@appstate.edu).  

This template's python source uses detailed NumPy/SciPy docustring conventions.

## Verisioning, Publishing and Licencing

Verisioning, publishing and licencing for all DataDash applications is handled through GitHub.  See the development handbook for details.
