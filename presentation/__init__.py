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

sns.set_theme(style='whitegrid', context='paper')
sns.set(rc={'figure.facecolor': hex_code('background_grey')})

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
    blues  = sns.dark_palette(hex_code('blue'))
    """Discrete palette of blue colors."""
    blues_c  = sns.dark_palette(hex_code('blue'), as_cmap=True)
    """Continuous palette of blue colors."""
    purples = sns.dark_palette(hex_code('purple'))
    """Discrete palette of purple colors."""
    purples_c = sns.dark_palette(hex_code('purple'), as_cmap=True)
    """Continuous palette of purple colors."""
    greys = sns.dark_palette(hex_code('background_grey'))
    """Discrete palette of grey colors terminating in the background grey."""
    greys_c = sns.dark_palette(hex_code('background_grey'), as_cmap=True)
    """Continuous palette of grey colors terminating in the background grey."""

if __name__ == '__main__':
    print("This file is not meant to be run like this!")