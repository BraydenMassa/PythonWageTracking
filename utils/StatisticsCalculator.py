class StatisticsCalculator:
    def __init__(self, shift_list):
        self.shift_list = shift_list

    def serving_shifts(self):
        return [shift for shift in self.shift_list if shift.shift_type == "Server"]

    def bartending_shifts(self):
        return [shift for shift in self.shift_list if shift.shift_type == "Bartender"]

    def total_hours(self):
        return sum(shift.hours for shift in self.shift_list)

    def total_tips(self):
        return f"{sum(shift.total_tips() for shift in self.shift_list):.2f}"

    def total_money(self):
        return f"{float(self.total_tips()) + sum(shift.hours * shift.base_pay for shift in self.shift_list):.2f}"

    def total_hourly_rate(self):
        if self.total_hours() == 0:
            return 0
        return f"{float(self.total_money()) / float(self.total_hours()):.2f}"

