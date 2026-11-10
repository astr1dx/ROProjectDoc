# Personal settings

Updated: **November 10, 2026**.

Type **`@settings`** to choose how pets, songs, messages and other information appear on your screen. Preferences are saved automatically and restored when you log in. Configure these preferences only through this menu.

Most preferences are **shared across your account**, including channel visibility. Your **storage withdrawal weight limit, autoloot configuration, Restock groups and Quick Store groups are saved per character**.

## Default chat channels

Every existing and new player automatically joins these channels when entering the game:

| Channel | Use | Message color |
| --- | --- | --- |
| `#main` | General discussion | Orange |
| `#recruit` | Party and guild recruitment | Blue |
| `#market` | Buying and selling | Red |

To send a message, enter the channel name in the whisper recipient box, then type your message. For example, set the recipient to `#recruit` to look for a party.

Open **`@settings` > Channel Config** to turn a channel On or Off for your account. A saved Off choice is respected on later logins; automatic joining does not reset it. These preferences affect your own view, not other players.

Turning a channel On joins it, subject to normal channel access. `#map` and the guild-alliance channel retain their existing map/guild behavior.

## Pets and song music

Open **`@settings`** and select the relevant option:

| Setting | Menu choice or effect |
| --- | --- |
| Hide Pets | Choose Show all pets, Only show my pet, Only show other pets, or Hide all pets. Show all is the default. |
| Mute Pets | Turn pet talk and emotes On or Off for your view. Pets still function normally. |
| Mute Songs | Turn song muting On or Off. Musical notes, ground effects and other sound effects remain available. |

Hidden pets do not chatter on your screen. Visible pets remain audible unless you also enable Mute Pets. Mute Pets and Mute Songs are Off by default.

A song already playing may finish after you change its setting. The setting filters subsequent song playback; stop the current performance and cast again to check it. Turning Mute Songs Off restores song audio.

## Drop notices and card artwork

### Show Rare Drops

Select **Show Rare Drops** in the menu and enter a threshold from **1 to 100%**. This sets the maximum **original database drop chance** for a personal loot notice. For example, 1% reports successful monster drops with a base chance of 1% or less.

Server rates, weekend rates and personal drop bonuses do not change which base chance is compared. This option reports items you actually receive; it does not change drop rates. Enter **0** in the menu to disable these notices. They are Off by default.

### Card Drop Illustration

Card Drop Illustration is **On by default**. When you receive a supported monster card through the tracked loot system, its artwork appears at the **bottom right for five seconds**, for you only. Select **Card Drop Illustration** in the settings menu to turn it On or Off.

[Card Drop Announcements](card-drop-announcements.md) name the successful recipient and show their recorded copy number for that specific card. The monster kill count is included for the recipient's own credited kill; party-shared cards and pickups from somebody else's kill omit it. Announcements follow Public chat filtering and the account's **Announcement Config > Drop** choice. Received copies are separate from the generated-card statistics in [Kill Count](kill-count.md).

Ordinary trades, NPC rewards and storage withdrawals do not trigger monster-drop artwork. Artwork is skipped when an NPC dialog is active or an illustration is unavailable. A later NPC illustration takes precedence over the timed card image.

See [Card exchange](card-exchange.md) for exchanging unwanted cards; exchange points are separate from these display preferences.

## Information and visibility

Choose these options in **`@settings`**:

| Setting | Behavior | Default |
| --- | --- | --- |
| Show Experience | Turn gained-EXP messages On or Off. | On |
| Show Guildmates HP | Show nearby guildmates' HP bars. Turning it Off retains party and Battleground HP bars. | On |
| Previous Teleport Position | Mark your departure cell on the minimap after a teleport within the same map. Cross-map travel does not create this marker. | Off |
| Direct Message Warning | Play a sound and show a personal on-screen notice for an accepted whisper. Alerts are limited to one per two seconds; server notices and channel messages do not trigger them. | Off |
| Time Mode | Choose Server cycle, Always day or Always night. Only your view changes. | Server cycle |
| Hide Headgear and Costumes during WoE | Hide everyone's headgear, costume headgear and robe visuals, including your own, on castle maps during their active WoE session. Equipment and bonuses remain intact. | Off |
| Status Color Effect | Choose Show status aura or Hide status aura. | Show |

Existing saved choices take precedence over defaults.

## Announcement configuration

Choose individual categories under **`@settings` > Announcement Config**:

- Welcome
- Drop
- Battlegrounds
- Kill
- Community News
- MVP
- Event
- PvP Arena

Select a category to turn its announcements On or Off for your account. All categories are visible by default. These choices control existing announcements; they do not activate an otherwise unavailable event or announcement system. General announcements use Event, while rotating EXP-region notices use Community News.

[Card Drop Announcements](card-drop-announcements.md) use Drop and are filtered as Public chat. Card Drop Illustration remains an independent option.

The **High-contrast yellow** option in the same submenu recolors server announcements for easier reading. It is Off by default.

## Storage weight limit and restock

Select **Storage Withdrawal Weight Limit** in **`@settings`** and enter a value from **1 to 100%**. This chooses the maximum carried-weight percentage after a withdrawal from personal storage. The default is **100%**, saved separately for each character. This does not increase carrying capacity or change overweight recovery restrictions.

Restock now uses named item/quantity lists. Open **Restock Supplies** to configure **target inventory totals**, or **Quick Store** to choose item IDs whose entire eligible inventory quantities should be deposited. Each feature supports **40 groups of 40 items**, with one active group per type.

Transfers require **already-open Main Storage in a town**, including Midgard Expedition Camp, Manuk and Splendide. Restock stays **strictly below 90% carried weight** and respects a lower personal withdrawal limit. Quick Store can unload items while overweight and **never asks for a quantity**.

See [Fast storage](fast-storage.md) for full setup, item eligibility and the Jellopy #909 example. The dedicated `@restockconfig` / `@qstoreconfig` menus open the same saved configuration; `@restock` / `@qstore` run the active lists.

## Autoloot configuration

Choose **Autoloot** inside `@settings`, or use **`@lootconfig`** to open the same menu. Configure Main Autoloot's original-drop-chance threshold, an ignore list of **100 items**, and up to **40 custom groups of 100 items**. Changes apply immediately and persist per character.

An active group adds its items even when they are ignored or Main Autoloot is Off. To loot everything except Jellopy, enable Main Autoloot at 100%, ignore #909, and ensure the active group does not include #909.

See [Advanced autoloot](autoloot.md) for filter precedence, defaults and setup. Visual/chat preferences remain configured only through `@settings`.

See [bulk purchases and storage](quality-of-life.md#bulk-purchases-and-personal-storage) for the separate large-purchase feature.
