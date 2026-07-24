from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class Variante(BaseModel):
    tamaño: str
    precio: float
    disponible: bool = True

class Categoria(BaseModel):
    nombre: str
    image: Optional[str] = None
    disponible: bool = True
    color: Optional[str] = None

class EstadoCliente(str, Enum):
    pendiente = "Pendiente"
    enviando = "Enviando"
    entregado = "Entregado"
    cancelado = "Cancelado"

class Item_pedido(BaseModel):
    idUnico: str
    producto_id: str
    nombre: str
    tamano: str
    precio: float
    cantidad: int 
      
class Producto(BaseModel):
    nombre: str
    descripcion: Optional(str) = None
    categoria_id: str
    variantes: list[Variante] = []
    disponible: bool = True
    imagen: Optional[str] = None
    destacado: bool = False

class Usuario(BaseModel):
    id: str
    nombre: str
    correo: str
    contraseña: str
