"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .pages.index import index
from .pages.resume import resume

app = rx.App()
app.add_page(index, route="/")
app.add_page(index, route="/home")
app.add_page(resume, route="/resume")
