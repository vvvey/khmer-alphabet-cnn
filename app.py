from flask import Flask, request, jsonify, render_template
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

# Load pretrained CNN, and the label encoder
loaded_model = tf.keras.models.load_model('my_model.h5')
loaded_label_encoder = joblib.load('label_encoder.pkl')

@app.route('/predict', methods=['POST'])
def save_image():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({'message': 'No image provided'}), 400

    image_data = data['image']
    # Remove the head part of the base64 string
    if image_data.startswith('data:image/png;base64,'):
        image_data = image_data.replace('data:image/png;base64,', '')

    image_bytes = base64.b64decode(image_data)

    # Create a BytesIO object from the bytes
    image_file = BytesIO(image_bytes)

    # Open the image using PIL
    image = Image.open(image_file)

    # Processing the image
    image = image.convert('L')
    image = image.resize((28, 28))  # Resize to 28x28
    image.save("./proceesed.png")
    image_array = np.array(image) / 255.0  # Normalize to [0, 1]
    
    image_array = image_array.reshape(1, 28, 28, 1)
    
    prediction = loaded_model.predict([image_array]) # predict

    predicted_classes = np.argmax(prediction, axis=1)  # Get class indices
    predicted_labels = loaded_label_encoder.inverse_transform(predicted_classes)  # Decode to original labels

    prediction = loaded_model.predict(image_array)

    # Get the predicted class
    predicted_class = np.argmax(prediction, axis=1) # get the max prob class
    print("Predicted Class:", predicted_class[0])

    class_probabilities = [{'class':f'{loaded_label_encoder.inverse_transform([i])[0]   }', 'probability': round(float(prob), 2)} for i, prob in enumerate(prediction[0])]
   
    return jsonify({'message': 'Image info fetched and processed', 'letter': predicted_labels[0], 'prob': class_probabilities})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()