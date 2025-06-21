# 📝 Serverless Notes App

This is a **serverless web application** built using Google Cloud Platform (GCP) that allows users to create, store, and manage notes. It is built using a static frontend and a Python Flask backend, all deployed using GCP services.

---

## 📌 Project Goals

✅ Use at least **4 Google Cloud services**  
✅ Host a frontend on a static platform  
✅ Create a backend API using Flask  
✅ Deploy backend as a **serverless container (Cloud Run)**  
✅ Connect backend to a cloud database (Firestore / Cloud SQL)  
✅ Make the project scalable, efficient, and modular

---

## 🚀 Tech Stack & Cloud Services Used

| Feature             | Technology / Service           |
|---------------------|-------------------------------|
| Frontend Hosting    | Firebase Hosting / Cloud Storage (GCS) |
| Backend API         | Cloud Run (Flask + Docker)    |
| Database            | Firestore (or Cloud SQL)      |
| Container Registry  | Artifact Registry / GCR       |

---

## 🧱 Project Structure

📁 frontend/ → HTML, CSS, JS (UI code)
📁 backend/ → Python Flask API
📝 Dockerfile → Container setup for backend
📝 requirements.txt → Python dependencies

---

## 🌐 Architecture Overview

[ User (browser) ]
↓
[ Firebase Hosting / GCS (Static Frontend) ]
↓
[ Cloud Run (Flask API) ]
↓
[ Firestore / Cloud SQL (Database) ]


---

## 🔗 How It Works

1. User opens the website from Firebase Hosting (or Cloud Storage static site)
2. Frontend sends HTTP requests to backend API hosted on Cloud Run
3. Flask API receives the request and interacts with Firestore (or Cloud SQL)
4. Notes are created, read, updated, or deleted from the cloud database
5. API sends the response back to frontend for display

---

## 💻 Running Locally (Optional)

To test Flask backend locally:

```bash
cd backend
pip install -r requirements.txt
python app.py

To build and run Docker container:

bash
Copy
Edit
docker build -t notes-api .
docker run -p 8080:8080 notes-api

Deploy Backend to Cloud Run
bash
Copy
Edit
gcloud builds submit --tag gcr.io/<PROJECT-ID>/notes-api

gcloud run deploy notes-api \
  --image gcr.io/<PROJECT-ID>/notes-api \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated
Deploy Frontend to Firebase Hosting
bash
Copy
Edit
cd frontend
firebase init
firebase deploy


 Cloud Services Connection Summary
Firebase Hosting (or GCS): Hosts the frontend website

Cloud Run: Hosts the Flask API as a serverless container

Firestore (or Cloud SQL): Stores notes in the cloud

Artifact Registry / GCR: Stores container images used by Cloud Run

📸 Architecture Diagram
+-------------+        +------------------------+       +------------------+
|   Browser   |  -->   | Firebase Hosting (UI) |  -->  |  Cloud Run (API)  |
+-------------+        +------------------------+       +------------------+
                                                              ↓
                                                      +------------------+
                                                      |  Firestore / DB  |
                                                      +------------------+

 Author
Bushra Khan
B.Tech IT | Cloud Enthusiast 🌩️ | GitHub: @Bushra-git
