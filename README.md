# ADTWINS-test
## Requerimiento previo a descargar el proyecto
- Tener instalado Python(version 3.10.4 utilizada en este proyecto)
- Tener instalado MongoDB(Utilizando por defecto puerto el localhost:)

## Instrucciones para ejecutar el proyecto:
- Posicionarse en la raiz del proyecto
- Instalar el entorno virtual
`python -m venv env`
- Una vez instalado, activarlo
`.\env\Scripts\activate`
- Instalar los paquetes requeridos
`pip install -r requirements.txt`
- Ejecutar uvicorn para iniciar el servidor(Puerto 8000 por defecto)
`uvicorn main:app --reload`
- Para lograr acceder a la documentacion y rutas
`http://127.0.0.1:8000/docs`
