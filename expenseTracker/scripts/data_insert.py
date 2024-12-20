# from ExpTrack.models import login
import datetime
from ExpTrack.models import Issue,login

emp_ins = login.objects.get(emp_id = "e001@gmail.com")
Issue.objects.create(emp_i = emp_ins,txn_id = "F458", txn_name = "Swipe at ATM",txn_date = datetime.date(2024,10,16),charges=2000,txn_type="Debited")
Issue.objects.create(emp_i = emp_ins,txn_id = "ZUP903", txn_name = "UPI payment to JioMart",txn_date = datetime.date(2024,10,16),charges=3700,txn_type="Debited")
Issue.objects.create(emp_i = emp_ins,txn_id = "T89", txn_name = "Refund from Amazon",txn_date = datetime.date(2024,10,16),charges=500,txn_type="Credited")

print("Sucessfull")