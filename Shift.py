from datetime import datetime

def default_date():
    return datetime.now().strftime("%m/%d/%y")

class Shift:
    def __init__(self, hours, card_tips,
                 cash_tips,
                 shift_type, base_pay,
                 date = default_date(),
                 _id = None):
        self.card_tips = float(card_tips)
        self.cash_tips = float(cash_tips)
        self.hours = float(hours)
        self.shift_type = shift_type
        self.base_pay = base_pay
        self._id = _id
        self.date = date

    # Total amount of tips on a shift
    def total_tips(self):
        return self.cash_tips + self.card_tips

    # Total money made per hour, including all tips and base pay
    def total_per_hour(self):
        return self.total_tips() / self.hours + self.base_pay

    def __str__(self):
        return f"Shift on {self.date} - Hours: {self.hours}, " \
               f"Card tips: ${self.card_tips:.2f}, Cash tips: ${self.cash_tips:.2f}, " \
               f"ShiftType: {self.shift_type}"

