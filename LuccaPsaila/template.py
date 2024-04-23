from typing import Callable

import reflex as rx

# from .components.menu import menu
from .components.navbar import navbar
from .components.footer import footer


def template(
    page: Callable[[], rx.Component]
) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            height="4em",
        ),
        page(),
        # rx.hstack(
        #     # rx.container(page(), widht="100%"),
        # ),
        footer(),
        width="100%",
    )
