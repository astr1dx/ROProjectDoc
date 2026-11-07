# Documentation publishing rules

- Keep internal client changes and patch notes in the excluded `docs/client-patches.md` source file. Preserve this file, but never publish it or add references, summaries, or links to it on public pages.
- New public pages must use the shared icon hook. Use colorful emoji in navigation and page titles, matching the reference wiki. Add new page mappings to `ICONS` in `hooks/publishing.py`; the default is a document emoji. Do not add monochrome Material navigation icons.
- Run `python -m mkdocs build --strict` before pushing. The publishing hook rejects internal client-change and patch references on public pages.
- Push completed documentation changes to GitHub, as requested by the user.
