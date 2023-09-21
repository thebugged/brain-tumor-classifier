
![braintc](https://github.com/thebugged/brain-tumor-classifier/assets/74977495/14e9c010-6f81-4e29-b699-9f2edd18c174)

## 
# Brain Tumor Classifier
'Brain Tumor Classifier' is an advanced web application powered by TensorFlow, designed to analyze MRI scans and accurately classify brain tumors. With a remarkable test accuracy of 92% and a low loss of 21%, this application provides reliable results.

The primary objective of 'Brain Tumor Classifier' is to assist medical professionals in diagnosing and planning treatments for patients suspected of having brain tumors. By leveraging deep learning and neural networks, the application processes MRI scans, identifying tumor types such as Glioma, Meningioma, Pituitary, or detecting the absence of a tumor.

Please note that 'Brain Tumor Classifier' is intended to support medical professionals and should not replace their expertise. It serves as a valuable tool for improving efficiency and contributing to better patient outcomes.


## Installation
1. Clone the repository:
```shell
git clone https://github.com/your-username/brain-tumor-classifier.git
```

2. Change into the project directory: 
```shell
cd brain-tumor-classifier
```

3. Install the required dependencies: 
```shell
pip install -r requirements.txt
```


## Dataset
The dataset used for training the brain tumor classifier is available on Kaggle. You can download it from the following link:

[Brain Tumor Classifier Dataset on Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)


## AI Model
To run the Brain Tumour Classifier, you will need to download the pretrained ResNet152V2 model in .h5 format. You have two options to obtain the model:


### Option 1: Running Jupyter Notebook
1. Ensure you have Jupyter Notebook installed. If not, you can install it using the following command:
```shell
   pip install jupyter notebook
```
2. Open the resnet.ipynb Jupyter Notebook.
3. Run the notebook cells sequentially by clicking on Cell and selecting Run All.
4. After running all the cells, the resnet.h5 file will be generated in the same directory as the notebook.

Make sure to place the resnet.h5 file in the same directory as the Streamlit app (app.py) before running the application.

### Option 2: Download from Mega
1. Access the Mega link to download the pretrained model by clicking [here](https://mega.nz/folder/46QwiSCY#kTgCWkBJFQ1durISD71zqQ).
2. Click on the download button to save the `resnet.h5` file to your local machine.

Make sure to place the `resnet.h5` file in the same directory as the Streamlit app (`mainapp.py`) before running the application.

## Running the App
Run the Streamlit application using the following command:

```shell
streamlit run mainapp.py
```
The application will be available in your browser at http://localhost:8501.

