
# Inventory Management System

A professional Flask-based Inventory Management System to manage products, storage locations, and product movements with real-time inventory reporting.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage Workflow](#usage-workflow)
- [Technologies Used](#technologies-used)
- [Customization & Extensibility](#customization--extensibility)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This inventory management application allows users to manage products, warehouses (locations), product transfers between locations, and view up-to-date inventory balances. Built with Flask, SQLAlchemy, and WTForms, it features a user-friendly web interface with CRUD operations and inventory reporting.

---

## Features

- **Product Management**: Create, read, update, and delete products with quantity tracking  
- **Location Management**: Manage warehouse locations  
- **Product Movements**: Record transfers of products between locations with timestamps  
- **Inventory Reporting**: Calculate and display final product stock per location, considering initial stock and movements  
- **Form validation** and user-friendly UI with confirmation for destructive actions  
- **Responsive design** with modern CSS styling and JavaScript enhancements

---

## Project Structure

```
inventory_app/
│
├── run.py                      # Application entry point
├── requirements.txt            # Python package dependencies
│
├── app/                       # Main Flask application package
│   ├── __init__.py             # Flask app initialization and DB setup
│   ├── models.py               # Database models for products, locations, movements
│   ├── routes.py               # Route handlers for all CRUD and reporting
│   ├── forms.py                # Flask-WTF form definitions (optional)
│
├── templates/                 # HTML templates for pages
│   ├── base.html               # Base layout template
│   ├── products.html           # View products listing
│   ├── add_product.html        # Add new product form
│   ├── edit_product.html       # Edit product form
│   ├── locations.html          # View locations listing
│   ├── add_location.html       # Add new location form
│   ├── edit_location.html      # Edit location form
│   ├── movements.html          # View product movement history
│   ├── add_movement.html       # Add new movement form
│   ├── report.html             # Inventory balance report
│
├── static/                    # Static assets (CSS, JS)
│   ├── css/
│   │   └── style.css           # Main styling
│   └── js/
│       └── scripts.js          # JavaScript functions (form confirmation, etc.)
```

---

## Setup & Installation

### Prerequisites

- Python 3.8+
- Git (optional, for cloning repo)

### Steps

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/inventory-management.git
   cd inventory-management
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python run.py
   ```

5. Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Usage Workflow

1. **Manage Products:**  
   Add new products with a unique ID, name, and quantity. Update or delete existing products.

2. **Manage Locations:**  
   Define warehouse/storage locations with unique IDs and names. Edit or delete locations as needed.

3. **Record Movements:**  
   Add product movements by specifying product, quantity, source location (optional if incoming), and destination location (optional if outgoing).

4. **View Inventory Report:**  
   Automatically calculate real-time stock balances per product and location, considering initial stock and all movements.

5. **Edit & Delete Operations:**  
   Easily update or remove products, locations, and movement records. Confirmation dialogs prevent accidental deletions.

---

## Technologies Used

- **Flask** – Micro web framework  
- **Flask-SQLAlchemy** – ORM for database operations  
- **Flask-WTF & WTForms** – Forms and validation  
- **SQLite** – Lightweight database for storage  
- **HTML/CSS/JavaScript** – Frontend interface  
- **Jinja2** – Templating engine  

---

## Customization & Extensibility

- Modify `app/__init__.py` to change configuration, database URI, or add middleware  
- Extend models or add new features like user authentication, role permissions  
- Replace SQLite with more robust DB (PostgreSQL, MySQL) by changing configurations  
- Enhance UI styling in `static/css/style.css` or add frontend frameworks  
- Integrate API endpoints for headless operations or external integrations

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for full details.

---

## Contact

Created and maintained by [Your Name] - [your.email@example.com]  
Feel free to open issues or pull requests to contribute.

---


## Screenshots 


## Product
![product] (images/Product.png)


## Location
![Location] (images/Location.png)


## Product Movement
![Product_Movement] (images/Product Movement.png)


## Final Balance Report 
![Final_Balance_Report] (images/Final Balance Report.png)


## Add New Product
![Add_New_Product] (images/Add New Product.png)


## Deleting item
![Deleting_item] (images/Deleting item.png)


Thank you for using this project! 🚀
```
