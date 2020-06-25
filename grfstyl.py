#!/usr/bin/env python3

# Copyright (C) 2020 Andrew Trettel

# Units (follow TeX's lead)
mm_per_inch     = 25.4
points_per_inch = 72.27
points_per_mm   = points_per_inch / mm_per_inch

# Matplotlib mostly uses inches for length, but also uses points for line
# widths.
inch_unit = 1.0
mm_unit   = 1.0 / mm_per_inch

# Page sizes
class PageSize:
    _width  = None
    _height = None

    def height( self ):
        return self._height

    def width( self ):
        return self._width

    def aspect_ratio( self ):
        if ( self._height > self._width ):
            return self._height / self._width
        else:
            return self._width / self._height

    def __init__( self, width, height ):
        self._width  = width
        self._height = height

page_sizes           = {}
page_sizes["letter"] = PageSize(   8.5 * inch_unit,  11.0 * inch_unit )
page_sizes["a4"]     = PageSize( 210.0 *   mm_unit, 297.0 *   mm_unit )
page_sizes["beamer"] = PageSize( 128.0 *   mm_unit,  96.0 *   mm_unit )

selected_page_size = None

# Aspect ratios
golden_ratio = 0.5*(5.0**0.5+1.0)
iso_ratio    = 2.0**0.5

