import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, m, year = date.split('.')
        creation_month = calendar.month_name[int(m)]

        return cls(name, id, int(year), creation_month, age_restriction)

    def rent(self):
        self.is_rented = True

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return (f'{self.id}: {self.name} ({self.creation_month} {self.creation_year})'
                f' has age restriction {self.age_restriction}. Status: {status}')