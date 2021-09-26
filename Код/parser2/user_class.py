
class User:
    def __init__(self, input_data):
        self.work_ability = input_data["work_ability"]
        self.salary = input_data["salary"]
        self.marital_status = input_data["marital_status"]
        # 3 statuses - married, single,
        # divorced with alimony (dwa)
        # divorced without alimony (dwoa)

        # Если пользователь в браке, рассчитывается общий семейный бюджет
        if self.marital_status == "married":
            self.family_income = input_data["family_income"]
        else:
            self.family_income = self.salary

        self.num_of_kids = input_data["num_of_kids"]
        self.disability = input_data["disability"]
        if self.disability:
            self.disability_category = input_data["disability_category"]
        # Стоимость недвижимости
        self.real_estate = input_data["real_estate"]
        # Стоимость движимого имущества
        self.movable_property = input_data["movable_property"]
        # Сумма кредитов
        self.loans = input_data["loans"]
        # Сумма по ипотеке
        self.estate_loans = input_data["estate_loans"]
        # Прочие задолженности, включая налоги, штрафы
        self.debts = input_data["debts"]
        # Выплаты пользователю (напр. алименты)
        self.other_payments = input_data["other_payments"]
        pass
