# Documentation publishing rules

- Keep internal client changes and patch notes in the excluded `docs/client-patches.md` source file. Preserve this file, but never publish it or add references, summaries, or links to it on public pages.
- New public pages must use the shared icon hook. Set a Material `icon` in front matter when appropriate; otherwise the hook supplies a document icon. Keep navigation and page titles consistent.
- Run `python -m mkdocs build --strict` before pushing. The publishing hook rejects internal client-change and patch references on public pages.
- Push completed documentation changes to GitHub, as requested by the user.
