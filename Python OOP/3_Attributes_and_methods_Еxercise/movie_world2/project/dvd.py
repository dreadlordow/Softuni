from calendar import month_name

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False
    
    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date_split = [int(x) for x in date.split('.')]
        year = date_split[2]
        month = date_split[1]
        month = month_name[month]
        day = date_split[0]
        return cls(name, id, year, month, age_restriction)
        
    def __repr__(self):
        self.status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.status}"
    
