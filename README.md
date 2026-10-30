# AmigaFAQ

Source for [amigafaq.org](https://amigafaq.org) - frequently asked questions about the Commodore Amiga.

The site is styled after AmigaOS 3.1 Workbench and is deliberately simple (ASCII HTML, table layout)
so it can be read on real Amiga web browsers such as AWeb and IBrowse as well as modern ones.

## Editing content

FAQ text lives in `tools/content.py`. After editing, regenerate the pages from the repo root:

    python3 tools/build.py .

Hosted on GitHub Pages from the `main` branch root. The `CNAME` file binds the site to `amigafaq.org`.
HTTPS is available but deliberately not enforced, so older machines can use plain HTTP.

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See [LICENSE](LICENSE).
