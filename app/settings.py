from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    ENV: str = "dev"
    SENTRY_DSN: str = None
    API_KEY: str = "you-will-want-something-safe-here"
    DEFAULT_EMAIL_ADDRESS: EmailStr = "default@email.com"
    SENDGRID_API_KEY: str = "get_your_api_key_from_sendgrid_dashboard"
    MAILJET_API_KEY: str = "get_your_api_key_from_mailjet_dashboard"
    MAILJET_API_SECRET: str = "get_your_api_secret_from_mailjet_dashboard"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
