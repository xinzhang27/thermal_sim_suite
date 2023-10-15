from nicegui import ui


def content() -> None:
    """
    Create the home page content.
    :return:
    """
    ui.upload(label="Input Model")
    # choose different heuristic method
    ui.radio(["Genetic Algorithm", "Simulated Annealing", "Particle Swarm Optimization"])
    ui.button("Run")
