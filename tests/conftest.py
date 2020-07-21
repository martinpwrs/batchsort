import pytest

from batchsort import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("batchsort.config.TestingConfig")
    with app.app_context():
        yield app