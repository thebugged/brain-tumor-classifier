
![Neural Tumor Classifier](screenshot.png)

## 
# Neural Tumor Classifier
Neural Tumor Classifier is a web application that processes MRI scans to determine the type of tumor present (Glioma, Meningioma, Pituitary) or if there is no tumor present.


## Function
Neural Tumor Classifier is designed to assist in the classification of brain tumors using convolutional neural networks. The application takes an MRI scan as input and applies a trained ResNet152V2 model to predict the type of tumor or indicate the absence of a tumor. It provides a quick and convenient way to analyze MRI scans and obtain tumor classification results.


## How to Use
1. Upload an MRI scan (in PNG, JPG, or JPEG format).
2. The application will analyze the scan and provide the predicted tumor type or indicate no tumor.


## Installation
1. Clone the repository:
```shell
git clone https://github.com/your-username/neural-tumor-classifier.git
```

2. Change into the project directory: 
```shell
cd neural-tumor-classifier
```

3. Install the required dependencies: 
```shell
pip install -r requirements.txt
```

## Running the App
Run the Streamlit application using the following command:

```shell
streamlit run app.py
```
The application will be available in your browser at http://localhost:8501.


## Dataset
The dataset used for training the neural tumor classifier is available on Kaggle. You can download it from the following link:

[Neural Tumor Classifier Dataset on Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)


