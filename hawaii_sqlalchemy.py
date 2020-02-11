import os 
from pprint import pprint
from sqlalchemy import create_engine ,inspect 


db_path = os.path.join("Resources", "hawaii.sqlite")

engine = create_engine(f"sqlite:///{db_path}")
inspector = inspect(engine)

print(inspector.get_table_names())
pprint(inspector.get_columns("measurement"))

cmd = "select * from measurement"
pprint(engine.execute(cmd).fetchall())