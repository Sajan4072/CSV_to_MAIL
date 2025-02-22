import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv()

#setup smtp port num nd server
smtp_port = 587
smtp_server = "smtp.gmail.com"

#add emails
email_from= os.getenv('email_from')
email_to=os.getenv('email_to')

pswd=os.getenv('pswd')


#content of msg
message = "Approval Message "


simple_email_context = ssl.create_default_context()

#trying to connect to the server
try:
    print("connecting to the server")
    TIE_server=smtplib.SMTP(smtp_server, smtp_port)  #making server object called TIE_Server and creating a connection
    TIE_server.starttls(context=simple_email_context)   #stating the tls using the context
    TIE_server.login(email_from,pswd)     #login using credential
    print("connected to the server")


    print()
    print("sending the email")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email sent to-{email_to}")
except Exception as e:
    print(f"Error: {e}")
finally:
    TIE_server.quit()

  




