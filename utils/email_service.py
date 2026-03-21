import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

def send_email( 
            receiver_email , 
            receiver_name , 
            sender_name = "David Kajinake Schenezare" , 
            sender_email = "folkwinx@gmail.com"
            ):
    e_mail = MIMEMultipart()
    e_mail["From"] = sender_name
    e_mail["To"] = receiver_name
    e_mail ["Subject"] = "E-MAIL SUCCESSFULLY RECEIVED"
    message = f"""
Hello {receiver_name} , We are testing if we can send email to contacters and as well notify the developer as well. Thank you
"""
    text_message = MIMEText(message , "plain")
    e_mail.attach(text_message)
    letter = e_mail.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    attempts = 0
    while attempts < 5 :
        try:
            server.login(sender_email,"pfma duds szop rxwe")
            break
        except Exception as e:
             print(f"Error connecting to the server {e}\nRetrying.....")
             attempts +=1
    try: 
        server.sendmail( sender_email , receiver_email , letter )
        server.quit()
    except Exception as e:
         print(f"Error occured trying to send an email: {e}")
    return{
        "contacter_email": receiver_email , 
        "contacter_name": receiver_name , 
        "contacter_message": message
    }

def notify_developer(
        self_email = "folkwinx@gmail.com",
        code ="pfma duds szop rxwe"
                   ):
    contacter = send_email( "mukundwadavid@gmail.com","Mukundwa David" )
    contacter_email_address = contacter["contacter_email"]
    contacter_name = contacter["contacter_name"]
    contacter_message = contacter["contacter_message"]
    e_mail = MIMEMultipart()
    e_mail["From"] = "Self"
    e_mail["To"] = "Self"
    e_mail["Subject"] = f"New person contacted {contacter_name}"
    body = f"""
A new person , with the email address '{contacter_email_address}' has contacted you.
Here is the message they sent:

{contacter_message}
""" 
    wrapped_body = MIMEText(body)
    e_mail.attach(wrapped_body)
    e_mail_to_send = e_mail.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(self_email,code)
    server.sendmail(self_email , self_email , e_mail_to_send)
    server.quit()



# send_email( receiver_email= "mukundwadavid250@gmail.com" , receiver_name= "Mukundwa David" )
# notify_developer()