"""Admin dashboard utilities."""

from __future__ import annotations

from pathlib import Path

TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "dashboard.html"


def get_dashboard_template() -> str:
    """Return the HTML template for the admin dashboard.

    The template is stored as a static HTML file to make it easy to integrate
    the prebuilt Tailwind-based design into whatever web framework is used
    by the travel agency system.
    """

    return TEMPLATE_PATH.read_text(encoding="utf-8")


__all__ = ["get_dashboard_template", "TEMPLATE_PATH"]
