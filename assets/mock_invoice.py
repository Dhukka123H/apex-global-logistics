
# Install if needed:
# python -m pip install reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from pathlib import Path


def create_pdf():
    path = Path(__file__).parent / "mock_invoice.pdf"

    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4

    # Corporate color palette
    navy = colors.HexColor("#142D4E")
    blue = colors.HexColor("#2463A6")
    light_blue = colors.HexColor("#EAF2FA")
    background = colors.HexColor("#F5F7FA")
    dark = colors.HexColor("#263445")
    muted = colors.HexColor("#6B7788")
    border = colors.HexColor("#DFE5ED")
    white = colors.white
    green = colors.HexColor("#21865B")

    # Page background
    c.setFillColor(background)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Main white report card
    card_x = 38
    card_y = 42
    card_w = width - 76
    card_h = height - 84

    c.setFillColor(white)
    c.setStrokeColor(border)
    c.roundRect(card_x, card_y, card_w, card_h, 12, fill=1, stroke=1)

    # Header
    header_h = 145
    header_y = card_y + card_h - header_h

    c.setFillColor(navy)
    c.roundRect(
        card_x, header_y, card_w, header_h,
        12, fill=1, stroke=0
    )

    # Square off lower header corners
    c.rect(card_x, header_y, card_w, 12, fill=1, stroke=0)

    # Company name
    left = card_x + 28
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(left, header_y + 91, "APEX GLOBAL")

    c.setFont("Helvetica-Bold", 19)
    c.drawString(left, header_y + 67, "LOGISTICS")

    c.setFillColor(colors.HexColor("#BBD1E8"))
    c.setFont("Helvetica", 8)
    c.drawString(left, header_y + 45, "CORPORATE FINANCE  |  VENDOR SERVICES")

    # Invoice label on right
    right = card_x + card_w - 28
    c.setFillColor(colors.HexColor("#BBD1E8"))
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(right, header_y + 104, "FINANCIAL DOCUMENT")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 17)
    c.drawRightString(right, header_y + 81, "INVOICE")

    c.setFillColor(colors.HexColor("#DCE8F5"))
    c.setFont("Helvetica", 9)
    c.drawRightString(right, header_y + 61, "AGL-2026-8839")

    # Main content start
    content_left = card_x + 28
    content_right = card_x + card_w - 28
    content_width = content_right - content_left

    # Invoice information heading
    section_y = header_y - 37

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(content_left, section_y, "Invoice Overview")

    c.setStrokeColor(border)
    c.line(content_left, section_y - 11,
           content_right, section_y - 11)

    # Two information panels
    panel_y = section_y - 108
    panel_h = 78
    gap = 14
    panel_w = (content_width - gap) / 2

    # Left panel
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(border)
    c.roundRect(content_left, panel_y, panel_w, panel_h,
                7, fill=1, stroke=1)

    c.setFillColor(muted)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(content_left + 13, panel_y + 56, "INVOICE NUMBER")

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(content_left + 13, panel_y + 37, "AGL-2026-8839")

    c.setFillColor(muted)
    c.setFont("Helvetica", 8)
    c.drawString(content_left + 13, panel_y + 17, "Document reference")

    # Right panel
    panel2_x = content_left + panel_w + gap

    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(border)
    c.roundRect(panel2_x, panel_y, panel_w, panel_h,
                7, fill=1, stroke=1)

    c.setFillColor(muted)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(panel2_x + 13, panel_y + 56, "APPROVAL CONTACT")

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(panel2_x + 13, panel_y + 37, "Jane Smith")

    c.setFillColor(muted)
    c.setFont("Helvetica", 8)
    c.drawString(panel2_x + 13, panel_y + 17, "Chief Executive Officer")

    # Amount due highlight
    amount_y = panel_y - 111
    amount_h = 86

    c.setFillColor(light_blue)
    c.roundRect(content_left, amount_y, content_width,
                amount_h, 9, fill=1, stroke=0)

    c.setFillColor(blue)
    c.roundRect(content_left, amount_y, 5,
                amount_h, 2, fill=1, stroke=0)

    c.setFillColor(muted)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(content_left + 18, amount_y + 61, "TOTAL AMOUNT DUE")

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 25)
    c.drawString(content_left + 18, amount_y + 27, "$14,250.00")

    c.setFillColor(blue)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(content_right - 16, amount_y + 43, "USD")

    c.setFillColor(muted)
    c.setFont("Helvetica", 8)
    c.drawRightString(
        content_right - 16, amount_y + 25,
        "Fourteen thousand two hundred fifty dollars"
    )

    # Department details section
    details_y = amount_y - 36

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(content_left, details_y, "Department Details")

    c.setStrokeColor(border)
    c.line(content_left, details_y - 10,
           content_right, details_y - 10)

    # Department row
    row_top = details_y - 30

    c.setFillColor(muted)
    c.setFont("Helvetica", 9)
    c.drawString(content_left, row_top, "Target Department")

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(
        content_right, row_top,
        "Q4 Financial Corporate Operations"
    )

    c.setStrokeColor(border)
    c.line(content_left, row_top - 12,
           content_right, row_top - 12)

    # Approval row
    row2_y = row_top - 31

    c.setFillColor(muted)
    c.setFont("Helvetica", 9)
    c.drawString(content_left, row2_y, "Approved By")

    c.setFillColor(dark)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(content_right, row2_y, "Jane Smith (CEO)")

    c.setStrokeColor(border)
    c.line(content_left, row2_y - 12,
           content_right, row2_y - 12)

    # Status strip
    status_y = row2_y - 43

    c.setFillColor(colors.HexColor("#EAF6EF"))
    c.roundRect(content_left, status_y - 5,
                content_width, 25, 5, fill=1, stroke=0)

    c.setFillColor(green)
    c.circle(content_left + 13, status_y + 7, 3, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 8)
    c.drawString(content_left + 23, status_y + 4, "CORPORATE INVOICE RECORD")

    c.setFillColor(muted)
    c.setFont("Helvetica", 8)
    c.drawRightString(content_right - 10, status_y + 4, "AGL | FINANCE")

    # Footer
    footer_y = card_y + 20

    c.setStrokeColor(border)
    c.line(content_left, footer_y + 13,
           content_right, footer_y + 13)

    c.setFillColor(muted)
    c.setFont("Helvetica", 7.5)
    c.drawString(content_left, footer_y, "APEX GLOBAL LOGISTICS")

    c.drawRightString(
        content_right, footer_y,
        "Vendor Invoice | AGL-2026-8839"
    )

    # PDF metadata
    c.setAuthor("Jane Smith")
    c.setTitle("AGL Q4 Financial Forecast Framework")
    c.setSubject(
        "Internal Network Path: "
        "//AGL-NAS-01/Volume1/Users/jsmith/Docs/"
    )

    c.showPage()
    c.save()

    print(f"Styled invoice generated successfully: {path}")


if __name__ == "__main__":
    create_pdf()
