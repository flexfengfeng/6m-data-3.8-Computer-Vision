# app.py — CIFAR-10 recogniser using YOUR fine-tuned ResNet18 (Hugging Face Space)
# ---------------------------------------------------------------------------
# This single-model app loads the transfer-learning model you trained in Part B
# of the assignment:
#   • Model B: a ResNet18 you fine-tuned on CIFAR-10  (file: cifar_resnet.pt)
#
# CIFAR-10 is COLOUR 32x32 photos in 10 everyday categories (below).
# Upload your model file (cifar_resnet.pt) next to this app.py in your Space.

import torch
import torch.nn as nn
import torchvision.transforms as T
from torchvision.models import resnet18
import gradio as gr

# The 10 CIFAR-10 classes, in the exact order the dataset uses (0..9).
CLASSES = ["airplane", "automobile", "bird", "cat", "deer",
           "dog", "frog", "horse", "ship", "truck"]

# ---------------------------------------------------------------------------
# Rebuild the SAME architecture you trained, then load the saved weights.
# In Part B you loaded a pretrained ResNet18 and replaced its final `fc` layer
# with a fresh 10-class head. Here we build the empty skeleton the same way and
# pour your learned weights into it.
# ---------------------------------------------------------------------------
model = resnet18(weights=None)                       # empty ResNet18 skeleton
model.fc = nn.Linear(model.fc.in_features, 10)       # same 10-class head you trained
model.load_state_dict(torch.load("cifar_resnet.pt", map_location="cpu"))
model.eval()

# ---------------------------------------------------------------------------
# Prepare each uploaded image EXACTLY how the model saw images during training
# (Part B's imagenet_tf): upscale to 96x96, normalise with ImageNet mean/std.
# Getting this preprocessing right is essential — a mismatch wrecks accuracy.
# ---------------------------------------------------------------------------
# IMPORTANT: during training this model NEVER saw sharp photos. It saw tiny
# 32x32 CIFAR images upscaled to 96x96 — i.e. blurry, low-detail images.
# If we feed it a sharp photo resized straight to 96x96, the image looks
# nothing like its training data and predictions get worse / less confident.
# So we replicate the training pipeline exactly: shrink to 32x32 FIRST
# (throwing away the extra detail), THEN upscale to 96x96.
prep = T.Compose([
    T.Resize((32, 32)),   # step 1: down to CIFAR size — match what training data looked like
    T.Resize((96, 96)),   # step 2: up to the input size the model expects
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def predict(image):
    if image is None:
        return {}
    image = image.convert("RGB")            # make sure it's 3-channel colour
    x = prep(image).unsqueeze(0)            # add batch dimension -> (1, 3, 96, 96)
    with torch.no_grad():
        probs = torch.softmax(model(x), dim=1)[0]
    return {CLASSES[i]: float(probs[i]) for i in range(10)}


description = (
    "Upload a colour photo and YOUR fine-tuned ResNet18 will guess which of 10 "
    "CIFAR-10 categories it is.\n\n"
    "⚠️ The model only ever saw tiny 32×32 CIFAR-10 images. It will confidently "
    "guess on anything — try photos inside and outside the 10 categories and watch "
    "where it succeeds or fails."
)

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload a colour image"),
    outputs=gr.Label(num_top_classes=3, label="Top guesses"),
    title="My CIFAR-10 Recogniser (ResNet18 transfer learning)",
    description=description,
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
