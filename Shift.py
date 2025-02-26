class Shift:
    def __init__(self, hours, card_tips,
                 cash_tips,
                 shift_type, base_pay,
                 date,
                 _id = None):
        self.card_tips = float(card_tips)
        self.cash_tips = float(cash_tips)
        self.hours = float(hours)
        self.shift_type = shift_type
        self.base_pay = base_pay
        self._id = _id
        self.date = date

    def get_id(self):
        return self._id

    # Total amount of tips on a shift
    def total_tips(self):
        return self.cash_tips + self.card_tips
    
    # Total amount of money made from a shift, before tax
    def total_money(self):
        return self.total_tips() + self.hours * self.base_pay

    # Total money made per hour, including all tips and base pay
    def total_per_hour(self):
        return self.total_tips() / self.hours + self.base_pay

    # String representation of a shift
    def __str__(self):
        shift_type_str = "Bartending" if self.shift_type == "Bartender" else "Serving"
        return f"{shift_type_str} shift on {self.date} - Hours: {self.hours}, " \
               f"Card tips: ${self.card_tips:.2f}, Cash tips: ${self.cash_tips:.2f}"
    
    # Converts shift to a dictionary, helpful for pandas DF
    def to_dict(self):
        return {
            "Date": self.date,
            "Shift Type": self.shift_type,
            "Hours": self.hours,
            "Card Tips": self.card_tips,
            "Cash Tips": self.cash_tips,
            "Total Money": self.total_money()
        }

