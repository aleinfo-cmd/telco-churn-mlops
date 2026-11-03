# Práctica 8 — CI/CD con GitHub Actions

Proyecto didáctico ejecutable en Windows, VS Code, Python 3.11 y Docker. El clasificador se entrenó con datos sintéticos; no es apto para decisiones reales.

## Ejecutar en CMD

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m pytest -v
python -m uvicorn app.main:app --reload
```

Abrir http://127.0.0.1:8000/, /docs y /health.

## Docker

```bat
docker build -t telco-api:v1 .
docker run --rm -p 8000:8000 telco-api:v1
```

## GitHub

Crear repositorio vacío en GitHub y reemplazar TU_USUARIO:

```bat
git init -b main
git add .
git commit -m "Proyecto inicial CI CD"
git remote add origin https://github.com/TU_USUARIO/telco-churn-cicd.git
git push -u origin main
```

Actions ejecuta pruebas en push y pull request. La imagen GHCR se publica solo en push a main y si las pruebas pasan. El nombre de la imagen se normaliza a minúsculas.

## Provocar fallo

En tests/test_health.py cambia temporalmente el esperado HTTP 200 por 404. Haz commit y push: el job test debe fallar y Docker no debe publicarse. Restaura 200, commit y push.

## Descargar imagen

`ghcr.io/tu_usuario/telco-churn-cicd:latest` (usar propietario en minúsculas). Si el paquete es privado, autenticar Docker antes de hacer pull.

```bat
docker pull ghcr.io/tu_usuario/telco-churn-cicd:latest
docker run --rm -p 8000:8000 ghcr.io/tu_usuario/telco-churn-cicd:latest
```

El pipeline realiza CI y publicación como entrega continua; no despliega automáticamente a producción. Para uso real se requiere dataset real, evaluación, seguridad, monitoreo y validación del modelo.

Este proyecto utiliza Regresión Logística, Random Forest y SVM.

Modelo SVM: lalala