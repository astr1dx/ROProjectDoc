---
icon: material/clipboard-text-outline
---

# Server rules

Updated: **November 10, 2026**.

## Core settings

| Setting | Current value |
| --- | --- |
| Episode profile | 14.2: Eclage, with a strict content allowlist |
| Game mode | Classic Pre-Renewal |
| Maximum Base Level | 99 |
| Maximum Job Level | 70, subject to the class-specific caps below |
| Maximum base stat | 99, including adopted characters |
| Maximum ASPD | 190 |
| Instant-cast DEX threshold | 150 under classic cast-time rules |
| Party EXP sharing range | 20 levels |
| Minimum skill delay | 100 milliseconds; higher skill-specific delays still apply |
| Minimum usable-item interval | 50 milliseconds; item-specific restrictions still apply |
| Server time | Philippine Standard Time, UTC+08:00 |
| Server language | English |

Novices retain Job Level 10. First jobs and ordinary non-transcendent second jobs generally retain Job Level 50. Transcendent second jobs, Super Novice/Super Baby and the customized Soul Linker/Baby Soul Linker reach Job Level 70.

The current environment is local/offline. Public international hosting is a separate deployment task.

## Rates

| Rate | Monday-Friday | Saturday-Sunday |
| --- | ---: | ---: |
| Monster Base EXP | 20x | 25x |
| Monster Job EXP | 20x | 25x |
| Normal non-card drops | 20x | 25x |
| Normal cards | 5x | 5x |
| MVP and mini-boss non-card drops | 3x | 3x |
| MVP bonus item rewards | 3x | 3x |
| MVP and mini-boss cards | 1x | 1x |
| Quest EXP | 5x | 5x |
| Pet and homunculus intimacy gain | 3x | 3x |

A standard 0.01% card becomes **0.05%** for a normal monster and remains **0.01%** for an MVP or mini-boss. Drop probabilities cannot exceed 100%.

Weekend rates run from Saturday 00:00 until Monday 00:00 in Philippine time. Card, boss-drop, quest-EXP and intimacy multipliers remain static. Rotating hunting-region bonuses multiply the active weekday/weekend monster EXP rates; see [quality of life](quality-of-life.md).

## Content profile

The server uses an explicit Episode 14.2 allowlist for maps, monsters, items, quests and regional scripts. Later content is excluded. This is an adapted classic-server profile, not an unmodified official Renewal database. Eclage's original level-100/120 requirements are adapted to level 90; existing level-99 requirements remain.

Some convenience features are explicit exceptions to the episode cutoff, including RODEX, [Market Street and the vendor system](vendor-system.md), Infinite Fly Wing, the documented custom platinum skills, and the selected ammunition, kunai and pet supplies in the [dealer catalogue](dealers.md#ammunition-and-pet-supply-exceptions). Their availability does not enable the rest of the later-episode content.

## Important map definitions

- **Natural MVP map:** a map with a positive-count natural MVP spawn definition, identified by the monster's native MVP spawn flag or MVP EXP. It remains an MVP map while the MVP is dead. Branch summons alone do not change the classification; ordinary mini-boss maps are not automatically included.
- **GvG/WoE map rules:** class restrictions that use the GvG/castle map flags apply on those maps even outside the active siege, where stated in the class guide.
- **RODEX siege restriction:** mail is blocked only in a castle during its relevant active WoE session. It is available on ordinary maps during WoE.

See [class changes](class-changes.md) for skill-specific exceptions and [quality of life](quality-of-life.md) for the mail rules.

## Trading and exchanges

Shops may open in **Market Street, Payon, Morocc, Alberta and Comodo** only. Pricing rules and the **one-listing-per-stackable-item-ID per account** limit apply to selling, buying and offline shops; see the [vendor system](vendor-system.md). Hardware-ID enforcement is deferred.

[Card exchange points](card-exchange.md) are shared across the account and are separate from hourly reward points and Gold Coins. Bloody Branch is the only enabled card-point reward.

## Chat channels and saved preferences

All existing and new players automatically join **`#main`** for discussion, **`#recruit`** for recruitment and **`#market`** for trading. A channel explicitly turned Off in **`@settings`** stays Off for that account on later logins.

See [Personal settings](personal-settings.md) for channel commands, display preferences and character-specific storage/restock limits.
