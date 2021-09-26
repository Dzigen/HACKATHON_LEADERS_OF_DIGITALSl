from user_class import User
from poverty_model import Model

input_data = {
    "work_ability": True,
    "salary": 43000,
    "marital_status": "married",
    "num_of_kids": 1,
    "disability": False,
    "disability_category": "None",
    "real_estate": 1500000,
    "movable_property": 190000,
    "loans": 4000,
    "debts": 4500,
    "other_payments": 0,
    "family_income": 50000,
    "estate_loans": 15000
}

user1 = User(input_data)
model1 = Model(user1)
print(model1.poverty_value)
