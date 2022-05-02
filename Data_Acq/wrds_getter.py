import wrds
import pandas as pd

#  Setup a .pgpass file for convience i.e. see https://matteocourthoud.github.io/post/wrds/
USER = 'jasondanielchoi'


def connect():
    return wrds.Connection(wrds_username=USER)


def list_libraries(conn):
    conn.list_libraries().sort()
    print(conn.list_libraries())




def list_tables(conn, library):
    """
    List all datasets within a given library
    :param conn:
    :param library:
    :return:
    """
    print(conn.list_tables(library=library))


def extract_obs(conn, table, library='comp', n_obs=5):
    """
    # Extract first n_obs observations from comp.company
    :param conn:
    :param table:
    :param library:
    :param n_obs:
    :return:
    """
    company = conn.get_table(library=library, table=table, obs=n_obs)
    company.shape

# Narrow down the specific columns to extract
# company_narrow = conn.get_table(library='comp', table='company',
#                                 columns = ['conm', 'gvkey', 'cik'], obs=5)
# company_narrow.shape
# company_narrow

def main():
    conn = connect()
    libs = list_libraries(conn)
    tables = list_tables(conn, library='comp')
    df = pd.DataFrame({'libraries': libs, 'tables': tables}, index=[0])
    df.to_excel('WRDS.xlsx')
    conn.close()


if __name__ == '__main__':
    main()