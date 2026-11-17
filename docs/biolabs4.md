# Bio Labs 4

**Bio Labs 4 is open as an adapted Classic Pre-Renewal party dungeon.** Its regular monsters, elites and MVPs have been retuned for Vestige Rift's 99/70 rules, with a classic-only direct-drop pool.

## Getting there

| Route | Portal | Arrival |
| --- | --- | --- |
| Bio Labs 3 to Bio Labs 4 | `lhz_dun03 239,78` | `lhz_dun04 245,56` |
| Bio Labs 4 to Bio Labs 3 | `lhz_dun04 244,61` | `lhz_dun03 240,75` |

The usual Bio Labs 3 access requirements still apply. The floor-4 entrance adds no separate level requirement.

## What changed

| Feature | Vestige Rift setting |
| --- | --- |
| Intended progression | Party endgame content above Bio Labs 3 |
| Regular monsters | Levels 96-98; 80,000-125,000 HP |
| Regular population | 28 of each of seven monster types: **196 total** |
| Regular respawn | **15 seconds** |
| Elites | Level 99; 240,000-330,000 HP |
| MVPs | Level 99; 1,500,000-1,900,000 HP |
| Rewards | Classic-compatible direct drops only |

The imported floor-4 population was 348 regular monsters with five-second respawns. This adaptation reduces crowding and retunes HP, attack, defenses, primary stats and attack timing against our existing Bio Labs 3 baseline. Floors 1-3 retain their existing monsters and spawns.

This is the initial balance profile. Encounter difficulty may be adjusted after feedback from actual level-99 parties.

## Regular monsters

Each type has **28 spawns**. The EXP values below are **base database values before server rates and personal or party modifiers**.

| Monster | ID | Level | HP | ATK range | DEF / MDEF | Base / Job EXP |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Randel | 2221 | 98 | 125,000 | 2,200-2,700 | 55 / 35 | 140,000 / 125,000 |
| Flamel | 2222 | 96 | 105,000 | 1,800-2,300 | 45 / 25 | 120,000 / 115,000 |
| Celia | 2223 | 97 | 80,000 | 650-1,300 | 20 / 60 | 115,000 / 135,000 |
| Chen | 2224 | 98 | 110,000 | 2,000-2,500 | 45 / 35 | 130,000 / 125,000 |
| Gertie | 2225 | 97 | 90,000 | 1,900-2,400 | 30 / 20 | 120,000 / 115,000 |
| Alphoccio | 2226 | 96 | 85,000 | 1,400-2,000 | 30 / 30 | 115,000 / 115,000 |
| Trentini | 2227 | 96 | 80,000 | 1,350-1,950 | 25 / 30 | 115,000 / 115,000 |

## Elites and MVPs

Seven elite types have natural spawns, with a 55-minute base respawn plus up to 50 minutes of variation. One additional random elite escort appears with the MVP.

There is **one random MVP at a time**, selected from the seven types below. Its respawn is **100-130 minutes after death**. It can summon two elite guards; a replacement pair can be called only after both guards die. The separate random escort is removed when the MVP dies.

**Elites, escorts and summoned guards give no EXP or loot.** The MVP itself gives EXP and its configured rewards.

| Type | Elite ID | Elite HP | MVP ID | MVP HP | MVP ATK range |
| --- | ---: | ---: | ---: | ---: | --- |
| Randel | 2228 | 330,000 | 2235 | 1,900,000 | 6,500-8,500 |
| Flamel | 2229 | 300,000 | 2236 | 1,700,000 | 5,000-7,000 |
| Celia | 2230 | 250,000 | 2237 | 1,550,000 | 1,800-3,500 |
| Chen | 2231 | 310,000 | 2238 | 1,800,000 | 6,000-8,000 |
| Gertie | 2232 | 280,000 | 2239 | 1,650,000 | 5,000-7,000 |
| Alphoccio | 2233 | 250,000 | 2240 | 1,500,000 | 4,000-6,000 |
| Trentini | 2234 | 240,000 | 2241 | 1,500,000 | 3,800-5,800 |

### MVP EXP

All figures are before server rates. MVP bonus EXP is an additional Base EXP reward for the MVP winner, subject to the server's MVP EXP rules.

| MVP | Base EXP | Job EXP | MVP bonus EXP |
| --- | ---: | ---: | ---: |
| Randel | 5,000,000 | 1,700,000 | 2,500,000 |
| Flamel | 4,400,000 | 1,550,000 | 2,200,000 |
| Celia | 4,200,000 | 1,650,000 | 2,100,000 |
| Chen | 4,600,000 | 1,600,000 | 2,300,000 |
| Gertie | 4,400,000 | 1,550,000 | 2,200,000 |
| Alphoccio | 4,200,000 | 1,500,000 | 2,100,000 |
| Trentini | 4,200,000 | 1,500,000 | 2,100,000 |

The dungeon uses the normal [weekday/weekend EXP rates](server-rules.md#rates), applicable party and personal bonuses, and [rotating regional EXP bonuses](dungeons.md#hunting-bonuses) when its region is selected. There is no separate permanent Bio4 EXP multiplier.

## Monster skills

| Monster | Main abilities |
| --- | --- |
| Randel | Auto Guard, Holy Cross, Grand Cross, Shield Charge and limited self-healing |
| Flamel | Acid Terror, Demonstration, fire attacks and limited Potion Pitcher |
| Celia | Elemental bolts, Heaven's Drive, Dispell and Land Protector |
| Chen | Finger Offensive, Investigate, Raging Palm Strike and Pneuma |
| Gertie | Envenom, weapon/armor stripping and poison attacks |
| Alphoccio | Musical Strike, Arrow Vulcan and wind attacks |
| Trentini | Throw Arrow, Arrow Vulcan and wind attacks |

Elites and MVPs add a low-frequency stun attack; MVPs can summon and recall their guards. Major attacks use cast times and cooldowns, with interruptible casts. The profiles exclude third-job skills, coma, Power Up/AGI Up multipliers, Asura Strike and Acid Demonstration. Monster Teleport is reserved for unreachable or rude attacks.

## Drops

Renewal equipment, upgrade materials, specialized reward boxes and **all Bio4 regular and MVP cards** have been removed from these monsters. The retained items are listed below. **Bradium and Carnium do not drop.**

| Source | Item | Item ID | Base chance |
| --- | --- | ---: | ---: |
| Randel, Flamel, Celia | Handcuffs | 7345 | 40% |
| Chen, Gertie, Alphoccio, Trentini | Research Chart | 7347 | 40% |
| Randel, Celia, Gertie, Trentini | Elunium | 985 | 2% |
| Flamel, Chen, Alphoccio | Oridecon | 984 | 2% |
| Randel, Flamel, Chen, Gertie, Alphoccio | Old Purple Box | 617 | 0.25% |
| Chen | Berserk | 1814 | 0.1% |
| Flamel MVP | Giant Axe | 1387 | 40% |
| Chen MVP | Chakram | 1285 | 40% |
| Chen MVP | Kaiser Knuckle | 1813 | 40% |
| All seven MVPs | Old Card Album | 616 | 10% |
| All seven MVPs, MVP reward table | Mystical Card Album | 12246 | 5% |
| All seven MVPs, MVP reward table | Old Purple Box | 617 | 50% |

These are base chances. Regular drops use **20x on weekdays / 25x on weekends**; MVP drops use the existing **static 3x** rules and native caps. Other applicable drop modifiers still follow the server rules.

Box and album base chances were reduced to account for those multipliers:

- A regular monster's Old Purple Box chance becomes **5% on weekdays / 6.25% on weekends**, before other modifiers.
- An MVP's Old Card Album chance becomes **30% at 3x**, before other modifiers.
- The Mystical Card Album entry has a **15% adjusted roll at 3x** in the MVP reward table. Native MVP reward selection still applies; it is not an independent ground-drop roll.

### Cards and Mercy

Bio4 has **no direct monster-card drops** in this adaptation. Consequently, its monsters do not provide a [Mercy System](mercy-system.md) card guarantee. Card Albums remain available as the listed item rewards.

The existing [Vestige Coin System](vestige-coins.md) and other global drop systems continue to apply under their own eligibility rules.

## Map restrictions

**Warp Portal, Ice Wall and Loki's Veil are blocked throughout Bio Labs 4**, including while its MVP is dead. The existing restrictions for normal hunting maps also remain in effect.

## Related guides

- [Hunting and instances](dungeons.md)
- [Server rates and rules](server-rules.md)
- [Class changes](class-changes.md)
- [Kill Count](kill-count.md)
- [Advanced autoloot](autoloot.md)
