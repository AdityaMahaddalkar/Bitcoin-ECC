#!/usr/bin/env python

from elliptic_curve_secp256k1 import elliptic_curve_secp256k1

ecc_object = elliptic_curve_secp256k1.ECC()


def test_point_exist_on_curve():
    point_1 = (5, 1)
    point_2 = ecc_object.return_initial_points()
    assert ecc_object.point_exist_on_curve(*point_1) is False
    assert ecc_object.point_exist_on_curve(*point_2) is True


def test_secp256k1_modulo():
    actual_modulo = 115792089237316195423570985008687907853269984665640564039457584007908834671663
    assert ecc_object.return_modulo() == actual_modulo
