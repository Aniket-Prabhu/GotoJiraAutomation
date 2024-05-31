import openpyxl


def create_excel(data):
    data.insert(0, ['Sprints', 'Committed', 'Completed', 'StartDate', 'EndDate','Velocity','DoneIndex'])
    
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    for row in data:
        worksheet.append(row)

    workbook.save('data.xlsx')