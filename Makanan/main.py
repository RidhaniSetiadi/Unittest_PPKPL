from repositories.food_repository import FoodRepository
from usecases.food_usecase import FoodUseCase
from interfaces.cli_interface import menu

def main():
    repo = FoodRepository()
    usecase = FoodUseCase(repo)

    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            id_ = int(input("ID: "))
            name = input("Nama: ")
            cal = int(input("Kalori: "))
            usecase.add_food(id_, name, cal)
        elif choice == "2":
            for food in usecase.list_foods():
                print(f"{food.id} - {food.name} ({food.calories} kal)")
        elif choice == "3":
            id_ = int(input("ID: "))
            food = usecase.get_food(id_)
            if food:
                print(f"{food.name} - {food.calories} kalori")
            else:
                print("Tidak ditemukan")
        elif choice == "4":
            id_ = int(input("ID: "))
            name = input("Nama Baru: ")
            cal = int(input("Kalori Baru: "))
            updated = usecase.update_food(id_, name, cal)
            print("Berhasil" if updated else "Gagal")
        elif choice == "5":
            id_ = int(input("ID: "))
            deleted = usecase.delete_food(id_)
            print("Berhasil" if deleted else "Gagal")
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
