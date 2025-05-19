import os

import cattrs
import pytest
import yaml
from playwright.sync_api import Playwright

from src.utils.environment import Config


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict, playwright: Playwright) -> dict:
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": [
            "--allow-file-access-from-files",
            "--use-fake-device-for-media-stream",
            "--use-fake-ui-for-media-stream",
            "--disable-popup-blocking",
            "--disable-search-engine-choice-screen",
            "--disable-infobars",
            "--disable-dev-shm-usage",
            "--disable-notifications",
            "--disable-blink-features=AutomationControlled",
        ],
    }

@pytest.fixture(scope="session")
def env_config() -> Config:
    env_name = os.environ.get("ENV_NAME")

    with open(f"environment/{env_name}.yaml", "r") as f:
        yaml_content = yaml.safe_load(f)
        return cattrs.structure(yaml_content, Config)
