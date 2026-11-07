---
icon: material/pencil-outline
---

# Editing these docs

MkDocs reads the Markdown files in `docs/` and builds a website. Edit those files in your IDE or a text editor; MkDocs itself is not a browser-based editing CMS.

## File layout

```text
docs-project/
├── mkdocs.yml
├── requirements.txt
└── docs/
    ├── index.md
    ├── server-rules.md
    ├── class-changes.md
    ├── quality-of-life.md
    ├── client-patches.md
    └── editing.md
```

`class-changes.md` contains the complete class guide as one portable page. Copy it into an existing MkDocs project and add it to that project's navigation if you prefer to use another site.

## Install documentation tools

Run from the **project root** folder (the folder containing `mkdocs.yml`) in PowerShell. A separate environment keeps documentation packages away from the Hercules build environment.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This site uses Material for MkDocs. The requirements file installs the theme and a compatible MkDocs version.

## Preview while editing

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

Open `http://127.0.0.1:8000/`. Saving a Markdown file refreshes the preview. Stop the preview with Ctrl+C.

## Validate and build

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

The generated website goes into `site/`. The source Markdown/configuration belongs in version control; `site/` and `.venv/` are ignored. Building does not publish the site.

## Add or update a page

1. Edit the appropriate `docs/*.md` file and update its date.
2. Record the final implemented behavior, including approved per-level costs, limits and exceptions.
3. If adding a page, add its relative filename under `nav` in `mkdocs.yml`.
4. Use relative Markdown links, such as `[Class changes](class-changes.md)`.
5. Run the strict build and check the local preview.

Use the class guide for current rules and keep detailed implementation/testing history in `doc/AD-INFINITUM.md`. Reconcile a rule against its active database/source and later clarifications before changing the guide. Automated checks and in-game confirmation are separate verification steps.

## Important implementation locations

Paths below are relative to the server repository unless stated otherwise. They are code references, not website links.

| Area | Location |
| --- | --- |
| Skill costs, delays, ammunition and durations | `db/pre-re/skill_db.conf` |
| Learnable class trees | `db/pre-re/skill_tree.conf` |
| Status persistence/removal flags | `db/pre-re/sc_config.conf` |
| Base-stat and ASPD limits | `db/pre-re/unit_parameters_db.conf` |
| Class data and EXP groups | `db/pre-re/job_db.conf`, `db/pre-re/exp_group_db.conf` |
| Skill execution and combat | `src/map/skill.cpp`, `battle.cpp`, `status.cpp`, `pc.cpp` |
| Custom NPCs | `npc/custom/`, loaded through `npc/scripts_custom.conf` |
| Deployment-specific battle/rate settings | `conf/import/battle.conf` |
| Local server configuration example | `conf/import-examples/` |
| English client skill resources in ROProject | `Client/data/luafiles514/lua files/skillinfoz/` and `Client/data/lua files/skillinfoz/` |
| Client patch profile in ROProject | `AdInfinitumFinal.yml` and `Prepare-AdInfinitum.ps1` |

The server-only repository does not include the separate `Client/`, `Tools/` or `Offline/` workspace folders. Documentation builds do not require those folders. Keep credentials and player/database files out of documentation pages.

## Skill images and presentation

Skill artwork lives in `docs/assets/skills/` and is served with the site, so the guide does not depend on an external image host. `manifest.json` records the skill-name-to-image mapping. The images were exported from the Ad Infinitum client's `data.grf`, using the icon names in its `skillinfolist.lub`, and converted from BMP to transparent PNG. Original game artwork belongs to its respective rights holders.

Custom skills use their actual client mappings: Super Blessing shares Blessing's icon, Madness Break shares Madness Canceller's icon, and Avarice uses `BS_UNFAIRLYTRICK`. Keep those mappings aligned with future client updates.

To place an existing icon beside a skill name:

```markdown
![Berserk icon](assets/skills/lk_berserk.png){ .skill-icon } **Berserk**
```

Keep the readable skill name alongside the image. The shared presentation styles live in `docs/assets/stylesheets/extra.css`. `classes.md` links into the full class reference; update its links if class headings change.

## MkDocs references

- [Getting started](https://www.mkdocs.org/getting-started/)
- [Configuration and navigation](https://www.mkdocs.org/user-guide/configuration/)

## Publish changes with GitHub Pages

The GitHub Actions workflow in `.github/workflows/publish.yml` validates pull requests and publishes every push to `main` to the `gh-pages` branch.

After the first successful workflow, open the repository's **Settings > Pages**, choose **Deploy from a branch**, select **gh-pages** and **/ (root)**, and save. The website URL is shown on that page.

For each update, run from the project root:

```powershell
git add .
git commit -m "Update documentation"
git push
```

Check the **Actions** tab for build or deployment errors. GitHub commit history and pull requests show the Markdown changes; the website displays the latest published version.
