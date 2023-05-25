from pydantic import BaseSettings


class Settings(BaseSettings):
    client_id: int = 72828
    client_secret: str = '4f0825d1530a7907f490bc6c45e982c7b11cea05'
