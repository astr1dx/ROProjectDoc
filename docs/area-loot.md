# Area Loot

Pick up nearby ground items with one click. Area Loot is **Off by default** and saved **per character**.

## Turn it On or Off

Open **`@settings` > Area Loot (3x3)**. The **`@arealoot`** command toggles the same setting; `@arealoot on` and `@arealoot off` set it explicitly.

## How pickup works

Click an item within normal pickup range. If that pickup succeeds, Area Loot also tries the items in the **3x3 square centered on the clicked item**, including the diagonal cells.

The square stays centered on the original item. Extra pickups do not start another sweep, so the effect never chains across the map.

## Normal pickup restrictions apply

- Loot ownership and party-sharing rules still apply to each item.
- Protected items and items you cannot carry remain on the ground.
- Your weight, inventory space and item-stack limits still apply.
- If the first clicked item cannot be collected, the area pickup does not begin.
- The sweep stops if you die, change maps or leave the pickup area.

## Area Loot versus Autoloot

**Area Loot is manual ground pickup.** It does not collect newly dropped items until you click something. [Advanced Autoloot](autoloot.md) automatically collects selected monster drops instead.

Autoloot ignore lists and chance thresholds do not block manual pickup. For example, Jellopy ignored by Autoloot can still be collected through Area Loot when ordinary pickup rules allow it.
