class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def get_customers(self):
        return len(self.customers)

    def get_dvds(self):
        return len(self.dvds)


    def get_customer_by_id(self, id):
        return [c for c in self.customers if c.id == id][0]

    def get_dvd_by_id(self, id):
        dvd = [dvd for dvd in self.dvds if dvd.id == id][0]
        if dvd:
            return dvd
        return False

    def check_customer_age(self, dvd, customer):
        if dvd.age_restriction > customer.age:
            return False
        return True
    
    def check_customer_dvds(self, id, dvd_id):
        customer = self.get_customer_by_id(id)
        rented = [d for d in customer.rented_dvds if d.id == dvd_id]
        if rented:
            return rented[0]
        return False

    def add_customer(self, customer):
        if self.get_customers() < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.get_dvds() < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'

        age = self.check_customer_age(dvd, customer)
        if not age:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        rented = self.check_customer_dvds(customer_id, dvd_id)
        customer = self.get_customer_by_id(customer_id)
        if not rented:
            return f'{customer.name} does not have that DVD'
        
        customer.rented_dvds.remove(rented)
        rented.is_rented = False
        self.dvds.append(rented)
        return f'{customer.name} has successfully returned {rented.name}'

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))

        return '\n'.join(customers + dvds)
