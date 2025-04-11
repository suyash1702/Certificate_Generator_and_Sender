import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.message import EmailMessage
import os

# Streamlit app
st.title("Certificate Generator and Sender")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Email configuration
email_address = st.text_input("Your Email Address")
email_password = st.text_input("Your App Password", type="password")

# Custom message
custom_message = st.text_area("Custom Message", "For participation in {event}, organized by Computer Department under ASCII in collaboration with PRECCON on April 12, 2025.")

# Certificate template
template_path = st.text_input("Certificate Template Path", "Final_1.png")

# Generate and send certificates
if st.button("Generate and Send Certificates"):
    if uploaded_file and email_address and email_password:
        # Load fonts
        font_name = ImageFont.truetype("Fonts/Shelley.ttf", 175)
        font_event_description = ImageFont.truetype("Fonts/Cormorant.ttf", 45)

        # Make sure 'certificates' folder exists
        os.makedirs("certificates", exist_ok=True)

        for index, row in df.iterrows():
            name = row['Name']
            event = row['Event']
            email = row['Email']

            # Load certificate template
            cert = Image.open(template_path)
            draw = ImageDraw.Draw(cert)

            # Example coordinates - adjust to your layout
            name_position = (1020, 640)
            event_position = (1000, 813)

            # Draw name and event
            draw.text(name_position, name, font=font_name, fill="black", anchor="mm")
            event_text = custom_message.format(event=event)
            draw.text(event_position, event_text, font=font_event_description, fill="black", anchor="mm")

            # Save output
            cert_path = f"certificates/{name}_{event}.png"
            cert.save(cert_path)

            # Send the certificate via email
            subject = f"Certificate for {event}"
            body = f"Dear {name},\n\n{event_text}\n\nBest regards,\nYour Organization"
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = email_address
            msg['To'] = email
            msg.set_content(body)

            with open(cert_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(cert_path)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)

            st.success(f"Certificate created and sent to {name} at {email}")

    else:
        st.error("Please provide all required inputs.")
