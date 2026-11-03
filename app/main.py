from pathlib import Path
import joblib, pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.schemas import CustomerInput
ROOT=Path(__file__).resolve().parent.parent
model=joblib.load(ROOT/'models'/'champion.joblib')
app=FastAPI(title='Telco Churn API',version='1.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/',response_class=HTMLResponse)
def home(): return (ROOT/'templates'/'index.html').read_text(encoding='utf8')
@app.post('/predict')
def predict(customer:CustomerInput):
    x=pd.DataFrame([customer.model_dump()]); pred=int(model.predict(x)[0]); p=float(model.predict_proba(x)[0,1])
    risk='Bajo' if p<.30 else 'Medio' if p<.70 else 'Alto'
    return {'prediction':pred,'churn_probability':p,'risk_level':risk}
