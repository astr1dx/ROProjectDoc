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

Run the existing `Prepare-AdInfinitum.ps1` from the complete ROProject workspace when rebuilding the client. Preserve its finishing steps; applying only a fresh WARP executable can omit required compatibility repairs. Close the game before replacing its executable.

Launch through **Play-Offline.bat** and reopen the client after resource changes. A normal server disconnect returns to login; a genuine crash is a separate failure that needs investigation.

The client/build workspace is separate from this server-only repository. These files are documented here so the team can preserve the working profile when maintaining it.
