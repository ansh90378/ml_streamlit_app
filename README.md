# ML Model Streamlit App 🌸  

## 🚀 Overview  
This project is an interactive web application built using [Streamlit](https://streamlit.io/) and Python. It showcases a **Random Forest Classifier** trained to classify iris flower species with **100% accuracy**.  

The application provides a user-friendly interface to interact with the trained model, making predictions on the famous **Iris Dataset**, which is included in the repository.  

## 🛠 Features  
- **ML Model**: Random Forest Classifier trained on the Iris dataset.  
- **Interactive UI**: Streamlit app for real-time predictions.  
- **100% Accuracy**: Achieved through careful training and evaluation.  
- **Deployment**: The app is deployed on Streamlit for easy access.  

## 📂 Project Structure  
```
ML_Model_Streamlit_App/
│
├── data/                # Contains the Iris dataset (iris.csv)
├── model/               # Contains the saved model file (model.pkl)
├── train.py             # Script for training the Random Forest model
├── app.py               # Streamlit application script
├── requirements.txt     # Dependencies for the project
└── README.md            # Project documentation
```  

## 📊 Dataset  
The Iris dataset is a standard dataset for classification tasks, containing 150 records of iris flowers with features such as:  
- **Sepal Length**  
- **Sepal Width**  
- **Petal Length**  
- **Petal Width**  
The target labels are the three species:  
1. Setosa  
2. Versicolor  
3. Virginica  

## 🛠 Tech Stack  
- **Programming Language**: Python  
- **Framework**: Streamlit  
- **Python Libraries**:  
  - `numpy`  
  - `pandas`  
  - `sklearn` (scikit-learn)  
  - `joblib`  

## 🖥 How to Run the Project Locally  
1. Clone the repository:  
   ```bash  
   git clone <repository_url>  
   cd <repository_folder>  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Train the model (if necessary):  
   ```bash  
   python train.py  
   ```  

4. Run the Streamlit app:  
   ```bash  
   streamlit run app.py  
   ```  

5. Open the app in your browser at `http://localhost:8501`.  

## 🚀 Deployment  
The app has been deployed on Streamlit and can be accessed [here]([https://ml-model-rf.streamlit.app/]).  

## 🏆 Accuracy  
Achieved **100% accuracy** in classifying iris flower species.  

## 🤝 Contributing  
Feel free to fork the repo, submit issues, or create pull requests!  

## 📄 License  
This project is licensed under the MIT License.  
