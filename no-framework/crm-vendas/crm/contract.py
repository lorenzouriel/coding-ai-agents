from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator, ValidationError
from datetime import datetime, time
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "WhatsApp com Gemini"
    produto2 = "WhatsApp com chatGPT"
    produto3 = "WhatsApp com Llama3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @field_validator('data')
    def validar_intervalo_data(cls, v):
        # Define o intervalo de datas permitido
        inicio_intervalo = datetime(2024, 1, 1)  # 01/09/2024
        fim_intervalo = datetime(2024, 12, 31, 23, 59, 59)  # 12/09/2024 até 23:59:59

        # Verifica se a data está dentro do intervalo permitido
        if not (inicio_intervalo <= v <= fim_intervalo):
            raise ValueError("A data da venda deve estar entre 01/01/2024 e 31/12/2024.")
        return v

    @field_validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v