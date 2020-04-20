from elliptic_curve_secp256k1.utils.modulo_arithmetic import get_modular_inverse


def test_multiplicative_inverse():
    a = 2
    m = 17
    assert get_modular_inverse(a, m) == 9
