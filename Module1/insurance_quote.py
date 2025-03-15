"""
* Name         : insurance_quote.py
* Author       : E Wilber
* Created      : 01/19/25
* Module       : 1
* Topic        : 4
* Description  : Insurance Quote Assignment
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
cost_dict = {
    16: {
        "min": 2593,
        "liability": 2957,
        "full": 6930
    },
    25: {
        "min": 608,
        "liability": 691,
        "full": 1745
    },
    35: {
        "min": 552,
        "liability": 627,
        "full": 1564
    },
    45: {
        "min": 525,
        "liability": 596,
        "full": 1469
    },
    55: {
        "min": 494,
        "liability": 560,
        "full": 1363
    },
    65: {
        "min": 515,
        "liability": 585,
        "full": 1402
    }
}
def get_name():
    while True:
        name = input("Enter your first name: ").strip()
        if name.isalpha():
            return name
        else:
            print("Invalid name.")
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 16:
                print("Age must be over 16.")
                continue
            return age
        except ValueError:
            print("Invalid age.")
def get_coverage():
    while True:
        coverage = input("Enter coverage level (SM, L, F): ").strip().lower()
        if coverage in ("sm", "l", "f"):
            return coverage
        else:
            print("Invalid, please enter 'SM', 'L', or 'F'.")
def has_accidents():
    while True:
        response = input("Have you been in any accidents? ('yes' or 'no'): ").strip().lower()
        if response in ("yes", "no"):
            return response == "yes"
        else:
            print("Please answer 'yes' or 'no'.")
def wants_upfront_discount():
    while True:
        response = input("Do you want to pay upfront for a 10% discount? ('yes' or 'no'): ").strip().lower()
        if response in ("yes", "no"):
            return response == "yes"
        else:
            print("Please answer 'yes' or 'no'.")
def calculate_cost(age, coverage, accidents, upfront_discount):
    age_key = max(k for k in cost_dict.keys() if k <= age)
    coverage_key = {"sm": "min", "l": "liability", "f": "full"}[coverage]
    base_cost = cost_dict[age_key][coverage_key]
    if accidents:
        base_cost *= 1.41
    if upfront_discount:
        base_cost *= 0.9
    return round(base_cost, 2)
def main():
    print("Welcome to Riley's Auto Insurance. Let's get started.")
    name = get_name()
    age = get_age()
    coverage = get_coverage()
    accidents = has_accidents()
    upfront_discount = wants_upfront_discount()

    total_cost = calculate_cost(age, coverage, accidents, upfront_discount)
    print(f"\n{name}, Your annual insurance cost will be: ${total_cost}")
if __name__ == "__main__":
    main()