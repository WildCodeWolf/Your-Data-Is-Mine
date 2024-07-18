"""This file contains style settings for the plots created within the repo."""

import seaborn as sns

_colors = {
    'blue': '#22AFFF',
    'purple': '#8546D6',
    'background_grey': '#EAEBEC',
    'black': '#000000',
    'white': '#FFFFFF',
    'grey0': '#EAEBEC',
    'grey1': '#0F0F0F',
    'grey2': '#4B4B4B',
    'grey3': '#545454',
    'grey4': '#737373',
    'grey5': '#A9A9A9',
    'grey6': '#EAEBEC',
    'grey7': '#EBEBEB',
    'grey8': '#EDF0F2',
}

def hex_code(color):
    """Returns the hex code for the given color.

    Parameters
    ----------
    color : {'blue', 'purple', 'background_grey', 'black', 'white', 'grey0', 'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8'}

        Name of the color.
    
    Returns
    -------
    str
        Hex code of the color (as a string).
    """
    return _colors[color]

class Colors():
    """This class holds the various color palettes we want to use in our presenttion.
    
    Examples
    --------
        Colors.selected_greys   # discrete palette of selected grey colors
        Colors.blues            # discrete palette of blue colors
        Colors.purples_c        # continuous palette of purple colors
    """

    selected_greys = sns.color_palette([color for color in _colors.values()][6:])
    """Discrete palette of selected grey colors."""
    blue = hex_code('blue')
    """Hex code for the selected blue color. Use it for single-color arguments in plots."""
    blues = sns.dark_palette(hex_code('blue'))
    """Discrete palette of blue colors, from dark to bright."""
    blues2 = [blue, blues[3]]
    """Discrete palette of exactly two blue tones, used for specific plots."""
    blues_r = blues.reverse()
    """Discrete palette of blue colors, from bright to dark."""
    blues_c = sns.dark_palette(hex_code('blue'), as_cmap=True)
    """Continuous palette of blue colors, from dark to bright."""
    blues_cr = blues_c.reversed()
    """Continuous palette of blue colors, from bright to dark."""
    purple = hex_code('purple')
    """Hex code for the selected purple color. Use it for single-color arguments in plots."""
    purples = sns.dark_palette(hex_code('purple'))
    """Discrete palette of purple colors, from dark to bright."""
    purples2 = [purple, purples[3]]
    """Discrete palette of exactly two purple tones, used for specific plots."""
    purples_r = purples.reverse()
    """Discrete palette of purple colors, from bright to dark."""
    purples_c = sns.dark_palette(hex_code('purple'), as_cmap=True)
    """Continuous palette of purple colors, from dark to bright."""
    purples_cr = purples_c.reversed()
    """Continuous palette of purple colors, from bright to dark."""
    grey = hex_code('grey3')
    """Hex code for the selected grey color. Use it for single-color arguments in plots."""
    greys = sns.dark_palette(hex_code('background_grey'))
    """Discrete palette of grey colors terminating in the background grey."""
    greys_r = greys.reverse()
    """Discrete palette of grey colors starting from the background grey."""
    greys_c = sns.dark_palette(hex_code('background_grey'), as_cmap=True)
    """Continuous palette of grey colors terminating in the background grey."""
    greys_cr = greys_c.reversed()
    """Continuous palette of grey colors starting from the background grey."""

sns.set_theme(
    style='whitegrid',
    context='paper',
    #context=sns.plotting_context('paper', font_scale=1.2),  # setting used for presentation graphics
    palette=Colors.blues,
    rc={
        'figure.facecolor': hex_code('background_grey'),
        'axes.facecolor': hex_code('background_grey'),
        'figure.figsize': (1.618*6.,6.),
    }
)