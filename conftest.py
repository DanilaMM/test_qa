from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from Configurations.TestData import TestData
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(params=['Chrome'])
def fixtureSetup(request):
    driver = None
    if request.param == 'Chrome':
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # mobile_emulation = { "deviceName": "iPhone SE" }
        # options.add_experimental_option("mobileEmulation", mobile_emulation)
        # options.add_argument('--headless')
        options.add_argument("--start-maximized")
        chrome_service = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
        # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager("").install()))
        driver = webdriver.Chrome(options=options, service=chrome_service)

    elif request.param == 'Firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager("").install()))
    driver.implicitly_wait(30)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def get_env_options(env_stand):
    return TestData.ENV_CONFIG[env_stand]

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--env_stand",
        action="store",
        default="dev",
        help="Select evn config",
    )

@pytest.fixture(scope="session")
def env_stand(request: pytest.FixtureRequest) -> str:
    opt = request.config.getoption("env_stand")
    return opt