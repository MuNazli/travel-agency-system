"""Utilities for generating marketing HTML pages."""

from __future__ import annotations

from textwrap import dedent


def generate_landing_page() -> str:
    """Return the static HTML for the marketing landing page.

    The markup matches the design provided by product and includes a hero
    message inviting users to interact with the application.  The HTML is
    intentionally returned as a string so that it can easily be embedded in
    different delivery channels (for example, an email campaign or a
    pre-rendered web page).
    """

    return dedent(
        """\
        <!DOCTYPE html>
        <html>
          <head>
            <title>My app</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta charset="utf-8">
            <script src="https://cdn.tailwindcss.com"></script>
          </head>
          <body class="flex justify-center items-center h-screen overflow-hidden bg-white font-sans text-center px-6">
            <div class="w-full">
              <span class="text-xs rounded-full mb-2 inline-block px-2 py-1 border border-amber-500/15 bg-amber-500/15 text-amber-500">🔥 New version dropped!</span>
              <h1 class="text-4xl lg:text-6xl font-bold font-sans">
                <span class="text-2xl lg:text-4xl text-gray-400 block font-medium">I'm ready to work,</span>
                Ask me anything.
              </h1>
            </div>
              <img src="https://huggingface.co/deepsite/arrow.svg" class="absolute bottom-8 left-0 w-[100px] transform rotate-[30deg]" />
            <script></script>
          </body>
        </html>
        """
    ).strip()


__all__ = ["generate_landing_page"]
