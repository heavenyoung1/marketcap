from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN_COINGECKO: str
    
    TOKEN_TELEGRAM: str

    DRIVER: str = 'sqlite+aiosqlite://'
    SYNC_DRIVER: str = 'sqlite://'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()