from pydantic import BaseModel
from datetime import datetime

class DocumentoCreate(BaseModel):
    titulo: str
    materia: str | None = None
    semestre: str | None = None
    descripcion: str | None = None

class Documento(BaseModel):
    id: int
    titulo: str
    materia: str | None = None
    semestre: str | None = None
    descripcion: str | None = None
    fecha_subida: datetime
    usuario_id: str
