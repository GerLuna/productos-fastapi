from fastapi import APIRouter, HTTPException
from typing import List
from . import schemas, services

router = APIRouter()

@router.get("/productos", response_model=List[schemas.ProductoRespuesta])
def get_productos():
    return services.listar_productos()

@router.get("/productos/{id}", response_model=schemas.ProductoRespuesta)
def get_producto(id: int):
    producto = services.obtener_producto(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos", response_model=schemas.ProductoRespuesta, status_code=201)
def crear_producto(producto: schemas.ProductoCrear):
    return services.crear_producto(producto)

@router.put("/productos/{id}", response_model=schemas.ProductoRespuesta)
def actualizar_producto(id: int, producto: schemas.ProductoCrear):
    actualizado = services.actualizar_producto(id, producto)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

@router.delete("/productos/{id}", status_code=204)
def eliminar_producto(id: int):
    if not services.eliminar_producto(id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
