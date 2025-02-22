# Method to display Statistics
from operations.StaticOperations import print_header
from utils.StatisticsCalculator import StatisticsCalculator


def display_statistics(shift_repo):
    shifts = shift_repo.get_all_shifts()
    stats_calc = StatisticsCalculator(shifts)
    server_calc = StatisticsCalculator(stats_calc.serving_shifts())
    bartender_calc = StatisticsCalculator(stats_calc.bartending_shifts())
    print_header("Statistics")
    print("\n" + '*' * 38)
    print("Overall:\n")
    print(f"Total hours worked: {stats_calc.total_hours()}")
    print(f"Total money made: ${stats_calc.total_money()}")
    print(f"Average hourly rate: ${stats_calc.total_hourly_rate()}/hr")
    print("*" * 38)
    print("Serving:\n")
    print(f"Serving hours worked: {server_calc.total_hours()}")
    print(f"Total money made serving: ${server_calc.total_money()}")
    print(f"Average hourly rate serving: ${server_calc.total_hourly_rate()}")
    print("*" * 38)
    print("Bartending:\n")
    print(f"Bartending hours worked: {bartender_calc.total_hours()}")
    print(f"Total money made bartending: ${bartender_calc.total_money()}")
    print(f"Average hourly rate bartending: ${bartender_calc.total_hourly_rate()}")
    print("*" * 38 + "\n")
