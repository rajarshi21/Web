import openpyxl

path = "D:\\Selenium_project\\EXCEL_DATA_write.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active  # This loads the active sheet.


# Now print the rows and cols.
for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)
