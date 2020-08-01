import pandas as pd
import sqlite3
from collections import Counter
import json

conn = sqlite3.connect('../data/data.db')
df = pd.read_sql_query('SELECT * from featuring_all', conn)
df['counts'] = df['text_for_embedding'].apply(lambda x: json.dumps(dict(Counter(x.split()))))


df.to_sql('featuring_all', conn, if_exists='replace', index=False)
conn.close()