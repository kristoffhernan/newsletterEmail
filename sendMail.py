import smtplib
from email.message import EmailMessage
import config

contacts = []
with open('contacts.txt', 'r') as c:
    next(c)
    for line in c:
        x = line.rstrip().split('\t')
        contacts.append(x[2])
    c.close()

msg = EmailMessage()
msg['Subject'] = 'Test message'
msg['From'] = config.EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Just testing the python code')

with open('D:/Documents/UCR/Fall2021/NorthDistrictCheckIn.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-straem', filename='NorthDistrictCheckIn.pdf')

with open('D:/Pictures/Saved Pictures/zcyhewq.jpg', 'rb') as j:
    jpg_data = j.read()
    jpg_name = j.name

msg.add_attachment(jpg_data, maintype='image', subtype='jpeg', filename=jpg_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    smtp.send_message(msg)   

