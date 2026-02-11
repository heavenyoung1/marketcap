from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ALPHA_VANTAGE_TOKEN: str
    
    TELEGRAM_TOKEN: str

    DRIVER: str = 'sqlite+aiosqlite://'
    SYNC_DRIVER: str = 'sqlite://'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()