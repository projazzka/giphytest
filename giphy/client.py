import httpx


class GiphyError(Exception):
    """Exception raised for errors in the Giphy API client."""

    pass


class GiphyClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.giphy.com/v1/gifs"

    async def get_gif(self, query: str) -> str | None:
        """
        Search for a GIF using the Giphy API and return its URL.

        Args:
            query: The search term to find a GIF

        Returns:
            str | None: The URL of the first GIF found, or None if no GIFs found

        Raises:
            GiphyError: If there's an error communicating with the Giphy API
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/search",
                    params={
                        "api_key": self.api_key,
                        "q": query,
                        "limit": 1,
                        "rating": "g",
                    },
                )
                response.raise_for_status()

                data = response.json()
                if not data["data"]:
                    return None

                return data["data"][0]["images"]["original"]["url"]

            except httpx.HTTPError as e:
                raise GiphyError(f"Failed to communicate with Giphy API: {str(e)}")
            except KeyError as e:
                raise GiphyError(f"Unexpected response format from Giphy API: {str(e)}")
