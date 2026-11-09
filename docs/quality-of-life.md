---
icon: material/bag-personal-outline
---

# Quality of life

Updated: **November 9, 2026**.

## Increased sitting recovery

After **seven seconds without attacking or taking damage**, a sitting character recovers **3% of Max HP and Max SP every 1.5 seconds**. An empty bar takes approximately 51 seconds of eligible pulses to fill, plus the initial combat delay. Standing retains ordinary recovery.

Eligible percentage pulses replace ordinary natural/skill sitting ticks rather than stacking with them. Fractional recovery carries between pulses. Attacks, including misses, offensive damaging skills and received damage restart the combat delay; paying a skill's normal resource cost alone does not.

Overweight disables the increase. Normal recovery restrictions are respected separately for HP and SP, including death, hidden states, disabling statuses and blocked recovery resources. Asura Strike blocks the increased recovery for five minutes during the session; actual relogging clears that session penalty and the native SP penalty as described in [class changes](class-changes.md).

Super Novice Doridori doubles normal recovery, not these percentage pulses.

## RODEX mail

[Attendance rewards](attendance.md) arrive through RODEX **after you claim them in Attendance Check**. Logging in or opening the attendance window alone does not send a reward. Attendance claims are limited to one per account per Philippine calendar day.

Mail can be used from ordinary towns and fields under the normal map and access restrictions.

| Attached item stacks | Postage |
| --- | ---: |
| 1 | 2,500z |
| 2 | 5,000z |
| 3 | 7,500z |
| 4 | 10,000z |
| 5 | 10,000z |

- Maximum five attached stacks and **2,000 total item weight**.
- Items must pass both trade and mail restrictions. Bound and rental items cannot be attached.
- Native inventory capacity, receiving-weight checks, 2% attached-Zeny tax and daily 100-mail limit remain.
- Mail expires **14 days after sending**, including unclaimed items and Zeny. There is no extra return-to-sender window.
- Receiving has no new postage charge.

During WoE, mail is blocked **only inside castles whose relevant WoE session is active**. Ordinary maps remain usable. FE and SE castles follow their respective sessions; custom castles without a registered siege type follow either active session. Castle mail is available outside its active siege. An already-open mailbox does not bypass the restriction.

## Party buff letters

Active buffs appear before online party members' names, in this fixed order:

| Marker | Buff |
| --- | --- |
| B | Blessing |
| A | Increase AGI |
| F | Full Chemical Protection coverage |
| S | Soul Link |
| U | Assumptio |
| + | Devotion on the protected recipient |

Example: `[BAFSU+] Infinite`.

Updates are triggered by buff application, expiry/removal and relevant equipment changes, without waiting for the fallback party timer. Ordinary network/client latency still applies.

`F` requires chemical-protection coverage for all currently equipped applicable slots. A two-handed weapon user does not need a shield coating. Equivalent individual coatings also count; partial coverage does not show `F`.

These labels do not rename the character. Long names may be shortened in the bounded party-menu field; use the full character name if a shortened label is ambiguous.

## Bulk purchases and personal storage

Buying **exactly 30,000 units of one stackable item** at a standard Zeny NPC shop opens a confirmation. Confirming sends the items directly to **account Main Storage**, using the normal price and Merchant discount. Carried inventory weight does not block that direct-storage purchase.

This covers ordinary SHOP NPCs and standard Zeny traders, including the tool dealers and Gunslinger Supplies. Player vending and special-currency, barter, market and attached custom purchase handlers retain their original rules. A bulk order must contain only one item type; smaller purchases still go to inventory.

Cancelling, closing or timing out the confirmation does not purchase anything. Confirmation rechecks the quote, shop access, price, balance and storage capacity. Failed insertion refunds the payment; a quote cannot be replayed.

Personal storage supports **ten stacks per stackable item ID**, each up to **30,000 units**, for a normal maximum of **300,000 units**. Partial compatible stacks fill first. Variants share the ten-stack limit but incompatible variants do not merge. Item-specific smaller stack limits, storage slots and item/bound restrictions still apply. Guild storage retains its normal rules.


## Sensible teleporting

Random Fly Wing and Teleport destinations reject NPC touch areas, active player Warp Portal cells and impassable cells. If no safe destination is found, the teleport fails instead of using an unsafe fallback. Deliberate return/save-point warps retain their normal behavior.

## Rotating EXP regions

Two **regions or dungeon groups**, rather than two individual maps, receive independently selected **20-30% Base and Job kill EXP bonuses**. They rotate together every **48-72 hours**.

Use `@bonusmaps` to see the active groups, eligible maps, percentages and next rotation in Philippine time. Eligible maps need natural spawns; towns, instances, PvP, castles/WoE, Battlegrounds and maps blocking the applicable EXP are excluded.

The bonus multiplies the active rates:

| Base rate | With a 20-30% region bonus |
| --- | --- |
| Weekday 20x | 24x-26x |
| Weekend 25x | 30x-32.5x |

Quest EXP, item/card drops and the separate native MVP bonus award are unaffected. Selections and deadlines persist through normal restarts; overdue selections rotate on startup.

## Summon timeout

Player item-generated monsters, including Dead Branch and Bloody Branch summons, and eligible Abracadabra Class Change/Monocell transformations have a **maximum one-hour lifetime**. Minions inherit the original deadline; transformations do not extend it. Shorter native lifetimes still apply.

Timeout removes them with **no EXP, loot or kill credit**. Normal kills before timeout retain their rewards. Ordinary natural/quest spawns, guardians and protected event-bound monsters retain their normal lifecycle.

## Rebirth weight allowance

Valkyrie permits up to **500 displayed carried weight** for rebirth. Existing Zeny, level/class, skill-point, cart, falcon and mount requirements remain.

## Same-stat food stacking

Foods of the same stat coexist by potency. Only the strongest surviving tier contributes its bonus. Lower-tier timers **continue counting down while suppressed**; they do not pause. When the strongest expires, the next strongest unexpired tier resumes with its remaining time.

Each newly consumed tier starts at its full scripted duration; consuming the same tier from the same source refreshes it. Normal and cash foods are compared together. Different stats operate independently. Only the effective food icon/countdown is shown. Saved tiers follow native offline-timer and source-specific removal rules.

Example: use +3 STR for 20 minutes, wait two minutes, then use +10 STR for five minutes. After the +10 ends, the +3 resumes for its remaining 13 minutes.

## Incubus pet

At **Loyal intimacy (900+)**, Incubus grants **+3% Max SP** and a **5% chance to recover 5% of physical weapon damage as SP**. SP leech is random and requires missing SP to observe recovery. Other pet settings are inherited from the classic definition.

## Respawn fallback

- Returning to the last save point repairs an unavailable/disabled saved map to the configured Prontera fallback, rather than reviving in place due to that invalid map. Valid saved points and Battleground respawns retain their normal rules.


## Hourly rewards

Earn **10 account-wide points per hour online**, up to a **300-point balance**. Click the top-right timer to convert complete **120-point bundles into Gold Coins**; spend them at the Gold Point Manager in Prontera, **144,200**. The costume shop keeps your character stationary until it is closed.

See [Hourly rewards](hourly-rewards.md) for saved partial-hour progress, inventory requirements, coin restrictions and the current sample costume.

## Convenient dealers

**43 existing Tool Dealers** now share the 35-item Enhanced Tool catalogue, and **8 existing Pet Groomers** share the 30-item Pet catalogue at their original locations. Jackie and Gunslinger Supplies remain dedicated Prontera shops.

See [Convenient dealers](dealers.md) for prices, custom kunai elements, NPC resale values and the complete location directory.
