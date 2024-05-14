import reflex as rx
from ..template import template

@rx.page(route="/")
@template
def index():
    """The home page."""
    return rx.box(
        rx.flex(
            rx.heading(
                "LUCCA PSAILA",
                font_size="min(9vw, 60px)",
                color="white",
                letterSpacing= "min(2.5vw, 40px)",
                fontWeight="500",
            ),
            rx.box(
                height="1em",
            ),
            rx.text(
                "Personal Portfolio",
                font_size="min(5.5vw, 40px)",
                color="white",
                letterSpacing= "min(2vw, 18px)",
                fontWeight="400",
            ),
            rx.box(
                height="1em",
            ),
            rx.chakra.image(
                src="/Lucca.jpg",
                width="200px",
                height="200px",
                border_radius="full",
            ),
            direction="column",
            justify="center",
            align="center",
            width="100%",
            height="100%",
            paddingTop="50vh",
        ),
        background="center/cover url('/city.jpg')",
        width="100%",
        height="100vh",
    )