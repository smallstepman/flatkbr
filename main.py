#!/usr/bin/env python3
from collections import namedtuple
import solid as sl

m = margin_of_error_for_my_3d_printer = 1.02


def choc_switch(test=5):
    """
    Kailh Choc switch V1
    """
    global m
    o = offset = 3
    body_xyz = [14.5 + m, 13.5 + m, test]
    socket_xyz = [body_xyz[0] - 1, body_xyz[1] - 1, 5.55 + o]
    # keycaphole_xyz = [1.2, 3.0, None]
    # distance_between_center_of_keycap_holes = 5.7
    # grip_fins = None

    body = sl.cube(body_xyz, center=True)
    body = sl.translate([0, 0, 3])(body)
    socket = sl.cube(socket_xyz, center=True)
    return body + socket


def choc_keycap():
    global m
    body_xyz = [17.5 + m, 16.5 + m, 3.2]
    # socket_legs z measured from the base
    # socket_legs_xyz = [1.2, 3, 5.2 - body_xyz[2] + 1.5]
    # distance_between_center_of_socket_legs = 6
    body = sl.cube(body_xyz, center=True)
    return body


def choc_key(test, h):
    kc = choc_keycap()
    ks = choc_switch(test)
    kc = sl.translate([0, 0, h])(kc)
    return kc + ks


def key_plate():
    p = sl.cube([20, 20, 6], center=True)
    return p


if __name__ == "__main__":
    keyboard_base = key_plate() - choc_key(6, 3)
    sl.scad_render_to_file(
        keyboard_base,
        "things/model.scad",
    )
