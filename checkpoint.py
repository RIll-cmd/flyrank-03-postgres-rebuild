from dotenv import load_dotenv
load_dotenv()
from repository import Repository
r=Repository();r.initialize();r.initialize()
with r.connect() as d: assert d.execute('SELECT COUNT(*) AS n FROM tasks').fetchone()['n']==3
print('PASS env connection, automatic table and exactly three seeds after restart')
