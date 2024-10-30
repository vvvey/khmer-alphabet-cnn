# Khmer Alphabet Handwriting CNN

This README provides instructions on how to set up and run a Flask application for the Khmer Alphabet CNN project, as well as information on training the model.

## Prerequisites

- Python 3.9
- pip
- Docker (optional, if you choose to run via Docker)

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:vvvey/khmer-alphabet-cnn.git
cd khmer-alphabet-cnn
```

### 2. Install Dependencies
To install the required Python packages, run:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
You can run the Flask application in one of two ways:

#### Option A: Run Locally
Start the Flask application using the following command:
```bash
python app.py
```
The application should be running on http://localhost:5000

#### Option B: Run Using Docker
If you prefer to run the application using Docker, you can build and run it with the following commands:

1. Build the Docker image
```bash
docker build -t khmer-cnn .
```
2. Run the Docker container:
```bash
docker run -d -p 5000:80 --name khmer-cnn khmer-cnn
```
In this case, the application will also be available at http://localhost:5000

### 4. Train the Model
To train the model, use the model.pynb Jupyter notebook. This notebook will save the trained model to my_model.h5 and the label encoder to label_encoder.pkl.

You can run the notebook using Jupyter Notebook: 
```bash
model.ipynb
```

### 5. Model Performance
The pretrained model has achieved a test accuracy of 95% .

## Notes
- Ensure the necessary system dependencies for running Flask and Docker are installed.
- If you make any changes to the model or requirements, remember to rebuild the Docker image.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.