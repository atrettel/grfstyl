#!/usr/bin/env python3

# Copyright (C) 2020 Andrew Trettel

from cycler import cycler

# Units (follow TeX's lead)
mm_per_inch     = 25.4
points_per_inch = 72.27
points_per_mm   = points_per_inch / mm_per_inch

# Matplotlib mostly uses inches for length, but also uses points for line
# widths.
inch_unit = 1.0
mm_unit   = 1.0 / mm_per_inch


# Aspect ratios
golden_ratio = 0.5*(5.0**0.5+1.0)
iso_ratio    = 2.0**0.5


# Page sizes
class PageSize:
    _width               = None
    _height              = None
    _figure_aspect_ratio = None
    _figure_width_ratio  = None

    def height( self ):
        return self._height

    def width( self ):
        return self._width

    def shortest_length( self ):
        if ( self.height() > self.width() ):
            return self.width()
        else:
            return self.height()

    def longest_length( self ):
        if ( self.height() > self.width() ):
            return self.height()
        else:
            return self.width()

    def aspect_ratio( self ):
        return self.longest_length() / self.shortest_length()

    def figure_size( self ):
        return ( self.figure_width(), self.figure_height() )

    def figure_width( self ):
        return self.width() * self._figure_width_ratio

    def figure_height( self ):
        return self.figure_width() / self._figure_aspect_ratio

    def __init__( self, width, height ):
        self._width               = width
        self._height              = height
        self._figure_aspect_ratio = golden_ratio
        self._figure_width_ratio  = 0.8

page_sizes           = {}
page_sizes["letter"] = PageSize(   8.5 * inch_unit,  11.0 * inch_unit )
page_sizes["a4"]     = PageSize( 210.0 *   mm_unit, 297.0 *   mm_unit )
page_sizes["beamer"] = PageSize( 128.0 *   mm_unit,  96.0 *   mm_unit )

selected_page_size = page_sizes["letter"]


# Colors
black = [ 0.0, 0.0, 0.0 ]
white = [ 1.0, 1.0, 1.0 ]
transparent_color = "None"

background_color = white
foreground_color = black
text_color       = black


# Line widths
def iso_line_width( level, default_width=0.35*mm_unit ):
    return round(                                       \
        ( default_width / mm_unit ) * iso_ratio**level, \
        2                                               \
    ) * points_per_mm

no_line_width         = 0.0 * mm_unit
very_thin_line_width  = iso_line_width( -2 )
thin_line_width       = iso_line_width( -1 )
medium_line_width     = iso_line_width( +0 )
thick_line_width      = iso_line_width( +1 )
very_thick_line_width = iso_line_width( +2 )

rc_custom_preamble = {
    "axes.edgecolor":        foreground_color,
    "axes.facecolor":        background_color,
    "axes.grid":             False,
    "axes.grid.axis":        "both",
    "axes.grid.which":       "both",
    "axes.linewidth":        very_thin_line_width,
    "axes.spines.bottom":    True,
    "axes.spines.left":      True,
    "axes.spines.right":     False,
    "axes.spines.top":       False,
    "axes.unicode_minus":    False,
    "axes.prop_cycle":       cycler( "color", [foreground_color] ),
    "figure.edgecolor":      background_color,
    "figure.facecolor":      background_color,
    "figure.frameon":        False,
    "figure.figsize":        selected_page_size.figure_size(),
    "grid.color":            foreground_color,
    "grid.linestyle":        "dotted",
    "grid.linewidth":        very_thin_line_width,
    "legend.frameon":        False,
    "lines.color":           foreground_color,
    "lines.linestyle":       "solid",
    "lines.linewidth":       medium_line_width,
    "lines.marker":          None,
    "lines.markeredgecolor": "auto",
    "lines.markeredgewidth": thin_line_width,
    "lines.markerfacecolor": "auto",
    "lines.markersize":      4.0*medium_line_width,
    "pgf.preamble": [
        r"\usepackage{amsmath}",
        r"\usepackage{amsfonts}",
        r"\usepackage{amssymb}",
    ],
    "pgf.rcfonts":         False,
    "pgf.texsystem":       "pdflatex",
    "savefig.transparent": True,
    "text.usetex":         False,
    "xtick.alignment":     "center",
    "xtick.bottom":        True,
    "xtick.color":         foreground_color,
    "xtick.direction":     "out",
    "xtick.labelbottom":   True,
    "xtick.labeltop":      False,
    "xtick.major.size":    4.0,
    "xtick.major.width":   very_thin_line_width,
    "xtick.minor.size":    2.0,
    "xtick.minor.visible": False,
    "xtick.minor.width":   very_thin_line_width,
    "xtick.top":           False,
    "ytick.alignment":     "center_baseline",
    "ytick.color":         foreground_color,
    "ytick.direction":     "out",
    "ytick.labelleft":     True,
    "ytick.labelright":    False,
    "ytick.left":          True,
    "ytick.major.size":    4.0,
    "ytick.major.width":   very_thin_line_width,
    "ytick.minor.size":    2.0,
    "ytick.minor.visible": False,
    "ytick.minor.width":   very_thin_line_width,
    "ytick.right":         False,
}
