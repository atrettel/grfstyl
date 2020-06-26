#!/usr/bin/env python3

# Copyright (C) 2020 Andrew Trettel

from cycler import cycler

# Units (follow TeX's lead)
mm_per_inch     = 25.4
points_per_inch = 72.27
points_per_mm   = points_per_inch / mm_per_inch

# Matplotlib mostly uses inches for length, but also uses points for line
# widths.
inch_unit   = 1.0
mm_unit     = 1.0 / mm_per_inch
points_unit = 1.0


# Aspect ratios
golden_ratio = 0.5*(5.0**0.5+1.0)
iso_ratio    = 2.0**0.5


# Page sizes
class PageSize:
    _name                = None
    _width               = None
    _height              = None
    _figure_aspect_ratio = None
    _figure_width_ratio  = None

    def name( self ):
        return self._name

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

    def __init__( self, name, width, height ):
        self._name                = name
        self._width               = width
        self._height              = height
        self._figure_aspect_ratio = golden_ratio
        self._figure_width_ratio  = 0.8

page_sizes           = {}
page_sizes["letter"] = PageSize( "letter",   8.5*inch_unit,  11.0*inch_unit )
page_sizes["a4"]     = PageSize( "a4",     210.0*  mm_unit, 297.0*  mm_unit )
page_sizes["beamer"] = PageSize( "beamer", 128.0*  mm_unit,  96.0*  mm_unit )

page_size = None


# Colors
black = [ 0.0 ] * 3
gray  = [ 0.5 ] * 3
white = [ 1.0 ] * 3
transparent_color = "None"

background_color = None
foreground_color = None
neutral_color    = None

axis_color = None
grid_color = None
plot_color = None
text_color = None


# Dimensions
no_line_width         = 0.0 * mm_unit
very_thin_line_width  = None
thin_line_width       = None
medium_line_width     = None
thick_line_width      = None
very_thick_line_width = None

axis_line_width   = None
grid_line_width   = None
plot_line_width   = None
marker_edge_width = None

marker_size       = None
major_tick_length = None
minor_tick_length = None
title_pad         = None
label_pad         = None


# Functions
def iso_line_width( level, default_width=0.35*mm_unit ):
    return round(                                       \
        ( default_width / mm_unit ) * iso_ratio**level, \
        2                                               \
    ) * points_per_mm

def label_axes( ax, x_label, y_label ):
    ax.set_xlabel(
        x_label,
        horizontalalignment="center",
        verticalalignment="top",
        rotation=0.0
    )
    ax.set_ylabel(
        y_label,
        horizontalalignment="right",
        verticalalignment="center",
        rotation=0.0
    )

def rc_custom_preamble():
    return {
        "axes.labelpad":         label_pad,
        "axes.titlepad":         title_pad,
        "axes.edgecolor":        axis_color,
        "axes.facecolor":        background_color,
        "axes.grid":             True,
        "axes.grid.axis":        "both",
        "axes.grid.which":       "both",
        "axes.labelcolor":       text_color,
        "axes.linewidth":        axis_line_width,
        "axes.prop_cycle":       cycler( "color", [plot_color] ),
        "axes.spines.bottom":    True,
        "axes.spines.left":      True,
        "axes.spines.right":     False,
        "axes.spines.top":       False,
        "axes.unicode_minus":    False,
        "figure.edgecolor":      background_color,
        "figure.facecolor":      background_color,
        "figure.frameon":        False,
        "figure.figsize":        page_size.figure_size(),
        "grid.color":            grid_color,
        "grid.linestyle":        "dotted",
        "grid.linewidth":        grid_line_width,
        "legend.frameon":        False,
        "lines.color":           plot_color,
        "lines.linestyle":       "solid",
        "lines.linewidth":       plot_line_width,
        "lines.marker":          None,
        "lines.markeredgecolor": "auto",
        "lines.markeredgewidth": marker_edge_width,
        "lines.markerfacecolor": "auto",
        "lines.markersize":      marker_size,
        "pgf.preamble": [
            r"\usepackage{amsmath}",
            r"\usepackage{amsfonts}",
            r"\usepackage{amssymb}",
            r"\usepackage{lettsymb}",
        ],
        "pgf.rcfonts":         False,
        "pgf.texsystem":       "pdflatex",
        "savefig.transparent": True,
        "text.color":          text_color,
        "text.usetex":         False,
        "xtick.alignment":     "center",
        "xtick.bottom":        True,
        "xtick.color":         axis_color,
        "xtick.direction":     "out",
        "xtick.labelbottom":   True,
        "xtick.labeltop":      False,
        "xtick.major.size":    major_tick_length,
        "xtick.major.width":   axis_line_width,
        "xtick.major.pad":     major_tick_length,
        "xtick.minor.pad":     major_tick_length,
        "ytick.major.pad":     major_tick_length,
        "ytick.minor.pad":     major_tick_length,
        "xtick.minor.size":    minor_tick_length,
        "xtick.minor.visible": False,
        "xtick.minor.width":   axis_line_width,
        "xtick.top":           False,
        "ytick.alignment":     "center_baseline",
        "ytick.color":         axis_color,
        "ytick.direction":     "out",
        "ytick.labelleft":     True,
        "ytick.labelright":    False,
        "ytick.left":          True,
        "ytick.major.size":    major_tick_length,
        "ytick.major.width":   axis_line_width,
        "ytick.minor.size":    minor_tick_length,
        "ytick.minor.visible": False,
        "ytick.minor.width":   axis_line_width,
        "ytick.right":         False,
    }

def update_page_size( name ):
    # Page sizes
    global page_size
    page_size = page_sizes[name]

    # Colors
    global background_color, foreground_color, neutral_color
    background_color = white
    foreground_color = black
    neutral_color    = gray

    global axis_color, grid_color, plot_color, text_color
    axis_color = foreground_color
    grid_color = neutral_color
    plot_color = foreground_color
    text_color = foreground_color

    # Dimensions
    global very_thin_line_width, thin_line_width, medium_line_width, \
        thick_line_width, very_thick_line_width
    very_thin_line_width  = iso_line_width( -2 )
    thin_line_width       = iso_line_width( -1 )
    medium_line_width     = iso_line_width( +0 )
    thick_line_width      = iso_line_width( +1 )
    very_thick_line_width = iso_line_width( +2 )

    global axis_line_width, grid_line_width, plot_line_width, marker_edge_width
    axis_line_width   =    very_thin_line_width
    grid_line_width   =    very_thin_line_width
    plot_line_width   =       medium_line_width
    marker_edge_width =         thin_line_width

    global marker_size, major_tick_length, minor_tick_length, title_pad, \
        label_pad
    marker_size       = 4.0 * medium_line_width
    major_tick_length = 4.0 * points_unit
    minor_tick_length = 2.0 * points_unit
    title_pad         = 4.0 * points_unit
    label_pad         = 4.0 * points_unit

update_page_size("letter")
