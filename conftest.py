import pytest

BASE_URL = "https://api.demo.com"


@pytest.fixture(scope="session")
def base_url():
    """被测服务地址。当前指向 mock 域名，真实请求由 requests-mock 拦截"""
    return BASE_URL
