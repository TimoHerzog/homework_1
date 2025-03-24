from main import price, discount_complete
import unittest

class Testfunction(unittest.TestCase):
    def test_price(self):
        self.assertEqual(price(4, 50), (2, 2)) #Die Funktion 'price' erhält beispielhafte Daten und vergleicht sie mit dem erwarteten Wert
        self.assertEqual(price(4.3, 31), (2.9, 1.4)) #Die Funktion 'price' erhält beispielhafte Daten und vergleicht sie mit dem erwarteten Wert
    
    def test_discount_complete(self):
        self.assertEqual(discount_complete(2, 1, 3, 1), 7) #Die Funktion 'discount_compelete' erhält beispielhafte Daten und vergleicht sie mit dem erwarteten Wert
        self.assertEqual(discount_complete(1.8, 1.4, 5, 4), 14.6) #Die Funktion 'discount_compelete' erhält beispielhafte Daten und vergleicht sie mit dem erwarteten Wert

if __name__ == "__main__":
    unittest.main()