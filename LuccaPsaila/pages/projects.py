import reflex as rx
from ..template import template

@rx.page(route="/projects")
@template
def projects():
    """The projects page."""
    return rx.box(
        rx.vstack(
            rx.heading("My Projects", fontSize="3em", color="black"),
        ),
        rx.flex(
            rx.box(
                rx.heading(
                    rx.link(
                        "OrganizeAI",
                        href="/MailAI",
                        color="black",
                        marginRight="2em",
                        marginBottom="0.5em",
                    ),
                    font_size="2em", marginBottom="0.5em"),
                rx.text(
                    "Use GSuite AI automation to streamline your business workflow.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.chakra.image(
                src="/organizeAI.jpg",
                width="40vw",
                # height="200px",
                # border_radius="full",
                ),
            ),
            rx.box(
                rx.heading("QandA Market", font_size="2em", marginBottom="0.5em"),
                rx.text(
                    "Instantly book appointments with experts from around the world.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.chakra.image(
                src="/qandamarket.jpg",
                width="50vw",
                # height="200px",
                # border_radius="full",
                ),
            ),
            rx.box(
                rx.heading("ChatVac", font_size="2em", marginBottom="0.5em"),
                rx.text(
                    "One place for all your messages.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.chakra.image(
                src="/ChatVacMain.png",
                width="50vw",
                # height="200px",
                # border_radius="full",
                ),
            ),
            direction="column",
            justify="center",
            align="start",
            width="100%",
            height="100%",
            marginTop="2em",
            gap="2em",
        ),
        padding="1em",
    )