# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.3",
#     "numpy==2.3.1",
#     "pandas==2.3.0",
#     "polars==1.31.0",
#     "requests==2.32.4",
# ]
# ///

import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Why matplotlib?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    *An introduction to Matplotlib's place in the Python visualization ecosystem and its design philosophy.*


    [matplotilb](https://matplotlib.org/) is an awesome Python data visualization library--it forms the backbone of several plotting libraries, it's incredibly well documented, and it supports everything from simple plots to complex and interactive graphs. In their own words:  

    > "matplotlib makes easy things easy and hard things possible"
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md(
        """
    insert examples here



    ### Who uses matplotib?
    Matplotlib is one of the python ecosystem's most widely used plotting libraries. It might be just *the* most popular.  Matplotlib was part of the O.G. Swiss army knife of python data science, alongside Numpy, pandas, scipy, and scikit-learn.  

    But you don't have to be a data scientist to work with Matplotlib. Analysts, Business Intelligence aficionados, and weekend hobbyists alike can all benefit from its extensive features.

    ### What about plotly, altair, and seaborn?

    Sure, there are some awesome new kids on the block, and they offer some amazing capabilities, sometimes extending on matplotlib itself. If you're data visualisation curious, you should check out the hvplot and plotly courses in marimo learn.  If you're just getting started with data visualisation with Python, you can't go wrong with getting your feet wet with matplotlib.


    ### When should I use matplotlib?

    matplotlib can be used for simple line, scatter, and bar charts, as well as statistical visualisations, choropleths, 3D plots, and more. matplotlib leverages python objects to nail the user experience with plots. You get a Figure, an Axes, and a cornucopia of functions and methods to spin up the chart you need.

    Use matplotlib when you:  
    - need reproducible charts  
    - want full control over a visual  
    - just want your chart to work, no frills  


    ### A taste of what plt can do with marimo

    Let's take a quick look at what matplotlib can do.

    #### Quick and easy data exploration
    """
    )
    return


@app.cell
def _(plt):
    plt.plot([1, 2, 3, 4])
    plt.ylabel("Some numbers")
    plt.title("Basic line plot")
    plt.show()
    return


@app.cell
def _(pd):
    climate_data = pd.read_csv(
        'https://assets.datacamp.com/production/repositories/3634/datasets/411add3f8570d5adf891127fd64095020210711b/climate_change.csv',
        parse_dates=True,
        index_col='date'
    )
    climate_data
    return (climate_data,)


@app.cell
def _(climate_data, plt):
    _fig, _ax = plt.subplots(2, 1, sharex=True)

    _ax[0].plot(
        climate_data.index,
        climate_data['co2']
    )
    _ax[1].plot(
        climate_data.index,
        climate_data['relative_temp']
    )
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""#### 3d plots""")
    return


@app.cell
def _(plt):
    import numpy as np

    from matplotlib import cbook, cm
    from matplotlib.colors import LightSource

    # Load and format data
    dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
    z = dem['elevation']
    nrows, ncols = z.shape
    x = np.linspace(dem['xmin'], dem['xmax'], ncols)
    y = np.linspace(dem['ymin'], dem['ymax'], nrows)
    x, y = np.meshgrid(x, y)

    region = np.s_[5:50, 5:50]
    x, y, z = x[region], y[region], z[region]

    # Set up plot
    _fig, _ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)
    # To use a custom hillshading mode, override the built-in shading and pass
    # in the rgb colors of the shaded surface calculated from "shade".
    rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    surf = _ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)

    plt.show()
    return


@app.cell
def _(mo):
    mo.md(
        """
    #### maps


    #### infographics


    ## learn more
    check out the rest of the course to learn more
    """
    )
    return


@app.cell
def _(plt):
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
