# Client patches and compatibility

Updated: **November 7, 2026**.

The current client is based on the clean **2024-06-19 Ragexe** and the Ad Infinitum WARP profile. English resources, the font/zoom adjustments and the compatibility finishing patches form part of the working client setup.

## Selected WARP patches

The profile currently selects **43 patches**. The following identifiers are copied from `AdInfinitumFinal.yml`; they are the actual WARP patch names rather than paraphrased labels.

```text
RestoreClientInfo
CustomQSDelay
NoWalkDelay
ZoomMax
UseOldLogin
AlwaysAscii
CustomSSQuality
DataFolderFirst
PlainTextDesc
LoadKrExtSettings
IncrMapQuality
TranslateClient
NoGGuard
CustomItemInfoLub
CustomAchieveLub
CustomMonSizeEffLub
CustomTownInfoLub
CustomPetEvoClnLub
CustomTipboxLub
CustomCheckAttLub
CustomPrivAirplaneLub
CustomMapInfoLub
CustomOngQuestInfoLub
CustomRcmdQuestInfoLub
CustomspopupLub
CustomQuestQualiLub
GRFsFromIni
NoFilenameCheck
CustomWinTitle
No1and1Arg
NoLoginOTP
NoHardCodedAddr
NoPacketEncr
CustomFadeDelay
NoGravityAds
NoGravityLogo
CustomFontName
CustomFontHeight
PreserveLargeFonts
HideLicense
CustomIcon
DisConnToLogin
EnableBerserkChat
```

The selections cover the local/classic login path, resource loading, English translations, client branding, readable fonts and larger map text, zoom, normal disconnect-to-login behavior, and Berserk chat support.

## Finishing patches after WARP

`Prepare-AdInfinitum.ps1` runs the WARP build and verification, then applies these compatibility steps:

| Finishing step | Purpose |
| --- | --- |
| Local-login routing | Preserves the tested localhost endpoint routing and old-login compatibility repairs. |
| RODEX postage | Matches the server's five-stack 10,000z postage discount. |
| Bulk-purchase warning | Removes the incorrect client warning for the supported exactly-30,000-unit NPC order. |
| Custom skill recognition | Accepts Madness Break (7997) and Super Blessing (7998), preserving the native classifier/fallback for other skill IDs. |

`EnableBerserkChat` is a WARP patch, not a replacement for the native Berserk status. The server and client retain the normal red-body status lifecycle so its effect persists through teleporting while chat remains usable.

## Resource updates

- English skill descriptions and relevant cost/range metadata in both loose skill-resource paths.
- Custom platinum skill entries, reused icons and job-tree placement.
- Devotion, Mind Breaker, Doridori and Angel status-icon support.
- Super Blessing's normal Blessing/Increase AGI effects and Blessing sound notifications.
- Compatible Lua resources for the June-2024 executable, replacing earlier mismatched TipBox, Adventure Guide and footprint resources.
- Readable UI/map-banner fonts and the tested expanded zoom range.
- Corrected server/client packet compatibility for emotes and modern character appearance updates.

These are the final working compatibility changes, not a record of every intermediate test executable. The protected original uaRO archive was not treated as a clean data source; the working setup uses the clean compatible client resources.

## Rebuilding and launching

### Attendance resource table

The installed `Client/System/CheckAttendance_EN.lub` and its generated translation copies contain the server's 20-day reward schedule and an active 2026-2037 date range. Restart the client after updating this table. Attendance uses the native window: opening it is read-only, and only an explicit claim sends a reward through RODEX. No executable change is required for this attendance correction.

### Repeated chat messages

As of November 8, 2026, the client-side repeated-message limit is **10**, increased from 2. The WARP profile selects `LimitedChatRepeat` with `$chatFloodLimit` set to 10. Unlimited repetition is not enabled.

The installed executable was updated using `Tools/Compatibility/patch-chat-repeat.py`, which changes only the native `IsSameSentence` comparison byte and verifies that every unrelated byte remains identical. The verification record is `Offline/chat-repeat-patch.json`; the original executable and profile are backed up under `Offline/Backups/ChatRepeat/20261108-160601/`. Restart the client to load the change. Existing server chat-delay and mute rules still apply.

Run the existing `Prepare-AdInfinitum.ps1` from the complete ROProject workspace when rebuilding the client. Preserve its finishing steps; applying only a fresh WARP executable can omit required compatibility repairs. Close the game before replacing its executable.

Launch through **Play-Offline.bat** and reopen the client after resource changes. A normal server disconnect returns to login; a genuine crash is a separate failure that needs investigation.

The client/build workspace is separate from this server-only repository. These files are documented here so the team can preserve the working profile when maintaining it.

## Dealer item information: November 9, 2026

Thirteen entries in `Client/System/LuaFiles514/itemInfo.lua` were added or updated for the dealer catalogue. This includes Hamaya Kunai (35360, Holy), Shadow Kunai (35361, Shadow), Formless Kunai (35362, Ghost), six additional elemental bullets and four pet supplies. The custom kunai are Ninja ammunition with 30 ATK, 0.5 weight and Level 1 access. Magic Stone Bullet's description now matches its Level 1 requirement.

Custom kunai reuse existing kunai icons and sprites; Delicious Meat and Luxurious Pet Food reuse existing pet-food artwork. Resource lookups were checked against the active GRF, and Lua 5.1 validation preserved all 14,619 unrelated item entries. Fully reopen the game after changing this item table. The dealer work does not replace the executable.

The hourly timer uses the existing reward display. Its click converts complete 120-point bundles into Gold Coins; shopping is through the fixed NPC. Server-side barter-shop movement handling rejects queued approach requests until the normal close event, without an additional executable change.

## Vendor integration and corrections: November 9, 2026

The vendor work adds `Client/data/buyingstoreitemlist.txt` with 2,938 eligible entries exported from the native server definitions. The server permits tradeable loose consumables and Etc-tab categories while rejecting crafted/brewed instances and equipment. The item #12548 KeepAfterUse override and server-side license handling defer consumption until successful shop creation. No additional executable patch is required for this integration.

The existing GRF supplies `prt_mk.gat`, `.gnd` and `.rsw`. `Server/maps/pre-re/prt_mk.mcache` was generated from the same map data and registered in the active map list/index. The map has 4,264 generated vending spots. The existing executable, fonts, effects and finishing repairs were preserved.

Server-side fixes after initial testing:

- `vendor_system.cpp` sends search page zero before incrementing the sent-page cursor.
- `clif_search_store_info_ack` rejects invalid/exhausted/overflowed offsets and writes rows at packet-local index `i - start`. `searchstore_querynext` now reports actual remaining pages. Empty command searches clear old UI rows.
- `clif_process_chat_message` accepts only the current character's exact generated `[V]` display label in addition to the canonical name, then reconstructs the canonical speaker before command/chat processing. Prefix reads are bounded by packet length, and the reconstructed output is length-checked. Other-character names still force rejection. This handles the name retained by the client after character selection, including the bounded long-name label.
- `ACMD(autotrade2)` reports success for the asynchronous handoff instead of an incorrect failure result.
- Offline vendors use distinct unit IDs, avoid unrelated account-storage sessions, do not overwrite shared account registries/account data, and wait for final-save acknowledgements independently. Character selection closes the chosen vendor and flushes its save before loading it.

Verification records are `Offline/card-exchange-verification.json`, `Offline/vendor-system-verification.json`, `Offline/vendor-search-crash-verification.json` and `Offline/vendor-name-commands-verification.json` in the full project workspace. Native tests cover transactions/restoration and guards; the connected-session suite covers actual login/map/character selection, retained-label commands, shop clicks and first/final/empty/exhausted search packets. The extracted production chat parser also passed canonical/own-label, long-name, malformed-prefix, spoofed-name and output-buffer cases. Tests use disposable data and opt-in test code excluded from the deployed binary.

Players confirmed Putty's exchange/reward list, the market NPCs, same-account `@at2` character switching and the corrected first `[V]` login attempt. The latest search correction has connected-session coverage; a separate player search confirmation is still pending. HWID enforcement and website merchant search were explicitly deferred.

## Personal-settings audio and assets: November 10, 2026

The normal executable includes the server-synchronized performance-audio filter. A runtime trace showed that native playback passes Korean performance filenames before resource-name translation. The corrected filter recognizes those names alongside the English aliases, preserves unrelated sounds and keeps the existing executable changes. Muting, retained notes/ground effects and restored audio when unmuted were confirmed by the player. The filter passed 821 emulator cases checking filename matching, registers, flags and stack behavior.

The rebuild finishing sequence in `Prepare-AdInfinitum.ps1` includes `Tools/PersonalSettings/patch-song-audio.py`. `Client/ad_settings.grf`, loaded before `data.grf` through `OFFLINE.INI`, supplies 506 existing card illustrations with native/ASCII aliases and the whisper alert sound. The original game archive remains unchanged. Diagnostic filename logging and its separate executable were removed after confirmation.

Server defaults now include `#main`, `#recruit` and `#market`; automatic joining respects account-level channel Off preferences. The isolated connected-session suite passed 93 native checks. Production test code is disabled. The settings menu and persistence are confirmed in-game; rendered card artwork and guild HP removal still await player confirmation. Disposable QA data was removed after verification.

## Menu-only preferences: November 10, 2026

Personal preferences and restock are now available only through the `@settings` menu. Standalone commands and the pet-muting alias were removed from native registration and group permissions, including GM access. The menu uses the same native persistence and audio synchronization. The public guide and in-game Restock Supplies instructions use menu choices exclusively.

The menu-only revision passed 127 native checks and connected-session tests using actual menu selections, Next and Close acknowledgements. Tests verify removed registrations/aliases even for GM sessions, ordinary-player song toggles, account persistence, per-character limits and channel visibility.

## Card announcement routing: November 10, 2026

`Tools/CardAnnouncements/patch-public-chat.py` adds a guarded finishing patch to the verified June executable. Only colored-chat packet 0x02c1 with reserved source ID 0x7ffffffe is routed to native Public category 1; the source tag is cleared before actor lookup. Ordinary colored messages retain their existing category. The patch preserves registers, flags and stack, and adds only a guarded call detour and appended code/section metadata.

`Prepare-AdInfinitum.ps1` now includes this step after the song-audio finishing patch. The 192 emulated cases verify one native chat event, Public-category matching, source clearing and unchanged ordinary colored messages. Existing executable bytes outside the hook/section metadata remain preserved. The installed client SHA-256 is `45d4de90e5f6090d7747df6ff36c2d421f287a5c628b700747e82e3b08d7db1b`.

Server announcement formatting credits successful recipients, keeps copy ordinals separate from generated-card tracking, omits kill counts for party-shared loot, and respects Drop visibility per recipient. The integrated suite passed 2,836 checks. The deployed Kill Count uses native private self-speech without a character-name prefix; no new executable change is needed for that counter. Final card-message rendering and Public-tab filtering still require an in-game check. Release records are `Offline/card-announcements-verification.json` and its scoped backups in the full project workspace.
