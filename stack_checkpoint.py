import httpx,subprocess,time
base='http://localhost:8103'
def ready():
 for _ in range(100):
  try:
   if httpx.get(base+'/health').status_code==200:return
  except httpx.HTTPError:pass
  time.sleep(.2)
 raise RuntimeError('stack did not start')
ready()
t=httpx.post(base+'/tasks',json={'title':'compose persistence checkpoint'});assert t.status_code==201
i=t.json()['id']
subprocess.run(['docker','compose','down'],check=True,capture_output=True)
subprocess.run(['docker','compose','up','-d','--wait'],check=True,capture_output=True)
ready()
r=httpx.get(base+'/tasks/'+str(i));assert r.status_code==200 and r.json()['title']=='compose persistence checkpoint'
print('PASS docker compose down/up volume persistence, API 201 and 200')
