import tkinter as tk
from tkinter import messagebox, ttk
from deliveryService import DeliveryService
from product import Product

class DeliveryApp:
    def __init__(self, root):
        self.deliveryService = DeliveryService()
        
        self.root = root
        self.root.title("Сервис по доставке продуктов")

        # Меню
        menuBar = tk.Menu(root)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Выход", command=root.quit)
        menuBar.add_cascade(label="Файл", menu=fileMenu)
        root.config(menu=menuBar)

        # Поля ввода
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

        self.deliveryTimeLabel = tk.Label(root, text="Время доставки:")
        self.deliveryTimeLabel.pack()
        self.deliveryTimeEntry = tk.Entry(root)
        self.deliveryTimeEntry.pack()

        self.addressLabel = tk.Label(root, text="Адрес доставки:")
        self.addressLabel.pack()
        self.addressEntry = tk.Entry(root)
        self.addressEntry.pack()

        self.addButton = tk.Button(root, text="Добавить продукт", command=self.addProduct)
        self.addButton.pack()

        self.removeButton = tk.Button(root, text="Удалить продукт", command=self.removeProduct)
        self.removeButton.pack()

        # Таблица для отображения продуктов
        self.tree = ttk.Treeview(root, columns=('Name', 'Quantity', 'Price', 'Delivery Time', 'Address'), show='headings')
        self.tree.heading('Name', text='Название')
        self.tree.heading('Quantity', text='Количество')
        self.tree.heading('Price', text='Цена')
        self.tree.heading('Delivery Time', text='Время доставки')
        self.tree.heading('Address', text='Адрес')
        self.tree.pack()

    def addProduct(self):
        name = self.nameEntry.get()
        quantity = self.quantityEntry.get()
        price = self.priceEntry.get()
        deliveryTime = self.deliveryTimeEntry.get()
        address = self.addressEntry.get()

        if not name or not quantity or not price or not deliveryTime or not address:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены")
            return

        try:
            quantity = int(quantity)
            price = float(price)
            product = Product(name, quantity, price, deliveryTime, address)
            self.deliveryService.addProduct(product)
            self.updateTable()
            messagebox.showinfo("Успех", "Продукт добавлен успешно")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def removeProduct(self):
        selectedItem = self.tree.selection()
        
        if not selectedItem:
            messagebox.showerror("Ошибка", "Выберите продукт для удаления")
            return
        
        index = self.tree.index(selectedItem[0])
        
        try:
            self.deliveryService.removeProduct(index)
            self.updateTable()
            messagebox.showinfo("Успех", "Продукт удален успешно")
        except IndexError as e:
            messagebox.showerror("Ошибка", str(e))

    def updateTable(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for product in self.deliveryService.getProducts():
            self.tree.insert('', 'end', values=(product.name, product.quantity, product.price, product.deliveryTime, product.address))