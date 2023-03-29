import psycopg2
import pandas as pd
import time

start_time = time.time()


def select(**kwargs):
    # need a connection with dbname=<username>_db
    cur = kwargs['cur']

    try:
        # SQL code
        cur.execute("""create temp table t1 as(
select cs.asin, cs.physical_id, cs.gl_product_group_desc
from catxin_idq_2."cs-data-v1" cs
where cs.marketplace_id = 44571
and cs.gl_product_group_desc in ('gl_apparel')
);

create temp table t2 as(
select t1.*, dama.product_type from t1
inner join catxin_idq_2.d_asins_marketplace_attributes dama
on t1.asin = dama.asin
);

select asin, max(physical_id) as physical_id from t2
where product_type in ('COMPUTER_VIDEO_GAME_CONTROLLER')
group by asin;
""")
    except Exception as err:
        print(err)

    colnames = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    print(colnames)
    df = pd.DataFrame(rows, columns=colnames)
    df.to_csv('/Users/bshrinid/Desktop/img_vec/cvgc_sql_output.csv', index=False)
    for row in rows:
        print(row)


print('start')
conn = psycopg2.connect(dbname='catxin_idq_2', host='catx3p.ciipw3zt1uq9.us-east-1.redshift.amazonaws.com',
                        port='8192', user='in3pcatxidq', password='Jade123$')
cursor = conn.cursor()
print('start select')
select(cur=cursor)
print('finish')
cursor.close()
conn.close()
end_time = time.time()
print("It took {} minutes to execute this.".format((end_time - start_time) / 60.))
