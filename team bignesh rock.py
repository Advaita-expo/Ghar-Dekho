


import csv
import pickle
import mysql.connector

# Create a MySQL database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="bignesh"
)

cursor = conn.cursor()

# Create tables for owners, properties, tenants, property listings, and transactions
cursor.execute('''
    CREATE TABLE  owners (
        id INT AUTO_INCREMENT PRIMARY KEY,
        OwnerName VARCHAR(255) NOT NULL,
        Password VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE properties (
        id INT AUTO_INCREMENT PRIMARY KEY,
        PropertyName VARCHAR(255) NOT NULL,
        Location VARCHAR(255) NOT NULL,
        Price DECIMAL(10, 2) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE  tenants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        TenantName VARCHAR(255) NOT NULL,
        PropertyName VARCHAR(255) NOT NULL,
        RentAmount DECIMAL(10, 2) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE property_listings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        PropertyName VARCHAR(255) NOT NULL,
        OwnerName VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        OwnerName VARCHAR(255) NOT NULL,
        TenantName VARCHAR(255) NOT NULL,
        Amount DECIMAL(10, 2) NOT NULL
    )
''')

# Commit the changes to the database
conn.commit()


print("""
========================================
    PROPERTY MANAGEMENT SYSTEM
========================================
""")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "bignesh"

def sign_up_owner():
    print("""
    ===============================
    !!! Please enter new owner details !!!
    ===============================
    """)

    u = input("Enter New Owner Name: ")
    p = input("Enter password (Combination of Letters, Digits, etc.): ")
    with open("property_owners.dat", "ab") as file:
        owner = {"OwnerName": u, "Password": p}
        pickle.dump(owner, file)
    print("""
    ===============================
    !!! Congratulations!!! New Owner Created !!!
    ===============================
    """)

def login_owner():
    while True:
        print("""
        ===============================
        !!! Owner Login with username and password !!!
        ===============================
        """)
        un = input("Username: ")
        ps = input("Password: ")
        found = False
        try:
            with open("property_owners.dat", "rb") as file:
                while True:
                    owner = pickle.load(file)
                    if owner["OwnerName"] == un and owner["Password"] == ps:
                        found = True
                        break
        except EOFError:
            pass
        if found:
            while True:
                print("""
                1. Property Management
                2. Tenants
                3. Property Listing
                4. Transactions
                5. Sign Out
                """)
                a = int(input("Enter your choice: "))
                if a == 1:
                    property_management_menu()
                elif a == 2:
                    tenants_menu()
                elif a == 3:
                    property_listing_menu()
                elif a == 4:
                    transaction_menu()
                elif a == 5:
                    return
        else:
            print("\nInvalid owner credentials. Please try again.\n")

def property_management_menu():
    while True:
        print("""
        1. Show Property Details
        2. Add New Property
        3. Remove Property
        4. Back
        """)
        b = int(input("Enter your choice: "))
        if b == 1:
            with open("property_data.pkl", "rb") as file:
                while True:
                    try:
                        property = pickle.load(file)
                        print(property)
                    except EOFError:
                        break
        elif b == 2:
            name = input("Enter property name: ")
            location = input("Enter location: ")
            price = float(input("Enter price: "))
            property = {
                "PropertyName": name,
                "Location": location,
                "Price": price
            }
            with open("property_data.pkl", "ab",) as file:
                pickle.dump(property, file)
            print("\nProperty details have been added successfully.\n")
        elif b == 3:
            name = input("Enter property name to remove: ")
            deleted = False
            with open("properties.dat", "rb") as file:
                properties = []
                while True:
                    try:
                        property = pickle.load(file)
                        if property["PropertyName"] != name:
                            properties.append(property)
                        else:
                            deleted = True
                    except EOFError:
                        break
            with open("properties.dat", "wb") as file:
                for property in properties:
                    pickle.dump(property, file)
            if deleted:
                print(f"\n{property} has been removed.\n")
            else:
                print(f"\nNo property found with the name {name}.\n")
        elif b == 4:
            return

def tenants_menu():
    while True:
        print("""
        1. Show Tenants
        2. Add Tenant
        3. Remove Tenant
        4. Back
        """)
        b = int(input("Enter your choice: "))
        if b == 1:
            with open("tenants.dat", "rb") as file:
                while True:
                    try:
                        tenant = pickle.load(file)
                        print(tenant)
                    except EOFError:
                        break
        elif b == 2:
            name = input("Enter tenant name: ")
            property_name = input("Enter property name: ")
            rent = float(input("Enter rent amount: "))
            tenant = {
                "TenantName": name,
                "PropertyName": property_name,
                "RentAmount": rent
            }
            with open("tenants.dat", "ab") as file:
                pickle.dump(tenant, file)
            print("\nTenant details have been added successfully.\n")
        elif b == 3:
            name = input("Enter tenant name to remove: ")
            deleted = False
            with open("tenants.dat", "rb") as file:
                tenants = []
                while True:
                    try:
                        tenant = pickle.load(file)
                        if tenant["TenantName"] != name:
                            tenants.append(tenant)
                        else:
                            deleted = True
                    except EOFError:
                        break
            with open("tenants.dat", "wb") as file:
                for tenant in tenants:
                    pickle.dump(tenant, file)
            if deleted:
                print(f"\n{tenant} has been removed.\n")
            else:
                print(f"\nNo tenant found with the name {name}.\n")
        elif b == 4:
            return

def property_listing_menu():
    while True:
        print("""
        1. Show Property Listings
        2. Add New Property Listing
        3. Search for Property Listing
        4. Back
        """)
        c = int(input("Enter your choice: "))
        if c == 1:
            with open("property_listings.dat", "rb") as file:
                while True:
                    try:
                        property_listing = pickle.load(file)
                        print(property_listing)
                    except EOFError:
                        break
        elif c == 2:
            property_name = input("Enter property name: ")
            owner_name = input("Enter owner name: ")
            property_listing = {
                "PropertyName": property_name,
                "OwnerName": owner_name
            }
            with open("property_listings.dat", "ab") as file:
                pickle.dump(property_listing, file)
            print("\nProperty listing details have been added successfully.\n")
        elif c == 3:
            search_name = input("Enter property name to search: ")
            found = False
            with open("property_listings.dat", "rb") as file:
                while True:
                    try:
                        property_listing = pickle.load(file)
                        if property_listing["PropertyName"] == search_name:
                            print(property_listing)
                            found = True
                    except EOFError:
                        break
            if not found:
                print("\nNo property listing found with the given property name.\n")
        elif c == 4:
            return

def transaction_menu():
    while True:
        print("""
        1. Show Transactions
        2. Add Transaction
        3. Back
        """)
        d = int(input("Enter your choice: "))
        if d == 1:
            with open("Ghar.csv", mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        elif d == 2:
            owner_name = input("Enter owner name: ")
            tenant_name = input("Enter tenant name: ")
            location=input("enter the location")
            amount = float(input("Enter transaction amount: "))
            transaction = {
                "OwnerName": owner_name,
                "TenantName": tenant_name,
                "Location":location,
                "Amount": amount
            }
            with open("Ghar.csv", mode='a', newline='') as file:
                fieldnames = ["OwnerName", "TenantName","Location","Amount"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(transaction)
            print("\nTransaction details have been added successfully.\n")
        elif d == 3:
            return

def admin_login():
    print("""
    ===============================
    !!! Admin Login with username and password !!!
    ===============================
    """)
    un = input("Admin Username: ")
    ps = input("Admin Password: ")
    if un == ADMIN_USERNAME and ps == ADMIN_PASSWORD:
        while True:
            print("""
            Admin Portal:
            1. Show Property Owners
            2. Show All Transactions
            3. Back
            """)
            a = int(input("Enter your choice: "))
            if a == 1:
                with open("property_data.pkl", "rb") as file:
                    while True:
                        try:
                            owner = pickle.load(file)
                            print(owner)
                        except EOFError:
                            break
            elif a == 2:
                with open("Ghar.csv", mode='r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        print(row)
            elif a == 3:
                break
    else:
        print("Invalid admin credentials. Please try again.")

while True:
    print("""
    1. Owner Sign Up
    2. Owner Log In
    3. Admin Login
    4. Exit
    """)
    r = int(input("Enter your choice: "))
    if r == 1:
        sign_up_owner()
    elif r == 2:
        login_owner()
    elif r == 3:
        admin_login()
    elif r == 4:
        print("\nThank you for using the property management system. Have a nice day!\n")
        break

