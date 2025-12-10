from pydantic import BaseModel

class ChunkCreate(BaseModel):
    documento_id: int
    texto: str
    pagina: int | None = None
    orden: int
    
class Chunk(BaseModel):
    id: int
    documento_id: int
    texto: str
    pagina: int | None = None
    orden: int
