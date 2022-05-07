import wrds
import pandas as pd

#  Setup a .pgpass file for convience i.e. see https://matteocourthoud.github.io/post/wrds/
USER = 'jasondanielchoi'


def connect():
    return wrds.Connection(wrds_username=USER)


def list_libraries(conn):
    return conn.list_libraries()
    #return conn.list_libraries().sort()



def list_tables(conn, library):
    """
    List all datasets within a given library
    :param conn:
    :param library:
    :return:
    """
    return conn.list_tables(library=library)
    #print(conn.list_tables(library=library))


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
def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list

def main():
    conn = connect()
    # libs = list_libraries(conn)
    # print(f'libraries are {libs} with type {type(libs)}')
    # tables = list_tables(conn, library='comp')
    # df = pd.DataFrame(pad_dict_list({'libraries': libs, 'compustat_tables': tables}, None))
    # df.to_excel('WRDS_libraries.xlsx')
    data = conn.raw_sql(
        """SELECT 
        gvkey,
        conm,
        tic,
        cusip,
        exchg,
        fyear,
        sich,
        act,
        ap,
        at,
        ceq,
        che,
        cogs,
        csho,
        dlc,
        dltis,
        dltt,
        dp,	
        ib,	
        invt,
        ivao,
        ivst,
        lct,
        lt,
        ni,
        ppegt,
        pstk,
        re,
        rect,
        sale,
        sstk,
        txp,
        txt,
        xint,
        EBIT
        FROM comp.funda WHERE fyear >= 1990 AND fyear <= 2022 AND exchg BETWEEN 11 AND 20
        AND
        act IS NOT NULL AND
        ap IS NOT NULL AND
        at IS NOT NULL AND
        ceq IS NOT NULL AND
        che IS NOT NULL AND
        cogs IS NOT NULL AND
        csho IS NOT NULL AND
        dlc IS NOT NULL AND
        dltis IS NOT NULL AND
        dltt IS NOT NULL AND
        dp IS NOT NULL AND	
        ib IS NOT NULL AND	
        invt IS NOT NULL AND
        ivao IS NOT NULL AND
        ivst IS NOT NULL AND
        lct IS NOT NULL AND
        lt IS NOT NULL AND
        ni IS NOT NULL AND
        ppegt IS NOT NULL AND
        pstk IS NOT NULL AND
        re IS NOT NULL AND
        rect IS NOT NULL AND
        sale IS NOT NULL AND
        sstk IS NOT NULL AND
        txp IS NOT NULL AND
        txt IS NOT NULL AND
        xint IS NOT NULL AND
        EBIT IS NOT NULL
    """)
    df_data = pd.DataFrame(data)
    print(f'Shape is {df_data.shape}')
    df_data.to_csv('1990_2021_sample.csv')
    print('Job done m\'lord')

    # df = pd.DataFrame({'tables': tables})
    # df.to_excel('COMP_tables.xlsx')
    conn.close()


if __name__ == '__main__':
    main()
