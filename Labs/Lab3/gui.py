import tkinter as tk
from tkinter import messagebox, ttk
from deliveryService import DeliveryService
from product import Product

class DeliveryApp:
    def __init__(self, root):
        self.deliveryService = DeliveryService()
        
        self.root = root
        self.root.title("Сервис по доставке продуктов")

        menuBar = tk.Menu(root)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Выход", command=root.quit)
        menuBar.add_cascade(label="Файл", menu=fileMenu)
        root.config(menu=menuBar)


        self.nameLabel = tk.Label(root, text="Название продукта:")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(root)
        self.nameEntry.pack()

        self.quantityLabel = tk.Label(root, text="Количество:")
        self.quantityLabel.pack()
        self.quantityEntry = tk.Entry(root)
        self.quantityEntry.pack()

        self.priceLabel = tk.Label(root, text="Цена:")
        self.priceLabel.pack()
        self.priceEntry = tk.Entry(root)
        self.priceEntry.pack()

        self.addButton = tk.Button(root, text="Добавить продукт", command=self.addProduct)
        self.addButton.pack()

        self.tree = ttk.Treeview(root, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.tree.heading('Name', text='Название')
        self.tree.heading('Quantity', text='Количество')
        self.tree.heading('Price', text='Цена')
        self.tree.pack()

    def addProduct(self):
        name = self.nameEntry.get()
        quantity = self.quantityEntry.get()
        price = self.priceEntry.get()

        if not name or not quantity or not price:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены")
            return

        try:
            quantity = int(quantity)
            price = float(price)
            product = Product(name, quantity, price)
            self.deliveryService.addProduct(product)
            self.updateTable()
            messagebox.showinfo("Успех", "Продукт добавлен успешно")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def updateTable(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for product in self.deliveryService.getProducts():
            self.tree.insert('', 'end', values=(product.name, product.quantity, product.price))