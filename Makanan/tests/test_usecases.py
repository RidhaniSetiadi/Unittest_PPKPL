import unittest
from repositories.food_repository import FoodRepository
from usecases.food_usecase import FoodUseCase
from io import StringIO
import sys

class TestFoodUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = FoodRepository()
        self.usecase = FoodUseCase(self.repo)
        self.usecase.add_food(1, "Nasi Goreng", 400)

    def test_add_food(self):
        self.usecase.add_food(2, "Sate", 350)
        self.assertIsNotNone(self.repo.get(2))

    def test_get_food(self):
        food = self.usecase.get_food(1)
        self.assertEqual(food.name, "Nasi Goreng")

    def test_update_food(self):
        result = self.usecase.update_food(1, "Nasi Uduk", 450)
        self.assertTrue(result)
        self.assertEqual(self.repo.get(1).name, "Nasi Uduk")

    def test_delete_food(self):
        result = self.usecase.delete_food(1)
        self.assertTrue(result)
        self.assertIsNone(self.repo.get(1))

if __name__ == '__main__':
    unittest.main()
