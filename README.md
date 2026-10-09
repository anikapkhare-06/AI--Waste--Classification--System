# ♻️ EcoVision AI

### Computer Vision-Based Waste Classification and Recycling Assistant

EcoVision AI is a computer vision project that applies deep learning-based image classification to identify waste-related objects from digital images. The system processes user-uploaded images, generates predictions using a pretrained vision model, and provides category-specific recycling guidance through an interactive web application.

The project demonstrates the practical application of **Computer Vision, Image Processing, Deep Learning, and Transfer Learning** in waste classification.

## 🎯 Project Objectives

* Apply computer vision techniques to waste image classification.
* Use a pretrained deep learning model to analyze visual input.
* Process uploaded images before model inference.
* Map model predictions to broader waste categories.
* Display prediction confidence scores and alternative predictions.
* Provide general recycling and disposal guidance.

## 🧠 Computer Vision Concepts Used

**1. Digital Image Input**

The system accepts images in JPG, JPEG, and PNG formats as input for visual analysis.

**2. Image Processing**

The Pillow library is used to open uploaded images, correct image orientation using EXIF metadata, and convert them to RGB format.

**3. Deep Learning-Based Image Classification**

The project uses a pretrained image classification model to analyze image features and predict the most likely class.

**4. Transfer Learning**

The application uses an already-trained model instead of training a new vision model from scratch.

**5. Prediction Scores**

The model returns scores for predicted labels. These scores help compare predictions but do not guarantee that the predicted class is correct.

**6. Category Mapping**

A custom Python function maps the model's original labels to broader waste categories to provide more understandable results.

## ✨ Key Features

* Image-based waste classification
* Pretrained computer vision model
* Image orientation correction and RGB conversion
* Top-five model predictions
* Prediction confidence visualization
* Category-specific recycling guidance
* Interactive Streamlit interface

## ♻️ Waste Categories

The application maps supported model labels into the following broader categories:

* Plastic
* Paper
* Cardboard
* Glass
* Metal
* Organic
* E-Waste
* Textile
* Trash
* Other

The final category depends on the original label returned by the model and the mapping rules implemented in `app.py`.

## 🛠️ Technology Stack

| Component                 | Technology                |
| ------------------------- | ------------------------- |
| Programming language      | Python                    |
| Computer vision task      | Image classification      |
| Deep learning framework   | PyTorch                   |
| Pretrained model pipeline | Hugging Face Transformers |
| Image processing          | Pillow (PIL)              |
| Web interface             | Streamlit                 |

## 🤖 Pretrained Model

**Model:** `watersplash/waste-classification`

The application loads the pretrained model through the Hugging Face Transformers image-classification pipeline. The model analyzes an uploaded image and returns predicted labels with associated scores.

The application uses the highest-ranked prediction for its category-mapping and recycling-guidance process.

## ⚙️ System Workflow

```text
User Uploads Waste Image
          |
          v
Image Loading using Pillow
          |
          v
Orientation Correction
and RGB Conversion
          |
          v
Pretrained Image
Classification Model
          |
          v
Prediction Labels and Scores
          |
          v
Waste Category Mapping
          |
          v
Recycling Guidance
and Result Visualization
```

## 📂 Project Structure

```text
EcoVision-AI/
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Execution

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/EcoVision-AI.git
cd EcoVision-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal to use the application.

An internet connection may be needed to download the pretrained model the first time it is loaded.

## 🖼️ Results and Demonstration

The application displays the uploaded image alongside the classification result. After the user selects **Classify Waste**, it presents the mapped category, original model label, confidence score, recycling guidance, and top-five model predictions.

To document the project, add screenshots of:

1. The main EcoVision AI interface.
2. An uploaded waste image.
3. The classification result and confidence score.
4. The top-five predictions, if visible.

Save screenshots in a `screenshots/` directory and add them to this section once uploaded to GitHub.

## ⚠️ Limitations

* Classification performance depends on the pretrained model and input image.
* The model's output is not a guarantee of correct identification.
* Category mapping is based on predefined text-matching rules.
* Recycling guidance is general and may not match local waste-management rules.
* Overall model accuracy has not been established without systematic evaluation on a labelled test dataset.

## 🔮 Future Scope

* Evaluate model performance using precision, recall, F1-score, and a confusion matrix.
* Develop a labelled waste-image test dataset.
* Explore fine-tuning on a broader waste classification dataset.
* Add camera-based image capture.
* Extend the application with detailed recycling recommendations.

## 👨‍💻 Author

**Anika Khare**

## 📌 Project Domain

Computer Vision | Image Processing | Deep Learning | AI for Sustainability

## 📄 Disclaimer

EcoVision AI is an educational computer vision project. Predictions should be verified, and local waste-disposal guidelines should be followed before disposing of any item.
 
 
