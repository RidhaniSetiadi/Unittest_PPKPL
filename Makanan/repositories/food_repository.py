from entities.food import Food

class FoodRepository:
    def __init__(self):
        self.foods = {}

    def add(self, food: Food):
        self.foods[food.id] = food

    def get(self, food_id: int):
        return self.foods.get(food_id)

    def get_all(self):
        return list(self.foods.values())

    def update(self, food_id: int, name: str, calories: int):
        if food_id in self.foods:
            self.foods[food_id].name = name
            self.foods[food_id].calories = calories
            return True
        return False

    def delete(self, food_id: int):
        if food_id in self.foods:
            del self.foods[food_id]
            return True
        return False
