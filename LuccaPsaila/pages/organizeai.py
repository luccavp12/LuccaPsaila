import reflex as rx
from ..template import template

@rx.page(route="/OrganizeAI")
@template
def organizeai():
    """The OrganizeAI project page."""
    return rx.box(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.heading("OrganizeAI", font_size="2em"),
                    rx.link(
                        "Google Workspace Marketplace",
                        href="https://workspace.google.com/marketplace/search/?host=gmail",  # Add your project link here
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
                    "Use GSuite AI automation to streamline your business workflow.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.list.unordered(
                    rx.list.item("Developed a GSuite add-on that uses AI to automate email attachment organization, saving users time and effort."),
                    rx.list.item("Implemented Google Cloud Natural Language API to analyze email content and classify attachments into predefined categories."),
                    rx.list.item("Utilized Google Apps Script to create a Gmail add-on, enabling users to interact with the AI model directly from their inbox."),
                    rx.list.item("Integrated Google Drive API to automatically move attachments to the appropriate folder based on the AI classification."),
                    rx.list.item("Designed a user-friendly interface using Google Workspace UI components, ensuring a seamless user experience."),
                    rx.list.item("Published the add-on on the Google Workspace Marketplace, allowing users to easily install and access the tool."),
                ),
                rx.flex(
                    rx.text(
                        "Built in Google Apps Script",
                        font_size="1em",
                        color="black",
                        marginBottom="0.5em",
                        marginTop="1em",
                        fontWeight="bold",
                    ),
                    rx.chakra.image(
                        src="/organizeAI.jpg",
                        width="40vw",
                        # height="200px",
                        # border_radius="full",
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