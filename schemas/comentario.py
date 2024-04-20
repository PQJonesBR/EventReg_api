from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produto_id: int = 1
    texto: str = "Só registrar a presença no evento se tiver se inscrito anteriormente!"
