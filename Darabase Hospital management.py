import pickle

class Property:
    def __init__(self, name, property_type, location, price):
        self.name = name
        self.property_type = property_type
        self.location = location
        self.price = price

# Initialize the properties list
properties = []

# Define the functions for property management
def add_property(name, property_type, location, price):
    property = Property(name, property_type, location, price)
    properties.append(property)

def load_properties_from_binary():
    try:
        with open("properties.pkl", "rb") as file:
            global properties
            properties = pickle.load(file)
    except FileNotFoundError:
        pass

def save_properties_to_binary():
    with open("properties.pkl", "wb") as file:
        pickle.dump(properties, file)


new_properties_data = [
    {'Name': 'Ashutosh and Family House', 'Type': '5 bhk', 'Location': 'nepensi road', 'Price': 250000},
    {'Name': 'Shravya Chena Apartment', 'Type': '2 bhk', 'Location': 'Andheri', 'Price': 45000},
{'Name': 'Ashutosh and Family House', 'Type': '5 bhk', 'Location': 'nepensi road', 'Price': 250000},
    {'Name': 'Shravya Chena Apartment', 'Type': '2 bhk', 'Location': 'Andheri', 'Price': 45000},
    {'Name': 'Geeta Tower', 'Type': '3 bhk', 'Location': 'Dadar', 'Price': 98000},
    {'Name': 'Deepali Bungalow', 'Type': '4 bhk', 'Location': 'Worli', 'Price': 128000},
    {'Name': 'Ashutosh Manor', 'Type': '5 bhk', 'Location': 'Vile Parle', 'Price': 220000},
    {'Name': 'Manan Villa', 'Type': '6 bhk', 'Location': 'Chembur', 'Price': 320000},
    {'Name': 'Shreeya Retreat', 'Type': '3 bhk', 'Location': 'Powai', 'Price': 118000},
    {'Name': 'Misbah Cabin', 'Type': '1 bhk', 'Location': 'Bhiwandi', 'Price': 16000},
    {'Name': 'Jafar Ali Mansion', 'Type': '5 bhk', 'Location': 'Bandra', 'Price': 550000},
    {'Name': 'Affan Ansari Retreat', 'Type': '3 bhk', 'Location': 'Malad', 'Price': 92000},
    {'Name': 'Affan Mia Tower', 'Type': '2 bhk', 'Location': 'Nala Sopara', 'Price': 48000},
    {'Name': 'Dilip Apartment', 'Type': '4 bhk', 'Location': 'Kandivali', 'Price': 128000},
    {'Name': 'Sarvanad Heights', 'Type': '2 bhk', 'Location': 'Vasai', 'Price': 75000},
    {'Name': 'Jignesh Tower', 'Type': '3 bhk', 'Location': 'Thane', 'Price': 88000},
    {'Name': 'Atharva Villa', 'Type': '2 bhk', 'Location': 'Goregaon', 'Price': 92000},
    {'Name': 'Goswami Mansion', 'Type': '4 bhk', 'Location': 'Mulund', 'Price': 128000},
    {'Name': 'Sharvya Heights', 'Type': '3 bhk', 'Location': 'Panvel', 'Price': 79000},
    {'Name': 'Lord Cheena Villa', 'Type': 'Villa', 'Location': 'Alibaug', 'Price': 350000},
    {'Name': 'Lord Sandy Tower', 'Type': '5 bhk', 'Location': 'Ulhasnagar', 'Price': 310000},
    {'Name': 'Goat Aditya Cottage', 'Type': 'Chawl', 'Location': 'Goregaon', 'Price': 82000},
    {'Name': 'Geeta Retreat', 'Type': '3 bhk', 'Location': 'Vasai', 'Price': 70000},
    {'Name': 'Deepali Tower', 'Type': '2 bhk', 'Location': 'Borivali', 'Price': 58000},
    {'Name': 'Ashutosh Heights', 'Type': '4 bhk', 'Location': 'Dombivali', 'Price': 110000},
    {'Name': 'Manan Cabin', 'Type': '1 bhk', 'Location': 'Panvel', 'Price': 22000},
    {'Name': 'Shreeya Manor', 'Type': '5 bhk', 'Location': 'Thane', 'Price': 256000},
    {'Name': 'Misbah Villa', 'Type': '6 bhk', 'Location': 'Worli', 'Price': 340000},
    {'Name': 'Jafar Ali Residence', 'Type': '3 bhk', 'Location': 'Andheri', 'Price': 85000},
    {'Name': 'Affan Ansari Tower', 'Type': '2 bhk', 'Location': 'Malad', 'Price': 54000},
    {'Name': 'Affan Mia Mansion', 'Type': '4 bhk', 'Location': 'Bandra', 'Price': 128000},
    {'Name': 'Dilip Retreat', 'Type': '3 bhk', 'Location': 'Kandivali', 'Price': 76000},
    {'Name': 'Sarvanad Villa', 'Type': 'Villa', 'Location': 'Powai', 'Price': 350000},
    {'Name': 'Jignesh Tower', 'Type': '5 bhk', 'Location': 'Goregaon', 'Price': 240000},
    {'Name': 'Atharva Heights', 'Type': '3 bhk', 'Location': 'Thane', 'Price': 97000},
    {'Name': 'Goswami Mansion', 'Type': '2 bhk', 'Location': 'Mulund', 'Price': 65000},
    {'Name': 'Sharvya Tower', 'Type': '4 bhk', 'Location': 'Panvel', 'Price': 116000},
    {'Name': 'Lord Cheena Apartment', 'Type': '3 bhk', 'Location': 'Alibaug', 'Price': 96000},
    {'Name': 'Lord Sandy Retreat', 'Type': '2 bhk', 'Location': 'Ulhasnagar', 'Price': 58000},
    {'Name': 'Goat Aditya Mansion', 'Type': '4 bhk', 'Location': 'Goregaon', 'Price': 112000},
    {'Name': 'Karan Heights Apartment', 'Type': '3 bhk', 'Location': 'Borivali', 'Price': 75000},
    {'Name': 'Meet Enclave House', 'Type': '2 bhk', 'Location': 'Andheri', 'Price': 62000},
    {'Name': 'Karan Residency Villa', 'Type': '4 bhk', 'Location': 'Dadar', 'Price': 135000},
    {'Name': 'Karan Towers', 'Type': '5 bhk', 'Location': 'Bandra', 'Price': 320000},
    {'Name': 'Meet Villa', 'Type': '6 bhk', 'Location': 'Juhu', 'Price': 420000},
    {'Name': 'Karan Retreat', 'Type': '3 bhk', 'Location': 'Malad', 'Price': 98000},
    {'Name': 'Meet Apartments', 'Type': '2 bhk', 'Location': 'Kandivali', 'Price': 56000},
    {'Name': 'Karan Mansion', 'Type': '4 bhk', 'Location': 'Goregaon', 'Price': 140000},
    {'Name': 'Karan Tower', 'Type': '3 bhk', 'Location': 'Navi Mumbai', 'Price': 72000},
    {'Name': 'Meet Manor', 'Type': '4 bhk', 'Location': 'Vasai', 'Price': 110000},
    {'Name': 'Karan Residences', 'Type': '2 bhk', 'Location': 'Panvel', 'Price': 51000},
    {'Name': 'Meet Villa Retreat', 'Type': 'Villa', 'Location': 'Thane', 'Price': 290000},
    {'Name': 'Karan Haven', 'Type': '3 bhk', 'Location': 'Mira Road', 'Price': 85000},
    {'Name': 'Meet Residence', 'Type': '4 bhk', 'Location': 'Kalyan', 'Price': 126000},
    {'Name': 'Karan Heights Cottage', 'Type': '1 bhk', 'Location': 'Badlapur', 'Price': 18000},
    {'Name': 'Karan Towers Mansion', 'Type': '5 bhk', 'Location': 'Malad', 'Price': 270000},
    {'Name': 'Meet Villa Mansion', 'Type': '4 bhk', 'Location': 'Worli', 'Price': 165000},
    {'Name': 'Karan Residency Villa', 'Type': '3 bhk', 'Location': 'Girgaon', 'Price': 99000},
    {'Name': 'Karan Villa Retreat', 'Type': '2 bhk', 'Location': 'Colaba', 'Price': 57000},
    {'Name': 'Meet Heights Residence', 'Type': '3 bhk', 'Location': 'Vile Parle', 'Price': 72000},
    {'Name': 'Meet Tower Apartments', 'Type': '4 bhk', 'Location': 'Thane', 'Price': 138000},
    {'Name': 'Raju Residency', 'Type': '2 bhk', 'Location': 'Vile Parle', 'Price': 55000},
    {'Name': 'Kanal Gardens', 'Type': '3 bhk', 'Location': 'Juhu', 'Price': 95000},
    {'Name': 'Krish Apartments', 'Type': '1 bhk', 'Location': 'Malad', 'Price': 48000},
    {'Name': 'Sai South India Tower', 'Type': '4 bhk', 'Location': 'Goregaon', 'Price': 125000},
    {'Name': 'Raju Residences', 'Type': '2 bhk', 'Location': 'Borivali', 'Price': 60000},
    {'Name': 'Kanal Heights', 'Type': '3 bhk', 'Location': 'Khar', 'Price': 98000},
    {'Name': 'Krish Towers', 'Type': '2 bhk', 'Location': 'Chembur', 'Price': 70000},
    {'Name': 'Sai South India Gardens', 'Type': '4 bhk', 'Location': 'Worli', 'Price': 130000},
    {'Name': 'Raju Enclave', 'Type': '1 bhk', 'Location': 'Lower Parel', 'Price': 45000},
    {'Name': 'Kanal Horizon', 'Type': '3 bhk', 'Location': 'Dahisar', 'Price': 92000},
    {'Name': 'Krish Heights', 'Type': '2 bhk', 'Location': 'Thane', 'Price': 67000},
    {'Name': 'Sai South India Oasis', 'Type': '4 bhk', 'Location': 'Bhandup', 'Price': 128000},
    {'Name': 'Raju Paradise', 'Type': '2 bhk', 'Location': 'Santacruz', 'Price': 57000},
    {'Name': 'Kanal Springs', 'Type': '3 bhk', 'Location': 'Kandivali', 'Price': 94000},
    {'Name': 'Krish Gardens', 'Type': '1 bhk', 'Location': 'Ghatkopar', 'Price': 49000},
    {'Name': 'Sai South India Residences', 'Type': '4 bhk', 'Location': 'Mulund', 'Price': 126000},
    {'Name': 'Raju Towers', 'Type': '2 bhk', 'Location': 'Colaba', 'Price': 56000},
    {'Name': 'Kanal Palms', 'Type': '3 bhk', 'Location': 'Marine Lines', 'Price': 91000},
    {'Name': 'Krish Mansions', 'Type': '2 bhk', 'Location': 'Navi Mumbai', 'Price': 68000},
    {'Name': 'Sai South India View', 'Type': '4 bhk', 'Location': 'Seawoods', 'Price': 129000},
    {'Name': 'Raju Homes', 'Type': '2 bhk', 'Location': 'Bhayander', 'Price': 58000},
    {'Name': 'Kanal Greens', 'Type': '3 bhk', 'Location': 'Mahim', 'Price': 93000},
    {'Name': 'Krish Plaza', 'Type': '1 bhk', 'Location': 'Dombivli', 'Price': 50000},
    {'Name': 'Sai South India Heights', 'Type': '4 bhk', 'Location': 'Kalyan', 'Price': 127000},
    {'Name': 'Raju Skies', 'Type': '2 bhk', 'Location': 'Malabar Hill', 'Price': 59000},
    {'Name': 'Kanal Residences', 'Type': '3 bhk', 'Location': 'Byculla', 'Price': 90000},
    {'Name': 'Krish Homes', 'Type': '2 bhk', 'Location': 'Wadala', 'Price': 69000},
    {'Name': 'Sai South India Retreat', 'Type': '4 bhk', 'Location': 'Sion', 'Price': 124000},
    {'Name': 'Raju Homes', 'Type': '2 bhk', 'Location': 'Bhayander', 'Price': 58000},
    {'Name': 'Kanal Greens', 'Type': '3 bhk', 'Location': 'Mahim', 'Price': 93000},
    {'Name': 'Krish Plaza', 'Type': '1 bhk', 'Location': 'Dombivli', 'Price': 50000},
    {'Name': 'Sai South India Heights', 'Type': '4 bhk', 'Location': 'Kalyan', 'Price': 127000},
    {'Name': 'Raju Skies', 'Type': '2 bhk', 'Location': 'Malabar Hill', 'Price': 59000},
    {'Name': 'Kanal Residences', 'Type': '3 bhk', 'Location': 'Byculla', 'Price': 90000},
    {'Name': 'Krish Homes', 'Type': '2 bhk', 'Location': 'Wadala', 'Price': 69000},
    {'Name': 'Sai South India Retreat', 'Type': '4 bhk', 'Location': 'Sion', 'Price': 124000},
    {'Name': 'Raju Crest', 'Type': '2 bhk', 'Location': 'Dharavi', 'Price': 60000},
    {'Name': 'Kanal Haven', 'Type': '3 bhk', 'Location': 'Matunga', 'Price': 92000},
    {'Name': 'Krish Towers', 'Type': '1 bhk', 'Location': 'Parel', 'Price': 47000},
    {'Name': 'Sai South India Retreat', 'Type': '4 bhk', 'Location': 'Lalbaug', 'Price': 123000},
    {'Name': 'Raju Springs', 'Type': '2 bhk', 'Location': 'Charni Road', 'Price': 59000},
    {'Name': 'Kanal Oasis', 'Type': '3 bhk', 'Location': 'Grant Road', 'Price': 93000},
    {'Name': 'Krish Residences', 'Type': '2 bhk', 'Location': 'Cuffe Parade', 'Price': 71000},
    {'Name': 'Sai South India Serenity', 'Type': '4 bhk', 'Location': 'Churchgate', 'Price': 131000},
    {'Name': 'Mangol Residency', 'Type': '3 bhk', 'Location': 'Malabar Hills', 'Price': 265000},
    {'Name': 'Black House Apartments', 'Type': '2 bhk', 'Location': 'Malabar Hills', 'Price': 195000},
    {'Name': 'Hillside Homes', 'Type': '4 bhk', 'Location': 'Gilbert Hill', 'Price': 330000},
    {'Name': 'Azad Villa', 'Type': '5 bhk', 'Location': 'Azad Nagar', 'Price': 465000},
    {'Name': 'DN Retreat', 'Type': '3 bhk', 'Location': 'DN Nagar', 'Price': 310000},
    {'Name': 'Apna Bazar Tower', 'Type': '2 bhk', 'Location': 'Apna Bazar', 'Price': 225000},
    {'Name': 'Mangol Mansions', 'Type': '4 bhk', 'Location': 'Malabar Hills', 'Price': 340000},
    {'Name': 'Black House Residences', 'Type': '2 bhk', 'Location': 'Malabar Hills', 'Price': 210000},
    {'Name': 'Hillside Heights', 'Type': '3 bhk', 'Location': 'Gilbert Hill', 'Price': 280000},
    
    {'Name': 'Azad Homes', 'Type': '2 bhk', 'Location': 'Azad Nagar', 'Price': 230000},
    {'Name': 'Raju Heights', 'Type': '1 bhk', 'Location': 'Dadar', 'Price': 40000},
    {'Name': 'Deepali Bungalow', 'Type': '4 bhk', 'Location': 'Worli', 'Price': 128000},
    {'Name': 'Ashutosh Manor', 'Type': '5 bhk', 'Location': 'Vile Parle', 'Price': 220000},
    {'Name': 'Manan Villa', 'Type': '6 bhk', 'Location': 'Chembur', 'Price': 320000},
    {'Name': 'Shreeya Retreat', 'Type': '3 bhk', 'Location': 'Powai', 'Price': 118000},
    {'Name': 'Misbah Cabin', 'Type': '1 bhk', 'Location': 'Bhiwandi', 'Price': 16000},
    {'Name': 'Jafar Ali Mansion', 'Type': '5 bhk', 'Location': 'Bandra', 'Price': 550000},
    {'Name': 'Affan Ansari Retreat', 'Type': '3 bhk', 'Location': 'Malad', 'Price': 92000},
    {'Name': 'Affan Mia Tower', 'Type': '2 bhk', 'Location': 'Nala Sopara', 'Price': 48000},
    {'Name': 'Dilip Apartment', 'Type': '4 bhk', 'Location': 'Kandivali', 'Price': 128000},
    {'Name': 'Sarvanad Heights', 'Type': '2 bhk', 'Location': 'Vasai', 'Price': 75000},
    {'Name': 'Jignesh Tower', 'Type': '3 bhk', 'Location': 'Thane', 'Price': 88000},
    {'Name': 'Atharva Villa', 'Type': '2 bhk', 'Location': 'Goregaon', 'Price': 92000},
    {'Name': 'Goswami Mansion', 'Type': '4 bhk', 'Location': 'Mulund', 'Price': 128000},
    {'Name': 'Sharvya Heights', 'Type': '3 bhk', 'Location': 'Panvel', 'Price': 79000},
    {'Name': 'Lord Cheena Villa', 'Type': 'Villa', 'Location': 'Alibaug', 'Price': 350000},
    {'Name': 'Lord Sandy Tower', 'Type': '5 bhk', 'Location': 'Ulhasnagar', 'Price': 310000},
    {'Name': 'Goat Aditya Cottage', 'Type': 'Chawl', 'Location': 'Goregaon', 'Price': 82000},
    {'Name': 'Geeta Retreat', 'Type': '3 bhk', 'Location': 'Vasai', 'Price': 70000},
    {'Name': 'Shlok Residency', 'Type': '3 bhk', 'Location': 'Malabar Hills', 'Price': 250000},
    {'Name': 'Shlok Apartments', 'Type': '2 bhk', 'Location': 'Malabar Hills', 'Price': 180000},
    {'Name': 'Shlok Heights', 'Type': '4 bhk', 'Location': 'Malabar Hills', 'Price': 320000},
    {'Name': 'Shlok Villa', 'Type': '5 bhk', 'Location': 'Malabar Hills', 'Price': 450000},
    {'Name': 'Shlok Retreat', 'Type': '3 bhk', 'Location': 'Malabar Hills', 'Price': 290000},
    {'Name': 'Shlok Tower', 'Type': '2 bhk', 'Location': 'Malabar Hills', 'Price': 210000},
    {'Name': 'Shlok Mansions', 'Type': '4 bhk', 'Location': 'Malabar Hills', 'Price': 350000},
    {'Name': 'Shlok Homes', 'Type': '2 bhk', 'Location': 'Malabar Hills', 'Price': 200000},
    {'Name': 'Shlok Residences', 'Type': '3 bhk', 'Location': 'Malabar Hills', 'Price': 270000},
    {'Name': 'Shlok Palace', 'Type': '6 bhk', 'Location': 'Malabar Hills', 'Price': 600000},
    {'Name': 'Deepali Tower', 'Type': '2 bhk', 'Location': 'Borivali', 'Price': 58000},
    {'Name': 'Ashutosh Heights', 'Type': '4 bhk', 'Location': 'Dombivali', 'Price': 110000},
    {'Name': 'Manan Cabin', 'Type': '1 bhk', 'Location': 'Panvel', 'Price': 22000},
    {'Name': 'Shreeya Manor', 'Type': '5 bhk', 'Location': 'Thane', 'Price': 256000},
    {'Name': 'Misbah Villa', 'Type': '6 bhk', 'Location': 'Worli', 'Price': 340000},
    {'Name': 'Jafar Ali Residence', 'Type': '3 bhk', 'Location': 'Andheri', 'Price': 85000},
    {'Name': 'Affan Ansari Tower', 'Type': '2 bhk', 'Location': 'Malad', 'Price': 54000},
    {'Name': 'Affan Mia Mansion', 'Type': '4 bhk', 'Location': 'Bandra', 'Price': 128000},
    {'Name': 'Dilip Retreat', 'Type': '3 bhk', 'Location': 'Kandivali', 'Price': 76000},
    {'Name': 'Sarvanad Villa', 'Type': 'Villa', 'Location': 'Powai', 'Price': 350000},
    {'Name': 'Jignesh Tower', 'Type': '5 bhk', 'Location': 'Goregaon', 'Price': 240000},
    {'Name': 'Atharva Heights', 'Type': '3 bhk', 'Location': 'Thane', 'Price': 97000},
    {'Name': 'Goswami Mansion', 'Type': '2 bhk', 'Location': 'Mulund', 'Price': 65000},
    {'Name': 'Sharvya Tower', 'Type': '4 bhk', 'Location': 'Panvel', 'Price': 116000},
    {'Name': 'Lord Cheena Apartment', 'Type': '3 bhk', 'Location': 'Alibaug', 'Price': 96000}]

# Function to add the new properties data to the existing list
def add_new_properties():
    for property_data in new_properties_data:
        add_property(property_data['Name'], property_data['Type'], property_data['Location'], property_data['Price'])

# Customer Portal
def customer_portal():
    load_properties_from_binary()
    while True:
        print("\nCustomer Portal")
        print("1. View Properties")
        print("2. View Transactions")
        print("3. Show All Properties")
        print("4. rent property")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Property Viewing
            print("Available Properties:")
            for index, property in enumerate(properties, start=1):
                print(f"{index}. Name: {property.name}, Type: {property.property_type}, Location: {property.location}, Price: {property.price}")

        elif choice == '2':
            # Transaction Viewing (You need to define your transaction logic)
            print("Transaction history: ")  # Implement your transaction history logic here

        elif choice == '3':
            # Show All Properties
            print("All Properties:")
            for index, property_data in enumerate(new_properties_data, start=1):
                print(f"{index}. Name: {property_data['Name']}, Type: {property_data['Type']}, Location: {property_data['Location']}, Price: {property_data['Price']}")
        elif choice == '4':
            # Rent a Property
            property_index = int(input("Enter the index of the property you want to rent: "))
            if property_index >= 1 and property_index <= len(properties):
                rented_property = properties.pop(property_index - 1)
                print(f"You have rented '{rented_property.name}' for ${rented_property.price}.")
            else:
                print("Invalid property index. Please enter a valid index.")

        elif choice == '4':
            break

# Admin Portal
def admin_portal():
    while True:
        print("\nAdmin Portal")
        print("1. Add Property")
        print("2. Modify Property")
        print("3. Delete Property")
        print("4. break")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Property
            name = input("Enter the property name: ")
            property_type = input("Enter the property type: ")
            location = input("Enter the property location: ")
            price = int(input("Enter the property price: "))
            add_property(name, property_type, location, price)
            print("Property added successfully!")

        elif choice == '2':
            # Modify Property
            property_index = int(input("Enter the index of the property to modify: "))
            if property_index >= 1 and property_index <= len(properties):
                property = properties[property_index - 1]
                print("Current Property Details:")
                print(f"Name: {property.name}")
                print(f"Type: {property.property_type}")
                print(f"Location: {property.location}")
                print(f"Price: {property.price}")

                new_name = input("Enter the new property name (or press Enter to keep the current name): ")
                new_property_type = input("Enter the new property type (or press Enter to keep the current type): ")
                new_location = input("Enter the new property location (or press Enter to keep the current location): ")
                new_price = int(input("Enter the new property price (or press Enter to keep the current price): "))

                if new_name:
                    property.name = new_name
                if new_property_type:
                    property.property_type = new_property_type
                if new_location:
                    property.location = new_location
                if new_price:
                    property.price = new_price

                print("Property modified successfully!")

            else:
                print("Invalid property index. Please enter a valid index.")

        elif choice == '3':
            # Delete Property
            property_index = int(input("Enter the index of the property to delete: "))
            if property_index >= 1 and property_index <= len(properties):
                deleted_property = properties.pop(property_index - 1)
                print(f"Property '{deleted_property.name}' has been deleted.")
            else:
                print("Invalid property index. Please enter a valid index.")
                
    

        elif choice == '4':
            break

        

if __name__ == "__main__":
    # Add the new properties data to the existing list
    add_new_properties()

    while True:
        print("\nProperty Hub Program")
        print("1. Admin Portal")
        print("2. Customer Portal")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_portal()

        elif choice == '2':
            customer_portal()

        elif choice == '3':
            save_properties_to_binary()
            break


       

