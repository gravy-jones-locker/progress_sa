from progress_sa import base, pyodbc

# default dialect
base.dialect = pyodbc.dialect

from progress_sa.base import dialect

__all__ = ['dialect']
