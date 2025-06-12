class Product:
    def __init__(self,product_id,name,price,quantity=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
#Grocceries 
class Grocery(Product):
    def __init__(self,product_id,name,price,quantity=0,expiry_date=None):
        super().__init__(product_id,name,price,quantity)
        self.expiry_date = expiry_date
    def __str__(self):
        return super().__str__() + f", Expiry Date: {self.expiry_date}"
    
#Clothing
class Clothing(Product):
    def __init__(self,product_id,name,price,quantity=0,size=None,color=None):
        super().__init__(product_id,name,price,quantity)
        self.size = size
        self.color = color
    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Color: {self.color}"
    
#Electronics
class Electronics(Product):
    def __init__(self,product_id,name,price,quantity=0,warranty_period=None):
        super().__init__(product_id,name,price,quantity)
        self.warranty_period = warranty_period
    def __str__(self):
        return super().__str__() + f", Warranty Period: {self.warranty_period}"
    