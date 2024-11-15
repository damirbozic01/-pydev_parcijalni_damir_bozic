import json


# TODO: dodati typ hiting na sve funkcije!


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    sub_total = sum (total)
    tax = sub_total * 0.25  
    total = sub_total + tax
    # Dodajte novu ponudu u listu offers
    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    print("Odaberite opciju:")
    print("1. Dodaj novi proizvod")
    print("2. Izmjeni postojeći proizvod")
    choice = input("Izbor: ")

    if choice == "1":
        name = input("Unesite naziv proizvoda: ")
        description = input("Unesite opis proizvoda: ")
        price = float(input("Unesite cijenu proizvoda: "))
        
        products.append({
            "id": len(products) + 1,
            "name": name,
            "description": description,
            "price": price
        })
        print(f"Proizvod '{name}' je uspješno dodan.")

    elif choice == "2" and products:
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product['name']} - ${product['price']}")

        product_choice = int(input("Odaberite broj proizvoda: ")) - 1
        if 0 <= product_choice < len(products):
            product = products[product_choice]
            product['name'] = input(f"Unesite novi naziv (trenutno: {product['name']}): ") or product['name']
            product['description'] = input(f"Unesite novi opis (trenutno: {product['description']}): ") or product['description']
            product['price'] = float(input(f"Unesite novu cijenu (trenutno: ${product['price']}): ") or product['price'])
            print(f"Proizvod '{product['name']}' je uspješno izmijenjen.")
        else:
            print("Neispravan izbor proizvoda.")
    


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    print("Odaberite opciju:")
    print("1. Dodaj novog kupca")
    print("2. Prikaz svih kupaca")
    choice = input("Izbor: ")

    if choice == "1":
        name = input("Unesite ime kupca: ")
        email = input("Unesite email kupca: ")
        vat_id = input("Unesite VAT ID kupca: ")
        new_customer = {
            "name": name,
            "email": email,
            "vat_id": vat_id
        }
        customers.append(new_customer)
        print(f"Kupac '{name}' je uspješno dodan.")
    
    # Za pregled: prikaži listu svih kupaca
    elif choice == "2":
        if not customers:
            print("Nema registriranih kupaca.")
        else:
            print("Lista svih kupaca:")
            for customer in customers:
                print(f"ID: {customer['id']}, Ime: {customer['name']}, Email: {customer['email']}, VAT ID: {customer['vat_id']}")



# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    print("Odaberite opciju:")
    print("1. Prikaz svih ponuda")
    print("2. Prikaz ponuda za određeni mjesec")
    print("3. Prikaz ponude prema ID-u")
    choice = input("Izbor: ")

    if choice == "1":
        for offer in offers:
            print_offer(offer)
    
    elif choice == "2":
        month = int(input("Unesite broj mjeseca (1-12): "))
        for offer in offers:
            if int(offer['date'].split('.')[1]) == month:
                print_offer(offer)

    # Prikaz relevantnih ponuda na temelju izbora
    elif choice == "3":
        offer_id = int(input("Unesite ID ponude: "))
        offer = next((o for o in offers if o['offer_number'] == offer_id), None)
        if offer:
            print_offer(offer)
        else:
            print("Ponuda s tim ID-em nije pronađena.")
    else:
        print("Nepoznata opcija.")
    


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
