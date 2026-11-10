# Personal settings

Updated: **November 10, 2026**.

Type **`@settings`** to choose how pets, songs, messages and other information appear on your screen. Preferences are saved automatically and restored when you log in. The menu and its commands update the same settings.

Most preferences are **shared across your account**, including channel visibility. Your **storage withdrawal weight limit and restock list are saved per character**.

## Default chat channels

Every existing and new player automatically joins these channels when entering the game:

| Channel | Use | Message color |
| --- | --- | --- |
| `#main` | General discussion | Orange |
| `#recruit` | Party and guild recruitment | Blue |
| `#market` | Buying and selling | Red |

To send a message, enter the channel name in the whisper recipient box, then type your message. For example, set the recipient to `#recruit` to look for a party.

Open **`@settings` > Channel Config** to turn a channel On or Off for your account. A saved Off choice is respected on later logins; automatic joining does not reset it. These preferences affect your own view, not other players.

```text
@channelvisibility main 0
@channelvisibility main 1
@channelvisibility recruit 1
@channelvisibility market 1
```

`0` hides the selected channel; `1` enables it and joins it, subject to normal channel access. `#map` and the guild-alliance channel retain their existing map/guild behavior.

## Pets and song music

| Setting | Command | Effect |
| --- | --- | --- |
| Hide Pets | `@hidepet 0` | Show all pets. This is the default. |
| Hide Pets | `@hidepet 1` | Show only your pet. |
| Hide Pets | `@hidepet 2` | Show other players' pets, hiding yours. |
| Hide Pets | `@hidepet 3` | Hide every pet on your screen. |
| Mute Pets | `@mutepets 0/1` | Hide pet talk and emotes for you. Pets still function normally. |
| Mute Songs | `@mutesongs 0/1` | Mute Bard/Dancer song music while retaining musical notes and ground effects. Other sound effects remain available. |

For On/Off commands, `1` enables the named option and `0` disables it. `@mutepet` is an alias for `@mutepets`. With no value, either pet-muting command and `@mutesongs` toggle their setting. `@hidepet` with no value shows all pets.

Hidden pets do not chatter on your screen. Visible pets remain audible unless you also enable Mute Pets. Mute Pets and Mute Songs are Off by default.

A song already playing may finish after you change its setting. The setting filters subsequent song playback; stop the current performance and cast again to check it. Turning Mute Songs Off restores song audio.

## Drop notices and card artwork

### Show Rare Drops

`@showrare 1-100` sets the maximum **original database drop chance**, in percent, for a personal loot notice. For example, `@showrare 1` reports successful monster drops with a base chance of 1% or less.

Server rates, weekend rates and personal drop bonuses do not change which base chance is compared. This option reports items you actually receive; it does not change drop rates. `@showrare 0`, or the command with no value, disables these notices. They are Off by default.

### Card Drop Illustration

Card Drop Illustration is **On by default**. When you receive a supported monster card through the tracked loot system, its artwork appears at the **bottom right for five seconds**, for you only. Use **`@cardillustration 0/1`** or the settings menu to change it; no value toggles it.

Normal pickup, autoloot and pet loot are credited to the character who actually receives the card. Card announcements name that recipient and show a per-character copy count. A kill count is included when that recipient is also credited with the kill; shared or picked-up loot does not claim somebody else's kill count. Counters track receipts and kills since tracking was introduced, rather than reconstructing historical totals.

Ordinary trades, NPC rewards and storage withdrawals do not trigger monster-drop artwork. Artwork is skipped when an NPC dialog is active or an illustration is unavailable. A later NPC illustration takes precedence over the timed card image.

See [Card exchange](card-exchange.md) for exchanging unwanted cards; exchange points are separate from these display preferences.

## Information and visibility

| Setting | Command | Behavior | Default |
| --- | --- | --- | --- |
| Show Experience | `@showexp` | Toggle gained-EXP messages. | On |
| Show Guildmates HP | `@guildhp 0/1` | Show nearby guildmates' HP bars. Turning it Off retains party and Battleground HP bars. | On |
| Previous Teleport Position | `@teleposition 0/1` | Mark your departure cell on the minimap after a teleport within the same map. Cross-map travel does not create this marker. | Off |
| Direct Message Warning | `@dmwarning 0/1` | Play a sound and show a personal on-screen notice for an accepted whisper. Alerts are limited to one per two seconds; server notices and channel messages do not trigger them. | Off |
| Time Mode | `@timemode 0/1/2` | `0`: server cycle; `1`: always day; `2`: always night. Only your view changes. | Server cycle |
| Hide Headgear and Costumes during WoE | `@woevisuals 0/1` | Hide everyone's headgear, costume headgear and robe visuals, including your own, on castle maps during their active WoE session. Equipment and bonuses remain intact. | Off |
| Status Color Effect | Settings menu | Show or hide the existing status aura effect. | Show |

The On/Off commands in this table toggle when used without a value. `@timemode` without a value cycles its three modes. Existing saved choices take precedence over defaults.

## Announcement configuration

Choose individual categories under **`@settings` > Announcement Config**:

| Category | Command keyword |
| --- | --- |
| Welcome | `welcome` |
| Drop | `drop` |
| Battlegrounds | `bg` |
| Kill | `kill` |
| Community News | `news` |
| MVP | `mvp` |
| Event | `event` |
| PvP Arena | `arena` |

For example, `@announcements drop 0` hides drop announcements for you, and `@announcements drop 1` shows them again. All categories are visible by default. These choices control existing announcements; they do not activate an otherwise unavailable event or announcement system. General announcements use Event, while rotating EXP-region notices use Community News.

**High-contrast yellow** recolors server announcements for easier reading. Use `@colorblind 1` to enable it, `@colorblind 0` to disable it, or `@colorblind` to toggle. It is Off by default.

## Storage weight limit and restock

Set **`@storageweight 1-100`** to choose the maximum carried-weight percentage after a withdrawal from personal storage. The default is **100%**, saved separately for each character. This does not increase carrying capacity or change overweight recovery restrictions.

To save and refill supplies:

1. Carry the loose consumable and ammunition quantities you want to keep stocked.
2. Type **`@restock save`** to save up to **64 item types**, with a target of up to **30,000 units per type**.
3. Open **Main Storage**, then type **`@restock`** to refill missing quantities from its available items.

You can also save or refill through **`@settings` > Restock Supplies**. Saving again replaces the saved supply list.

Restocking requires Main Storage to be open and respects your withdrawal weight limit, carrying capacity and inventory space. It takes available stock only, skips unavailable supplies and never deposits excess items. Equipped, bound, rental, favorite and crafted/brewed item instances are excluded from the saved supply list.

See [bulk purchases and storage](quality-of-life.md#bulk-purchases-and-personal-storage) for the separate large-purchase feature.
