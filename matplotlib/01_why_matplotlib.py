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

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Why matplotlib?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    *An introduction to Matplotlib's place in the Python visualization ecosystem and its design philosophy.*


    [Matplotilb](https://matplotlib.org/) is an awesome Python data visualization library--it forms the backbone of several plotting libraries, it's incredibly well documented, and it supports everything from simple plots to complex and interactive graphs. In their own words:

    /// admonition | "Matplotlib makes easy things easy and hard things possible"
    ///
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib import cbook, cm
    from matplotlib.colors import LightSource

    return LightSource, cbook, cm, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Some examples
    Here's some examples from the Matplotlib docs and across the web.

    Matplotlib offers a couple interfaces: one functional, one OOP. Let's take a look at the functional interface first:
    """)
    return


@app.cell
def _(plt):
    # 4 lines of code gets us a simple visual :)
    plt.plot([1, 2, 3, 4])
    plt.ylabel("Some numbers")
    plt.title("Basic line plot")
    # plt.gca() gets the current `Axes`
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's take a look at the OOP interface:
    """)
    return


@app.cell
def _(pd, plt):
    climate_data = pd.read_csv(
        "https://assets.datacamp.com/production/repositories/3634/datasets/411add3f8570d5adf891127fd64095020210711b/climate_change.csv",
        parse_dates=True,
        index_col="date",
    )

    # plt.subplots returns a Figure and Axis object. 
    # here, we ask for 2 rows and one column that share an x-axis
    _fig, _ax = plt.subplots(2, 1, sharex=True)

    # Data is plotted by indexing a row  
    _ax[0].plot(
        climate_data.index,
        climate_data['co2']
    )
    _ax[1].plot(
        climate_data.index,
        climate_data['relative_temp']
    )

    # Chart customisations must also be called on each index
    # The axis annotation methods are different to the plt.plot() interface
    _ax[0].set_title("Global rise in C02 and relative temperature")
    _ax[0].set_ylabel("C02 (ppm)")
    _ax[1].set_xlabel("Year")
    _ax[1].set_ylabel("Relative temperature (°C)")

    # Return the Figure
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 3d plots
    Everybody thinks 3D plots are cool. Here's an example which is available from the marimo snippets pane:
    """)
    return


@app.cell(hide_code=True)
def _(LightSource, cbook, cm, np, plt):
    # Load and format data
    dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
    _z = dem['elevation']
    nrows, ncols = _z.shape
    _x = np.linspace(dem['xmin'], dem['xmax'], ncols)
    _y = np.linspace(dem['ymin'], dem['ymax'], nrows)
    _x, _y = np.meshgrid(_x, _y)

    region = np.s_[5:50, 5:50]
    _x, _y, _z = _x[region], _y[region], _z[region]

    # Set up plot
    _fig, _ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)

    # To use a custom hillshading mode, override the built-in shading and pass
    # in the rgb colors of the shaded surface calculated from "shade".
    rgb = ls.shade(_z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    surf = _ax.plot_surface(_x, _y, _z, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)

    plt.gca()
    return


@app.cell
def _(mo):
    mo.md("""
    ### maps


    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Adding Interactivity
    Naturally, since we're using marimo we may want to add some interactivity to our Matplotlib charts.

    Here's an example with some simple [sliders](https://docs.marimo.io/api/inputs/slider/#marimo.ui.slider):
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    n_points = mo.ui.slider(
        20,
        100,
        value=50,
        label="Smoothness"
    )
    n_points
    return (n_points,)


@app.cell(hide_code=True)
def _(mo):
    wave_length = mo.ui.slider(
        2,
        10,
        value=5,
        label="Wave length"
    )
    wave_length
    return (wave_length,)


@app.cell
def _(n_points, np, plt, wave_length):
    _x = np.linspace(0, wave_length.value * np.pi, n_points.value)

    plt.plot(_x, np.sin(_x))
    plt.title(f"Sine wave with {n_points.value} points")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// admonition | Marimo also supports using lasso and box selection tools!

    Use [`mo.ui.matplotlib`](https://docs.marimo.io/api/plotting/#marimo.ui.matplotlib) to make matplotlib plots reactive: select data on the frontend, then use the selection to filter your data in Python.

    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Design philosophy

    ### Parts of a figure

    At the core of Matplotlib chart architecture are four objects:
    * a `Figure`
    * an `Axes`
    * two or more `Axis` objects
    * `Artists`

    The Axes are the individual sets of indices, starting with at least one X-axis and Y-axis.

    The Figure is where the Axes are contained.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src="https://matplotlib.org/stable/_images/anatomy.png",
        alt="Parts of a Matplotlib figure",
        width=500,
        height=500,
        caption="An example of a Matplotlib figure, with annotations for the different objects, artists, and code."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Coding style
    As we saw earlier, Matplotlib offers two* interfaces for graphing data: `pyplot`, the functional interface, and the object-oriented (OO) style.

    In Matplotlib documentation, you'll see a mix of both styles, with the OO style recommended in general, especially for complex graphs and reproducible behaviours.

    For quick interactive work, the pyplot interface may be preferred.

    For Marimo,


    *There's also a third interface, to be used when embedding Matplotlib in GUI applications.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## More
    * Check out the rest of this Marimo Learn course
    * Read the docs for marimo-specific considerations when working with matplotlib: https://docs.marimo.io/guides/working_with_data/plotting/
    * Read the [Matplotlib Quick Start Guide](https://matplotlib.org/stable/users/explain/quick_start.html)
    * Search the marimo snippets list in the developer panel (`ctrl/cmd + j`) for a bunch of Matplotlib examples
    """)
    return


if __name__ == "__main__":
    app.run()
