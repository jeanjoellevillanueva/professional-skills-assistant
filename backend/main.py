from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read():
    return {'message': 'Hi Thaddy'}
