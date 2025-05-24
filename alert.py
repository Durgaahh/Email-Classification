import smtplib
from email.mime.text import MIMEText

def send_alert_email(message):
    try:
        sender = "youremail@example.com"
        receiver = "alertrecipient@example.com"
        password = "your_app_specific_password"  # Avoid hardcoding real password in production!

        # Create the message
        msg = MIMEText(f"Spam alert triggered:\n\n{message}")
        msg['Subject'] = "Spam Detection Alert"
        msg['From'] = sender
        msg['To'] = receiver

        # Connect to SMTP server
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("✅ Alert email sent successfully!")

    except Exception as e:
        print("❌ Email alert failed:", e)
