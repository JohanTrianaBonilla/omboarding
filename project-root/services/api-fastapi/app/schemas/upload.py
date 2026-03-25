from pydantic import BaseModel


class RunEtlRequest(BaseModel):
    file_path: str
