import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Function to generate QR code
def generate_qr_code(url):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit app
def main():
    st.title('QR Code Generator')
    
    # User input for URL
    website_url = st.text_input("Enter the website URL to generate a QR code:", "")
    
    if website_url:
        # Generate QR code
        qr_image = generate_qr_code(website_url)
        
        # Convert PIL image to bytes to display in Streamlit
        buf = BytesIO()
        qr_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.image(byte_im, caption="Generated QR Code", use_column_width=True)
        st.success("QR code generated successfully!")

if __name__ == "__main__":
    main()
