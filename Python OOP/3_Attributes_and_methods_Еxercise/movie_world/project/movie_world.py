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

    def add_customer(self, customer):
        if len(self.customers) >= MovieWorld.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) >= MovieWorld.dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer, customer_dvds, current_dvd = self.get_lists(customer_id, dvd_id)
        if customer_dvds:
            return f'{customer[0].name} has already rented {customer_dvds[0].name}'
        if current_dvd[0].is_rented:
            return f'DVD is already rented'
        if current_dvd[0].age_restriction > customer[0].age:
            return f'{customer[0].name} should be at least {current_dvd[0].age_restriction} to rent this movie'

        customer[0].rented_dvds.append(current_dvd[0])
        current_dvd[0].is_rented = True
        return f'{customer[0].name} has successfully rented {current_dvd[0].name}'

    def return_dvd(self, customer_id, dvd_id):
        customer, customer_dvds, current_dvd = self.get_lists(customer_id, dvd_id)
        if not customer_dvds:
            return f'{customer[0].name} does not have that DVD'
        customer[0].rented_dvds.remove(current_dvd[0])
        current_dvd[0].is_rented = False
        self.dvds.append(current_dvd[0])
        return f'{customer[0].name} has successfully returned {current_dvd[0].name}'

    def get_lists(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id]
        customer_dvds = [dvd for dvd in customer[0].rented_dvds if dvd.id == dvd_id]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        return customer, customer_dvds, current_dvd

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))

        return '\n'.join(customers + dvds)