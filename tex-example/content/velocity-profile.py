#!/usr/bin/env python3

# Copyright (C) 2020 Andrew Trettel
#
# Licensed under the MIT License.  See LICENSE.txt for additional details.

import numpy as np
import matplotlib as mpl
mpl.use("pgf")
import matplotlib.pylab as plt
import grfstyl as gfx
mpl.rcParams.update( gfx.rc_custom_preamble( use_grid=False, columns=1 ) )

fig = plt.figure()
ax  = fig.add_subplot( 1, 1, 1 )

y_bounds = ( 0.0, 1.0 )
u_bounds = ( 0.0, 2.0 )

y = np.linspace( y_bounds[0], y_bounds[1], gfx.page_size.max_elements() )

u_laminar   = 2.0 * ( 1.0 - y**2.0 )
u_turbulent = 1.25 * ( 1.0 - y )**( 1.0 / 7.0 )

ax.plot( y, u_laminar,   linestyle="solid",  clip_on=False, label="Laminar"   )
ax.plot( y, u_turbulent, linestyle="dashed", clip_on=False, label="Turbulent" )

ax.set_xlim( y_bounds )
ax.set_ylim( u_bounds )

legend = ax.legend()
legend.get_frame().set_linewidth( gfx.axis_line_width )

gfx.label_axes(
    ax,
    r"$\cCylindricalCoordinate{1} / \aRadius$",
    r"$\frac{ \cCylindricalVelocity{3} }{ \qVelocity[\textrm{b}] }$",
)

aspect_ratio = gfx.aspect_ratio( y_bounds, u_bounds )
ax.set_aspect( aspect_ratio )

fig.savefig( "content/figure-velocity-profile.pgf" )
