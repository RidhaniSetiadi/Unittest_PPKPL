from entities.food import Food

class FoodUseCase:
    def __init__(self, repository):
        self.repository = repository

    def add_food(self, food_id, name, calories):
        food = Food(food_id, name, calories)
        self.repository.add(food)

    def get_food(self, food_id):
        return self.repository.get(food_id)

    def list_foods(self):
        return self.repository.get_all()

    def update_food(self, food_id, name, calories):
        return self.repository.update(food_id, name, calories)

    def delete_food(self, food_id):
        return self.repository.delete(food_id)
