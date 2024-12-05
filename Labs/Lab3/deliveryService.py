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
        logging.info(f"Product added: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

    def getProducts(self):
        return self.productList