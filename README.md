# Django + htmx list view

This repo demonstrates how to use [htmx](https://htmx.org/) for a paginated, searchable list view in Django:

- [Before adding htmx](https://github.com/MattSegal/django-htmx-list-view/tree/before-htmx)
- [After adding htmx](https://github.com/MattSegal/django-htmx-list-view/tree/after-htmx)

This repo is a part of this [tutorial article](https://mattsegal.dev/django-htmx-list-view.html). View a quick video demo [here](https://www.loom.com/share/d087a55bd667449386edd54868369f7f)

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
