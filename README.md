# App Template

A template for small Django tutorial apps

## Setup

Follow these instructions to try this demo out locally.
This requires Python 3 and the pip package manager.

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment (Bash for Linux or Mac)
. env/bin/activate

# Activate virtual environment (cmd / PowerShell for Windows)
./env/Scripts/activate

# Install requirements
pip install -r requirements.txt

# Go into the Django application folder
cd app

# Setup database.
./manage.py migrate

# Setup test data.
./manage.py setup_test_data

# Run the development server.
./manage.py runserver

# Now you can view the project at http://localhost:8000
```
