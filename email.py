import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Email configuration
smtp_host = 'your_smtp_host'
smtp_port = 587
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
recipient_email = 'recipient@example.com'

# Create the email content
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Image Embedded in Email Body'

# HTML content of the email
html_content = """\
<html>
  <body>
    <p>Here is an embedded image:</p>
    <p><img src="cid:image"></p>
  </body>
</html>
"""
message.attach(MIMEText(html_content, 'html'))

# Load the image
image_path = 'path_to_your_image.png'
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()

# Attach the image to the email
image = MIMEImage(image_data, name='image.png')
image.add_header('Content-ID', '<image>')
message.attach(image)

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
finally:
    server.quit()
