"""Keep page icons consistent and internal client notes out of public pages."""
import re
from mkdocs.exceptions import PluginError

ICONS = {
    "endless-tower.md": "\U0001f5fc",
    "endless-cellar.md": "\U0001f573",
    "updates/2026-11-22.md": "\U0001f5fc",
    "headgear-quests.md": "\U0001f452",
    "visual-afk.md": "\U0001f4a4",
    "updates/2026-11-20.md": "\U0001f452",
    "updates/2026-11-19.md": "\U0001f431",
    "pet-system.md": "\U0001f431",
    "pet-catalogue.md": "\U0001f43e",
    "warper.md": "\U0001f30d",
    "novice-training.md": "\U0001f331",
    "updates/2026-11-18.md": "\U0001f331",
    "character-services.md": "\U0001f465",
    "biolabs4.md": "\U0001f9ec",
    "main-office.md": "\U0001f3e2",
    "card-removal.md": "\U0001fa84",
    "updates/2026-11-17.md": "\U0001f4cd",
    "area-loot.md": "🧺",
    "mercy-system.md": "🍀",
    "vestige-coins.md": "🪙",
    "coin-exchange.md": "🛍️",
    "refining.md": "🔨",
    "index.md": "🏡",
    "server-rules.md": "📖",
    "classes.md": "🧙",
    "class-changes.md": "🔮",
    "personal-settings.md": "🎛️",
    "quality-of-life.md": "🦋",
    "attendance.md": "🔔",
    "hourly-rewards.md": "🕥",
    "dealers.md": "🍬",
    "kill-steal-protection.md": "🛡️",
    "kill-count.md": "🎯",
    "card-drop-announcements.md": "🃏",
    "card-exchange.md": "🎟️",
    "vendor-system.md": "💰",
    "quest-changes.md": "📜",
    "all-pages.md": "🔎",
    "getting-started.md": "⭐",
    "autoloot.md": "🧲",
    "fast-storage.md": "📦",
    "features.md": "🧭",
    "dungeons.md": "🗺️",
    "events.md": "🎉",
    "updates.md": "📰",
    "updates/2026-11-10.md": "🍂",
    "companion-commands.md": "🐾",
    "updates/2026-11-11.md": "🍁",
    "build-manager.md": "🧰",
    "baby-characters.md": "👶",
    "updates/2026-11-13.md": "🌀",
    "adjusted-prices.md": "💸",
    "updates/2026-11-16.md": "📉",
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
