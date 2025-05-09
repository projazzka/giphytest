import httpx


class GiphyError(Exception):
    pass


class GiphyClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.giphy.com/v1/gifs"

    async def get_gif(self, query: str) -> str | None:
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
