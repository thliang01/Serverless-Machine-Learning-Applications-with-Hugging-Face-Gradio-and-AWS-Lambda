# app.py
import gradio as gr
import torch
import requests
from PIL import Image
from torchvision import transforms

model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True).eval()

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
  inp = transforms.ToTensor()(inp).unsqueeze(0)
  with torch.no_grad():
    prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(999)}    
  return confidences

# create gradio interface, with text input and dict output
gr.Interface(title="Image Classification in PyTorch",
             fn=predict, 
             inputs=gr.Image(type="pil"),
             outputs=gr.Label(num_top_classes=3),
             examples=["lion.jpg", "cheetah.jpg"]).launch()

# run the app
gr.launch(server_port=7680, enable_queue=False, share=True)
