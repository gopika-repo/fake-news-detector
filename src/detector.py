import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

class CrossModalDetector:
    def __init__(self):
        # Load the AI Model (CLIP)
        print("Loading Model...")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def predict(self, text, image_path):
        try:
            image = Image.open(image_path)
            
            # Process text and image
            inputs = self.processor(
                text=[text], 
                images=image, 
                return_tensors="pt", 
                padding=True
            ).to(self.device)

            # Get similarity score
            outputs = self.model(**inputs)
            logits_per_image = outputs.logits_per_image 
            raw_score = logits_per_image.item()
            
            # Convert to percentage (Heuristic scaling)
            probs = min(max((raw_score - 15) * 4, 0), 100)
            
            if probs > 60:
                return probs, "Consistent (Likely Real)"
            elif probs > 40:
                return probs, "Uncertain"
            else:
                return probs, "Inconsistent (Potential Fake)"
                
        except Exception as e:
            return 0, f"Error: {str(e)}"