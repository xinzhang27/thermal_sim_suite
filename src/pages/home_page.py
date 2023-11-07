import logging

import httpx
from nicegui import ui
from src.backend.server import Server

logger = logging.getLogger(__name__)


def content() -> None:
    with ui.element().classes("column justify-left items-center"):
        # ui.label("Welcome to the Thermal Simulation Suite").classes("text-3xl font-bold")
        ui.link("PDF Viewer", "/pdf_viewer").classes("text-center text-2xl font-bold text-black leading-10")
        ui.separator()
        ui.link("Search", "/data_analysis").classes("text-center text-2xl font-bold text-black leading-10")
        ui.separator()
        ui.link("Data Analysis", "/results").classes("text-center text-2xl font-bold text-black leading-10")
        ui.separator()
        ui.link("Results", "/search").classes("text-center text-2xl font-bold text-black leading-10")
