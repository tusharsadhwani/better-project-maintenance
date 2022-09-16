import myproject


def test_homepage() -> None:
    output = myproject.home()
    assert output == "This is the home page"


def test_api() -> None:
    user = myproject.get_user()
    assert user.username == "Michael"
