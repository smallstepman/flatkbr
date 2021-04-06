#!/usr/bin/env python3

import solid as sl


def choc_switch():
    """
    Kailh Choc switch V1
    """
    o = offset = 3
    m = margin = 1.01
    body_xyz = [14.5 + m, 13.5 + m, 2]
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


keyboard_base = plate() - choc_switch()
sl.scad_render_to_file(keyboard_base, "model.scad")
