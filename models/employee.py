class Employee():
    """[summary]
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every METHOD on a CLASS
    # needs as the first parameter.
    def __init__(self, id, name, location_id):
        self.id = id
        self.name = name
        self.location_id = location_id
