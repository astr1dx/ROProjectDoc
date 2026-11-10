# Advanced autoloot

Updated: **November 10, 2026**.

Choose **`@settings` > Autoloot**, or type **`@lootconfig`** to open the same menu. Changes take effect immediately, save automatically and return on login. Autoloot preferences and lists belong to **each character**.

## Main Autoloot

Main Autoloot starts **Off**, with a saved threshold of **100%**. Enable it in the menu and choose **Set Drop Threshold** to enter **0-100%**, with up to two decimal places.

The threshold uses the monster's **original database drop chance**, before server rates. For example, **0.05%** selects eligible drops with an original chance of 0.05% or less. Weekday/weekend rates and personal bonuses do not change the chance used by this filter. A 0% threshold selects nothing through Main Autoloot.

### Ignore unwanted items

Open **Main Autoloot > Ignore Items > Add Item** and enter an item ID. The ignore list supports **100 distinct IDs**. You can view, remove or clear entries in the same menu.

**Example: loot everything except Jellopy**

1. Enable Main Autoloot and set its threshold to **100%**.
2. Add **Jellopy, item ID 909**, to Ignore Items.
3. Disable any active loot group containing Jellopy, or remove Jellopy from that group.
4. Hunt normally. Eligible unignored drops are collected automatically; ignored Jellopy stays on the ground and can still be picked up manually.

Ignoring an item never removes copies already in your inventory.

## Custom loot groups

Keep separate farming lists, with **up to 40 groups and 100 distinct item IDs per group**. Only **one group** can be active at a time; enabling another switches the active group.

1. Choose **Add Autoloot Group**, or open an existing group.
2. Use **Rename Group** to give it a recognizable name.
3. Open **Manage Items > Add Item** and enter the item ID. Use the same menu to view or remove entries.
4. Choose **Enable Group**.

Use `@ii <item name or ID>` to look up item IDs. Group names support up to 32 bytes; avoid colons, color codes and leading/trailing spaces.

An active group adds its listed items to your selection **regardless of the percentage threshold**. It also works while Main Autoloot is Off. Deleting a group clears its list and disables it if active; other groups and inventory items remain intact.

## How the filters combine

| Item selection | Result |
| --- | --- |
| In the active group | Selected, even when ignored or Main Autoloot is Off |
| Not in the active group, but ignored | Not selected by Main Autoloot |
| Not ignored, with Main Autoloot On and original chance at or below its threshold | Selected |
| No matching rule | Normal ground drop |

The active group **adds** items to Main Autoloot. To collect **only** your group's items, turn Main Autoloot Off and enable the group you want.

## Restrictions and related settings

Normal map, idle, distance, homunculus and party-loot rules still apply, as do inventory capacity and weight checks. Selecting an item does not bypass these rules or create items. If automatic delivery cannot complete, the normal ground-drop path remains available.

[Show Rare Drops and Card Drop Illustration](personal-settings.md#drop-notices-and-card-artwork) control notifications for successful receipts. They do not configure which items are collected. Use [Quick Store](fast-storage.md#quick-store-store-all-listed-items) later to deposit selected inventory items into open Main Storage.
