<div align="center">
  <br />
    <a href="https://brain-tumor-classifier.streamlit.app">
      <img src="https://github.com/user-attachments/assets/dc5a6b47-87ed-4f8a-a924-1b9742492e8f" alt="Banner">
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
This application processes MRI scans to identify and classify brain tumors into three categories: Pituitary, Glioma, and Meningioma.
    </div>
</div>
<br/>

**Dataset(s)** 🗃️
- [Brain Tumor MRI Dataset
](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) 


## Setup & Installation
**Prerequisites**

Ensure the following are installed;
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
- [Jupter Notebook](https://jupyter.org/install) (or install the Jupyter extension on [Visual Studio Code](https://code.visualstudio.com/)).

<br/>
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

## Running the application
1. Run the command: 
```shell
streamlit run mainapp.py
```
2. Alternatively, you can run the `brain.ipynb` notebook to get the model & weights (`brain_model.json`, `brain_weights.h5`) then run the command in 1.

The application will be available in your browser at http://localhost:8501.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://brain-tumor-classifier.streamlit.app)

