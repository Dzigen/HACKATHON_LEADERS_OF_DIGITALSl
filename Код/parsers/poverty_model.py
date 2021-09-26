
# Statistically defined data

# Here should be statistically defined data across of all republic
# but we will use fictive data to test our model

class Model:
    poverty_value = 0

    def __init__(self, user):
        self.poverty_value = 0
        # Для работоспособного населения (married)
        self.poverty_value = user.family_income - user.num_of_kids * 10434 * 1 - 10930 * 2 - \
                             0.95 * user.estate_loans - 0.9 * user.loans + user.other_payments - \
                             + 0.001 * user.real_estate + 0.005 * user.movable_property - \
                             0.8 * user.debts - 0.09 * user.salary

        # > 10 => Средний класс
        # От 5 до 10 => На грани бедности
        # < 5 => За чертой бедности

        print(round(100 * (self.poverty_value/user.family_income)/3, 2))
