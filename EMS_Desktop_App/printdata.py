from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def create_pdf(data):
    dir = 'salary_pdf_reports'
    if not os.path.exists(dir):
        os.mkdir(dir)
    pdf_file = dir + '/'+ data['title'] + '.pdf'
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    c.drawString(50, 730, "GAPAN CITY COLLEGE")
    c.drawString(50, 710, "Date: " + data['current_date'])


    c.drawString(50, 670, "Time Report")
    c.drawString(50, 650, "Total Time: " + data['total_time'])
    c.drawString(50, 630, "Total Over Time: " + data['total_overtime'])
    c.drawString(50, 610, "No. of Days Present: " + data['days_present'])
    c.drawString(50, 590, "No. of Days Absent: " + data['days_absent'])

    c.drawString(50, 560, "Deductions")
    c.drawString(50, 540, "SSS Contribution: PHP" + data['sss'])
    c.drawString(50, 520, "Philhealth Contribution: PHP" + data['philhealth'])
    c.drawString(50, 500, "Pagibig Contribution: PHP" + data['pagibig'])
    c.drawString(50, 480, "Tax: PHP" + data['tax'])
    c.drawString(50, 460, "Total: PHP" + data['total_ded'])

    c.drawString(50, 430, "SPECIAL PAY: PHP" + data['special_pay'])
    c.drawString(50, 410, "GROSS PAY: PHP" + data['gross_pay'])
    c.drawString(50, 390, "PERIOD: " + data['period'])
    c.drawString(50, 370, "STATUS: " + data['status'])

    c.drawString(50, 340, "NET PAY: PHP" + data['net_pay'])
    c.drawString(50, 320, "NAME: " + data['name'])
    c.drawString(50, 300, "POSITION: " + data['position'])

    c.save()

    import subprocess
    import base64
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    with open(pdf_file, 'rb') as f:
        encoded_string = base64.b64encode(f.read())
        lpr.stdin.write(encoded_string)
