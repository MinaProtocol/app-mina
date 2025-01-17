from ragger.conftest import configuration
import pytest

###########################
### CONFIGURATION START ###
###########################

# You can configure optional parameters by overriding the value of ragger.configuration.OPTIONAL_CONFIGURATION
# Please refer to ragger/conftest/configuration.py for their descriptions and accepted values
configuration.OPTIONAL.BACKEND_SCOPE = "function"

configuration.OPTIONAL.CUSTOM_SEED = "course grief vintage slim tell hospital car maze model style elegant kitchen state purpose matrix gas grid enable frown road goddess glove canyon key"

#########################
### CONFIGURATION END ###
#########################

# Pull all features from the base ragger conftest using the overridden configuration
pytest_plugins = ("ragger.conftest.base_conftest", )

def pytest_addoption(parser):
    parser.addoption(
        "--all", action="store_true", default=False, help="Run all tests including crypto tests (not for release builds)"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "all: only run for not release builds")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--all"):
        return
    skip = pytest.mark.skip(reason="Use --all flag to run")
    for item in items:
        if "all" in item.keywords:
            item.add_marker(skip)
