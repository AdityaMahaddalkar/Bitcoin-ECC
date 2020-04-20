from elliptic_curve_secp256k1.utils.modulo_arithmetic import get_modular_inverse


class ECC:
    def __init__(self):
        '''
        Initialization
        - Define base points self._x and self._y with modulus self._p
        '''
        self._x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        self._y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self._m = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        self._a = 0
        self._b = 7
        self._curve_equation = 'y^2 = x^3 + 7'

    def return_g_uncompressed(self, x, y):
        '''
        Returns representation of point (x, y) on elliptic curve as one number G
        Input: (x, y) point
        Output: G = 4 + x + y
        '''
        assert self.point_exist_on_curve(x, y) == True
        return 4 + x + y

    def _add_points(self, x0, y0, x1, y1):
        '''
        Addition of 2 points on the elliptic curve
        Input: (x0, y0), (x1, y1) as coordinates of 2 points
        Output: (x2, y2) coordinates of addition of 2 points
        '''

        # Case 1 : If points are equal
        if x0 == x1 and y0 == y1:
            holder = 3 * pow(x0, 2) * get_modular_inverse(2 * y0, self._m)
        else:
            holder = (y1 - y0) * get_modular_inverse((x1 - x0), self._m)

        x2 = (pow(holder, 2) - x1 - x0) % self._m
        y2 = (holder * (x0 - x2) - y0) % self._m

        while x2 < 0:
            x2 += self._m

        while y2 < 0:
            y2 += self._m

        return x2, y2

    def get_public_key_pair(self, k):
        '''
        Starting from initial x, y i.e self._x, self._y,
        represented by G, this function computes and returns k*G
        '''
        x, y = self._x, self._y

        binary_representation_k = bin(k)[2:]

        for i in range(1, len(binary_representation_k)):
            bit_holder = binary_representation_k[i]
            x, y = self._add_points(x, y, x, y)

            if bit_holder == '1':
                x, y = self._add_points(x, y, self._x, self._y)
        return x, y

    def point_exist_on_curve(self, x, y):
        equation = (pow(y, 2) - (pow(x, 3) + self._b)) % self._m
        if equation == 0:
            return True
        return False

    def return_initial_points(self):
        return self._x, self._y

    def return_modulo(self):
        return self._m
