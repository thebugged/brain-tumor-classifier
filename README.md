<div align="center">
  <br />
    <a href="">
      <img src="https://github.com/thebugged/brain-tumor-classifier/assets/74977495/66062708-2ed4-4a79-b17a-7db89bf697a7" alt="Banner">
    </a>
  <br />

  <div>
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB" alt="python" />
   <img src="https://img.shields.io/badge/-TensorFlow-black?style=for-the-badge&logoColor=white&logo=tensorflow&color=FF6F00" alt="tensorflow" />
   <img src="https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logoColor=white&logo=sqlite&color=003B57" alt="sqlite" />
   <img src="https://img.shields.io/badge/-Streamlit-black?style=for-the-badge&logoColor=white&logo=streamlit&color=FF4B4B" alt="streamlit" />

</div>


  <h3 align="center">Brain Tumor Classifier</h3>

   <div align="center">
There are more than 100 distinct types of primary brain tumors, each with its own spectrum of presentations, treatments, and outcomes. This app processes MRI scans to identify various tumor types.
    </div>
</div>
<br/>

🗃️ The dataset can be accessed [here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)


## Setup & Installation
**Prerequisites**

Ensure the following are installed;
- [Python](https://www.python.org/downloads/)
- [Jupter Notebook](https://jupyter.org/install) (or install the Jupyter extension on Visual Studio Code).

To set up this project locally, follow these steps:

1. Clone the repository:
```shell
git clone https://github.com/thebugged/brain-tumor-classifier.git
```

2. Change into the project directory: 
```shell
cd brain-tumor-classifier
```

3. Install the required dependencies: 
```shell
pip install -r requirements.txt
```
<br/>

## Running the App
1. Run the `ResNet152V2.ipynb` notebook to get the `resnet.h5` file to run the aplication. You can also downlaod the saved model [here](https://mega.nz/folder/46QwiSCY#kTgCWkBJFQ1durISD71zqQ).

2. Make sure the `resnet.h5` and `mainapp.py` are in the same directory then run the  streamlit application using the command: 
```shell
streamlit run mainapp.py
```
The application will be available in your browser at http://localhost:8501.

