from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime


def generate_bill(filename,bill_data):
    c=canvas.Canvas(filename,pagesize=A4)
    subtotal=bill_data.get("subtotal",0)
    discount=bill_data.get("total_discount",0)
    tax=bill_data.get("tax",0)
    invoice_no = bill_data.get("invoice_no", "INV-0001")
    date_time = datetime.now().strftime("%d-%m-%Y")
    items = bill_data.get("items", [])
    c.line(50, 810, 550, 810)
    c.setFont("Helvetica-Bold",18)
    c.drawCentredString(595//2,780,"STORE NAME")
    c.setFont("Helvetica",10)
    c.drawCentredString(595//2,765, "Kottarakara, Kerala")
    c.line(50,750,550,750)
    c.drawString(50,730,f"Invoice No :  {invoice_no}")
    c.drawString(50,710,f"Date       :  {date_time}")
    c.line(50,680,550,680)
    y=660
    c.drawString(50,y,"Items")
    c.drawString(150,y,"Category")
    c.drawString(250,y,"Qty")
    c.drawString(350,y,"Price")
    c.drawString(450,y,"Total")
    c.line(50,y-2,550,y-2)
    # items
    for item in items:
        if y < 120:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 700
        y -= 20
        c.drawString(50,y,str(item.get("name","")))
        c.drawString(150,y,str(item.get("category","")))
        c.drawString(250,y,str(item.get("quantity",0)))
        c.drawString(350,y,str(item.get("price",0)))
        c.drawString(450,y,str(item.get("total",0)))
    c.line(50,y-2,550,y-2)
    y-=40
    c.drawString(50,y,"Subtotal")
    c.drawString(400,y,str(subtotal))
    y-=20
    c.drawString(50,y,"Discount")
    c.drawString(400,y,str(discount))
    y-=20
    c.drawString(50,y,"Tax")
    c.drawString(400,y,str(tax))
    y-=20
    Total=subtotal-discount+tax
    c.line(50,y,550,y)
    y-=20
    c.drawString(50,y,"Total")
    c.drawString(400,y,str(Total))
    y-=20
    c.line(50,y,550,y)
    y-=20
    c.drawString(50,y,"Items Purchased")
    c.drawString(400,y,str(bill_data.get("item_count",0)))
    y-=20
    c.drawString(50,y,"Thank you for shopping with us!")
    y-=20
    c.drawString(50,y,"Visit Again!")
    c.save()

