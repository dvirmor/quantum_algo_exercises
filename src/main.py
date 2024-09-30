from pydantic_settings import BaseSettings, SettingsConfigDict
from HWs.HW4_b import run_4_b
from HWs.HW1 import run_1_d


class IBMCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file="/home/dvir/PycharmProjects/Quantum/quantum_algorithms/.env")
    token: str


credentials = IBMCredentials()

if __name__ == '__main__':

    run_4_b()  # For the explanation see the doc string of the function
