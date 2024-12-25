import streamlit as st
import base64
# Display some text on the page
st.write('Hello, Sigmoiterians!')

# Create a placeholder to show/hide the image
image_placeholder = st.empty()

# Add custom CSS to style the button and show image on hover
st.markdown("""
    <style>
        button {
            background: transparent;
            border: none !important;
            font-size: 0; /* No visible text */
            cursor: pointer; /* Interactive button */
        }
        
        .stButton:hover + .image_container {
            display: block;
        }
        
        .stButton {
            background-color: transparent;
            border: none;
            padding: 0;
        }
        
        .image_container {
            display: none;
            text-align: center;
            margin-top: 10px;
        }
        
        .image_container img {
            width: 100px;  /* Image size 100x100px */
            height: 100px;
        }
    </style>
    <div class="stButton">
        <button>Hover to see image</button>
    </div>
    <div class="image_container">
        <img src="data:image/png;base64,{}">
    </div>
""", unsafe_allow_html=True)

# Encode the image
with open('src/textquery/secret/sigmoid.png', 'rb') as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()

# Add the base64-encoded image to the HTML
st.markdown(f"""
    <style>
        .image_container img {{
            content: url('data:image/png;base64,{encoded_image}');
        }}
    </style>
""", unsafe_allow_html=True)
