from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class_name = 'CSCE 331'
crn = '50593'
seats_open = 1
sender_email = "clahey922@gmail.com"
sender_password = 'Areyoumal1!'
receiver_email = 'yasir@yilmazcoban.com'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Course Available Notification'
body = f'{class_name} with CRN {crn} has {seats_open} seats open!'
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 25)
server.set_debuglevel(1)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, sender_password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()