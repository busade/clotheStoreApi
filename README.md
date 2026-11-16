# ThreadCraft API

A FastAPI clothing-store capstone starter with a Router → Controller/Service → Model layout. Routes and Pydantic schemas are wired; selected controller and authorization functions intentionally return HTTP 501 for students to implement. Health, SQLite setup, seed data, public product reads, and cart viewing are the working references.

## Setup

```bash
python -m venv .venv
source .venv/scripts/activate
pip install -r requirements.txt
copy .env.example .env  
python -m app.db.seed
uvicorn app.main:app --reload
```

Browse `/docs` for the API schema and `/health` for the health check. Seeded users: `admin@threadcraft.test` / `AdminPass123!` and `customer@threadcraft.test` / `Customer123!`.

## Tests

Run `pytest`. The tests describe intended success and error behavior. Unfinished student endpoints initially return 501, so those tests are expected to fail until their implementation is complete. Test fixtures use isolated in-memory SQLite and test identities.

## Capstone Milestone Checklist

- [ ] `auth_controller.py` — registration, login, and profile; unlocks `tests/test_auth.py`.
- [ ] `api/deps.py` — JWT user lookup and admin RBAC; unlocks authenticated routes across the suite.
- [ ] `product_controller.py` — filtering and admin CRUD; unlocks `tests/test_products.py`.
- [ ] `cart_controller.py` — add/update/remove/clear and stock checks; unlocks `tests/test_cart.py`.
- [ ] `order_controller.py` — checkout, ownership, status transitions, and cancellation restock; unlocks `tests/test_orders.py`.

The starter includes SQLAlchemy 2 models, Pydantic v2 schemas, SQLite session management, CORS/lifespan initialization, and sample catalog plus admin/customer seed records.
