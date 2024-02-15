from fastapi import FastAPI

app = FastAPI()

@app.get('/raiz')
async def raiz():
    return {"msg": "FastAPI na Geek University"}

if __name__ == '__main__': #esse if facilita a parte de rodar o código onde é necessário apenas colocar: python main.py ao invés de ficar escrevendo uvicorn...
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)