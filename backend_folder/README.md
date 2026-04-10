---
title: Assignment Validator Backend
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Backend API Endpoints


Hugging Face Spaces per aapka backend successfully run ho gaya hai! Jo `{"detail":"Not Found"}` aapko root URL (jaise `https://abdulqayyum360-backend.hf.space/`) pe show ho raha hai, wo is liye hai kyunki aapke code mein root `/` pe koi data nahi bheja gaya. Yeh bilkul normal hai! Aapke saare asl endpoints perfectly kaam kar rahay hain.

Niche aapki sab APIs ki list hai jinhe aap apnay **Frontend** me connect kar saktay hain:

### Base URL:
`https://abdulqayyum360-backend.hf.space`

---

## 1. Submit Assignment
Ye endpoint assignment submit karne k liye hai.
- **Method:** `POST`
- **URL:** `https://abdulqayyum360-backend.hf.space/submit`
- **Body Example (JSON):**
  ```json
  {
      "studentId": "insert_student_id_here",
      "assignmentId": "insert_assignment_id_here",
      "link": "https://github.com/your-repo"
  }
  ```

---

## 2. Student Dashboard 
Student ka specific data, errors aur missed assignments check karne k liye (notifications ke sath).
- **Method:** `GET`
- **URL:** `https://abdulqayyum360-backend.hf.space/student-dashboard/{student_id}`
*(Note: `{student_id}` ko actual student ID se replace karein, eg: `/student-dashboard/654abc...`)*

---

## 3. Student Progress
Ek student ki total, submitted, aur missed assignments ki progress dekhne k liye.
- **Method:** `GET`
- **URL:** `https://abdulqayyum360-backend.hf.space/student-progress/{student_id}`
*(Note: `{student_id}` ko actual student ID se replace karein)*

---

## 4. Missed Students
Kisi specific assignment ke liye wo students nikalne k liye jinhone deadline miss kardi hai.
- **Method:** `GET`
- **URL:** `https://abdulqayyum360-backend.hf.space/missed-students/{assignment_id}`
*(Note: `{assignment_id}` ko actual assignment ID se replace karein)*

---

## 5. Overall Assignment Status
Tamam assignments ka overall status check karne k liye k domain me se kitny logo ne submit kiya aur kitny rehtay hain.
- **Method:** `GET`
- **URL:** `https://abdulqayyum360-backend.hf.space/assignment-status`

---

**FastAPI Swagger Docs:**
Agar aap sab endpoints ka interface aur testing direct browser se karna chahte hain, to simply apnay URL ke aagay `/docs` laga kar check karein:
👉 `https://abdulqayyum360-backend.hf.space/docs`
