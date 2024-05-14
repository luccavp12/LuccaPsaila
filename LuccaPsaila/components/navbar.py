import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.heading("Lucca Psaila", font_size="min(5vw, 35px)"),
            marginRight="1em"
        ),
        rx.hstack(
            rx.link(
                "Home",
                href="/",
                color="black",
                marginRight="1em",
            ),
            rx.link(
                "Resume",
                href="/resume",
                color="black",
                marginRight="1em",
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.link(
                        "Projects",
                        href="/projects",
                        color="black",
                        marginRight="1em",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.link(
                            "MailAI",
                            href="/MailAI",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            "QandA Market",
                            href="/QandAMarket",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            "ChatVac",
                            href="/ChatVac",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    width="10rem",
                ),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="white",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
        align="center",
    )
