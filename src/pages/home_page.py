import logging

import httpx
from nicegui import ui
from src.backend.server import Server

logger = logging.getLogger(__name__)


def content() -> None:
    with ui.element().classes("column"):
        ui.label("a").classes("font-sans")
        ui.label("a").classes("flex")
        ui.label("a").classes("order-first")
        admin = httpx.get(Server.hostname + "/admin")
        print(admin.status_code)
        ui.markdown(admin.text)
