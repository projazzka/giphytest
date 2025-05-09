import pytest

from settings import Settings


@pytest.fixture
def settings():
    """Fixture that provides a Settings instance."""
    return Settings()  # type: ignore
