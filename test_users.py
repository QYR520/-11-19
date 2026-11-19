import pytest
import requests


def test_get_user_success(requests_mock, base_url):
    """查询用户详情：状态码 200，关键字段齐全"""
    requests_mock.get(
        f"{base_url}/users/1",
        json={"id": 1, "name": "张三", "email": "zs@test.com"},
    )

    response = requests.get(f"{base_url}/users/1", timeout=5)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "张三"
    assert "email" in data


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(requests_mock, base_url, user_id):
    """不同 id 都能查到对应的用户"""
    requests_mock.get(
        f"{base_url}/users/{user_id}",
        json={"id": user_id, "name": f"用户{user_id}"},
    )

    response = requests.get(f"{base_url}/users/{user_id}", timeout=5)

    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_get_user_not_found(requests_mock, base_url):
    """查询不存在的用户：期望 404，且响应体带错误信息"""
    requests_mock.get(
        f"{base_url}/users/999",
        status_code=404,
        json={"error": "not found"},
    )

    response = requests.get(f"{base_url}/users/999", timeout=5)

    assert response.status_code == 404
    assert response.json()["error"] == "not found"
