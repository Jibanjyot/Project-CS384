from reportlab.pdfgen import canvas 
from reportlab.platypus import Paragraph, Table, TableStyle, Frame,Image
from reportlab.lib import colors 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import  A3
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

pdf = canvas.Canvas ("tutorials.pdf",pagesize=A3)

print(A3)
pdf.setPageSize((842,800))
flow_obj= []

styles = getSampleStyleSheet()

#------------------------------------------------------------#
"""main name table and add box to it"""
headertable = Table([["Roll No: ","1901ME29","Name: ","Jibanjyoti Kalita", "Year of Admission: ","2019"], 
            ["Programme: ","Bachelor of Technology","Course: ","Mechanical Engineering"],"",""])
flow_obj.append(headertable)
frame=Frame (350, 500, 100, 200, showBoundary=0)
frame.addFromList(flow_obj, pdf)
frame=Frame (150, 651, 530, 40, showBoundary=1)
frame.addFromList(flow_obj, pdf)
#------------------------------------------------------------#


#------------------------------------------------------------#
#code to add tables
t1 = Paragraph("Semester 1", style=styles ["Normal"]) 
flow_obj.append(t1)
t = Table([["Sub Code","Sub Name","L-T-P","Grade"], 
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"]])
ts=TableStyle( [("GRID", (0,0),(-1,-1),1, colors.black), ("BACKGROUND", (0,0),(-1,-1), colors.white)])
t.setStyle(ts) 
flow_obj.append(t)
frame=Frame (80,450, 100, 200, showBoundary=0)
frame.addFromList(flow_obj, pdf)

#------------------------------------------------------------#


#------------------------------------------------------------#
#code to add tables
t1 = Paragraph("Semester 2", style=styles ["Normal"]) 
flow_obj.append(t1)
t = Table([["Sub Code","Sub Name","L-T-P","Grade"], 
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"]])
ts=TableStyle( [("GRID", (0,0),(-1,-1),1, colors.black), ("BACKGROUND", (0,0),(-1,-1), colors.white)])
t.setStyle(ts) 
flow_obj.append(t)
frame=Frame (300,450, 100, 200, showBoundary=0)
frame.addFromList(flow_obj, pdf)

#------------------------------------------------------------#



#------------------------------------------------------------#
#code to add tables
t1 = Paragraph("Semester 3", style=styles ["Normal"]) 
flow_obj.append(t1)
t = Table([["Sub Code","Sub Name","L-T-P","Grade"], 
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"],
            ["AB110","ABCD","1-2-3","AA"]])
ts=TableStyle( [("GRID", (0,0),(-1,-1),1, colors.black), ("BACKGROUND", (0,0),(-1,-1), colors.white)])
t.setStyle(ts) 
flow_obj.append(t)
frame=Frame (520,450, 100, 200, showBoundary=0)
frame.addFromList(flow_obj, pdf)

#------------------------------------------------------------#

frame=Frame (20, 20, 800, 760, showBoundary=1)
frame.addFromList(flow_obj, pdf)

#------------------------------------------------------------#

#------------------------------------------------------------#

frame=Frame (20, 200, 800, 260, showBoundary=1)
frame.addFromList(flow_obj, pdf)

#------------------------------------------------------------#

#add image
image = Image("IITPLOGO2.PNG",750,70)
print(image)
t = Table([[image]])
flow_obj.append(t)
frame=Frame (350, 577, 120, 200, showBoundary=0)
frame.addFromList(flow_obj, pdf)
#------------------------------------------------------------#





pdf.save()