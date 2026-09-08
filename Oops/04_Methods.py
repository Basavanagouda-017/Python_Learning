class Mobile:
        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price
    
        def display_info(self):
            print("Brand :",self.brand)
            print("Model :",self.model)
            print("Price :",self.price)

m1=Mobile("Apple", "iPhone 13", 99999)
m2=Mobile("Samsung", "Galaxy S21", 79999)
m1.display_info()
m2.display_info()

#in this code we can see that how to create a class and how to create a constructor in python and also how to create instance variable in python.   