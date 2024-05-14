import reflex as rx
from ..template import template

@rx.page(route="/QandAMarket")
@template
def qandamarket():
    """The QandA project page."""
    return rx.box(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.heading("QandA Market", font_size="2em"),
                    rx.link(
                        "qandamarket.com",
                        href="qandamarket.com",  # Add your project link here
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
                    "Instantly book appointments with experts from around the world.",
                    font_size="1em",
                    color="black",
                    marginBottom="0.5em",
                ),
                rx.list.unordered(
                    rx.list.item("Developed a dynamic marketplace application utilizing the MERN stack, enabling experts across various domains to monetize their expertise through online consultations."),
                    rx.list.item("Managed data storage and retrieval with MongoDB, ensuring robust and scalable database operations."),
                    rx.list.item("Utilized Node.js with Express.js for backend development, efficiently managing URL routing and resource requests."),
                    rx.list.item("Crafted an intuitive frontend user experience using React, integrating MUI for pleasing and consistent design elements."),
                    rx.list.item("Enhanced application performance by integrating AWS S3 and CloudFront for image storage and retrieval, achieving a 50% reduction in user profile rendering time."),
                    rx.list.item("Incorporated Stripe payments using their API with webhooks for real-time payment notifications and secure tokenizationv for card storage."),
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
                        src="/qandamarket.jpg",
                        width="min(100vw, 1000px)",
                    ),
                    rx.text(
                        "Join as an expert",
                        font_size="1em",
                        color="black",
                        marginBottom="0.5em",
                        marginTop="1em",
                        fontWeight="bold",
                    ),
                    rx.chakra.image(
                        src="/qandamarket2.jpg",
                        width="min(100vw, 1000px)",
                    ),
                    rx.text(
                        "Expert Page with Available Meetings",
                        font_size="1em",
                        color="black",
                        marginBottom="0.5em",
                        marginTop="1em",
                        fontWeight="bold",
                    ),
                    rx.chakra.image(
                        src="/qandamarket3.jpg",
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