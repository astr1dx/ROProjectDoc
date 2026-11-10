# Fast storage

Updated: **November 10, 2026**.

Keep named lists for replenishing supplies and unloading loot. Lists save automatically **per character** and remain available after login. Restock and Quick Store each support **40 independent groups of 40 distinct item IDs**, with **one active group of each type**.

| Feature | Configuration menu | Action |
| --- | --- | --- |
| Restock | `@settings` > Restock Supplies, or `@restockconfig` | `@restock` fills inventory up to your saved targets |
| Quick Store | `@settings` > Quick Store, or `@qstoreconfig` | `@qstore` stores all eligible inventory units of listed items |

Both menus also offer **Run Active List**. Use `@ii <item name or ID>` to find item IDs.

## Restock: refill target quantities

1. Open **Restock Supplies** in `@settings`, or type `@restockconfig`.
2. Choose **Add Restock Group**, then **Add Item**.
3. Enter the item ID and the **target inventory total**, from **1 to 30,000**.
4. Add any other supplies, rename the group if desired, and choose **Enable Group**.
5. In a town, open **Main Storage** through Kafra or a storage item and use `@restock`.

**Example:** a target of 100 Red Potions (#501), with 25 already carried, withdraws up to 75 from available storage stock. Restock does not add 100 on top of what you already carry, and it never deposits an excess.

Select an item in the group to **Set Quantity** or **Remove Item**. Stored stock, inventory capacity and weight may prevent a target from being filled completely.

## Quick Store: store all listed items

Quick Store lists contain **item IDs only**. There is **no quantity, deposit-count or Keep setting**.

1. Open **Quick Store** in `@settings`, or type `@qstoreconfig`.
2. Choose **Add Quick Store Group**, then **Add Item**.
3. Enter **909** to add Jellopy. The item saves immediately without asking for a quantity.
4. Add other item IDs as needed and choose **Enable Group**.
5. In a town, open **Main Storage** and use `@qstore`.

**Every eligible Jellopy in inventory moves to storage**, subject to normal storage capacity and item restrictions. Items outside the active list stay in inventory. Menu entries show **Store all**; selecting one lets you remove it from the list.

Existing Quick Store groups keep their names, items and active selection. Any previously saved Keep amounts are discarded; every listed item now uses the all-units behavior.

## Where transfers work

- Be in a **town**, including **Midgard Expedition Camp, Manuk and Splendide**. Market Street also qualifies.
- Have **Main Storage already open**, through Kafra or an appropriate storage item. These features never open storage remotely.
- Guild or other storage cannot substitute for Main Storage.
- Finish trades, vending, buying stores and other NPC interactions first. Dead characters cannot transfer items.

Configuration menus can be used outside towns when normal commands are available; the location and open-storage requirements apply to transfers.

## Eligible items and protections

Consumables, stackable miscellaneous items, loose cards and **loose ammunition** (including arrows, bullets and kunai) are supported. Equipment, equipped items, favorites and rental items are skipped. Item properties, including brewed-item details, remain intact. Normal bound-item and storage restrictions still apply.

Storage slots, item-specific stack limits and the [ten-stack personal-storage limit](quality-of-life.md#bulk-purchases-and-personal-storage) still apply. Items that cannot be transferred remain at their source; the completion message reports the units actually moved.

## Weight limits

Restock stays **strictly below 90% carried weight**. It also obeys any lower **Storage Withdrawal Weight Limit** chosen in `@settings`. For example, a saved 70% limit caps restocking at 70%; a saved 100% limit still leaves Restock below 90%.

Quick Store can be used **while overweight** so you can unload inventory. It does not increase storage capacity or relax item restrictions.

## Managing groups

Rename, enable, remove items or delete a group through its menu. Enabling another group of the same type replaces the previous active choice. Restock and Quick Store selections are independent and can both be enabled. Deleting a group clears only its configuration, not any items in inventory or storage. Recreating a group starts with an empty list.
