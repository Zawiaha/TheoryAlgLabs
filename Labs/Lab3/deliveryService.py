import logging
from product import Product

logging.basicConfig(filename='deliveryService.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class DeliveryService:
    def __init__(self):
        self.productList = []

    def addProduct(self, product):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        self.productList.append(product)
        logging.info(f"Product added: {product.name}, Quantity: {product.quantity}, Price: {product.price}, Delivery Time: {product.deliveryTime}, Address: {product.address}")

    def getProducts(self):
        return self.productList

    def removeProduct(self, index):
        if 0 <= index < len(self.productList):
            removedProduct = self.productList.pop(index)
            logging.info(f"Product removed: {removedProduct.name}")
        else:
            raise IndexError("Invalid index")