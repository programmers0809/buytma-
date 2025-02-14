# Fast Food buyurtma tizimi
import time

def show_menu():
    print("\nFast Food menyusi:")
    print("1. Burger - 30,000 so'm")
    print("2. Pizza - 50,000 so'm")
    print("3. Lavash - 25,000 so'm")
    print("4. Kola - 10,000 so'm")
    print("5. Chiqish")

def take_order():
    menu = {
        1: ("Burger", 30000),
        2: ("Pizza", 50000),
        3: ("Lavash", 25000),
        4: ("Kola", 10000)
    }

    order = []
    total_price = 0

    while True:
        show_menu()
        choice = int(input("\nBuyurtma raqamini kiriting: "))

        if choice == 5:
            print("\nBuyurtma yakunlandi!")
            break
        elif choice in menu:
            item, price = menu[choice]
            quantity = int(input(f"{item} sonini kiriting: "))
            order.append((item, quantity, price * quantity))
            total_price += price * quantity
            print(f"{item} ({quantity} ta) buyurtma qabul qilindi.\n")
        else:
            print("Noto'g'ri raqam kiritildi. Qayta urinib ko'ring!\n")

    print_order_summary(order, total_price)

def print_order_summary(order, total_price):
    print("\nBuyurtma tafsilotlari:")
    for item, quantity, price in order:
        print(f"{item} - {quantity} ta - {price:,} so'm")
    print(f"\nUmumiy narx: {total_price:,} so'm")
    print("\nBuyurtmangiz yetkazib berish uchun qabul qilindi. Rahmat!")

    print("\nBuyurtmangiz tayyorlanmoqda...")
    time.sleep(3)  # Buyurtma tayyorlash uchun 3 soniya kutish
    print("Buyurtmangiz tayyor bo'ldi va yetkazib berishga tayyor!")

# Dastur ishga tushiriladi
take_order()
