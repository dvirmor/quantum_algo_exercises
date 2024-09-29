from pydantic_settings import BaseSettings, SettingsConfigDict
from HWs.HW4_b import run_4_b


class IBMCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    token: str


credentials = IBMCredentials()

if __name__ == '__main__':
    run_4_b()  # For the explanation see the doc string of the function
