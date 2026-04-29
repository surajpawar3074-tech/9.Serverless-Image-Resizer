# 9.Serverless-Image-Resizer

# 🖼️ Serverless Image Resizer using AWS Lambda & S3

## 📌 Project Overview
This project demonstrates a **serverless image processing system** that automatically processes images when they are uploaded to an S3 bucket.

Whenever a new image is uploaded:
- Lambda function is triggered
- Image is processed (copied/resized logic)
- Stored in another S3 bucket

---

## 🎯 Objective
To:
- Automate image processing  
- Use event-driven architecture  
- Eliminate manual intervention  

---

## 🧰 AWS Services Used

- AWS Lambda – Executes image processing code  
- :contentReference[oaicite:1]{index=1} – Stores original and processed images  

---

## 🏗️ Architecture Flow

S3 Upload → Lambda Trigger → Process Image → Store in Destination Bucket

---

## ⚙️ Features

- ✅ Automatic processing on image upload  
- ✅ Serverless (no infrastructure required)  
- ✅ Real-time event trigger  
- ✅ Scalable and efficient  

---

1. S3 Buckets:

<img width="1037" height="483" alt="Screenshot 2026-04-29 174027" src="https://github.com/user-attachments/assets/a88b8f48-ed75-46f5-b0eb-45b66acd04a9" />

2. Output :
  - Original Image:

    <img width="1338" height="366" alt="Screenshot 2026-04-29 174218" src="https://github.com/user-attachments/assets/6004885a-53ff-4d72-a7a3-0311c5853788" />

  - Resized image:

    <img width="1338" height="354" alt="Screenshot 2026-04-29 174336" src="https://github.com/user-attachments/assets/08092df0-04b8-40d6-8bf9-106878cdd500" />

## Conclusion
This project demonstrates how AWS can be used to build a fully automated serverless image processing system, reducing manual work and improving efficiency.
