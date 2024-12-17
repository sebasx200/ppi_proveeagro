# ProveeAgro Backend Setup Guide

## Prerequisites

1. **Python**: Make sure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. **PostgreSQL**: Ensure PostgreSQL is installed. You can find installation guides for different operating systems on the [PostgreSQL website](https://www.postgresql.org/download/).

## Steps to Setup

1. **Clone the repository** and navigate to the project directory.

2. **Create a virtual environment**:

   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment**:

   - On Mac/Linux:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```

4. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

5. **Create the PostgreSQL database**.

6. **Clone the `.env.template` file, rename it to `.env`, and fill in the necessary information**, ensuring the database settings matches the one you created.

7. **Apply database migrations**:

   ```sh
   python manage.py migrate
   ```

8. **Create a superuser** and then create a department and a city in `localhost:8000/admin`:

   ```sh
   python manage.py createsuperuser
   ```

9. **Execute the script to load initial data**:
   ```sh
   python proveeagro/scripts/load_data.py
   ```

## Note

The `requirements.txt` file includes `pandas`, `numpy`, `python-dateutil`, `pytz`, `openpyxl`, and `et-xmlfile`, which are necessary to run the `load_data.py` script. If you do not need to run this script, you can skip installing these dependencies by running:

```sh
pip install -r requirements.txt --no-deps pandas numpy python-dateutil pytz openpyxl et-xmlfile
```
