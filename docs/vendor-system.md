# Vendor system

Updated: **November 10, 2026**.

Find shops, buy and sell from towns, or keep a merchant trading while you play another character on the same account.

!!! info "Start here"
    Enter Market Street through **Merchants Warp** at `/navi prontera 139/171`. Open a shop, then use **`@at2`** to return directly to character selection while the shop stays open.

## Market Street

Market Street uses map **`prt_mk`**, with arrival at **162,142**. It has numbered vending spots, a Vending Helper, a Spot Picker and personal-storage access.

| NPC / destination | Navigation | Service |
| --- | --- | --- |
| Merchants Warp | `/navi prontera 139/171` | Enter Market Street |
| Market center | `/navi prt_mk 162/142` | Arrival and `@market` destination |
| Vending Helper | `/navi prt_mk 158/142` | Nearest/random/numbered spots, import instructions and return to Prontera |
| Spot Picker | `/navi prt_mk 166/142` | Choose the closest free spot, a random one or a spot number |
| Market Kafra | `/navi prt_mk 162/138` | Open personal storage |

The server generates **4,264 walkable vending spots** on a four-cell grid and keeps the central crossing lanes clear. Preparing a shop in Market Street selects the nearest available spot if you are not already on one. Nearby occupied spots are rejected.

Use `@vendorspot` for the closest free spot, `@vendorspot random` for a random one, or `@vendorspot NUMBER` to choose a numbered spot. Your chosen number and the total are displayed after selection. These commands work inside Market Street.

`@market` returns you to the market center **from within Market Street only**. Enter from Prontera through Merchants Warp; use the Vending Helper to return to Prontera.

Characters without an open shop are returned to Prontera after **five minutes**. Skills cannot be used while a selling or buying store is open. Market Street is a town with branch use and death penalties disabled.

## Where shops are allowed

Selling and buying stores may open only on:

| Area | Map |
| --- | --- |
| Market Street | `prt_mk` |
| Payon | `payon` |
| Morocc | `morocc` |
| Alberta | `alberta` |
| Comodo | `comodo` |

Dungeons and other maps are excluded. Ordinary restricted-cell and trade rules still apply within an allowed map.

## Find a selling or buying shop

| Command | Results | Price order |
| --- | --- | --- |
| `@ws ITEM` / `@whosell ITEM` | Selling shops in the search window | Cheapest first |
| `@wb ITEM` / `@whobuy ITEM` | Buying shops in the search window | Highest offer first |
| `@ws2 ITEM` / `@whosell2 ITEM` | Selling-shop information in chat | Cheapest first |
| `@wb2 ITEM` / `@whobuy2 ITEM` | Buying-shop information in chat | Highest offer first |

Both the short and long command names are available to **ordinary players**, including new accounts. They use the same search behavior and filters.

Use an **item ID or part of its name**. Text results include the item, refine level, quantity, price, shop owner, shop name and navigation coordinates. The text commands do not open a search window.

### Filters and examples

```text
@ws 504
@ws white potion
@ws +4 2302 0-500000
@wb red potion 45-60
@ws2 gold
@wb2 969
```

The third example finds Cotton Shirt [1] at **+4 or higher**, costing up to **500,000z**. The fourth finds Red Potion buying offers between **45z and 60z**. Enter `+REFINE` before the item and `MIN-MAX` after it. Opening `@ws` or `@wb` without an item opens the ordinary search interface.

The long names accept the same arguments:

```text
@whosell +7 knife 1000-2000
@whosell2 white potion
@whobuy red herb 65-90
@whobuy2 909
```

Use `@wb` or `@whobuy` for buying offers; `@ws` and `@whosell` search selling shops.

### Remote trading and result limits

**Remote purchases and sales through search results are available only in towns**, including Market Street. Outside towns, use the text results and navigation to reach a shop. Normal stock, Zeny, capacity, item and trade checks still apply.

Allow **two seconds** between command searches. Window results are bounded to **200 matches**, displayed ten per page; text results show up to 50. Narrow the item name, price range or refine filter when there are more matches. Searches with no matches clear previous result rows.

The existing **`#trade`** channel is also available for player advertisements and requests.

## Open a buying store

Any class can open a buying store with the appropriate license. You must already possess the requested item, have enough Zeny and carrying capacity, and use an allowed shop location. Equipment and crafted/brewed item instances are excluded; tradeable consumables and permitted Etc-tab categories are supported.

| Character / service | NPC | Requirements and price |
| --- | --- | --- |
| Non-Merchant license | Black Marketeer, `/navi morocc 45/108` | 500z per license; up to 100 per purchase |
| Merchant skill unlock | Purchasing Team, `/navi alberta_in 58/52` | Vending Level 1; 10,000z registration; grants Open Buying Store and five starter licenses |
| Merchant replacement licenses | Same Purchasing Team | 200z per license; up to 100 per purchase |

The Purchasing Team is inside the Merchant Guild, reached from Alberta near **35,42**.

A license is consumed **only when the buying store successfully opens**. Canceling setup does not use one. Restoring an already-open offline buying store does not charge a second license; importing a closed shop normally requires a license again.

## Price limits

Prices are checked when a shop opens, including restored and imported shops.

| Shop / item | Rule |
| --- | --- |
| Ordinary item sold by a standard Zeny NPC | A vending price above the lowest available NPC catalogue price is lowered to that price |
| Refined, carded, named, random-option or individually serialized item | Exempt from the ordinary vending price cap |
| Buying-store offer | An offer below the item's NPC resale value is raised to that value |

You receive a message for each adjusted price. The vending cap uses the actual loaded catalogues, including our [customized dealers](dealers.md), rather than assuming every shop uses the base item-database Buy price.

The existing **2% vending tax** remains. Transactions that would exceed a seller's Zeny limit are refused rather than discarding the excess.

## One listing per stackable item

Each **stackable item ID may appear only once across an account's active selling and buying shops**, including offline shops. Another character on the account cannot create a second listing for that ID. The same stackable item cannot be repeated in one shop either.

This is an **account-based restriction**. Hardware-ID enforcement is not enabled, and IP addresses are not used as a substitute.

## Autotrade 2: keep playing on the same account

1. Open a selling or buying shop in an allowed location, with its items and prices listed.
2. Type **`@at2`** or **`@autotrade2`**.
3. You should return **directly to character selection** while the shop stays open.
4. Choose another character on the same account and continue playing.

Characters vending through `@at2` show a **`[V]` marker** in character selection and count as offline. Multiple characters on an account can keep shops open, subject to the one-listing-per-item rule.

To close a vendor, **log into that character**. Its shop closes and its latest saved items and Zeny are loaded before you enter the map. Other vendors on the account stay open. Offline selling and buying shops are saved for restoration after a normal server restart.

The existing `@autotrade` / `@at` command remains available. Use `@at2` for the explicit return-to-character-selection workflow.

!!! note "Expected behavior"
    A successful `@at2` should not require a disconnect, a login retry or a second attempt. Chat and commands should work immediately after selecting a character marked `[V]`.

## Import the last shop

Use **`@importshop`** to reopen the most recent shop saved for the current character. It restores the shop name, remaining item listings and prices without entering them all again.

- History belongs to the **character**, not the entire account.
- Items that were sold, moved or no longer match the saved item are omitted.
- Import does not create replacement stock.
- Current map, skills/cart, license, Zeny, capacity, pricing and duplicate-listing rules are checked again.
- Close an existing shop or dialog before importing.

## Sales recap

Closing a vending shop displays the quantities sold, actual Zeny credited after tax and remaining cart contents. **`@vendrecap`** shows the retained sales quantities and Zeny earned for the character's most recent vending shop. The sales recap is retained for an `@at2` shop across restoration.

The current recap is a totals summary. A **View All** menu with individual buyers, sale timestamps and shop opening/closing times is not implemented.

## November 10 search aliases

Added **`@whosell`**, **`@whosell2`**, **`@whobuy`** and **`@whobuy2`** as the long forms of `@ws`, `@ws2`, `@wb` and `@wb2`. Ordinary-player checks passed for all eight names, including selling/buying routes and requests using item names, IDs, refine and price filters. Existing cooldowns and town-only remote trading still apply.

## November 9 corrections and verification

- Corrected search-result handling so `@ws` and `@wb` safely display the first and subsequent pages. Empty searches clear old rows, the Next option reflects remaining results, and requests past the final page do not return invalid rows.
- Corrected the disconnect that could occur when issuing commands immediately after logging into a `[V]` character. The marker is recognized for that character without changing its actual name.
- Successful `@at2` no longer reports a command-failure message.

**Confirmed in-game:** Market Street and its NPCs; `@at2` and same-account character switching; and a successful first attempt after logging into a merchant marked `[V]`.

Connected-session automated checks cover same-account vendors, offline transactions/restoration, search windows and shop clicks, single/multiple/empty/exhausted result pages, buying-store searches, shop import, name validation and the return to character selection. Separate player confirmation of searching after the latest correction has not yet been recorded.

## Not enabled

Hardware-ID enforcement and a website merchant-search page are deferred. Use the in-game search commands for the current implementation.
