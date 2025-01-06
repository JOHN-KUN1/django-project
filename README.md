
# Setup Instructions

A guide on how to setup and run this project on your local machine


## Setup and Deployment

Clone the Repository

```bash
  git clone <repository_url>
  cd myProject
```

Activate the Virtual Environment

```bash
  .venv/Scripts/activate
```

Install the Dependencies

```bash
  pip install -r requirements.txt
```

Run Migrations

```bash
  python manage.py migrate
```

Create a Superuser

```bash
  python manage.py createsuperuser
```

Run the Development Server

```bash
  python manage.py runserver
```

Access the Application

```bash
  http://127.0.0.1:8000/
```

## How to Run Test

```bash
  python manage.py test
```

