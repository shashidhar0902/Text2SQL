import pandas as pd
from sqlalchemy import create_engine
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
from openpyxl import load_workbook

def load_excel(file_path: str) -> pd.DataFrame:
    """
    Load data from an Excel file into a pandas DataFrame using pandas with openpyxl engine.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error loading Excel file with pandas and openpyxl engine: {e}")
        return None

def get_postgresql_engine():
    """
    Create and return a SQLAlchemy engine for PostgreSQL connection.
    """
    try:
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"Error creating PostgreSQL engine: {e}")
        return None

def load_postgresql_table(table_name: str) -> pd.DataFrame:
    """
    Load data from a PostgreSQL table into a pandas DataFrame.
    """
    engine = get_postgresql_engine()
    if engine is None:
        return None
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Error loading PostgreSQL table: {e}")
        return None
