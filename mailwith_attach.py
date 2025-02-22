import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
load_dotenv()

#setup smtp port num nd server
smtp_port = 587
smtp_server = "smtp.gmail.com"

#add emails
email_from= os.getenv('email_from')

def read_emails_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        emails = file.read().split(',')
    return emails

csv_filename = 'email.csv'
email_to = read_emails_from_csv(csv_filename)

print(email_to)
pswd=os.getenv('pswd')


#content of msg
subject="Any Appropriate Subject"
message = "Any appropriate message"



def send_emails(email_to):
    for person in email_to:
        body=f"""
        line 1 
        line 2 
        line 3
        etc
        """

        #make a Mime object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['subject']= subject

        #attach the body to the message
        msg.attach(MIMEMultipart(body,'plain'))


        #define file to attach
        filenames=["testpdf.pdf","testdocs.docx"]

        #open the files in python as a binary
        for file in filenames:
            attachment =open(file, 'rb')  #r for read and b for binary

            #encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + file)
            msg.attach(attachment_package)

            #cast as string
            text=msg.as_string()


        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()
        
    # Close the connection
    TIE_server.quit()
#call the function
send_emails(email_to)




        







  




