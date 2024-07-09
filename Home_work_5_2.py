from typing import Callable
import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
def generator_numbers(text: str):
    for i in  re.findall(r"\d+\.\d+",text):
        yield i
def sum_profit(text: str, func: Callable):
    total_profit = 0
    for i in generator_numbers(text):
        total_profit += float(i)
    return total_profit
def main():
    total_profit = sum_profit(text,generator_numbers)
    return f"Загальний дохід : {total_profit}"
if __name__ == "__main__":
    main()
print(main())