from contextlib import contextmanager

from nicegui import ui

from src.pages.info import PageInfo


@contextmanager
def frame(nav_title: str):
    """
    Custom page frame to share the same styling and behavior across all pages.
    :param nav_title: the title of the page
    :return:
    """
    # ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header(fixed=True).classes("bg-gradient-to-r from-cyan-500 to-blue-500 justify-center text-white"):
        # ui.label("Thermal Simulation Suite").classes("font-bold")
        # ui.label(nav_title)
        with ui.row():
            ui.link(PageInfo.home_page.get("text"), PageInfo.home_page.get("target")).classes("text-white")
            ui.link(PageInfo.pdf_page.get("text"), PageInfo.pdf_page.get("target")).classes("text-white")
            ui.link(PageInfo.search_page.get("text"), PageInfo.search_page.get("target")).classes("text-white")
            ui.link(PageInfo.data_page.get("text"), PageInfo.data_page.get("target")).classes("text-white")
            ui.link(PageInfo.results_page.get("text"), PageInfo.results_page.get("target")).classes("text-white")
    with ui.column().classes("w-full items-center"):
        yield
