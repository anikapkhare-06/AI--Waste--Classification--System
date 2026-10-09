
import streamlit as st
import torch
from PIL import Image, ImageOps
from transformers import pipeline

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="EcoVision AI",
    page_icon="♻️",
    layout="wide"
)

# -----------------------------
# Waste category information
# -----------------------------
WASTE_INFO = {
    "Plastic": {
        "icon": "🧴",
        "color": "#0D9488",
        "advice": (
            "Empty and clean plastic containers. "
            "Check local recycling rules before disposal."
        )
    },
    "Paper": {
        "icon": "📄",
        "color": "#2563EB",
        "advice": (
            "Keep paper clean and dry. "
            "Separate it from food and liquid waste."
        )
    },
    "Cardboard": {
        "icon": "📦",
        "color": "#B45309",
        "advice": (
            "Flatten cardboard boxes and keep them dry "
            "for paper/cardboard recycling."
        )
    },
    "Glass": {
        "icon": "🍾",
        "color": "#059669",
        "advice": (
            "Separate glass items and follow your local "
            "glass collection guidelines."
        )
    },
    "Metal": {
        "icon": "🥫",
        "color": "#64748B",
        "advice": (
            "Empty metal cans and containers. "
            "Use an appropriate metal recycling stream."
        )
    },
    "Organic": {
        "icon": "🍃",
        "color": "#65A30D",
        "advice": (
            "Food and plant waste may be suitable for "
            "composting, depending on local facilities."
        )
    },
    "E-Waste": {
        "icon": "🔋",
        "color": "#DC2626",
        "advice": (
            "Take batteries and electronic waste to an "
            "authorized collection or recycling centre."
        )
    },
    "Textile": {
        "icon": "👕",
        "color": "#9333EA",
        "advice": (
            "Reuse or donate wearable items. "
            "Check local textile collection options."
        )
    },
    "Trash": {
        "icon": "🗑️",
        "color": "#6B7280",
        "advice": (
            "Check whether the item can be reused or "
            "recycled before putting it in general waste."
        )
    },
    "Other": {
        "icon": "♻️",
        "color": "#0F766E",
        "advice": (
            "Check the original prediction and local "
            "waste disposal guidelines."
        )
    }
}


def map_category(label):
    """Map the model's original label to a broad category."""
    label = label.lower().replace("_", "-").strip()

    if "cardboard" in label:
        return "Cardboard"
    if "paper" in label:
        return "Paper"
    if "glass" in label:
        return "Glass"
    if "plastic" in label:
        return "Plastic"
    if "metal" in label:
        return "Metal"
    if "biological" in label or "brown-grass" in label:
        return "Organic"
    if "battery" in label:
        return "E-Waste"
    if "clothes" in label or "shoes" in label:
        return "Textile"
    if "trash" in label:
        return "Trash"

    return "Other"


# -----------------------------
# Load pretrained model once
# -----------------------------
@st.cache_resource(show_spinner=False)
def load_model():
    device = 0 if torch.cuda.is_available() else -1

    return pipeline(
        task="image-classification",
        model="watersplash/waste-classification",
        device=device
    )


# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div style="
        background: linear-gradient(120deg, #064e3b, #0f766e);
        padding: 28px;
        border-radius: 16px;
        color: white;
        margin-bottom: 20px;
    ">
        <h1 style="margin:0;">♻️ EcoVision AI</h1>
        <p style="margin:8px 0 0 0;">
            AI-Powered Waste Classification and Recycling Assistant
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Upload a waste image to get a model prediction, "
    "confidence score, and general disposal guidance."
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("About EcoVision AI")
st.sidebar.write(
    "This application uses a pretrained image "
    "classification model to recognize waste-related images."
)

st.sidebar.markdown("---")
st.sidebar.subheader("Supported categories")
st.sidebar.write(
    "Plastic, paper, cardboard, glass, metal, "
    "organic waste, textiles, batteries and trash."
)

# -----------------------------
# Upload image
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = ImageOps.exif_transpose(image).convert("RGB")

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with right:
        st.subheader("Classification Result")

        if st.button("🔍 Classify Waste", type="primary",
                     use_container_width=True):

            try:
                with st.spinner(
                    "Loading model and analyzing image..."
                ):
                    classifier = load_model()
                    predictions = classifier(
                        image,
                        top_k=5
                    )

                best = predictions[0]
                raw_label = best["label"]
                category = map_category(raw_label)
                confidence = float(best["score"]) * 100

                info = WASTE_INFO[category]

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #d1d5db;
                        border-left: 6px solid {info['color']};
                        padding: 18px;
                        border-radius: 12px;
                    ">
                        <h2 style="margin:0;">
                            {info['icon']} {category}
                        </h2>
                        <p style="margin:8px 0 0 0;">
                            <b>Model label:</b> {raw_label}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.metric(
                    "Model confidence",
                    f"{confidence:.2f}%"
                )

                st.progress(min(confidence / 100, 1.0))

                st.subheader("Recycling Guidance")
                st.write(info["advice"])

                st.caption(
                    "Confidence is the model's score, not a "
                    "guarantee that the prediction is correct."
                )

                with st.expander("View top 5 model predictions"):
                    for item in predictions:
                        name = item["label"]
                        score = float(item["score"]) * 100

                        st.write(
                            f"**{name}** — {score:.2f}%"
                        )
                        st.progress(min(score / 100, 1.0))

            except Exception as error:
                st.error(
                    "The model could not be loaded or the "
                    "image could not be classified."
                )
                st.info(
                    "Check your internet connection and "
                    "installed libraries, then try again."
                )
                st.code(str(error))

else:
    st.info(
        "👆 Upload an image above to begin classification."
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "EcoVision AI | Computer Vision Project | "
    "Predictions should be verified before real-world disposal."
)