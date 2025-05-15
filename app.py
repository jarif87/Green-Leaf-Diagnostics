# Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

# Loading the Model
model = load_model('my_model.keras')

# Name of Classes
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

# Setting Title of App
st.title("Plant Disease Detection")
st.markdown("Upload an image of the plant leaf")

# Uploading the plant image
plant_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "tiff", "gif", "webp", "heic", "svg"])
submit = st.button('Predict')

# On predict button click
if submit:
    if plant_image is not None:
        # Convert the file to an opencv image
        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # Displaying the image
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)

        # Resizing the image
        opencv_image = cv2.resize(opencv_image, (256, 256))
        # Convert image to 4 dimensions
        opencv_image = opencv_image.reshape(1, 256, 256, 3)
        # Make prediction
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]

        # Parse the result to extract plant and condition
        try:
            parts = result.split('___')
            if len(parts) == 2:
                plant, condition = parts
                display_text = f"This is a {plant} leaf with {condition.replace('_', ' ')}"
            else:
                display_text = f"Prediction: {result}"  # Fallback for unexpected format
            st.title(display_text)
        except IndexError:
            st.error("Error parsing prediction result. Please check the class names format.")