"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .pages.index import index
from .pages.resume import resume
from .pages.projects import projects
from .pages.organizeai import organizeai
from .pages.qandamarket import qandamarket
from .pages.chatvac import chatvac

app = rx.App()
app.add_page(index, route="/")
app.add_page(resume, route="/resume")
app.add_page(projects, route="/projects")
app.add_page(organizeai, route="/OrganizeAI")
app.add_page(qandamarket, route="/QandAMarket")
app.add_page(chatvac, route="/ChatVac")