
# 💊 PharmaSupplyChain

A Django-based system that streamlines pharmaceutical supply chain operations between pharmacies and suppliers. It provides secure access for pharmacists, suppliers, admins, and customers.

---

## 🚀 Features

- User authentication and role-based authorization  
- Pharmacy and supplier onboarding with verification  
- Medication and category management  
- Per-pharmacy inventory control  
- Supplier offers and discounts  
- Order management between pharmacies and suppliers  
- Shipment tracking with delivery zones  
- Customizable shipping costs by area  
- System notifications  
- Audit logging for system transparency

---

## 📁 Project Structure

```plaintext
pharma_project/
├── accounts/           # User management (custom User model)
├── pharmacies/         # Pharmacy logic and models
├── suppliers/          # Supplier data and offer management
├── medications/        # Medication categories and details
├── inventory/          # Per-pharmacy stock management
├── orders/             # Order lifecycle
├── shipments/          # Shipment tracking and delivery
├── notifications/      # Notification triggers
├── auditlog/           # Action logging
├── areas/              # City and shipping zone management
├── manage.py
└── pharma_project/     # Project settings and URL configuration
```

---

## 🔧 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/DevOps-With-Hammad/Pharma.git
cd Pharma
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add the following:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3  # or your PostgreSQL connection string
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## 🧠 Development Plan

### User System
- Start with a custom User model in the `accounts` app  
- Implement login, registration, and user roles

### Pharmacy & Supplier Onboarding
- Create linked models for pharmacies and suppliers  
- Add verification workflows

### Area & Delivery Management
- Implement delivery zones and shipping cost logic

### Medication & Inventory
- Categorize medications  
- Track stock, expiry dates, and discounts per pharmacy

### Supplier Offers
- Enable suppliers to post deals for medications

### Order Workflow
- Pharmacies order from suppliers  
- Auto-calculate shipping and total costs

### Shipments & Notifications
- Handle tracking by area  
- Trigger system notifications

### Audit Logging
- Record user actions across the system for admin visibility

---

## 🤝 Contribution Guidelines

1. Fork the repository  
2. Create a feature branch: `feature/your-feature-name`  
3. Commit your changes  
4. Submit a pull request with a clear description

---

## 🛠 Tech Stack

- Django 5+  
- Python 3.10+  
- PostgreSQL / SQLite  
- Bootstrap (for admin UI tweaks)  
- Docker (planned)  
- Django REST Framework (planned)

---

## 📖 License

This project is under active development and will be open-sourced once stabilized.

---

## ❤️ Author

Made with 💊 and 💻 by **Hammad**  
Feel free to contribute or reach out!
