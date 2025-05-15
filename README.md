# PlantDiseaseDetector

**PlantDiseaseDetector** is a Jupyter Notebook-based project that uses a deep learning model to detect diseases in plant leaves from uploaded images. Built with Streamlit for a web interface, it currently focuses on potato leaf diseases (Early Blight, Late Blight, and Healthy), making it useful for farmers, researchers, and plant enthusiasts to diagnose plant health.

## Features

- **Image Upload**: Upload leaf images (JPG, PNG, etc.) via a Streamlit web interface.
- **Disease Prediction**: Classifies potato leaf conditions using a pre-trained Keras model.
- **Interactive Notebook**: Explore and modify the code in a Jupyter Notebook environment.
- **Real-Time Results**: Displays the predicted disease or health status with confidence.



# Installation

Follow these steps to set up the project locally:

# Prerequisites
- Python 3.8+
- pip (Python package manager)
- Jupyter Notebook or JupyterLab
- Virtual environment (recommended)

## Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/PlantDiseaseDetector.git
   cd PlantDiseaseDetector

2. **Create and activate a virtual environment:**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies:**
```

pip install -r requirements.txt

```
4. **Download the pre-trained model:**

- Place my_model.keras in the project root (model file not included in repo due to size).

- Alternatively, train your own model (see Training (#training)).

5. **Launch Jupyter Notebook:**
```
jupyter notebook

Open the Agricultural Disease Forecasting.ipynb notebook in your browser.

```
# Usage
- Open PlantDiseaseDetector.ipynb in Jupyter Notebook.

- Run the cells to start the Streamlit app (ensure all dependencies are installed).

- Follow the notebook instructions to launch the Streamlit interface.

- Upload a potato leaf image via the web interface.

- Click the Predict button to view the diagnosis (e.g., "This is a Potato leaf with Early Blight").

Model Details
Architecture: Convolutional Neural Network (CNN) built with Keras.

# Classes:
- Potato___Early_blight

- Potato___Late_blight

- Potato___healthy

- Input: 256x256 RGB images.

### Training Data: Potato Disease Dataset (https://www.kaggle.com/datasets/aarishasifkhan/plantvillage-potato-disease-dataset).


# Training
### To train your own model:
- Prepare a dataset with labeled images (e.g., Early Blight, Late Blight, Healthy).

- Preprocess images (resize to 256x256, normalize, etc.).

- Use the provided training cells in PlantDiseaseDetector.ipynb or adapt your training pipeline.

- Save the trained model as my_model.keras.


# Project Structure

```
PlantDiseaseDetector/
├── PlantDiseaseDetector.ipynb  # Main Jupyter Notebook
├── my_model.keras             # Pre-trained model (not included)
├── requirements.txt           # Dependencies
├── data/                      # Dataset folder (optional, not included)
└── README.md                  # This file
```

# Dependencies
### Listed in requirements.txt:
- streamlit

- numpy

- opencv-python

- tensorflow (or keras)

- pillow (for image handling)

- jupyter

## Install with
```
pip install -r requirements.txt
```