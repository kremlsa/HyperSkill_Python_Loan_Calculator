import math
import argparse

principal = 0
periods = 0
payment = 0
interest = 0
type_ = ""
options = ""

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str,
                    help='type of payment')
parser.add_argument('--payment', type=float,
                    help='the monthly payment amount.')
parser.add_argument('--principal', type=int,
                    help='principal')
parser.add_argument('--periods', type=int,
                    help='the number of months needed to repay the loan.')
parser.add_argument('--interest', type=float,
                    help='interest')
args = parser.parse_args()


def print_error_parameters():
    print("Incorrect parameters")


def parse_args():
    global principal
    global periods
    global payment
    global interest
    global type_
    global options
    if args.principal:
        principal = args.principal
    if args.periods:
        periods = args.periods
    if args.payment:
        payment = args.payment
    if args.interest:
        interest = args.interest
    if args.type:
        type_ = args.type
    if int(payment) < 0 or int(principal) < 0 or int(periods) < 0 or int(interest) < 0:
        print_error_parameters()
        return False

    if type_ != "diff" and type_ != "annuity":
        print_error_parameters()
        return False


def calculate_count():
    i = interest / (12 * 100)
    number_months = math.log(payment / (payment - i * principal), 1 + i)
    number_months = math.ceil(number_months)
    total_payment = number_months * payment
    years = "" if number_months < 12 else "{} year".format(number_months // 12)
    months = "" if number_months % 12 == 0 else "{} month".format(number_months % 12)
    ending_month = "s" if number_months % 12 > 1 else ""
    ending_year = "s" if number_months // 12 > 1 else ""
    and_ = "" if years == "" or months == "" else " and "
    print("It will take {}{}{}{}{} to repay this loan!".format(years, ending_year, and_, months, ending_month))
    print("Overpayment = {}".format(int(total_payment - principal)))


def calculate_annuitet():
    i = interest / (12 * 100)
    annuity = principal * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)
    print("Your annuity payment = {}!".format(math.ceil(annuity)))
    print("Overpayment = {}".format(math.ceil(annuity) * periods - int(principal)))

def calculate_principal():
    i = interest / (12 * 100)
    principal = payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
    print("Your loan principal = {}!".format(int(principal)))
    print("Overpayment = {}".format(int(payment * periods) - int(principal)))


def calculate_diff():
    print()
    i = interest / (12 * 100)
    sum_ = 0
    for m in range(1, periods + 1):
        pay = principal / periods + i * (principal - principal * (m - 1) / periods)
        print("Month {}: payment is {}".format(m, math.ceil(pay)))
        sum_ = sum_ + math.ceil(pay)
    print()
    print("Overpayment = {}".format(sum_ - principal))


parse_args()
if args.type and args.principal and args.payment and args.interest:
    calculate_count()
elif args.type and args.periods and args.payment and args.interest:
    calculate_principal()
elif args.type == "annuity" and args.periods and args.principal and args.interest:
    calculate_annuitet()
elif args.type == "diff" and args.periods and args.principal and args.interest:
    calculate_diff()
else:
    print_error_parameters()
