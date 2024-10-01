from pydantic_settings import BaseSettings, SettingsConfigDict
from HWs.HW4_b import run_4_b
from HWs.HW1 import run_1_c


class IBMCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    token: str


credentials = IBMCredentials()

if __name__ == '__main__':
    run_1_c(credentials.token)  # For explanation see the README and the code
    run_4_b()  # For the explanation see the doc string of the function
