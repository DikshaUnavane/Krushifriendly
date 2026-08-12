# 🌾 KrushiFriendly – Agricultural Equipment Rental & Marketplace

> **A digital platform that connects farmers with agricultural equipment providers, making farm machinery affordable, accessible, and easy to rent.**

## 📌 Overview

**KrushiFriendly** is a web-based agricultural equipment rental and marketplace platform developed to help farmers access farming machinery and equipment without the need to purchase expensive equipment.

The platform connects **farmers and equipment owners**, allowing users to browse available agricultural equipment, check availability, select rental dates, make bookings, and manage their rental activities through a centralized system.

The platform is designed with a focus on **accessibility, affordability, multilingual support, and simplified equipment rental management**.

---

## 🎯 Problem Statement

Many small and marginal farmers cannot afford to purchase expensive agricultural machinery such as tractors, harvesters, cultivators, and other farm equipment.

At the same time, agricultural equipment owned by individuals, organizations, or businesses may remain unused for significant periods.

KrushiFriendly aims to solve this problem by providing a digital marketplace where:

* 👨‍🌾 Farmers can find required equipment.
* 🚜 Equipment owners can list their machinery for rental.
* 📅 Farmers can check equipment availability and book it.
* 💳 Users can make online payments.
* 🌐 Users can access the platform in multiple languages.

---

## ✨ Key Features

### 👨‍🌾 Farmer Module

Farmers can:

* Create an account and log in.
* Browse available agricultural equipment.
* Search and filter equipment.
* View equipment details.
* Check rental availability.
* Select rental dates.
* Book equipment.
* View booking information.
* Make online payments.
* Manage their rental activities.

---

### 🚜 Equipment Owner Module

Equipment owners can:

* Register and log in.
* Add agricultural equipment.
* Provide equipment details and rental prices.
* Upload equipment images.
* Manage listed equipment.
* Update equipment availability.
* View rental bookings.
* Manage their equipment inventory.

---

### 📅 Booking & Availability

The platform provides a booking workflow that helps prevent scheduling conflicts.

Users can:

```text
Select Equipment
       ↓
Check Availability
       ↓
Select Rental Dates
       ↓
Confirm Booking
       ↓
Make Payment
       ↓
Booking Confirmed
```

---

### 💳 Payment Integration

KrushiFriendly supports online payment functionality using:

* **Razorpay**
* **UPI QR-based payment**

This provides users with a convenient way to complete equipment rental transactions.

---

### 🌐 Multilingual Support

The platform is designed to support multiple languages:

* 🇬🇧 English
* 🇮🇳 Hindi
* 🇮🇳 Marathi

This feature is particularly useful for improving accessibility for farmers who may prefer regional languages.

---

### 🔍 Equipment Search

Users can browse and find equipment based on relevant information such as:

* Equipment name
* Equipment category
* Rental price
* Location
* Availability

---

## 🛠️ Technologies Used

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| **Python**       | Backend programming                 |
| **Django**       | Web framework and backend           |
| **HTML5**        | Frontend structure                  |
| **CSS3**         | Styling and responsive design       |
| **JavaScript**   | Client-side interactions            |
| **Bootstrap**    | UI components and responsive design |
| **jQuery**       | Frontend interactions               |
| **SQLite**       | Development database                |
| **MySQL**        | Database option                     |
| **Razorpay**     | Online payment integration          |
| **UPI QR**       | Digital payment                     |
| **Git & GitHub** | Version control                     |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    │  Farmer / Owner     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Frontend        │
                    │ HTML / CSS / JS     │
                    │ Bootstrap / jQuery  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Django        │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       User Management    Equipment          Booking
                          Management         Management
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Database       │
                    │ SQLite / MySQL      │
                    └─────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Payment Gateway     │
                    │ Razorpay / UPI      │
                    └─────────────────────┘
```

---

## 📂 Project Structure

```text
KrushiFriendly/
│
├── manage.py
│
├── requirements.txt
│
├── db.sqlite3
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── equipment.html
│   ├── booking.html
│   └── payment.html
│
├── static/
│   ├── css/
│   ├── js/
   └── images/
│
├── media/
│   └── equipment/
│
└── README.md
```

> The exact structure may vary depending on the Django apps and modules in the current repository.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/gayatri320/Krushifriendly.git
```

Move into the project directory:

```bash
cd Krushifriendly
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django
```

Install other dependencies required by the project as specified in the project configuration.

---

## 4. Configure Environment Variables

For security, sensitive credentials such as payment gateway keys and Django secret keys should be stored in environment variables rather than directly in the source code.

Example:

```text
SECRET_KEY=your_secret_key
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
```

**Do not upload API keys, passwords, or secret credentials to GitHub.**

---

## 5. Apply Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 🔄 Application Workflow

```text
                    User Registration
                           │
                           ▼
                         Login
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
          Farmer                   Equipment Owner
             │                           │
             ▼                           ▼
     Browse Equipment             Add Equipment
             │                           │
             ▼                           ▼
    Select Equipment             Manage Equipment
             │
             ▼
     Check Availability
             │
             ▼
       Select Dates
             │
             ▼
        Book Equipment
             │
             ▼
       Online Payment
             │
             ▼
     Booking Confirmation
```

---

# 🗄️ Main Database Entities

The application can be logically divided into the following entities:

### User

Stores user information such as:

* User ID
* Name
* Email
* Password
* Contact information
* User role

### Equipment

Stores agricultural equipment information:

* Equipment ID
* Equipment name
* Category
* Description
* Rental price
* Location
* Owner
* Availability
* Image

### Booking

Stores rental information:

* Booking ID
* Farmer
* Equipment
* Start date
* End date
* Booking status
* Total amount

### Payment

Stores transaction information:

* Payment ID
* Booking
* Amount
* Payment status
* Transaction/reference ID

---

# 🔐 Security Considerations

The application follows common web-application security practices such as:

* User authentication
* Django's password hashing
* CSRF protection
* Role-based access
* Server-side validation
* Secure handling of payment credentials

For production deployment, additional measures should be implemented, including:

* HTTPS
* Secure cookies
* Environment-based secret management
* Database security
* Input sanitization
* Proper payment verification

---

# 📱 User Interface

The application is designed to provide a simple interface for users with limited technical experience.

The interface focuses on:

* Simple navigation
* Clear service categories
* Equipment cards
* Booking forms
* Easy payment flow
* Multilingual accessibility
* Responsive design

---

# 🌱 Social Impact

KrushiFriendly aims to contribute to agricultural digitization by helping farmers access machinery without requiring large upfront investments.

### Benefits for Farmers

* 💰 Lower machinery costs
* 🚜 Easy access to agricultural equipment
* ⏱️ Saves time searching for equipment
* 📅 Convenient booking
* 💳 Digital payment
* 🌐 Regional language support

### Benefits for Equipment Owners

* 📈 Better utilization of machinery
* 💵 Additional rental income
* 📋 Easier booking management
* 🌾 Direct connection with farmers

---

# 🔮 Future Enhancements

The project can be extended with:

### 🤖 AI-Based Recommendations

Recommend suitable equipment based on:

* Crop type
* Farm size
* Soil conditions
* Season
* Previous rental history

### 📍 Location-Based Search

Use GPS/location services to find equipment available near the farmer.

### 🗺️ Map Integration

Display equipment providers and rental locations on an interactive map.

### 🔔 Notifications

Send:

* Booking confirmations
* Payment confirmations
* Rental reminders
* Cancellation notifications

through SMS, email, or push notifications.

### 📊 Analytics Dashboard

Provide analytics for:

* Most rented equipment
* Revenue
* Booking trends
* Equipment utilization
* Farmer demand

### ☁️ Cloud Deployment

Deploy the application using cloud platforms and use a production-grade database such as PostgreSQL.

---

# 🧪 Testing

The application can be tested using different scenarios:

* User registration
* User login/logout
* Equipment listing
* Equipment search
* Equipment availability
* Booking creation
* Booking cancellation
* Payment processing
* Invalid input handling
* Unauthorized access
* Multilingual functionality

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Django web application development
* Python backend development
* Database design and CRUD operations
* User authentication
* Role-based application design
* REST/API integration
* Payment gateway integration
* Multilingual web applications
* Frontend development
* Git and GitHub
* Debugging and deployment concepts

---

# 👩‍💻 Author

## Gayatri Dhangar

**B.Tech – Artificial Intelligence & Data Science**

K. K. Wagh Institute of Engineering Education and Research, Nashik

GitHub:
https://github.com/gayatri320

---

# ⭐ Project Highlights

| Feature                   | Status |
| ------------------------- | ------ |
| Farmer Registration/Login | ✅      |
| Equipment Listing         | ✅      |
| Equipment Search          | ✅      |
| Equipment Rental          | ✅      |
| Booking Management        | ✅      |
| Availability Management   | ✅      |
| Multilingual Support      | ✅      |
| Razorpay Integration      | ✅      |
| UPI Payment               | ✅      |
| Django Backend            | ✅      |
| Database Integration      | ✅      |
| Responsive UI             | ✅      |

---

## 📌 Project Summary

**KrushiFriendly is a Django-based agricultural equipment rental and marketplace platform that connects farmers with equipment owners. It provides equipment discovery, availability checking, booking, multilingual support, and digital payment functionality, with the goal of making agricultural machinery more accessible and affordable for farmers.**

---

## ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

**Made with 🌱 for smarter and more accessible agriculture.**
