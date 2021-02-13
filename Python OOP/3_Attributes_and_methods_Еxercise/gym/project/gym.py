class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscriptions = [sub for sub in self.subscriptions if sub.id == subscription_id]
        subscription = subscriptions[0] # SUBSCRIPTION OBJECT
        customers = [c for c in self.customers if c.id == subscription.customer_id]
        customer = customers[0] # CUSTOMER OBJECT
        trainers = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id]
        trainer = trainers[0]  # TRAINER OBJECT
        plans = [plan for plan in self.plans if plan.trainer_id == trainer.id]
        plan = plans[0]
        equipments = [eq for eq in self.equipment if eq.id == plan.equipment_id]

        sub = list(map(str, subscriptions))
        cust = list(map(str, customers))
        train = list(map(str, trainers))
        pl = list(map(str, plans))
        eq = list(map(str, equipments))
        res = [sub[0], cust[0], train[0], eq[0], pl[0]]
        return '\n'.join(res)