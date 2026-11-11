# Homunculus and Pet Commands

Updated: **November 11, 2026**.

These commands are available to **all regular players**, including new accounts. Your homunculus or pet must be active for its commands to work.

| Command | What it does |
| --- | --- |
| `@hominfo` | Shows your active homunculus's current combat stats, HP/SP, hunger and intimacy. |
| `@homstats` | Shows its growth stats alongside the possible minimum and maximum values for its level and evolution. |
| `@homtalk <message>` | Makes your homunculus say a message above its head. |
| `@pettalk <message>` | Makes your pet say a message above its head, or display a supported emote. |

## Check your homunculus

Type **`@hominfo`** to see:

- Current and maximum **HP and SP**.
- **ATK** and the **MATK range**.
- **Hunger** and **intimacy**.
- Current **STR, AGI, VIT, INT, DEX and LUK**.

Type **`@homstats`** to see the homunculus's level and type, maximum HP/SP, and permanent growth stats with their possible ranges. Use this to compare its growth; `@hominfo` reports its current combat stats instead. Neither command changes your homunculus.

For the homunculus roster, Bioethics and other Alchemist changes, see [Class Changes](class-changes.md#alchemist-creator).

## Speak through your companion

With your homunculus active:

```text
@homtalk Hello everyone!
```

With your pet active:

```text
@pettalk Ready for another hunt!
```

Nearby players see the message from the companion, prefixed by its name. Supported pet emotes can also be used, for example:

```text
@pettalk /ok
```

Using a talk command without a message shows its usage. If the required companion is unavailable, the command reports that instead.

## Chat rules and logging

Companion speech is **logged as the owner's public chat**, with the companion identified in the record. Supported pet emotes are also logged under the owner.

Speaking through a companion does **not bypass a player chat mute**. The normal configured chat-delay checks still apply, and pet emotes retain their normal cooldown. A rejected message is not recorded as successfully sent companion speech.

## Pet visibility and muting

Configure these preferences only through **`@settings`**:

| Setting | Effect on companion messages |
| --- | --- |
| **Mute Pets** | Hides pet speech and pet emotes on your screen. |
| **Hide Pets** | A pet hidden by your chosen visibility mode also has its speech and emotes hidden. |

These are personal viewing preferences. Other players keep their own choices, and the pet continues to function normally. Hidden or muted pet speech is still logged under its owner.

Pet settings do **not** suppress player chat or homunculus speech. See [Personal Settings](personal-settings.md#pets-and-song-music) for the visibility modes and other preferences.

## Verification

Ordinary-player tests covered all four commands, overhead messages, owner-attributed logging, chat-mute restrictions, pet emotes and per-viewer filtering. The integrated server suite passed **3,174 checks**, followed by production command and logging checks. Rendered in-game confirmation of this update is still pending.
