from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio: float

class ProductoCrear(ProductoBase):
    pass

class ProductoRespuesta(ProductoBase):
    id: int
