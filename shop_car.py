class ShopCart:
    def __init__(self):
        self.items = []  

    def addItem(self, name, price):
        self.items.append((name, price))

    def removeItem(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                break
        else:
            print(f"Položka '{name}' sa nenachádza v košíku.")

    def printContent(self):
        if not self.items:
            print("Košík je prázdny.")
            return

        total_price = 0
        print("Obsah košíka:")
        for item in self.items:
            print(f"{item[0]} - {item[1]:.2f} EUR")
            total_price += item[1]
        print(f"Celková cena: {total_price:.2f} EUR")
