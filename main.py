#!/usr/bin/env python3

import solid as sl


def choc_switch(test=5):
    """
    Kailh Choc switch V1
    """
    o = offset = 3
    m = margin = 1.02
    body_xyz = [14.5 + m, 13.5 + m, test]
    socket_xyz = [body_xyz[0] - 1, body_xyz[1] - 1, 5.55 + o]
    # keycaphole_xyz = [1.2, 3.0, None]
    # distance_between_center_of_keycap_holes = 5.7
    # grip_fins = None

    body = sl.cube(body_xyz, center=True)
    body = sl.translate([0, 0, 3])(body)
    socket = sl.cube(socket_xyz, center=True)
    return body + socket


def key_hole():
    base_xyz = [15, 14, 7]
    base = sl.cube(base_xyz, center=True)
    return base - choc_switch()


def plate():
    p = sl.cube([20, 20, 6], center=True)
    return p


gg = 19
keyboard_base = plate() - choc_switch()
keyboard_base1 = sl.translate([2 * gg, 0, 0])(plate() - choc_switch(test=6))
keyboard_base2 = sl.translate([gg, 0, 0])(plate() - choc_switch(test=4))
keyboard_base3 = sl.translate([-gg, 0, 0])(plate() - choc_switch(test=3))

# keyboard_base = choc_switch()
sl.scad_render_to_file(
    keyboard_base + keyboard_base2 + keyboard_base3 + keyboard_base1,
    "things/model.scad",
)
