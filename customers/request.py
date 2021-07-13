CUSTOMERS = [
    {
      "id": 1,
      "name": "Billy Bob",
      "address": "7002 Chestnut Ct",
      "email": "billy@bob.com"
    },
    {
      "id": 2,
      "name": "Jackie Doe",
      "address": "2000 Blvd",
      "email": "jackie@doe.com"
    },
    {
      "id": 3,
      "name": "Jill Jolly",
      "address": "2030 Washington Blvd",
      "email": "jill@jolly.com"
    }
]

def get_all_customers():
    return CUSTOMERS


# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer