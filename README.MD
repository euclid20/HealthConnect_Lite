# 🏥 HealthConnect Lite API
HealthConnect Lite is a beginner-friendly Flask API aligned with **SDG 3 (Good Health and Well-being)**. It allows users to register clinics and users, with input validation and secure password handling.
---

## 🌐 Base URL
http://localhost:5000
---

## 📌 Endpoints
### 🔹 `GET /clinics`
- Returns a list of all clinics
- **Response:**
```json
[
  {
    "contact": "0712345678",
    "id": 1,
    "location": "Nairobi",
    "name": "HealthCare Center"
  },
  {
    "contact": "0742757028",
    "id": 2,
    "location": "Nakuru",
    "name": "Nakuru Hospital"
  },
  {
    "contact": "0798765432",
    "id": 3,
    "location": "Kilimani",
    "name": "WellCare Clinic"
  }
]
```
---

### 🔹 `POST /clinics`
- Adds a new clinic
- **Required fields:** `name`, `location`, `contact`
- **Validation:**
  - All fields must be present
  - Contact must be a valid Kenyan mobile number (e.g., `0712345678`)
- **Sample request:**
```json
{
  "name": "WellCare Clinic",
  "location": "Kilimani",
  "contact": "0798765432"
}
```

---

### 🔹 `GET /users`
- Returns a list of all registered users (excluding passwords)
- **Response:**
```json
[
  {
    "id": 1,
    "name": "Euclid",
    "email": "euclid@example.com"
  }
]
```

---

### 🔹 `POST /users`
- Registers a new user
- **Required fields:** `name`, `email`, `password`
- **Validation:**
  - All fields must be present
  - Email must be valid (contain `@` and `.`)
  - Password must be at least 6 characters
  - Email must be unique
- **Security:**
  - Passwords are hashed using `werkzeug.security`
- **Sample request:**
```json
{
  "name": "Euclid",
  "email": "euclid@example.com",
  "password": "secure123"
}
```

---

## ⚠️ Error Handling

| Scenario                  | Status Code | Message                                      |
|---------------------------|-------------|----------------------------------------------|
| Missing fields            | `400`       | `"All fields are required"`                  |
| Invalid email format      | `400`       | `"Invalid email format"`                     |
| Short password            | `400`       | `"Password must be at least 6 characters"`   |
| Duplicate email           | `409`       | `"Email already exists"`                     |
| Invalid contact format    | `400`       | `"Invalid contact format"`                   |

---

## 🛠️ Technologies Used

- Flask
- SQLAlchemy
- MySQL (via XAMPP)
- Werkzeug (for password hashing)
- dotenv (for config management)
- curl/Postman (for API testing)

---

## 🚀 How to Run

1. Clone the repository
2. Set up your `.env` file with:
   ```
   CONFIG_MODE=development
   BASE_URL=http://localhost
   ```
3. Start MySQL via XAMPP
4. Run the app:
   ```bash
   python run.py
   ```

---

## 📈 Future Enhancements

- `/login` route with password verification
- Token-based authentication (JWT)
- Health tracking or tips endpoint for SDG 3
- Swagger/OpenAPI documentation

---

## 👨‍💻 Author
Euclid Mwendwa
Python & Flask Developer  
Nairobi, Kenya