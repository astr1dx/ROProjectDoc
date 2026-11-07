"""Keep page icons consistent and internal client notes out of public pages."""
import re
from mkdocs.exceptions import PluginError

ICONS = {
    "index.md": "material/home-outline",
    "server-rules.md": "material/clipboard-text-outline",
    "classes.md": "material/account-group-outline",
    "class-changes.md": "material/sword-cross",
    "quality-of-life.md": "material/bag-personal-outline",
    "editing.md": "material/pencil-outline",
}
INTERNAL_CONTENT = re.compile(
    r"client[\s_-]+(?:changes|patch(?:es)?|resources)\b"
    r"|finishing patches?\b|WARP (?:profile|patch)|AdInfinitumFinal|Prepare-AdInfinitum",
    re.IGNORECASE,
)


def on_page_markdown(markdown, page, **kwargs):
    hidden = page.meta.setdefault("hide", [])
    if "toc" not in hidden:
        hidden.append("toc")
    if INTERNAL_CONTENT.search(markdown):
        raise PluginError(
            f"{page.file.src_uri}: internal client notes must stay in the excluded source file."
        )
    icon = page.meta.setdefault(
        "icon", ICONS.get(page.file.src_uri, "material/file-document-outline")
    )
    emoji = ":" + icon.replace("/", "-", 1) + ":"
    return re.sub(r"^(# )", lambda match: match[1] + emoji + " ", markdown, count=1, flags=re.MULTILINE)
