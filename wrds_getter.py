import wrds
import pandas as pd

#%
 #  2. Establish connection with WRDS server
def connect():
    return wrds.Connection()
 #  3. List all libraries
def list_libraries(conn):
    conn.list_libraries().sort()
    type(conn.list_libraries())

#4. List all datasets within a given library
def list_tables(conn, library):
    conn.list_tables(library='comp')

# Extract first 5 obs from comp.company
def extract_obs(conn, table, library='comp', n_obs=5):
    company = conn.get_table(library=library, table=table, obs=n_obs)
    company.shape

# Narrow down the specific columns to extract
company_narrow = conn.get_table(library='comp', table='company',
                                columns = ['conm', 'gvkey', 'cik'], obs=5)
company_narrow.shape
company_narrow