# Ad Infinitum documentation

Current server rules and customizations, updated **November 7, 2026**.

| Page | Contents |
| --- | --- |
| [Server rules](server-rules.md) | Episode profile, rates, level/stat caps and server time. |
| [Class changes](class-changes.md) | All implemented class adjustments, shared combat rules, platinum skills and related NPC locations. |
| [Quality of life](quality-of-life.md) | Recovery, mail, party indicators, bulk storage, teleporting, food and other convenience changes. |
| [Client patches](client-patches.md) | Current WARP selections, finishing patches and compatibility fixes. |
| [Editing these docs](editing.md) | How to preview, edit, validate and build this MkDocs site. |

## Scope

These pages describe the final implemented behavior. They consolidate the development notes and later corrections; they are not a chronological patch log. The server uses Classic Pre-Renewal mechanics with a custom Episode 14.2 content profile. Skill names may have different English translations in the client; aliases are included where useful.

The complete class guide is a single portable Markdown file, `class-changes.md`. It can also be copied into another MkDocs project's documentation folder.

## Verification status

The changes have build, configuration and focused automated checks. Some gameplay and UI interactions still await in-game confirmation. Do not interpret this guide as a claim that every class has completed gameplay or balance testing.

Confirmed player checks include Super Blessing on self/other players with both effects and Blessing sound, Berserk chat with the red body effect persisting through teleports, bulk-purchase confirmation/storage delivery, improved zoom, emotes staying connected, and returning to login after a tested disconnect.

## Documentation ownership

Edit the relevant Markdown page whenever a rule changes, and update its date. The technical implementation history remains in `doc/AD-INFINITUM.md` in the server repository; these MkDocs pages are the current rules reference.
