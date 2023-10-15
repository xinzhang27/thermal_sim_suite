from nicegui import ui


def content() -> None:
    with ui.element().classes("column"):
        ui.label("a").classes("font-sans")
        ui.label("a").classes("flex")
        ui.label("a").classes("order-first")
