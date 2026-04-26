import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load model once during initialization to avoid retracing"""
        try:
            model_path = os.path.join("model", "model.h5")
            self.model = load_model(model_path)
            print(f"Model loaded successfully from: {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def predict(self):
        """Make prediction on the image"""
        try:
            imagename = self.filename
            
            # Load and preprocess image
            test_image = image.load_img(imagename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            
            # CRITICAL: Normalize image by dividing by 255 (same as training preprocessing)
            test_image = test_image / 255.0
            
            test_image = np.expand_dims(test_image, axis=0)
            
            # Make prediction
            result = np.argmax(self.model.predict(test_image), axis=1)
            print(f"Prediction result: {result}")

            if result[0] == 1:
                prediction = 'Tumor'
                return [{ "image": prediction}]
            else:
                prediction = 'Normal'
                return [{ "image": prediction}]
        except Exception as e:
            print(f"Error during prediction: {e}")
            raise