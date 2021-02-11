class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if isinstance(value, float):
            return 'value is not a float'
        return cls(int(value))

    @classmethod
    def from_roman(cls, value: str):
        pass

    @classmethod
    def from_string(cls, value: str):
        try:
            if not isinstance(value, str):
                raise ValueError('Not an instance of string')
            return Integer(int(value))
        except ValueError:
            return 'wrong type'

    def add(self, other):
        if not isinstance(other, Integer):
            return 'number should be an Integer instance'
        return self.value + other.value