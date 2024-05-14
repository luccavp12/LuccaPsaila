import reflex as rx
from ..template import template

@rx.page(route="/ChatVac")
@template
def chatvac():
    """The ChatVac project page."""
    return rx.box(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.heading("ChatVac", font_size="2em"),
                    rx.link(
                        "chatvac.com",
                        href="chatvac.com",  # Add your project link here
                        target="_blank",
                        color="blue",
                        trim="end",
                        # marginTop="1em",
                        # marginBottom="1em",
                    ),
                    direction="row",
                    gap="1em",
                    alignItems="center",
                    marginBottom="1em",
                ),
                rx.text(
                    "One place for all your messages.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.list.unordered(
                    rx.list.item("Javascript and Python-based web application which combines both Slack and Discord APIs such that a user can fully access both services solely within their web browser."),
                    rx.list.item("Implemented Redis Publish/Subscribe messaging system to connect APIs with server code."),
                    rx.list.item("Integrated Socket.io to allow for fluid communication between server and client side."),
                    rx.list.item("Stored messaging data from Discord and Slack in a SQLite3 database, and displayed using jQuery."),
                    rx.list.item("Ran server side of application on an AWS EC2 instance and hosted client side using S3 and Route 53."),
                ),
                rx.flex(
                    rx.text(
                        "Home Page",
                        font_size="1em",
                        color="black",
                        marginBottom="0.5em",
                        marginTop="1em",
                        fontWeight="bold",
                    ),
                    rx.chakra.image(
                        src="/ChatVacMain.png",
                        width="min(100vw, 1000px)",
                    ),
                    direction="column",
                ),
            ),
            direction="column",
            justify="center",
            align="start",
            width="100%",
            height="100%",
        ),
        padding="1em",
    )