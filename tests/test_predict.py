from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
S={'tenure':5,'MonthlyCharges':85.5,'TotalCharges':427.5,'Contract':'Month-to-month','InternetService':'Fiber optic'}
def test_predict():
 r=client.post('/predict',json=S); assert r.status_code==200; d=r.json(); assert d['prediction'] in (0,1); assert 0<=d['churn_probability']<=1; assert d['risk_level'] in ('Bajo','Medio','Alto')
def test_invalid():
 assert client.post('/predict',json={**S,'tenure':-1}).status_code==422
