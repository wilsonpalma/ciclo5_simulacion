import unittest

from domain.entities import ModelParameters
from domain.rain_model import RainIndexModel
from domain.temperature import LinearInterpolationTemperatureStrategy


class RainModelTest(unittest.TestCase):
    def setUp(self) -> None:
        self.model = RainIndexModel(
            ModelParameters(),
            LinearInterpolationTemperatureStrategy(),
        )

    def test_example_from_guide(self) -> None:
        tf, index = self.model.calculate_index(0.90, 0.80, 18)
        self.assertEqual(tf, 0.60)
        self.assertAlmostEqual(index, 0.81, places=2)

    def test_temperature_interpolation_for_17_degrees(self) -> None:
        tf = self.model.calculate_temperature_factor(17)
        self.assertAlmostEqual(tf, 0.65, places=2)

    def test_classification_thresholds(self) -> None:
        self.assertEqual(self.model.classify(0.39), "Sin lluvia")
        self.assertEqual(self.model.classify(0.40), "Baja posibilidad")
        self.assertEqual(self.model.classify(0.60), "Lluvia probable")
        self.assertEqual(self.model.classify(0.75), "Lluvia")


if __name__ == "__main__":
    unittest.main()
