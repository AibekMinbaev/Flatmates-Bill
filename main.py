from final_report import PdfReport, FileSharer
from used_classes import Bill, Flatmate

amount = float(input('Hey user, enter the bill amount: '))
period = input('What is the bill period: ')

name1 = input('What is your name? ')
days_in_house1 = int(input(f'How many days {name1} stay in the house during the period: '))

name2 = input('What is the name of other flatmate? ')
days_in_house2 = int(input(f'How many days {name2} stay in the house during the period: '))


the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_share = FileSharer(filepath=pdf_report.filename)
print(file_share.share())
