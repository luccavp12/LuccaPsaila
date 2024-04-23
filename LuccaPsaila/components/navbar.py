import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.heading("Lucca Psaila", font_size="2em"),
            marginRight="1em"
        ),
        # rx.hstack(*[rx.button(name, on_click=lambda: rx.navigate(f"/{name.lower()}")) for name in ["Home", "Resume", "Projects"]]),
        rx.hstack(*[rx.link(name, href=f"/{name.lower()}", color="black", marginRight="1em") for name in ["Home", "Resume", "Projects"]]),
        position="fixed",
        top="0px",
        background_color="white",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
        align="center",
    )
