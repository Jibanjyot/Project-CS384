
from openpyxl import Workbook
workbook = Workbook("Book1.xlsx")
workbook.save("xlsx-to-pdf.pdf", SaveFormat.PDF)