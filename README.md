# PharmaSupplyChain

An advanced Django-based project that aims to streamline the pharmaceutical supply chain across pharmacies and suppliers. It provides secure access for different user types such as pharmacists, suppliers, admins, and customers.

---

## 🚀 Features

- User authentication & authorization (pharmacist, supplier, admin, customer)
- Pharmacy & supplier onboarding and verification
- Medication management & categorization
- Inventory control per pharmacy
- Supplier offers and deals
- Order processing between pharmacies and suppliers
- Shipment tracking
- Area-based delivery with customizable shipping costs
- Notifications system
- Action logging with audit trails

---

## 📁 Project Structure

```plaintext
pharma_project/
├── accounts/            # Handles user management (Users model)
├── pharmacies/          # Handles pharmacy logic & models
├── suppliers/           # Supplier data and offers
├── medications/         # Medications & categories
├── inventory/           # Stock per pharmacy
├── orders/              # Order processing
├── shipments/           # Shipping logic
├── notifications/       # System notifications
├── auditlog/            # Tracks user actions
├── areas/               # Cities and shipping data
├── manage.py
└── pharma_project/      # Main settings and URL configuration

🔧 Getting Started (Local Setup)
1. Clone the project:
bash
Copy
Edit
git clone https://github.com/yourusername/pharma-supply-chain.git
cd pharma-supply-chain
2. Create virtual environment and activate it:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4. Configure .env (Optional but recommended):
Create a .env file and set:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3  # or your PostgreSQL connection
5. Apply Migrations:
bash
Copy
Edit
python manage.py migrate
6. Create Superuser:
bash
Copy
Edit
python manage.py createsuperuser
7. Run the Development Server:
bash
Copy
Edit
python manage.py runserver
🧠 How the App Will Be Built (Dev Plan)
User System:

Start with accounts app (custom User model if needed)

Handle registration, login, roles (user_type)

Pharmacy/Supplier Onboarding:

Create models for Pharmacy & Supplier linked to User

Add verification workflows

Area & Delivery Management:

Setup Areas model to handle delivery zones and shipping costs

Medication System:

Add categories and medication details

Inventory Management:

Inventory model per pharmacy for stock, expiry, discount

Supplier Offers:

Model offers from suppliers for medications

Order Workflow:

Pharmacies place orders to suppliers

Auto calculation of shipping, total, expected delivery

Shipments & Notifications:

Shipment tracking between areas

Notification triggers and logs

Audit Logging:

Record user actions across the system for admin visibility

🤝 Contribution Guidelines
Fork the repo

Create a new branch: feature/your-feature-name

Make your changes

Submit a pull request with clear description

📌 Tech Stack
Django 5+

PostgreSQL / SQLite

Python 3.10+

Bootstrap (for admin UI tweaks if needed)

Docker (planned for production)

REST API (planned via DRF)

📖 License
This project is under development and not licensed yet. Will be open-sourced once stable.

❤️ Author
Made with 💊 and 💻 by [Your Name] – Feel free to contribute or reach out!
