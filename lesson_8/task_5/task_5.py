import csv
import openpyxl


def from_csv_to_exel():

    with open('../task_4/file.csv', 'r') as f:
        reader = csv.reader(f)
        new_list = []
        for row in reader:
            new_list.append(row)
        print(new_list)

    for i in new_list:
        del i[2]

    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet.insert_rows(0)
    sheet['B1'].value = 'Person1'
    sheet['C1'].value = 'Person2'
    sheet['D1'].value = 'Person3'
    sheet['E1'].value = 'Person4'
    sheet['F1'].value = 'Person5'
    sheet['G1'].value = 'Person6'

    for i, row in enumerate(new_list):
        for k, j in enumerate(row):
            sheet.cell(row=k+2, column=i+1).value = j

    wb.save('file.xlsx')


from_csv_to_exel()
