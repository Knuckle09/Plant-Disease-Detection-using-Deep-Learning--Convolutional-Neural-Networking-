
# 🌿 Plant Disease Detection Web App  

This repository contains a fully functional web application for detecting plant diseases, deployed on the **Heroku cloud server**. Follow the instructions below to set up and run the project on your local machine or deploy it to Heroku.  

## Breif Description:
This Flask-based web application leverages Deep Learning (CNN) to diagnose plant health by analyzing an uploaded leaf image of fruit or vegetable plants. The model identifies diseases (if any) and provides:

✅ Disease Description – Detailed insights into the identified disease.
✅ Recommended Treatment – Suggested medicines with purchase links.
✅ Healthy Plant Guidance – If the plant is healthy, users receive growth tips to maximize yield.
✅ Fertilizer Suggestions – Recommendations for fertilizers with buy links to enhance production.

With this intelligent solution, farmers and gardeners can detect plant diseases early, improve yield, and make data-driven decisions for better plant care. 🚀🌱

---

## 📌 Setup Instructions  

### 1️⃣ Install Dependencies  
Ensure you have all the required dependencies installed. Save the following packages in `requirements.txt` and run:  

```bash
pip install -r requirements.txt
```

### 2️⃣ Model File  
- The trained model file **(`plant_disease_model_1_latest.pt`)** must be present in this folder.  
- Train the model on your local machine and place it in the project directory.  
- If you rename the model file, ensure you update the corresponding argument in `app.py`.  

### 3️⃣ Running the App Locally  
After installing the requirements, you can run the web app locally using:  

```bash
python app.py
```

### 4️⃣ Deployment on Heroku  
For Heroku deployment, ensure:  
- You have a `Procfile` in the root directory.  
- All dependencies are listed in `requirements.txt`.  
- The trained model file is included in the project directory.  

To deploy, follow the standard Heroku deployment steps:  

```bash
heroku login
heroku create <your-app-name>
git push heroku main
```

---

## 📂 Project Structure  

- `app.py` – Main application file  
- `requirements.txt` – Required dependencies  
- `Procfile` – Configuration for Heroku deployment  
- `plant_disease_model_1_latest.pt` – Trained model file  

---

## 🚀 Additional Notes  
- Before making changes, check the **Model section** of this repository for details on the deployed app.  
- Ensure all files are correctly placed before running or deploying.  

DEMO IMAGES:
<center>
![image](https://github.com/user-attachments/assets/a4558b5a-1c76-4add-82e2-43c574996e56)
![image](https://github.com/user-attachments/assets/71ec3b87-7dd5-4ede-938c-50f9b8b78991)
![image](https://github.com/user-attachments/assets/60354166-27b3-4345-b1ef-45f7bcccc61d)
![image](https://github.com/user-attachments/assets/e8715306-d293-442c-92d3-364e19fa8b7d)
</center>


Google Drive link for plant_disease_model_1_latest.pt: (https://drive.google.com/drive/folders/1ewJWAiduGuld_9oGSrTuLumg9y62qS6A?usp=share_link)
