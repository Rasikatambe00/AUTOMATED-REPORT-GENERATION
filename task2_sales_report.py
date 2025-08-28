from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import datetime

def generate_sales_report(input_file, output_pdf):
    # Read sales data
    data = []
    with open(input_file, "r") as f:
        for line in f:
            row = line.strip().split(",")
            try:
                row[1] = int(row[1])
                row[2] = int(row[2])
            except:
                pass
            data.append(row)

    # Totals
    total_units = sum([row[1] for row in data[1:]])
    total_revenue = sum([row[2] for row in data[1:]])

    # Create PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.darkblue)
    c.drawCentredString(width / 2, height - 80, "📊 Monthly Sales Report")

    # Subtitle
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 105, "Generated using Python & ReportLab")

    # Table
    table = Table(data, colWidths=[150, 150, 150])
    style = TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#4CAF50")),  # header green
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 12),
        ("BOTTOMPADDING", (0,0), (-1,0), 10),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("GRID", (0,0), (-1,-1), 0.8, colors.black),
    ])
    table.setStyle(style)

    # Place table closer to title (was -350 earlier, reduced to -250)
    table.wrapOn(c, width, height)
    table.drawOn(c, 100, height - 250)

    # Summary just below table
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(colors.black)
    c.drawString(100, height - 280, f"✅ Total Units Sold: {total_units}")
    c.drawString(100, height - 300, f"💰 Total Revenue: ${total_revenue}")

    # Footer with date
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.gray)
    c.drawCentredString(width / 2, 30, f"Report generated on {datetime.date.today()}")

    # Save
    c.save()
    print(f"✅ Sales report generated: {output_pdf}")


# Paths
input_path = "C:/Users/rudra/OneDrive/Desktop/rasika python practicals/sales_data.txt"
output_path = "C:/Users/rudra/OneDrive/Desktop/rasika python practicals/sales_report.pdf"

generate_sales_report(input_path, output_path)
