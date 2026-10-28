from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    jwt_issuer: str = "psys-auth-service"
    jwt_access_token_minutes: int = 15
    private_key_path:str = "keys/private.pem"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()