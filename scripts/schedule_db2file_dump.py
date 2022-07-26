from src import config
from src.db.db.session import engine
from sqlalchemy import inspect
import pandas as pd
import schedule
from time import sleep

FILE_DUMPS_DIR = config["FILE_DUMPS_DIR"]


def db2file_dump():
    table_names = inspect(engine).get_table_names()
    for table_name in table_names:
        df = pd.read_sql_table(table_name, con=engine)

        df.to_parquet(FILE_DUMPS_DIR / f"parquet/{table_name}.parquet")
        df.to_csv(FILE_DUMPS_DIR / f"csv/{table_name}.csv")


schedule.every().day.at("03:00").do(db2file_dump)
while True:
    schedule.run_pending()
    sleep(60 * 30)  # check once every 30 minute
