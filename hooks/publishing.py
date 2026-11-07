"""Keep page icons consistent and internal client notes out of public pages."""
import re
from mkdocs.exceptions import PluginError

ICONS = {
    "index.md": "🏡",
    "server-rules.md": "📖",
    "classes.md": "🧙",
    "class-changes.md": "🔮",
    "quality-of-life.md": "🦋",
    "editing.md": "📝",
}
INTERNAL_CONTENT = re.compile(
    r"client[\s_-]+(?:changes|patch(?:es)?|resources)\b"
    r"|finishing patches?\b|WARP (?:profile|patch)|AdInfinitumFinal|Prepare-AdInfinitum",
    re.IGNORECASE,
)


def page_emoji(page):
    return page.meta.get("emoji", ICONS.get(page.file.src_uri, "📄"))


def on_nav(nav, **kwargs):
    for page in nav.pages:
        page.title = ICONS.get(page.file.src_uri, "📄") + " " + page.title


def on_page_markdown(markdown, page, **kwargs):
    hidden = page.meta.setdefault("hide", [])
    if "toc" not in hidden:
        hidden.append("toc")
    if INTERNAL_CONTENT.search(markdown):
        raise PluginError(
            f"{page.file.src_uri}: internal client notes must stay in the excluded source file."
        )
    # Navigation and headings use colorful native emoji, matching the reference wiki.
    page.meta.pop("icon", None)
    emoji = page_emoji(page)
    return re.sub(r"^(# )", lambda match: match[1] + emoji + " ", markdown, count=1, flags=re.MULTILINE)
