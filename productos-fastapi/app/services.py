from typing import List, Optional
from .models import Producto
from .schemas import ProductoCrear

productos: List[Producto] = []
contador_id = 1

def listar_productos() -> List[Producto]:
    return productos

def obtener_producto(id: int) -> Optional[Producto]:
    return next((p for p in productos if p.id == id), None)

def crear_producto(datos: ProductoCrear) -> Producto:
    global contador_id
    nuevo = Producto(id=contador_id, nombre=datos.nombre, precio=datos.precio)
    productos.append(nuevo)
    contador_id += 1
    return nuevo

def actualizar_producto(id: int, datos: ProductoCrear) -> Optional[Producto]:
    for i, p in enumerate(productos):
        if p.id == id:
            productos[i] = Producto(id=id, nombre=datos.nombre, precio=datos.precio)
            return productos[i]
    return None

def eliminar_producto(id: int) -> bool:
    for i, p in enumerate(productos):
        if p.id == id:
            productos.pop(i)
            return True
    return False
