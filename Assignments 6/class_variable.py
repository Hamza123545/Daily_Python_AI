class Bank:
    bank_name = "Faysal Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
