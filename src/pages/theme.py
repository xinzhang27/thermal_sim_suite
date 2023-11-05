from contextlib import contextmanager

from src.pages.menu import menu

from nicegui import ui


@contextmanager
def frame(nav_title: str):
    """
    Custom page frame to share the same styling and behavior across all pages.
    :param nav_title: the title of the page
    :return:
    """
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header(fixed=True).classes("justify-between text-white"):
        ui.label("Thermal Simulation Suite").classes("font-bold")
        ui.label(nav_title)
        with ui.row():
            menu()
    with ui.column().classes("w-full items-center"):
        yield
