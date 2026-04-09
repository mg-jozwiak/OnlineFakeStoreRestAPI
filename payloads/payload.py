from  faker import Faker
import random
from data_models.product import Product
from data_models.cart import Cart, Item

class Payload:
    fake:Faker = Faker()
    categories:list[str] = ["men's clothing", "women's clothing", "jewelery", "electronics", "books"]

    def product_payload(self) -> Product:
        title:str = self.fake.catch_phrase()
        price:float = float(self.fake.pricetag().replace("$","").replace(",", ""))
        description:str = self.fake.paragraph()
        image:str = "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg"
        category:str = random.choice(self.categories)
        return Product(title=title, price=price, description=description, category=category, image=image)
    
    def cart_payload(self) -> Cart:
        #dummy data - need to double check once the API page is back online
        user_id:int = 1 #todo: change
        date:str = "2026-04-01" #todo: check
        cart_products:list[Item] = [Item(1, 4)] #todo: check
        return Cart(user_id, date, cart_products)
