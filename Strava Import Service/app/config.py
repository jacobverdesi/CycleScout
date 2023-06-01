from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Strava Import Service"
    debug: bool = True
    host: str = 'localhost'
    port: int = 8080
    client_id: int = 72828
    client_secret: str = '4f0825d1530a7907f490bc6c45e982c7b11cea05'

settings = Settings()