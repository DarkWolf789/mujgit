from unittest import TestCase
from kalkulacka import ValidatorHesla


"""
class TestKalkulacka(TestCase):
    kalkulacka = Kalkulacka()

    def test_secti(self):
        self.assertEqual(10, self.kalkulacka.secti(2, 8))
        self.assertEqual(100, self.kalkulacka.secti(-100, 200))

    def test_odecti(self):
        self.assertEqual(5, self.kalkulacka.odecti(10, 5))
        self.assertEqual(100, self.kalkulacka.odecti(200, 100))

    def test_vynasob(self):
        self.assertEqual(20, self.kalkulacka.vynasob(10, 2))
        self.assertEqual(100, self.kalkulacka.vynasob(5, 20))

    def test_vydel(self):
        self.assertEqual(20, self.kalkulacka.vydel(100, 5))
        self.assertEqual(4, self.kalkulacka.vydel(8, 2))
"""
"""
class Test(TestCase):
    def test_validuj_heslo(self):
        self.assertEqual("heslo123", self.test_validuj_heslo())
        self.assertEqual("heslo456", self.test_validuj_heslo(self))
        
"""


class TestValidatorHesla(TestCase):
    def test_validuj(self):
        self.fail()
