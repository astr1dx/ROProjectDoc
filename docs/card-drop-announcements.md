# Card Drop Announcements

Updated: **November 10, 2026**.

When a player successfully receives a monster card, a short yellow message announces the find to online players who have Drop announcements enabled:

> Tubbs has obtained their 1st [Lude Card] on the 559th kill.

## Who receives credit?

The announcement names the **actual card recipient**, after the card reaches their inventory successfully. Normal pickup, autoloot and pet delivery all use the recipient's name. A card collected by your pet is credited to **you**.

A card left on the ground does not announce yet. Failed inventory delivery does not announce or increase the received-copy count. Trades, storage withdrawals and NPC rewards are not monster-card receipts.

## Copy number and kill count

| Part of the message | Meaning |
| --- | --- |
| `their 1st [Lude Card]` | This character's recorded received-copy number for this specific card. It is saved per character and card. |
| `on the 559th kill` | The recorded count for that monster on the kill that generated the card, when the recipient is also credited with that kill. |

Cards distributed through **party loot sharing** omit the kill clause, even if the recipient also participated in the kill:

> Tubbs has obtained their 2nd [Lude Card].

Cards picked up from somebody else's kill also omit the kill clause. Picking up a card from your own credited kill can retain it. Counts use recorded history; unrecorded past card receipts are not reconstructed.

Kills made by your **homunculus, mercenary, elemental or pet** count toward your recorded monster-kill total. See [Kill Count](kill-count.md) for tracking and card-drop statistics.

## Public chat and visibility

Card announcements follow the **Public chat filter**. A chat tab with Public messages disabled excludes them. Each receipt produces one Public event, without a separate duplicate system-announcement entry.

Choose **`@settings` > Announcement Config > Drop** to turn Drop announcements On or Off for your account. Drop announcements are **On by default**. Your choice changes your own view; it does not prevent another player's announcement or change drop rates.

Long names and narrow chat windows can still cause normal text wrapping; the shortened format avoids the earlier verbose wording.

## Card artwork and rare-drop notices

**Card Drop Illustration** is a separate option in **`@settings`**. Supported card artwork appears at the bottom right for five seconds, for the recipient only. Turning off Drop announcements does not automatically turn off the illustration.

**Show Rare Drops** controls a separate personal notice based on the original database drop chance. It does not replace the public card announcement or alter drop rates.

See [Personal settings](personal-settings.md#drop-notices-and-card-artwork) for both options, and [Card exchange](card-exchange.md) for exchanging unwanted cards.

!!! note "Verification"
    Loot attribution, copy numbering, shared-loot wording and per-viewer visibility have automated coverage. Final in-game confirmation of the new message's appearance and chat-tab filtering is pending.
