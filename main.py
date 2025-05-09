#!/usr/bin/env python3

import asyncio

import typer
from pydantic_settings import BaseSettings, SettingsConfigDict

from giphy.client import GiphyClient, GiphyError


class Settings(BaseSettings):
    giphy_api_key: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


app = typer.Typer()
settings = Settings()  # type: ignore


async def fetch_gif_url(query: str) -> None:
    try:
        client = GiphyClient(settings.giphy_api_key)
        gif_url = await client.get_gif(query)

        if not gif_url:
            typer.echo(f"No GIF found for query: {query}")
            return

        typer.echo(gif_url)

    except GiphyError as e:
        typer.echo(f"Error: {e}", err=True)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)


@app.command()
def main(query: str) -> None:
    asyncio.run(fetch_gif_url(query))


if __name__ == "__main__":
    app()
