from sqlmodel import Field, SQLModel, create_engine, Session, Relationship
from datetime import date


class Customers(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    vat_id: int

    offers: list["Offers"] = Relationship(back_populates="customer")



class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float

    items: list["Items"] = Relationship(back_populates="product")



class Items(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
   
    quantity: int
    item_total: float
    discount: float = 0.0  

     
    product_id: int = Field(foreign_key="products.id")
    offer_id: int = Field(foreign_key="offers.id")

    product: Products = Relationship(back_populates="items")
    offer: "Offers" = Relationship(back_populates="items")

class Offers(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: date
    subtotal: float
    tax: float = 0.0
    total: float = 0.0

    customer_id: int = Field(foreign_key="customers.id")

    customer: Customers = Relationship(back_populates="offers")
    items: list["Items"] = Relationship(back_populates="offer")

    def calculate_tax_and_total(self):
        self.tax = self.subtotal * 0.25  
        self.total = self.subtotal + self.tax


engine = create_engine("sqlite:///aplikacijaSQL.db")
SQLModel.metadata.create_all(engine)


with Session(engine) as session:
    
    customer1 = Customers(
        name="Alice Johnson", 
        email="alice@company.com", 
        vat_id=11234567890)
    
    customer2 = Customers(
        name="Bob Smith", 
        email="bob@company.com", 
        vat_id=12345678901)
    
    customer3 = Customers(
        name="Charlie Daniels", 
        email="charlie@company.com", 
        vat_id=23456789012)
    
    customer4 = Customers(
        name="Dana White", 
        email="dana@company.com", 
        vat_id=34567890123)
    
    customer5 = Customers(
        name="Evelyn Moore", 
        email="evelyn@company.com", 
        vat_id=45678901234)
    
    customer6 = Customers(
        name="Frank Rivera", 
        email="frank@company.com", 
        vat_id=56789012345)
    
    customer7 = Customers(
        name="Grace Kim", 
        email="grace@company.com", 
        vat_id=67890123456)

    session.add_all([customer1, customer2, customer3, customer4, customer5, customer6, customer7])
    session.commit()

    
    product1 = Products(
        name="Laptop", 
        description="15-inch screen, 8GB RAM, 256GB SSD", 
        price=800.00)
    
    product2 = Products(
        name="Smartphone", 
        description="6-inch screen, 128GB storage", 
        price=500.00)
    
    product3 = Products(
        name="Headphones", 
        description="Wireless, noise-canceling", 
        price=50.00)
    
    product4 = Products(
        name="Tablet", 
        description="10-inch screen, 64GB storage, WiFi", 
        price=300.00)
    
    product5 = Products(
        name="Monitor", 
        description="24-inch Full HD screen", 
        price=150.00)
    
    product6 = Products(
        name="Keyboard", 
        description="Mechanical, RGB lighting", 
        price=25.00)
    
    product7 = Products(
        name="Mouse", 
        description="Wireless, ergonomic design", 
        price=20.00)
    
    product8 = Products(
        name="External Hard Drive", 
        description="1TB, USB 3.0", 
        price=100.00)
    
    product9 = Products(
        name="Printer", 
        description="Inkjet, color printing", 
        price=120.00)
    
    product10 = Products(
        name="Webcam", 
        description="1080p HD, autofocus", 
        price=60.00)
    
    product11 = Products(
        name="Speakers", 
        description="Bluetooth, portable", 
        price=45.00)
    
    product12 = Products(
        name="Smartwatch", 
        description="Fitness tracking, heart rate sensor", 
        price=150.00)
    
    product13 = Products(
        name="Router", 
        description="Dual-band, WiFi 6 support", 
        price=70.00)
    
    product14 = Products(
        name="USB Flash Drive", 
        description="64GB, USB 3.1", 
        price=10.00)
    
    product15 = Products(
        name="USB Flash Drive", 
        description="64GB, USB 3.1", 
        price=10.00)
    

    session.add_all([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15])
    session.commit()


    offer1 = Offers(
        customer_id=customer1.id, 
        date=date(2024, 11, 1), 
        subtotal=1800.00)
    offer1.calculate_tax_and_total()

    offer2 = Offers(
        customer_id=customer2.id, 
        date=date(2024, 11, 2), 
        subtotal=490.00)
    offer2.calculate_tax_and_total()

    offer3 = Offers(
        customer_id=customer3.id,
        date=date(2024, 11, 3), 
        subtotal=425.00)
    offer3.calculate_tax_and_total()

    offer4 = Offers(
        customer_id=customer4.id, 
        date=date(2024, 11, 4), 
        subtotal=1160.00)
    offer4.calculate_tax_and_total()

    offer5 = Offers(
        customer_id=customer5.id, 
        date=date(2024, 11, 5), 
        subtotal=1000.00)
    offer5.calculate_tax_and_total()

    offer6 = Offers(
        customer_id=customer6.id, 
        date=date(2024, 11, 6), 
        subtotal=1100.00)
    offer6.calculate_tax_and_total()

    offer7 = Offers(
        customer_id=customer7.id, 
        date=date(2024, 11, 7), 
        subtotal=700.00)
    offer7.calculate_tax_and_total()

    session.add_all([offer1, offer2, offer3, offer4, offer5, offer6, offer7])
    session.commit()

    
    item1 = Items(
        product_id=product1.id, 
        offer_id=offer1.id, 
        quantity=1, 
        item_total=800.00)
    
    item2 = Items(
        product_id=product2.id, 
        offer_id=offer1.id, 
        quantity=2, 
        item_total=1000.00)
    
    item3 = Items(
        product_id=product3.id, 
        offer_id=offer2.id, 
        quantity=3, 
        item_total=150.00)
    
    item4 = Items(
        product_id=product4.id, 
        offer_id=offer2.id, 
        quantity=1, 
        item_total=300.00)
    
    item5 = Items(
        product_id=product7.id, 
        offer_id=offer2.id, 
        quantity=2, 
        item_total=40.00)
    
    item6 = Items(
        product_id=product5.id, 
        offer_id=offer3.id, 
        quantity=2, 
        item_total=300.00)
    
    item7 = Items(
        product_id=product6.id, 
        offer_id=offer3.id, 
        quantity=5, 
        item_total=125.00)
    
    item8 = Items(
        product_id=product2.id, 
        offer_id=offer4.id, 
        quantity=1, 
        item_total=500.00)
    
    item9 = Items(
        product_id=product4.id, 
        offer_id=offer4.id, 
        quantity=2, 
        item_total=600.00)
    
    item10 = Items(
        product_id=product7.id,
        offer_id=offer4.id, 
        quantity=3, 
        item_total=60.00)
    
    item11 = Items(
        product_id=product3.id, 
        offer_id=offer5.id, 
        quantity=4, 
        item_total=200.00)
    
    item12 = Items(
        product_id=product1.id, 
        offer_id=offer5.id, 
        quantity=1, 
        item_total=800.00)
    
    item13 = Items(
        product_id=product4.id, 
        offer_id=offer6.id, 
        quantity=3, 
        item_total=900.00)
    
    item14 = Items(
        product_id=product6.id, 
        offer_id=offer6.id, 
        quantity=2, 
        item_total=50.00)
    
    item15 = Items(
        product_id=product5.id, 
        offer_id=offer6.id, 
        quantity=1, 
        item_total=150.00)
    
    item16 = Items(
        product_id=product7.id, 
        offer_id=offer7.id, 
        quantity=5, 
        item_total=100.00)
    
    item17 = Items(
        product_id=product2.id, 
        offer_id=offer7.id, 
        quantity=1, 
        item_total=500.00)
    
    item18 = Items(
        product_id=product3.id, 
        offer_id=offer7.id, 
        quantity=2, 
        item_total=100.00)

    session.add_all([item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18])
    session.commit()


with Session(engine) as session:
    
    customer = session.get(Customers, 3)  
    if customer:
        print(f"Customer: {customer.name}")
        
        
        offers = customer.offers
        
        for offer in offers:
            print(f"\nOffer ID: {offer.id} - Date: {offer.date} - Subtotal: {offer.subtotal} - Total: {offer.total}")
            
            
            items = offer.items
            for item in items:
                product = item.product
                print(f"Product: {product.name} - Quantity: {item.quantity} - Item Total: {item.item_total}")
