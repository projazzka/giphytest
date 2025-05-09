import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict

from giphy.client import GiphyClient, GiphyError


@pytest.mark.asyncio
async def test_get_gif_happy_path(settings):
    """Test that searching for 'igor' returns a valid GIF URL."""
    client = GiphyClient(settings.giphy_api_key)

    # Test the happy path with a known query
    gif_url = await client.get_gif("igor")

    # Verify we got a URL back
    assert gif_url is not None
    assert gif_url.startswith("https://")
    assert gif_url.lower().endswith(".gif")


@pytest.mark.asyncio
async def test_get_gif_no_response(settings):
    """Test that searching with an impossible query returns None."""
    client = GiphyClient(settings.giphy_api_key)

    # Test with an censored query string
    gif_url = await client.get_gif("nazi")

    # Verify we got None back
    assert gif_url is None


@pytest.mark.asyncio
async def test_get_gif_connection_error(settings):
    """Test that the client properly handles connection errors."""
    client = GiphyClient(settings.giphy_api_key)
    # Corrupt the base URL to force a connection error
    client.base_url = "https://invalid-giphy-api-url-that-does-not-exist.com"

    # Verify that attempting to get a GIF raises a GiphyException
    with pytest.raises(GiphyError) as exc_info:
        await client.get_gif("test")

    # Verify the exception contains information about the connection error
    assert "communicate" in str(exc_info.value).lower()
