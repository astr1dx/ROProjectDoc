# Endless Tower

Climb **101 floors** with your party, defeat every floor's monsters and face **Naght Sieger** at the top. The full monster catalogue below includes sprites, monster IDs and spawn counts for each floor.

## Quick facts

| Requirement | Vestige Rift rule |
| --- | --- |
| Entry NPC | **Captain Janssen**, Prontera **217,187** |
| Staging area | **Misty Island** (`e_tower`) |
| Party | **6 or more members**, each using a different account |
| Minimum Base Level | **85** for every member |
| Readiness | Every starting member types **`!ready`** within **60 seconds** |
| Time limit | **4 hours**, starting after everyone confirms readiness |
| Weekly allowance | **1 run per account**, shared by all its characters |
| Weekly reset | **Monday at 06:00 Philippines time (UTC+8)** |

## Getting there

1. Speak to **Captain Janssen** in Prontera: `/navi prontera 217/187`.
2. Follow his conversations and make the **10,000z donation** when asked. Speak to him again to continue the story and board the ship to Misty Island.
3. Your first voyage unlocks the **Misty Island - 5,000z** route in the [Warper](warper.md#misty-island) for this character.
4. Gather the entire party on Misty Island and visit the **Tower Protection Stone**.

Captain Janssen also offers return voyages for **10,000z**. The unlocked Warper route costs **5,000z** per trip.

### Misty Island services

| NPC | Location | Service |
| --- | --- | --- |
| Tower Protection Stone | `e_tower 81,105` | Start a readiness check, rejoin the current floor or view weekly run information |
| Cellar Protection Stone | `e_tower 82,110` | Start or rejoin [Endless Cellar](endless-cellar.md), which has a separate weekly allowance |
| Kafra Employee | `e_tower 76,99` | Main Storage, Guild Storage and return to Prontera |

## Starting a run

1. Form a party of **at least six** characters. Every member must be **online, alive, Base Level 85+ and present on Misty Island**. Close other dialogs, shops and storage.
2. The party leader selects **Start Endless Tower** at the Tower Protection Stone.
3. Every member types **`!ready` in public chat within 60 seconds**. Keep the same party roster throughout the readiness check.
4. Once everyone is ready, the party is sent to Floor 1 and each participating account consumes its weekly run.

If readiness expires or the party fails the final checks, the party returns to its save points and **no weekly run is consumed**. A member who disconnects or leaves the island during readiness must return and confirm `!ready` again.

Use **`@instanceinfo`**, or **Weekly run information** at the stone, to see the account's remaining allowance and the party's active tower status.

## Tower rules

| Feature | Rule |
| --- | --- |
| Clearing floors | Defeat every required monster to open the next gate. **Taming does not count as defeating a monster.** |
| Floor skips | Advance through the floor gates; skipping floors is unavailable. |
| Death | Normal death rules apply. Players may be resurrected or leave and re-enter. |
| Re-entry | Only the **original characters in the starting party** may rejoin, while at least one original party member remains inside. Rejoin through the island stone to reach the party's current floor. |
| Everyone leaves | The instance closes when every original member leaves or disconnects. The weekly run remains consumed. |
| Time expires | The instance closes after four hours. The weekly run remains consumed. |
| Storage | Personal and Guild Storage are **unavailable inside**. Island storage is available before entry or while restocking outside. |
| Mail | **RODEX is available** inside the tower. |
| Drops | Monsters use their normal configured drops. **Bubble Gum does not increase tower drop rates.** |
| Restricted actions | Random teleportation, Warp Portal, vending and branch use are blocked inside. |

The weekly allowance belongs to the **account**. Switching characters does not grant another run, and a successful clear still uses that week's single run.

## Completion and rewards

After defeating **Naght Sieger**, speak to the **Lost Soul** and exit through the NPC to record completion. The cleared tower remains available for up to **five minutes**, within the original four-hour limit.

Copies of the starting party members appear near the exit. Speak to a copy to see that character's **damage dealt, damage taken, healing done, healing received, deaths and monster kills** for the run.

### Violet Fear exchange

The Lost Soul can combine **one Twin Edge of Naght Sieger (#13412)** and **one Twin Edge of Naght Sieger (#13413)** into **one Violet Fear (#1185)**. Refinements and cards on the two original swords are lost when they are consumed.

## Monster catalogue

The tables list the configured floor encounters. Counts describe the starting wave; monsters summoned during combat are additional. Expand a floor to see its monsters.

[Floors 1-25](#floors-1-25) · [Floors 26-50](#floors-26-50) · [Floors 51-75](#floors-51-75) · [Floors 76-98](#floors-76-98) · [Floor 99](#floor-99-random-encounters) · [Floor 100](#floor-100-entweihen-crothen) · [Floor 101](#floor-101-final-encounter)

<div class="tower-catalogue" markdown="1">

## Floors 1-25

??? info "Floor 1 - 36 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Metaling](assets/endless-tower/1613.gif){ .tower-monster-sprite loading="lazy" } | **Metaling**<br>ID: `1613` | **15** |
    | ![Marin](assets/endless-tower/1242.gif){ .tower-monster-sprite loading="lazy" } | **Marin**<br>ID: `1242` | **5** |
    | ![Poporing](assets/endless-tower/1031.gif){ .tower-monster-sprite loading="lazy" } | **Poporing**<br>ID: `1031` | **5** |
    | ![Drops](assets/endless-tower/1113.gif){ .tower-monster-sprite loading="lazy" } | **Drops**<br>ID: `1113` | **5** |
    | ![Mastering](assets/endless-tower/1090.gif){ .tower-monster-sprite loading="lazy" } | **Mastering**<br>ID: `1090` | **1** |
    | ![Poring](assets/endless-tower/1002.gif){ .tower-monster-sprite loading="lazy" } | **Poring**<br>ID: `1002` | **5** |

??? info "Floor 2 - 31 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Desert Wolf](assets/endless-tower/1106.gif){ .tower-monster-sprite loading="lazy" } | **Desert Wolf**<br>ID: `1106` | **20** |
    | ![Vagabond Wolf](assets/endless-tower/1092.gif){ .tower-monster-sprite loading="lazy" } | **Vagabond Wolf**<br>ID: `1092` | **1** |
    | ![Baby Desert Wolf](assets/endless-tower/1107.gif){ .tower-monster-sprite loading="lazy" } | **Baby Desert Wolf**<br>ID: `1107` | **10** |

??? info "Floor 3 - 30 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Archer Skeleton](assets/endless-tower/1016.gif){ .tower-monster-sprite loading="lazy" } | **Archer Skeleton**<br>ID: `1016` | **5** |
    | ![Skel Worker](assets/endless-tower/1169.gif){ .tower-monster-sprite loading="lazy" } | **Skel Worker**<br>ID: `1169` | **5** |
    | ![Soldier Skeleton](assets/endless-tower/1028.gif){ .tower-monster-sprite loading="lazy" } | **Soldier Skeleton**<br>ID: `1028` | **5** |
    | ![Orc Skeleton](assets/endless-tower/1152.gif){ .tower-monster-sprite loading="lazy" } | **Orc Skeleton**<br>ID: `1152` | **5** |
    | ![Pirate Skeleton](assets/endless-tower/1071.gif){ .tower-monster-sprite loading="lazy" } | **Pirate Skeleton**<br>ID: `1071` | **5** |
    | ![Skeleton](assets/endless-tower/1076.gif){ .tower-monster-sprite loading="lazy" } | **Skeleton**<br>ID: `1076` | **5** |

??? info "Floor 4 - 36 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Argiope](assets/endless-tower/1099.gif){ .tower-monster-sprite loading="lazy" } | **Argiope**<br>ID: `1099` | **15** |
    | ![Mantis](assets/endless-tower/1139.gif){ .tower-monster-sprite loading="lazy" } | **Mantis**<br>ID: `1139` | **5** |
    | ![Argos](assets/endless-tower/1100.gif){ .tower-monster-sprite loading="lazy" } | **Argos**<br>ID: `1100` | **5** |
    | ![Vocal](assets/endless-tower/1088.gif){ .tower-monster-sprite loading="lazy" } | **Vocal**<br>ID: `1088` | **1** |
    | ![Rocker](assets/endless-tower/1052.gif){ .tower-monster-sprite loading="lazy" } | **Rocker**<br>ID: `1052` | **5** |
    | ![Hornet](assets/endless-tower/1004.gif){ .tower-monster-sprite loading="lazy" } | **Hornet**<br>ID: `1004` | **5** |

??? info "Floor 5 - 51 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Golden Thief Bug](assets/endless-tower/1086.gif){ .tower-monster-sprite loading="lazy" } | **Golden Thief Bug**<br>ID: `1086` | **1** |
    | ![Thief Bug Male](assets/endless-tower/1054.gif){ .tower-monster-sprite loading="lazy" } | **Thief Bug Male**<br>ID: `1054` | **15** |
    | ![Thief Bug Female](assets/endless-tower/1053.gif){ .tower-monster-sprite loading="lazy" } | **Thief Bug Female**<br>ID: `1053` | **15** |
    | ![Thief Bug](assets/endless-tower/1051.gif){ .tower-monster-sprite loading="lazy" } | **Thief Bug**<br>ID: `1051` | **15** |
    | ![Thief Bug Egg](assets/endless-tower/1048.gif){ .tower-monster-sprite loading="lazy" } | **Thief Bug Egg**<br>ID: `1048` | **5** |

??? info "Floor 6 - 20 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Dragon Egg](assets/endless-tower/1721.gif){ .tower-monster-sprite loading="lazy" } | **Dragon Egg**<br>ID: `1721` | **5** |
    | ![Thief Bug Egg](assets/endless-tower/1048.gif){ .tower-monster-sprite loading="lazy" } | **Thief Bug Egg**<br>ID: `1048` | **5** |
    | ![Ant Egg](assets/endless-tower/1097.gif){ .tower-monster-sprite loading="lazy" } | **Ant Egg**<br>ID: `1097` | **5** |
    | ![Pupa](assets/endless-tower/1008.gif){ .tower-monster-sprite loading="lazy" } | **Pupa**<br>ID: `1008` | **5** |

??? info "Floor 7 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Explosion](assets/endless-tower/1383.gif){ .tower-monster-sprite loading="lazy" } | **Explosion**<br>ID: `1383` | **15** |
    | ![Drainliar](assets/endless-tower/1111.gif){ .tower-monster-sprite loading="lazy" } | **Drainliar**<br>ID: `1111` | **15** |
    | ![Anopheles](assets/endless-tower/1627.gif){ .tower-monster-sprite loading="lazy" } | **Anopheles**<br>ID: `1627` | **15** |
    | ![Farmiliar](assets/endless-tower/1005.gif){ .tower-monster-sprite loading="lazy" } | **Farmiliar**<br>ID: `1005` | **15** |

??? info "Floor 8 - 30 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Firelock Soldier](assets/endless-tower/1403.gif){ .tower-monster-sprite loading="lazy" } | **Firelock Soldier**<br>ID: `1403` | **15** |
    | ![Cruiser](assets/endless-tower/1248.gif){ .tower-monster-sprite loading="lazy" } | **Cruiser**<br>ID: `1248` | **15** |

??? info "Floor 9 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Obsidian](assets/endless-tower/1615.gif){ .tower-monster-sprite loading="lazy" } | **Obsidian**<br>ID: `1615` | **15** |
    | ![Golem](assets/endless-tower/1040.gif){ .tower-monster-sprite loading="lazy" } | **Golem**<br>ID: `1040` | **15** |
    | ![Stapo](assets/endless-tower/1784.gif){ .tower-monster-sprite loading="lazy" } | **Stapo**<br>ID: `1784` | **10** |

??? info "Floor 10 - 46 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Mistress](assets/endless-tower/1059.gif){ .tower-monster-sprite loading="lazy" } | **Mistress**<br>ID: `1059` | **1** |
    | ![Giant Hornet](assets/endless-tower/1303.gif){ .tower-monster-sprite loading="lazy" } | **Giant Hornet**<br>ID: `1303` | **25** |
    | ![Hornet](assets/endless-tower/1004.gif){ .tower-monster-sprite loading="lazy" } | **Hornet**<br>ID: `1004` | **20** |

??? info "Floor 11 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Dryad](assets/endless-tower/1493.gif){ .tower-monster-sprite loading="lazy" } | **Dryad**<br>ID: `1493` | **15** |
    | ![Parasite](assets/endless-tower/1500.gif){ .tower-monster-sprite loading="lazy" } | **Parasite**<br>ID: `1500` | **15** |
    | ![Hermit Plant](assets/endless-tower/1413.gif){ .tower-monster-sprite loading="lazy" } | **Hermit Plant**<br>ID: `1413` | **15** |
    | ![Rafflesia](assets/endless-tower/1162.gif){ .tower-monster-sprite loading="lazy" } | **Rafflesia**<br>ID: `1162` | **5** |

??? info "Floor 12 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Demon Pungus](assets/endless-tower/1378.gif){ .tower-monster-sprite loading="lazy" } | **Demon Pungus**<br>ID: `1378` | **25** |
    | ![Punk](assets/endless-tower/1199.gif){ .tower-monster-sprite loading="lazy" } | **Punk**<br>ID: `1199` | **25** |

??? info "Floor 13 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Yao Yun](assets/endless-tower/1512.gif){ .tower-monster-sprite loading="lazy" } | **Yao Yun**<br>ID: `1512` | **15** |
    | ![Bongunn](assets/endless-tower/1188.gif){ .tower-monster-sprite loading="lazy" } | **Bongunn**<br>ID: `1188` | **15** |
    | ![Munak](assets/endless-tower/1026.gif){ .tower-monster-sprite loading="lazy" } | **Munak**<br>ID: `1026` | **10** |

??? info "Floor 14 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![High Orc](assets/endless-tower/1213.gif){ .tower-monster-sprite loading="lazy" } | **High Orc**<br>ID: `1213` | **15** |
    | ![Orc Archer](assets/endless-tower/1189.gif){ .tower-monster-sprite loading="lazy" } | **Orc Archer**<br>ID: `1189` | **10** |
    | ![Orc Lady](assets/endless-tower/1273.gif){ .tower-monster-sprite loading="lazy" } | **Orc Lady**<br>ID: `1273` | **10** |
    | ![Orc Warrior](assets/endless-tower/1023.gif){ .tower-monster-sprite loading="lazy" } | **Orc Warrior**<br>ID: `1023` | **5** |
    | ![Orc Baby](assets/endless-tower/1686.gif){ .tower-monster-sprite loading="lazy" } | **Orc Baby**<br>ID: `1686` | **5** |

??? info "Floor 15 - 52 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Maya](assets/endless-tower/1147.gif){ .tower-monster-sprite loading="lazy" } | **Maya**<br>ID: `1147` | **1** |
    | ![Phreeoni](assets/endless-tower/1159.gif){ .tower-monster-sprite loading="lazy" } | **Phreeoni**<br>ID: `1159` | **1** |
    | ![Deniro](assets/endless-tower/1105.gif){ .tower-monster-sprite loading="lazy" } | **Deniro**<br>ID: `1105` | **15** |
    | ![Pierre](assets/endless-tower/1160.gif){ .tower-monster-sprite loading="lazy" } | **Pierre**<br>ID: `1160` | **15** |
    | ![Andre](assets/endless-tower/1095.gif){ .tower-monster-sprite loading="lazy" } | **Andre**<br>ID: `1095` | **15** |
    | ![Ant Egg](assets/endless-tower/1097.gif){ .tower-monster-sprite loading="lazy" } | **Ant Egg**<br>ID: `1097` | **5** |

??? info "Floor 16 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Raydric Archer](assets/endless-tower/1276.gif){ .tower-monster-sprite loading="lazy" } | **Raydric Archer**<br>ID: `1276` | **10** |
    | ![Orc Archer](assets/endless-tower/1189.gif){ .tower-monster-sprite loading="lazy" } | **Orc Archer**<br>ID: `1189` | **10** |
    | ![Gargoyle](assets/endless-tower/1253.gif){ .tower-monster-sprite loading="lazy" } | **Gargoyle**<br>ID: `1253` | **10** |
    | ![Archer Skeleton](assets/endless-tower/1016.gif){ .tower-monster-sprite loading="lazy" } | **Archer Skeleton**<br>ID: `1016` | **10** |

??? info "Floor 17 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Merman](assets/endless-tower/1264.gif){ .tower-monster-sprite loading="lazy" } | **Merman**<br>ID: `1264` | **10** |
    | ![Baphomet Jr.](assets/endless-tower/1101.gif){ .tower-monster-sprite loading="lazy" } | **Baphomet Jr.**<br>ID: `1101` | **10** |
    | ![Strouf](assets/endless-tower/1065.gif){ .tower-monster-sprite loading="lazy" } | **Strouf**<br>ID: `1065` | **15** |
    | ![Hill Wind](assets/endless-tower/1629.gif){ .tower-monster-sprite loading="lazy" } | **Hill Wind**<br>ID: `1629` | **5** |

??? info "Floor 18 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Cramp](assets/endless-tower/1209.gif){ .tower-monster-sprite loading="lazy" } | **Cramp**<br>ID: `1209` | **25** |
    | ![Tarou](assets/endless-tower/1175.gif){ .tower-monster-sprite loading="lazy" } | **Tarou**<br>ID: `1175` | **15** |

??? info "Floor 19 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Deviace](assets/endless-tower/1108.gif){ .tower-monster-sprite loading="lazy" } | **Deviace**<br>ID: `1108` | **10** |
    | ![Megalodon](assets/endless-tower/1064.gif){ .tower-monster-sprite loading="lazy" } | **Megalodon**<br>ID: `1064` | **10** |
    | ![Swordfish](assets/endless-tower/1069.gif){ .tower-monster-sprite loading="lazy" } | **Swordfish**<br>ID: `1069` | **10** |
    | ![Phen](assets/endless-tower/1158.gif){ .tower-monster-sprite loading="lazy" } | **Phen**<br>ID: `1158` | **10** |

??? info "Floor 20 - 51 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Drake](assets/endless-tower/1112.gif){ .tower-monster-sprite loading="lazy" } | **Drake**<br>ID: `1112` | **1** |
    | ![Pirate Skeleton](assets/endless-tower/1071.gif){ .tower-monster-sprite loading="lazy" } | **Pirate Skeleton**<br>ID: `1071` | **50** |

??? info "Floor 21 - 35 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Plasma](assets/endless-tower/1693.gif){ .tower-monster-sprite loading="lazy" } | **Plasma**<br>ID: `1693` | **10** |
    | ![Plasma](assets/endless-tower/1696.gif){ .tower-monster-sprite loading="lazy" } | **Plasma**<br>ID: `1696` | **10** |
    | ![Plasma](assets/endless-tower/1695.gif){ .tower-monster-sprite loading="lazy" } | **Plasma**<br>ID: `1695` | **5** |
    | ![Plasma](assets/endless-tower/1697.gif){ .tower-monster-sprite loading="lazy" } | **Plasma**<br>ID: `1697` | **5** |
    | ![Plasma](assets/endless-tower/1694.gif){ .tower-monster-sprite loading="lazy" } | **Plasma**<br>ID: `1694` | **5** |

??? info "Floor 22 - 80 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Muscipular](assets/endless-tower/1780.gif){ .tower-monster-sprite loading="lazy" } | **Muscipular**<br>ID: `1780` | **15** |
    | ![Drosera](assets/endless-tower/1781.gif){ .tower-monster-sprite loading="lazy" } | **Drosera**<br>ID: `1781` | **15** |
    | ![Flora](assets/endless-tower/1118.gif){ .tower-monster-sprite loading="lazy" } | **Flora**<br>ID: `1118` | **15** |
    | ![Hydra](assets/endless-tower/1068.gif){ .tower-monster-sprite loading="lazy" } | **Hydra**<br>ID: `1068` | **15** |
    | ![Mandragora](assets/endless-tower/1020.gif){ .tower-monster-sprite loading="lazy" } | **Mandragora**<br>ID: `1020` | **10** |
    | ![Rafflesia](assets/endless-tower/1162.gif){ .tower-monster-sprite loading="lazy" } | **Rafflesia**<br>ID: `1162` | **10** |

??? info "Floor 23 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Penomena](assets/endless-tower/1216.gif){ .tower-monster-sprite loading="lazy" } | **Penomena**<br>ID: `1216` | **15** |
    | ![Obeaune](assets/endless-tower/1044.gif){ .tower-monster-sprite loading="lazy" } | **Obeaune**<br>ID: `1044` | **10** |
    | ![Marse](assets/endless-tower/1144.gif){ .tower-monster-sprite loading="lazy" } | **Marse**<br>ID: `1144` | **10** |
    | ![Swordfish](assets/endless-tower/1069.gif){ .tower-monster-sprite loading="lazy" } | **Swordfish**<br>ID: `1069` | **10** |
    | ![Hydra](assets/endless-tower/1068.gif){ .tower-monster-sprite loading="lazy" } | **Hydra**<br>ID: `1068` | **5** |

??? info "Floor 24 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Joker](assets/endless-tower/1131.gif){ .tower-monster-sprite loading="lazy" } | **Joker**<br>ID: `1131` | **15** |
    | ![Carat](assets/endless-tower/1267.gif){ .tower-monster-sprite loading="lazy" } | **Carat**<br>ID: `1267` | **15** |
    | ![Jakk](assets/endless-tower/1130.gif){ .tower-monster-sprite loading="lazy" } | **Jakk**<br>ID: `1130` | **10** |

??? info "Floor 25 - 31 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Cat o' Nine Tails](assets/endless-tower/1307.gif){ .tower-monster-sprite loading="lazy" } | **Cat o' Nine Tails**<br>ID: `1307` | **15** |
    | ![Moonlight](assets/endless-tower/1150.gif){ .tower-monster-sprite loading="lazy" } | **Moonlight**<br>ID: `1150` | **1** |
    | ![Nine Tail](assets/endless-tower/1180.gif){ .tower-monster-sprite loading="lazy" } | **Nine Tail**<br>ID: `1180` | **15** |

## Floors 26-50

??? info "Floor 26 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Gibbet](assets/endless-tower/1503.gif){ .tower-monster-sprite loading="lazy" } | **Gibbet**<br>ID: `1503` | **10** |
    | ![Enchanted Peach Tree](assets/endless-tower/1410.gif){ .tower-monster-sprite loading="lazy" } | **Enchanted Peach Tree**<br>ID: `1410` | **10** |
    | ![Wooden Golem](assets/endless-tower/1497.gif){ .tower-monster-sprite loading="lazy" } | **Wooden Golem**<br>ID: `1497` | **10** |
    | ![Stone Shooter](assets/endless-tower/1495.gif){ .tower-monster-sprite loading="lazy" } | **Stone Shooter**<br>ID: `1495` | **10** |
    | ![Elder Willow](assets/endless-tower/1033.gif){ .tower-monster-sprite loading="lazy" } | **Elder Willow**<br>ID: `1033` | **5** |

??? info "Floor 27 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Goblin Archer](assets/endless-tower/1258.gif){ .tower-monster-sprite loading="lazy" } | **Goblin Archer**<br>ID: `1258` | **10** |
    | ![Goblin](assets/endless-tower/1122.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1122` | **10** |
    | ![Goblin](assets/endless-tower/1123.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1123` | **5** |
    | ![Goblin](assets/endless-tower/1124.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1124` | **5** |
    | ![Gobin](assets/endless-tower/1125.gif){ .tower-monster-sprite loading="lazy" } | **Gobin**<br>ID: `1125` | **5** |
    | ![Goblin](assets/endless-tower/1126.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1126` | **5** |

??? info "Floor 28 - 70 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Arclouse](assets/endless-tower/1194.gif){ .tower-monster-sprite loading="lazy" } | **Arclouse**<br>ID: `1194` | **30** |
    | ![Neraid](assets/endless-tower/1255.gif){ .tower-monster-sprite loading="lazy" } | **Neraid**<br>ID: `1255` | **15** |
    | ![Pest](assets/endless-tower/1256.gif){ .tower-monster-sprite loading="lazy" } | **Pest**<br>ID: `1256` | **15** |
    | ![Kukre](assets/endless-tower/1070.gif){ .tower-monster-sprite loading="lazy" } | **Kukre**<br>ID: `1070` | **10** |

??? info "Floor 29 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Dark Frame](assets/endless-tower/1260.gif){ .tower-monster-sprite loading="lazy" } | **Dark Frame**<br>ID: `1260` | **10** |
    | ![The Paper](assets/endless-tower/1375.gif){ .tower-monster-sprite loading="lazy" } | **The Paper**<br>ID: `1375` | **10** |
    | ![Hylozoist](assets/endless-tower/1510.gif){ .tower-monster-sprite loading="lazy" } | **Hylozoist**<br>ID: `1510` | **10** |
    | ![Quve](assets/endless-tower/1508.gif){ .tower-monster-sprite loading="lazy" } | **Quve**<br>ID: `1508` | **5** |
    | ![Lude](assets/endless-tower/1509.gif){ .tower-monster-sprite loading="lazy" } | **Lude**<br>ID: `1509` | **5** |
    | ![Whisper](assets/endless-tower/1179.gif){ .tower-monster-sprite loading="lazy" } | **Whisper**<br>ID: `1179` | **10** |

??? info "Floor 30 - 31 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![White Lady](assets/endless-tower/1630.gif){ .tower-monster-sprite loading="lazy" } | **White Lady**<br>ID: `1630` | **1** |
    | ![Evil Nymph](assets/endless-tower/1416.gif){ .tower-monster-sprite loading="lazy" } | **Evil Nymph**<br>ID: `1416` | **30** |

??? info "Floor 31 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Gig](assets/endless-tower/1387.gif){ .tower-monster-sprite loading="lazy" } | **Gig**<br>ID: `1387` | **20** |
    | ![Iron Fist](assets/endless-tower/1212.gif){ .tower-monster-sprite loading="lazy" } | **Iron Fist**<br>ID: `1212` | **15** |
    | ![Argiope](assets/endless-tower/1099.gif){ .tower-monster-sprite loading="lazy" } | **Argiope**<br>ID: `1099` | **10** |
    | ![Scorpion](assets/endless-tower/1001.gif){ .tower-monster-sprite loading="lazy" } | **Scorpion**<br>ID: `1001` | **5** |

??? info "Floor 32 - 41 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Goblin Leader](assets/endless-tower/1299.gif){ .tower-monster-sprite loading="lazy" } | **Goblin Leader**<br>ID: `1299` | **1** |
    | ![Goblin Archer](assets/endless-tower/1258.gif){ .tower-monster-sprite loading="lazy" } | **Goblin Archer**<br>ID: `1258` | **10** |
    | ![Goblin](assets/endless-tower/1122.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1122` | **10** |
    | ![Goblin](assets/endless-tower/1123.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1123` | **5** |
    | ![Goblin](assets/endless-tower/1124.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1124` | **5** |
    | ![Goblin](assets/endless-tower/1125.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1125` | **5** |
    | ![Goblin](assets/endless-tower/1126.gif){ .tower-monster-sprite loading="lazy" } | **Goblin**<br>ID: `1126` | **5** |

??? info "Floor 33 - 46 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Kobold Leader](assets/endless-tower/1296.gif){ .tower-monster-sprite loading="lazy" } | **Kobold Leader**<br>ID: `1296` | **1** |
    | ![Kobold](assets/endless-tower/1133.gif){ .tower-monster-sprite loading="lazy" } | **Kobold**<br>ID: `1133` | **15** |
    | ![Kobold_Archer](assets/endless-tower/1282.gif){ .tower-monster-sprite loading="lazy" } | **Kobold_Archer**<br>ID: `1282` | **15** |
    | ![Kobold](assets/endless-tower/1134.gif){ .tower-monster-sprite loading="lazy" } | **Kobold**<br>ID: `1134` | **10** |
    | ![Kobold](assets/endless-tower/1135.gif){ .tower-monster-sprite loading="lazy" } | **Kobold**<br>ID: `1135` | **5** |

??? info "Floor 34 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Flame Skull](assets/endless-tower/1869.gif){ .tower-monster-sprite loading="lazy" } | **Flame Skull**<br>ID: `1869` | **20** |
    | ![Whisper](assets/endless-tower/1179.gif){ .tower-monster-sprite loading="lazy" } | **Whisper**<br>ID: `1179` | **10** |
    | ![Giant Whisper](assets/endless-tower/1186.gif){ .tower-monster-sprite loading="lazy" } | **Giant Whisper**<br>ID: `1186` | **10** |

??? info "Floor 35 - 41 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Turtle General](assets/endless-tower/1312.gif){ .tower-monster-sprite loading="lazy" } | **Turtle General**<br>ID: `1312` | **1** |
    | ![Freezer](assets/endless-tower/1319.gif){ .tower-monster-sprite loading="lazy" } | **Freezer**<br>ID: `1319` | **10** |
    | ![Solider](assets/endless-tower/1316.gif){ .tower-monster-sprite loading="lazy" } | **Solider**<br>ID: `1316` | **10** |
    | ![Heater](assets/endless-tower/1318.gif){ .tower-monster-sprite loading="lazy" } | **Heater**<br>ID: `1318` | **10** |
    | ![Permeter](assets/endless-tower/1314.gif){ .tower-monster-sprite loading="lazy" } | **Permeter**<br>ID: `1314` | **10** |

??? info "Floor 36 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Anolian](assets/endless-tower/1206.gif){ .tower-monster-sprite loading="lazy" } | **Anolian**<br>ID: `1206` | **30** |
    | ![Grove](assets/endless-tower/1687.gif){ .tower-monster-sprite loading="lazy" } | **Grove**<br>ID: `1687` | **10** |
    | ![Alligator](assets/endless-tower/1271.gif){ .tower-monster-sprite loading="lazy" } | **Alligator**<br>ID: `1271` | **10** |

??? info "Floor 37 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Clock Tower Manager](assets/endless-tower/1270.gif){ .tower-monster-sprite loading="lazy" } | **Clock Tower Manager**<br>ID: `1270` | **10** |
    | ![Clock](assets/endless-tower/1269.gif){ .tower-monster-sprite loading="lazy" } | **Clock**<br>ID: `1269` | **10** |
    | ![Alarm](assets/endless-tower/1193.gif){ .tower-monster-sprite loading="lazy" } | **Alarm**<br>ID: `1193` | **30** |

??? info "Floor 38 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Death Word](assets/endless-tower/1698.gif){ .tower-monster-sprite loading="lazy" } | **Death Word**<br>ID: `1698` | **25** |
    | ![Rideword](assets/endless-tower/1195.gif){ .tower-monster-sprite loading="lazy" } | **Rideword**<br>ID: `1195` | **25** |

??? info "Floor 39 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Evil Nymph](assets/endless-tower/1416.gif){ .tower-monster-sprite loading="lazy" } | **Evil Nymph**<br>ID: `1416` | **10** |
    | ![Mao Gui](assets/endless-tower/1513.gif){ .tower-monster-sprite loading="lazy" } | **Mao Gui**<br>ID: `1513` | **10** |
    | ![Taoist Hermit](assets/endless-tower/1412.gif){ .tower-monster-sprite loading="lazy" } | **Taoist Hermit**<br>ID: `1412` | **10** |
    | ![Zhu Po Long](assets/endless-tower/1514.gif){ .tower-monster-sprite loading="lazy" } | **Zhu Po Long**<br>ID: `1514` | **10** |
    | ![Jin Guai](assets/endless-tower/1517.gif){ .tower-monster-sprite loading="lazy" } | **Jin Guai**<br>ID: `1517` | **5** |

??? info "Floor 40 - 41 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Samurai Specter](assets/endless-tower/1492.gif){ .tower-monster-sprite loading="lazy" } | **Samurai Specter**<br>ID: `1492` | **1** |
    | ![Shinobi](assets/endless-tower/1401.gif){ .tower-monster-sprite loading="lazy" } | **Shinobi**<br>ID: `1401` | **10** |
    | ![Tengu](assets/endless-tower/1405.gif){ .tower-monster-sprite loading="lazy" } | **Tengu**<br>ID: `1405` | **10** |
    | ![Firelock Soldier](assets/endless-tower/1403.gif){ .tower-monster-sprite loading="lazy" } | **Firelock Soldier**<br>ID: `1403` | **5** |
    | ![Miyabi Doll](assets/endless-tower/1404.gif){ .tower-monster-sprite loading="lazy" } | **Miyabi Doll**<br>ID: `1404` | **10** |
    | ![Karakasa](assets/endless-tower/1400.gif){ .tower-monster-sprite loading="lazy" } | **Karakasa**<br>ID: `1400` | **5** |

??? info "Floor 41 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Kraben](assets/endless-tower/1587.gif){ .tower-monster-sprite loading="lazy" } | **Kraben**<br>ID: `1587` | **50** |

??? info "Floor 42 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Sleeper](assets/endless-tower/1386.gif){ .tower-monster-sprite loading="lazy" } | **Sleeper**<br>ID: `1386` | **20** |
    | ![Sting](assets/endless-tower/1207.gif){ .tower-monster-sprite loading="lazy" } | **Sting**<br>ID: `1207` | **10** |
    | ![Mi Gao](assets/endless-tower/1516.gif){ .tower-monster-sprite loading="lazy" } | **Mi Gao**<br>ID: `1516` | **10** |
    | ![Sandman](assets/endless-tower/1165.gif){ .tower-monster-sprite loading="lazy" } | **Sandman**<br>ID: `1165` | **5** |
    | ![Hode](assets/endless-tower/1127.gif){ .tower-monster-sprite loading="lazy" } | **Hode**<br>ID: `1127` | **5** |

??? info "Floor 43 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Medusa](assets/endless-tower/1148.gif){ .tower-monster-sprite loading="lazy" } | **Medusa**<br>ID: `1148` | **10** |
    | ![Sidewinder](assets/endless-tower/1037.gif){ .tower-monster-sprite loading="lazy" } | **Sidewinder**<br>ID: `1037` | **40** |
    | ![Anacondaq](assets/endless-tower/1030.gif){ .tower-monster-sprite loading="lazy" } | **Anacondaq**<br>ID: `1030` | **5** |
    | ![Boa](assets/endless-tower/1025.gif){ .tower-monster-sprite loading="lazy" } | **Boa**<br>ID: `1025` | **5** |

??? info "Floor 44 - 61 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Hatii Baby](assets/endless-tower/1515.gif){ .tower-monster-sprite loading="lazy" } | **Hatii Baby**<br>ID: `1515` | **20** |
    | ![Baphomet Jr.](assets/endless-tower/1101.gif){ .tower-monster-sprite loading="lazy" } | **Baphomet Jr.**<br>ID: `1101` | **20** |
    | ![Orc Baby](assets/endless-tower/1686.gif){ .tower-monster-sprite loading="lazy" } | **Orc Baby**<br>ID: `1686` | **1** |
    | ![Baby Desert Wolf](assets/endless-tower/1107.gif){ .tower-monster-sprite loading="lazy" } | **Baby Desert Wolf**<br>ID: `1107` | **10** |
    | ![Savage Babe](assets/endless-tower/1167.gif){ .tower-monster-sprite loading="lazy" } | **Savage Babe**<br>ID: `1167` | **10** |

??? info "Floor 45 - 51 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Osiris](assets/endless-tower/1038.gif){ .tower-monster-sprite loading="lazy" } | **Osiris**<br>ID: `1038` | **1** |
    | ![Ancient Mummy](assets/endless-tower/1297.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Mummy**<br>ID: `1297` | **15** |
    | ![Verit](assets/endless-tower/1032.gif){ .tower-monster-sprite loading="lazy" } | **Verit**<br>ID: `1032` | **15** |
    | ![Mummy](assets/endless-tower/1041.gif){ .tower-monster-sprite loading="lazy" } | **Mummy**<br>ID: `1041` | **20** |

??? info "Floor 46 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Seeker](assets/endless-tower/1774.gif){ .tower-monster-sprite loading="lazy" } | **Seeker**<br>ID: `1774` | **20** |
    | ![Beholder](assets/endless-tower/1633.gif){ .tower-monster-sprite loading="lazy" } | **Beholder**<br>ID: `1633` | **20** |

??? info "Floor 47 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Deleter](assets/endless-tower/1384.gif){ .tower-monster-sprite loading="lazy" } | **Deleter**<br>ID: `1384` | **20** |
    | ![Deleter](assets/endless-tower/1385.gif){ .tower-monster-sprite loading="lazy" } | **Deleter**<br>ID: `1385` | **10** |
    | ![Petite](assets/endless-tower/1156.gif){ .tower-monster-sprite loading="lazy" } | **Petite**<br>ID: `1156` | **10** |
    | ![Petite](assets/endless-tower/1155.gif){ .tower-monster-sprite loading="lazy" } | **Petite**<br>ID: `1155` | **10** |

??? info "Floor 48 - 30 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Ancient Worm](assets/endless-tower/1305.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Worm**<br>ID: `1305` | **10** |
    | ![Ancient Mummy](assets/endless-tower/1297.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Mummy**<br>ID: `1297` | **10** |
    | ![Ancient Mimic](assets/endless-tower/1699.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Mimic**<br>ID: `1699` | **10** |

??? info "Floor 49 - 42 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Grizzly](assets/endless-tower/1381.gif){ .tower-monster-sprite loading="lazy" } | **Grizzly**<br>ID: `1381` | **20** |
    | ![Leib Olmai](assets/endless-tower/1306.gif){ .tower-monster-sprite loading="lazy" } | **Leib Olmai**<br>ID: `1306` | **7** |
    | ![Zipper Bear](assets/endless-tower/1417.gif){ .tower-monster-sprite loading="lazy" } | **Zipper Bear**<br>ID: `1417` | **5** |
    | ![Sasquatch](assets/endless-tower/1243.gif){ .tower-monster-sprite loading="lazy" } | **Sasquatch**<br>ID: `1243` | **5** |
    | ![Bigfoot](assets/endless-tower/1060.gif){ .tower-monster-sprite loading="lazy" } | **Bigfoot**<br>ID: `1060` | **5** |

??? info "Floor 50 - 32 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Pharaoh](assets/endless-tower/1157.gif){ .tower-monster-sprite loading="lazy" } | **Pharaoh**<br>ID: `1157` | **1** |
    | ![Amon Ra](assets/endless-tower/1511.gif){ .tower-monster-sprite loading="lazy" } | **Amon Ra**<br>ID: `1511` | **1** |
    | ![Anubis](assets/endless-tower/1098.gif){ .tower-monster-sprite loading="lazy" } | **Anubis**<br>ID: `1098` | **10** |
    | ![Marduk](assets/endless-tower/1140.gif){ .tower-monster-sprite loading="lazy" } | **Marduk**<br>ID: `1140` | **10** |
    | ![Matyr](assets/endless-tower/1146.gif){ .tower-monster-sprite loading="lazy" } | **Matyr**<br>ID: `1146` | **10** |

## Floors 51-75

??? info "Floor 51 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Mini Demon](assets/endless-tower/1292.gif){ .tower-monster-sprite loading="lazy" } | **Mini Demon**<br>ID: `1292` | **20** |
    | ![Diabolic](assets/endless-tower/1382.gif){ .tower-monster-sprite loading="lazy" } | **Diabolic**<br>ID: `1382` | **20** |
    | ![Deviruchi](assets/endless-tower/1109.gif){ .tower-monster-sprite loading="lazy" } | **Deviruchi**<br>ID: `1109` | **10** |

??? info "Floor 52 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Harpy](assets/endless-tower/1376.gif){ .tower-monster-sprite loading="lazy" } | **Harpy**<br>ID: `1376` | **20** |
    | ![Grand Peco](assets/endless-tower/1369.gif){ .tower-monster-sprite loading="lazy" } | **Grand Peco**<br>ID: `1369` | **10** |
    | ![Bloody Butterfly](assets/endless-tower/1408.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Butterfly**<br>ID: `1408` | **10** |
    | ![Gargoyle](assets/endless-tower/1253.gif){ .tower-monster-sprite loading="lazy" } | **Gargoyle**<br>ID: `1253` | **10** |
    | ![Hill Wind](assets/endless-tower/1680.gif){ .tower-monster-sprite loading="lazy" } | **Hill Wind**<br>ID: `1680` | **5** |
    | ![Hill Wind](assets/endless-tower/1629.gif){ .tower-monster-sprite loading="lazy" } | **Hill Wind**<br>ID: `1629` | **5** |

??? info "Floor 53 - 55 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Assaulter](assets/endless-tower/1315.gif){ .tower-monster-sprite loading="lazy" } | **Assaulter**<br>ID: `1315` | **25** |
    | ![Shinobi](assets/endless-tower/1401.gif){ .tower-monster-sprite loading="lazy" } | **Shinobi**<br>ID: `1401` | **30** |

??? info "Floor 54 - 30 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Chepet](assets/endless-tower/1250.gif){ .tower-monster-sprite loading="lazy" } | **Chepet**<br>ID: `1250` | **10** |
    | ![Mariontte](assets/endless-tower/1143.gif){ .tower-monster-sprite loading="lazy" } | **Mariontte**<br>ID: `1143` | **10** |
    | ![Miyabi Doll](assets/endless-tower/1404.gif){ .tower-monster-sprite loading="lazy" } | **Miyabi Doll**<br>ID: `1404` | **10** |

??? info "Floor 55 - 56 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Medusa](assets/endless-tower/1148.gif){ .tower-monster-sprite loading="lazy" } | **Medusa**<br>ID: `1148` | **25** |
    | ![Evil Snake Lord](assets/endless-tower/1418.gif){ .tower-monster-sprite loading="lazy" } | **Evil Snake Lord**<br>ID: `1418` | **1** |
    | ![Isis](assets/endless-tower/1029.gif){ .tower-monster-sprite loading="lazy" } | **Isis**<br>ID: `1029` | **15** |
    | ![Sidewinder](assets/endless-tower/1037.gif){ .tower-monster-sprite loading="lazy" } | **Sidewinder**<br>ID: `1037` | **15** |

??? info "Floor 56 - 55 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Freezer](assets/endless-tower/1319.gif){ .tower-monster-sprite loading="lazy" } | **Freezer**<br>ID: `1319` | **10** |
    | ![Hatii Baby](assets/endless-tower/1515.gif){ .tower-monster-sprite loading="lazy" } | **Hatii Baby**<br>ID: `1515` | **10** |
    | ![Ice Titan](assets/endless-tower/1777.gif){ .tower-monster-sprite loading="lazy" } | **Ice Titan**<br>ID: `1777` | **15** |
    | ![Snowier](assets/endless-tower/1775.gif){ .tower-monster-sprite loading="lazy" } | **Snowier**<br>ID: `1775` | **10** |
    | ![Gazeti](assets/endless-tower/1778.gif){ .tower-monster-sprite loading="lazy" } | **Gazeti**<br>ID: `1778` | **10** |

??? info "Floor 57 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Arc Angeling](assets/endless-tower/1388.gif){ .tower-monster-sprite loading="lazy" } | **Arc Angeling**<br>ID: `1388` | **1** |
    | ![Deviling](assets/endless-tower/1582.gif){ .tower-monster-sprite loading="lazy" } | **Deviling**<br>ID: `1582` | **1** |
    | ![Angeling](assets/endless-tower/1096.gif){ .tower-monster-sprite loading="lazy" } | **Angeling**<br>ID: `1096` | **1** |
    | ![Ghostring](assets/endless-tower/1120.gif){ .tower-monster-sprite loading="lazy" } | **Ghostring**<br>ID: `1120` | **1** |
    | ![Mastering](assets/endless-tower/1090.gif){ .tower-monster-sprite loading="lazy" } | **Mastering**<br>ID: `1090` | **1** |
    | ![Metaling](assets/endless-tower/1613.gif){ .tower-monster-sprite loading="lazy" } | **Metaling**<br>ID: `1613` | **25** |
    | ![Marin](assets/endless-tower/1242.gif){ .tower-monster-sprite loading="lazy" } | **Marin**<br>ID: `1242` | **5** |
    | ![Poporing](assets/endless-tower/1031.gif){ .tower-monster-sprite loading="lazy" } | **Poporing**<br>ID: `1031` | **5** |
    | ![Drops](assets/endless-tower/1113.gif){ .tower-monster-sprite loading="lazy" } | **Drops**<br>ID: `1113` | **5** |

??? info "Floor 58 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Phendark](assets/endless-tower/1202.gif){ .tower-monster-sprite loading="lazy" } | **Phendark**<br>ID: `1202` | **20** |
    | ![Rybio](assets/endless-tower/1201.gif){ .tower-monster-sprite loading="lazy" } | **Rybio**<br>ID: `1201` | **10** |
    | ![Zombie Prisoner](assets/endless-tower/1197.gif){ .tower-monster-sprite loading="lazy" } | **Zombie Prisoner**<br>ID: `1197` | **10** |
    | ![Skeleton Prisoner](assets/endless-tower/1196.gif){ .tower-monster-sprite loading="lazy" } | **Skeleton Prisoner**<br>ID: `1196` | **5** |
    | ![Injustice](assets/endless-tower/1257.gif){ .tower-monster-sprite loading="lazy" } | **Injustice**<br>ID: `1257` | **5** |

??? info "Floor 59 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Ancient Mimic](assets/endless-tower/1699.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Mimic**<br>ID: `1699` | **30** |
    | ![Mimic](assets/endless-tower/1191.gif){ .tower-monster-sprite loading="lazy" } | **Mimic**<br>ID: `1191` | **20** |
    | ![Mystcase](assets/endless-tower/1249.gif){ .tower-monster-sprite loading="lazy" } | **Mystcase**<br>ID: `1249` | **10** |

??? info "Floor 60 - 62 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Egnigem Cenia](assets/endless-tower/1658.gif){ .tower-monster-sprite loading="lazy" } | **Egnigem Cenia**<br>ID: `1658` | **1** |
    | ![Doppelganger](assets/endless-tower/1046.gif){ .tower-monster-sprite loading="lazy" } | **Doppelganger**<br>ID: `1046` | **1** |
    | ![Armeyer Dinze](assets/endless-tower/1654.gif){ .tower-monster-sprite loading="lazy" } | **Armeyer Dinze**<br>ID: `1654` | **10** |
    | ![Wickebine Tres](assets/endless-tower/1653.gif){ .tower-monster-sprite loading="lazy" } | **Wickebine Tres**<br>ID: `1653` | **10** |
    | ![Laurell Winder](assets/endless-tower/1657.gif){ .tower-monster-sprite loading="lazy" } | **Laurell Winder**<br>ID: `1657` | **10** |
    | ![Kavach Icarus](assets/endless-tower/1656.gif){ .tower-monster-sprite loading="lazy" } | **Kavach Icarus**<br>ID: `1656` | **10** |
    | ![Errende Ebecee](assets/endless-tower/1655.gif){ .tower-monster-sprite loading="lazy" } | **Errende Ebecee**<br>ID: `1655` | **10** |
    | ![Egnigem Cenia](assets/endless-tower/1652.gif){ .tower-monster-sprite loading="lazy" } | **Egnigem Cenia**<br>ID: `1652` | **10** |

??? info "Floor 61 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Agav](assets/endless-tower/1769.gif){ .tower-monster-sprite loading="lazy" } | **Agav**<br>ID: `1769` | **10** |
    | ![Echio](assets/endless-tower/1770.gif){ .tower-monster-sprite loading="lazy" } | **Echio**<br>ID: `1770` | **10** |
    | ![Isilla](assets/endless-tower/1772.gif){ .tower-monster-sprite loading="lazy" } | **Isilla**<br>ID: `1772` | **5** |
    | ![Mobster](assets/endless-tower/1313.gif){ .tower-monster-sprite loading="lazy" } | **Mobster**<br>ID: `1313` | **10** |
    | ![Pasana](assets/endless-tower/1154.gif){ .tower-monster-sprite loading="lazy" } | **Pasana**<br>ID: `1154` | **10** |
    | ![Vanberk](assets/endless-tower/1771.gif){ .tower-monster-sprite loading="lazy" } | **Vanberk**<br>ID: `1771` | **5** |

??? info "Floor 62 - 35 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Wanderer](assets/endless-tower/1208.gif){ .tower-monster-sprite loading="lazy" } | **Wanderer**<br>ID: `1208` | **35** |

??? info "Floor 63 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Ragged Zombie](assets/endless-tower/1865.gif){ .tower-monster-sprite loading="lazy" } | **Ragged Zombie**<br>ID: `1865` | **20** |
    | ![Zombie Master](assets/endless-tower/1298.gif){ .tower-monster-sprite loading="lazy" } | **Zombie Master**<br>ID: `1298` | **10** |
    | ![Zombie Prisoner](assets/endless-tower/1197.gif){ .tower-monster-sprite loading="lazy" } | **Zombie Prisoner**<br>ID: `1197` | **5** |
    | ![Orc Zombie](assets/endless-tower/1153.gif){ .tower-monster-sprite loading="lazy" } | **Orc Zombie**<br>ID: `1153` | **5** |
    | ![Zombie](assets/endless-tower/1015.gif){ .tower-monster-sprite loading="lazy" } | **Zombie**<br>ID: `1015` | **5** |

??? info "Floor 64 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Ungoliant](assets/endless-tower/1618.gif){ .tower-monster-sprite loading="lazy" } | **Ungoliant**<br>ID: `1618` | **30** |
    | ![Ancient Worm](assets/endless-tower/1305.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Worm**<br>ID: `1305` | **2** |
    | ![Caterpillar](assets/endless-tower/1300.gif){ .tower-monster-sprite loading="lazy" } | **Caterpillar**<br>ID: `1300` | **2** |
    | ![Creamy Fear](assets/endless-tower/1293.gif){ .tower-monster-sprite loading="lazy" } | **Creamy Fear**<br>ID: `1293` | **2** |
    | ![Killer Mantis](assets/endless-tower/1294.gif){ .tower-monster-sprite loading="lazy" } | **Killer Mantis**<br>ID: `1294` | **2** |
    | ![Giant Hornet](assets/endless-tower/1303.gif){ .tower-monster-sprite loading="lazy" } | **Giant Hornet**<br>ID: `1303` | **2** |

??? info "Floor 65 - 21 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Atros](assets/endless-tower/1785.gif){ .tower-monster-sprite loading="lazy" } | **Atros**<br>ID: `1785` | **1** |
    | ![Galion](assets/endless-tower/1783.gif){ .tower-monster-sprite loading="lazy" } | **Galion**<br>ID: `1783` | **20** |

??? info "Floor 66 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Incubus](assets/endless-tower/1374.gif){ .tower-monster-sprite loading="lazy" } | **Incubus**<br>ID: `1374` | **20** |
    | ![Aliot](assets/endless-tower/1736.gif){ .tower-monster-sprite loading="lazy" } | **Aliot**<br>ID: `1736` | **20** |
    | ![Injustice](assets/endless-tower/1257.gif){ .tower-monster-sprite loading="lazy" } | **Injustice**<br>ID: `1257` | **10** |

??? info "Floor 67 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Acidus](assets/endless-tower/1716.gif){ .tower-monster-sprite loading="lazy" } | **Acidus**<br>ID: `1716` | **10** |
    | ![Acidus](assets/endless-tower/1713.gif){ .tower-monster-sprite loading="lazy" } | **Acidus**<br>ID: `1713` | **10** |
    | ![Deleter](assets/endless-tower/1384.gif){ .tower-monster-sprite loading="lazy" } | **Deleter**<br>ID: `1384` | **5** |
    | ![Mutant Dragonoid](assets/endless-tower/1262.gif){ .tower-monster-sprite loading="lazy" } | **Mutant Dragonoid**<br>ID: `1262` | **10** |
    | ![Petite](assets/endless-tower/1156.gif){ .tower-monster-sprite loading="lazy" } | **Petite**<br>ID: `1156` | **5** |

??? info "Floor 68 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Lava Golem](assets/endless-tower/1366.gif){ .tower-monster-sprite loading="lazy" } | **Lava Golem**<br>ID: `1366` | **10** |
    | ![Stalactic Golem](assets/endless-tower/1278.gif){ .tower-monster-sprite loading="lazy" } | **Stalactic Golem**<br>ID: `1278` | **10** |
    | ![Ice Titan](assets/endless-tower/1777.gif){ .tower-monster-sprite loading="lazy" } | **Ice Titan**<br>ID: `1777` | **10** |
    | ![Wooden Golem](assets/endless-tower/1497.gif){ .tower-monster-sprite loading="lazy" } | **Wooden Golem**<br>ID: `1497` | **5** |
    | ![Golem](assets/endless-tower/1040.gif){ .tower-monster-sprite loading="lazy" } | **Golem**<br>ID: `1040` | **5** |

??? info "Floor 69 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Dame of Sentinel](assets/endless-tower/1700.gif){ .tower-monster-sprite loading="lazy" } | **Dame of Sentinel**<br>ID: `1700` | **20** |
    | ![Mistress of Shelter](assets/endless-tower/1701.gif){ .tower-monster-sprite loading="lazy" } | **Mistress of Shelter**<br>ID: `1701` | **10** |
    | ![Baroness of Retribution](assets/endless-tower/1702.gif){ .tower-monster-sprite loading="lazy" } | **Baroness of Retribution**<br>ID: `1702` | **10** |
    | ![Lady Solace](assets/endless-tower/1703.gif){ .tower-monster-sprite loading="lazy" } | **Lady Solace**<br>ID: `1703` | **10** |
    | ![False Angel](assets/endless-tower/1371.gif){ .tower-monster-sprite loading="lazy" } | **False Angel**<br>ID: `1371` | **10** |

??? info "Floor 70 - 22 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Orc Hero](assets/endless-tower/1087.gif){ .tower-monster-sprite loading="lazy" } | **Orc Hero**<br>ID: `1087` | **1** |
    | ![Orc Lord](assets/endless-tower/1190.gif){ .tower-monster-sprite loading="lazy" } | **Orc Lord**<br>ID: `1190` | **1** |
    | ![Orc Baby](assets/endless-tower/1686.gif){ .tower-monster-sprite loading="lazy" } | **Orc Baby**<br>ID: `1686` | **20** |

??? info "Floor 71 - 65 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Succubus](assets/endless-tower/1370.gif){ .tower-monster-sprite loading="lazy" } | **Succubus**<br>ID: `1370` | **20** |
    | ![Nightmare Terror](assets/endless-tower/1379.gif){ .tower-monster-sprite loading="lazy" } | **Nightmare Terror**<br>ID: `1379` | **20** |
    | ![Incubus](assets/endless-tower/1374.gif){ .tower-monster-sprite loading="lazy" } | **Incubus**<br>ID: `1374` | **20** |
    | ![Nightmare](assets/endless-tower/1061.gif){ .tower-monster-sprite loading="lazy" } | **Nightmare**<br>ID: `1061` | **5** |

??? info "Floor 72 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Margaretha Sorin](assets/endless-tower/1637.gif){ .tower-monster-sprite loading="lazy" } | **Margaretha Sorin**<br>ID: `1637` | **10** |
    | ![Permeter](assets/endless-tower/1314.gif){ .tower-monster-sprite loading="lazy" } | **Permeter**<br>ID: `1314` | **10** |
    | ![Errende Ebecee](assets/endless-tower/1655.gif){ .tower-monster-sprite loading="lazy" } | **Errende Ebecee**<br>ID: `1655` | **10** |
    | ![Enchanted Peach Tree](assets/endless-tower/1410.gif){ .tower-monster-sprite loading="lazy" } | **Enchanted Peach Tree**<br>ID: `1410` | **10** |

??? info "Floor 73 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Succubus](assets/endless-tower/1370.gif){ .tower-monster-sprite loading="lazy" } | **Succubus**<br>ID: `1370` | **10** |
    | ![Loli Ruri](assets/endless-tower/1505.gif){ .tower-monster-sprite loading="lazy" } | **Loli Ruri**<br>ID: `1505` | **20** |
    | ![Aliza](assets/endless-tower/1737.gif){ .tower-monster-sprite loading="lazy" } | **Aliza**<br>ID: `1737` | **10** |
    | ![Zealotus](assets/endless-tower/1200.gif){ .tower-monster-sprite loading="lazy" } | **Zealotus**<br>ID: `1200` | **5** |
    | ![Alice](assets/endless-tower/1275.gif){ .tower-monster-sprite loading="lazy" } | **Alice**<br>ID: `1275` | **5** |
    | ![Green Maiden](assets/endless-tower/1519.gif){ .tower-monster-sprite loading="lazy" } | **Green Maiden**<br>ID: `1519` | **10** |

??? info "Floor 74 - 54 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Dimik](assets/endless-tower/1671.gif){ .tower-monster-sprite loading="lazy" } | **Dimik**<br>ID: `1671` | **6** |
    | ![Dimik](assets/endless-tower/1673.gif){ .tower-monster-sprite loading="lazy" } | **Dimik**<br>ID: `1673` | **6** |
    | ![Dimik](assets/endless-tower/1672.gif){ .tower-monster-sprite loading="lazy" } | **Dimik**<br>ID: `1672` | **6** |
    | ![Venatu](assets/endless-tower/1677.gif){ .tower-monster-sprite loading="lazy" } | **Venatu**<br>ID: `1677` | **6** |
    | ![Dimik](assets/endless-tower/1670.gif){ .tower-monster-sprite loading="lazy" } | **Dimik**<br>ID: `1670` | **6** |
    | ![Archdam](assets/endless-tower/1668.gif){ .tower-monster-sprite loading="lazy" } | **Archdam**<br>ID: `1668` | **6** |
    | ![Venatu](assets/endless-tower/1678.gif){ .tower-monster-sprite loading="lazy" } | **Venatu**<br>ID: `1678` | **6** |
    | ![Venatu](assets/endless-tower/1679.gif){ .tower-monster-sprite loading="lazy" } | **Venatu**<br>ID: `1679` | **6** |
    | ![Venatu](assets/endless-tower/1676.gif){ .tower-monster-sprite loading="lazy" } | **Venatu**<br>ID: `1676` | **6** |

??? info "Floor 75 - 32 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Baphomet](assets/endless-tower/1039.gif){ .tower-monster-sprite loading="lazy" } | **Baphomet**<br>ID: `1039` | **1** |
    | ![Dark Lord](assets/endless-tower/1272.gif){ .tower-monster-sprite loading="lazy" } | **Dark Lord**<br>ID: `1272` | **1** |
    | ![Baphomet Jr.](assets/endless-tower/1101.gif){ .tower-monster-sprite loading="lazy" } | **Baphomet Jr.**<br>ID: `1101` | **20** |
    | ![Dark Illusion](assets/endless-tower/1302.gif){ .tower-monster-sprite loading="lazy" } | **Dark Illusion**<br>ID: `1302` | **10** |

## Floors 76-98

??? info "Floor 76 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Abysmal Knight](assets/endless-tower/1219.gif){ .tower-monster-sprite loading="lazy" } | **Abysmal Knight**<br>ID: `1219` | **30** |
    | ![Nightmare Terror](assets/endless-tower/1379.gif){ .tower-monster-sprite loading="lazy" } | **Nightmare Terror**<br>ID: `1379` | **20** |
    | ![Nightmare](assets/endless-tower/1061.gif){ .tower-monster-sprite loading="lazy" } | **Nightmare**<br>ID: `1061` | **10** |

??? info "Floor 77 - 70 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Banshee](assets/endless-tower/1867.gif){ .tower-monster-sprite loading="lazy" } | **Banshee**<br>ID: `1867` | **30** |
    | ![Wraith Dead](assets/endless-tower/1291.gif){ .tower-monster-sprite loading="lazy" } | **Wraith Dead**<br>ID: `1291` | **10** |
    | ![Evil Druid](assets/endless-tower/1117.gif){ .tower-monster-sprite loading="lazy" } | **Evil Druid**<br>ID: `1117` | **10** |
    | ![Wraith](assets/endless-tower/1192.gif){ .tower-monster-sprite loading="lazy" } | **Wraith**<br>ID: `1192` | **10** |
    | ![Wind Ghost](assets/endless-tower/1263.gif){ .tower-monster-sprite loading="lazy" } | **Wind Ghost**<br>ID: `1263` | **10** |

??? info "Floor 78 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Sword Master](assets/endless-tower/1829.gif){ .tower-monster-sprite loading="lazy" } | **Sword Master**<br>ID: `1829` | **5** |
    | ![Bloody Knight](assets/endless-tower/1268.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Knight**<br>ID: `1268` | **10** |
    | ![Abysmal Knight](assets/endless-tower/1219.gif){ .tower-monster-sprite loading="lazy" } | **Abysmal Knight**<br>ID: `1219` | **5** |
    | ![Dullahan](assets/endless-tower/1504.gif){ .tower-monster-sprite loading="lazy" } | **Dullahan**<br>ID: `1504` | **10** |
    | ![Raydric](assets/endless-tower/1163.gif){ .tower-monster-sprite loading="lazy" } | **Raydric**<br>ID: `1163` | **20** |

??? info "Floor 79 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Hydro](assets/endless-tower/1720.gif){ .tower-monster-sprite loading="lazy" } | **Hydro**<br>ID: `1720` | **10** |
    | ![Ferus](assets/endless-tower/1714.gif){ .tower-monster-sprite loading="lazy" } | **Ferus**<br>ID: `1714` | **10** |
    | ![Ferus](assets/endless-tower/1717.gif){ .tower-monster-sprite loading="lazy" } | **Ferus**<br>ID: `1717` | **10** |
    | ![Deleter](assets/endless-tower/1385.gif){ .tower-monster-sprite loading="lazy" } | **Deleter**<br>ID: `1385` | **5** |
    | ![Petite](assets/endless-tower/1155.gif){ .tower-monster-sprite loading="lazy" } | **Petite**<br>ID: `1155` | **5** |

??? info "Floor 80 - 16 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Falling Bishop](assets/endless-tower/1871.gif){ .tower-monster-sprite loading="lazy" } | **Falling Bishop**<br>ID: `1871` | **1** |
    | ![Necromancer](assets/endless-tower/1870.gif){ .tower-monster-sprite loading="lazy" } | **Necromancer**<br>ID: `1870` | **15** |

??? info "Floor 81 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Mysteltainn](assets/endless-tower/1203.gif){ .tower-monster-sprite loading="lazy" } | **Mysteltainn**<br>ID: `1203` | **20** |
    | ![Ogretooth](assets/endless-tower/1204.gif){ .tower-monster-sprite loading="lazy" } | **Ogretooth**<br>ID: `1204` | **20** |
    | ![Executioner](assets/endless-tower/1205.gif){ .tower-monster-sprite loading="lazy" } | **Executioner**<br>ID: `1205` | **20** |

??? info "Floor 82 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Bloody Knight](assets/endless-tower/1268.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Knight**<br>ID: `1268` | **10** |
    | ![Agav](assets/endless-tower/1769.gif){ .tower-monster-sprite loading="lazy" } | **Agav**<br>ID: `1769` | **10** |
    | ![Bloody Murderer](assets/endless-tower/1507.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Murderer**<br>ID: `1507` | **10** |
    | ![Skogul](assets/endless-tower/1752.gif){ .tower-monster-sprite loading="lazy" } | **Skogul**<br>ID: `1752` | **10** |
    | ![Injustice](assets/endless-tower/1257.gif){ .tower-monster-sprite loading="lazy" } | **Injustice**<br>ID: `1257` | **10** |

??? info "Floor 83 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Skeggiold](assets/endless-tower/1754.gif){ .tower-monster-sprite loading="lazy" } | **Skeggiold**<br>ID: `1754` | **10** |
    | ![Dark Illusion](assets/endless-tower/1302.gif){ .tower-monster-sprite loading="lazy" } | **Dark Illusion**<br>ID: `1302` | **10** |
    | ![Gryphon](assets/endless-tower/1259.gif){ .tower-monster-sprite loading="lazy" } | **Gryphon**<br>ID: `1259` | **10** |
    | ![Chimera](assets/endless-tower/1283.gif){ .tower-monster-sprite loading="lazy" } | **Chimera**<br>ID: `1283` | **10** |

??? info "Floor 84 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Succubus](assets/endless-tower/1370.gif){ .tower-monster-sprite loading="lazy" } | **Succubus**<br>ID: `1370` | **10** |
    | ![Dark Illusion](assets/endless-tower/1302.gif){ .tower-monster-sprite loading="lazy" } | **Dark Illusion**<br>ID: `1302` | **20** |
    | ![Owl Duke](assets/endless-tower/1320.gif){ .tower-monster-sprite loading="lazy" } | **Owl Duke**<br>ID: `1320` | **10** |
    | ![Owl Baron](assets/endless-tower/1295.gif){ .tower-monster-sprite loading="lazy" } | **Owl Baron**<br>ID: `1295` | **10** |
    | ![Incubus](assets/endless-tower/1374.gif){ .tower-monster-sprite loading="lazy" } | **Incubus**<br>ID: `1374` | **10** |

??? info "Floor 85 - 1 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Ifrit](assets/endless-tower/1832.gif){ .tower-monster-sprite loading="lazy" } | **Ifrit**<br>ID: `1832` | **1** |

??? info "Floor 86 - 40 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Hydro](assets/endless-tower/1720.gif){ .tower-monster-sprite loading="lazy" } | **Hydro**<br>ID: `1720` | **10** |
    | ![Gryphon](assets/endless-tower/1259.gif){ .tower-monster-sprite loading="lazy" } | **Gryphon**<br>ID: `1259` | **10** |
    | ![Chimera](assets/endless-tower/1283.gif){ .tower-monster-sprite loading="lazy" } | **Chimera**<br>ID: `1283` | **10** |
    | ![Majoruros](assets/endless-tower/1310.gif){ .tower-monster-sprite loading="lazy" } | **Majoruros**<br>ID: `1310` | **10** |

??? info "Floor 87 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Salamander](assets/endless-tower/1831.gif){ .tower-monster-sprite loading="lazy" } | **Salamander**<br>ID: `1831` | **15** |
    | ![Kasa](assets/endless-tower/1833.gif){ .tower-monster-sprite loading="lazy" } | **Kasa**<br>ID: `1833` | **20** |
    | ![Lava Golem](assets/endless-tower/1366.gif){ .tower-monster-sprite loading="lazy" } | **Lava Golem**<br>ID: `1366` | **15** |
    | ![Gajomart](assets/endless-tower/1309.gif){ .tower-monster-sprite loading="lazy" } | **Gajomart**<br>ID: `1309` | **10** |

??? info "Floor 88 - 60 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Necromancer](assets/endless-tower/1870.gif){ .tower-monster-sprite loading="lazy" } | **Necromancer**<br>ID: `1870` | **15** |
    | ![Anubis](assets/endless-tower/1098.gif){ .tower-monster-sprite loading="lazy" } | **Anubis**<br>ID: `1098` | **15** |
    | ![Wraith Dead](assets/endless-tower/1291.gif){ .tower-monster-sprite loading="lazy" } | **Wraith Dead**<br>ID: `1291` | **10** |
    | ![Ancient Mummy](assets/endless-tower/1297.gif){ .tower-monster-sprite loading="lazy" } | **Ancient Mummy**<br>ID: `1297` | **10** |
    | ![Khalitzburg](assets/endless-tower/1132.gif){ .tower-monster-sprite loading="lazy" } | **Khalitzburg**<br>ID: `1132` | **10** |

??? info "Floor 89 - 24 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Odium of Thanatos](assets/endless-tower/1704.gif){ .tower-monster-sprite loading="lazy" } | **Odium of Thanatos**<br>ID: `1704` | **6** |
    | ![Despero of Thanatos](assets/endless-tower/1705.gif){ .tower-monster-sprite loading="lazy" } | **Despero of Thanatos**<br>ID: `1705` | **6** |
    | ![Maero of Thanatos](assets/endless-tower/1706.gif){ .tower-monster-sprite loading="lazy" } | **Maero of Thanatos**<br>ID: `1706` | **6** |
    | ![Dolor of Thanatos](assets/endless-tower/1707.gif){ .tower-monster-sprite loading="lazy" } | **Dolor of Thanatos**<br>ID: `1707` | **6** |

??? info "Floor 90 - 31 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Valkyrie Randgris](assets/endless-tower/1751.gif){ .tower-monster-sprite loading="lazy" } | **Valkyrie Randgris**<br>ID: `1751` | **1** |
    | ![Baroness of Retribution](assets/endless-tower/1702.gif){ .tower-monster-sprite loading="lazy" } | **Baroness of Retribution**<br>ID: `1702` | **10** |
    | ![Lady Solace](assets/endless-tower/1703.gif){ .tower-monster-sprite loading="lazy" } | **Lady Solace**<br>ID: `1703` | **10** |
    | ![False Angel](assets/endless-tower/1371.gif){ .tower-monster-sprite loading="lazy" } | **False Angel**<br>ID: `1371` | **10** |

??? info "Floor 91 - 50 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Cecil Damon](assets/endless-tower/1638.gif){ .tower-monster-sprite loading="lazy" } | **Cecil Damon**<br>ID: `1638` | **10** |
    | ![Bow Master](assets/endless-tower/1830.gif){ .tower-monster-sprite loading="lazy" } | **Bow Master**<br>ID: `1830` | **10** |
    | ![Kavac](assets/endless-tower/1656.gif){ .tower-monster-sprite loading="lazy" } | **Kavac**<br>ID: `1656` | **30** |

??? info "Floor 92 - 55 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Kathryne Keyron](assets/endless-tower/1639.gif){ .tower-monster-sprite loading="lazy" } | **Kathryne Keyron**<br>ID: `1639` | **15** |
    | ![Elder](assets/endless-tower/1377.gif){ .tower-monster-sprite loading="lazy" } | **Elder**<br>ID: `1377` | **10** |
    | ![Laurell Weinder](assets/endless-tower/1657.gif){ .tower-monster-sprite loading="lazy" } | **Laurell Weinder**<br>ID: `1657` | **10** |
    | ![Wind Ghost](assets/endless-tower/1263.gif){ .tower-monster-sprite loading="lazy" } | **Wind Ghost**<br>ID: `1263` | **10** |
    | ![Marduk](assets/endless-tower/1140.gif){ .tower-monster-sprite loading="lazy" } | **Marduk**<br>ID: `1140` | **10** |

??? info "Floor 93 - 45 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Seyren Windsor](assets/endless-tower/1634.gif){ .tower-monster-sprite loading="lazy" } | **Seyren Windsor**<br>ID: `1634` | **15** |
    | ![Bloody Knight](assets/endless-tower/1268.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Knight**<br>ID: `1268` | **10** |
    | ![Abysmal Knight](assets/endless-tower/1219.gif){ .tower-monster-sprite loading="lazy" } | **Abysmal Knight**<br>ID: `1219` | **10** |
    | ![Wanderer](assets/endless-tower/1208.gif){ .tower-monster-sprite loading="lazy" } | **Wanderer**<br>ID: `1208` | **10** |

??? info "Floor 94 - 30 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Sword Master](assets/endless-tower/1829.gif){ .tower-monster-sprite loading="lazy" } | **Sword Master**<br>ID: `1829` | **15** |
    | ![Bow Master](assets/endless-tower/1830.gif){ .tower-monster-sprite loading="lazy" } | **Bow Master**<br>ID: `1830` | **15** |

??? info "Floor 95 - 46 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Beelzebub](assets/endless-tower/1873.gif){ .tower-monster-sprite loading="lazy" } | **Beelzebub**<br>ID: `1873` | **1** |
    | ![Hunter Fly](assets/endless-tower/1035.gif){ .tower-monster-sprite loading="lazy" } | **Hunter Fly**<br>ID: `1035` | **30** |
    | ![Steel Chonchon](assets/endless-tower/1042.gif){ .tower-monster-sprite loading="lazy" } | **Steel Chonchon**<br>ID: `1042` | **5** |
    | ![Dragon FLy](assets/endless-tower/1091.gif){ .tower-monster-sprite loading="lazy" } | **Dragon FLy**<br>ID: `1091` | **5** |
    | ![Chonchon](assets/endless-tower/1011.gif){ .tower-monster-sprite loading="lazy" } | **Chonchon**<br>ID: `1011` | **5** |

??? info "Floor 96 - 25 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Valkyrie](assets/endless-tower/1765.gif){ .tower-monster-sprite loading="lazy" } | **Valkyrie**<br>ID: `1765` | **5** |
    | ![Skeggiold](assets/endless-tower/1755.gif){ .tower-monster-sprite loading="lazy" } | **Skeggiold**<br>ID: `1755` | **10** |
    | ![Skeggiold](assets/endless-tower/1754.gif){ .tower-monster-sprite loading="lazy" } | **Skeggiold**<br>ID: `1754` | **10** |

??? info "Floor 97 - 20 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Incarnation of Morroc](assets/endless-tower/1918.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1918` | **5** |
    | ![Incarnation of Morroc](assets/endless-tower/1919.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1919` | **5** |
    | ![Incarnation of Morroc](assets/endless-tower/1920.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1920` | **5** |
    | ![Incarnation of Morroc](assets/endless-tower/1921.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1921` | **5** |

??? info "Floor 98 - 12 monsters"

    | Sprite | Monster | Count |
    | --- | --- | ---: |
    | ![Kathryne Keyron](assets/endless-tower/1639.gif){ .tower-monster-sprite loading="lazy" } | **Kathryne Keyron**<br>ID: `1639` | **2** |
    | ![Seyren Windsor](assets/endless-tower/1634.gif){ .tower-monster-sprite loading="lazy" } | **Seyren Windsor**<br>ID: `1634` | **2** |
    | ![Margaretha Sorin](assets/endless-tower/1637.gif){ .tower-monster-sprite loading="lazy" } | **Margaretha Sorin**<br>ID: `1637` | **2** |
    | ![Eremes Guile](assets/endless-tower/1635.gif){ .tower-monster-sprite loading="lazy" } | **Eremes Guile**<br>ID: `1635` | **2** |
    | ![Howard Alt-Eisen](assets/endless-tower/1636.gif){ .tower-monster-sprite loading="lazy" } | **Howard Alt-Eisen**<br>ID: `1636` | **2** |
    | ![Cecil Damon](assets/endless-tower/1638.gif){ .tower-monster-sprite loading="lazy" } | **Cecil Damon**<br>ID: `1638` | **2** |

## Floor 99 - random encounters

**Seven groups** are selected independently from the following **30 possibilities**. A group can be selected more than once, so its monsters may appear repeatedly. The count shown is the number spawned each time that group is selected.

| Group | Sprite | Monster | Per selection |
| --- | --- | --- | ---: |
| 1 | ![Kathryne Keyron](assets/endless-tower/1639.gif){ .tower-monster-sprite loading="lazy" } | **Kathryne Keyron**<br>ID: `1639` | **2** |
| 2 | ![Seyren Windsor](assets/endless-tower/1634.gif){ .tower-monster-sprite loading="lazy" } | **Seyren Windsor**<br>ID: `1634` | **2** |
| 3 | ![Margaretha Sorin](assets/endless-tower/1637.gif){ .tower-monster-sprite loading="lazy" } | **Margaretha Sorin**<br>ID: `1637` | **2** |
| 4 | ![Eremes Guile](assets/endless-tower/1635.gif){ .tower-monster-sprite loading="lazy" } | **Eremes Guile**<br>ID: `1635` | **2** |
| 5 | ![Howard Alt-Eisen](assets/endless-tower/1636.gif){ .tower-monster-sprite loading="lazy" } | **Howard Alt-Eisen**<br>ID: `1636` | **2** |
| 6 | ![Cecil Damon](assets/endless-tower/1638.gif){ .tower-monster-sprite loading="lazy" } | **Cecil Damon**<br>ID: `1638` | **2** |
| 7 | ![Incarnation of Morroc](assets/endless-tower/1918.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1918` | **5** |
| 8 | ![Incarnation of Morroc](assets/endless-tower/1919.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1919` | **5** |
| 9 | ![Incarnation of Morroc](assets/endless-tower/1920.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1920` | **5** |
| 10 | ![Incarnation of Morroc](assets/endless-tower/1921.gif){ .tower-monster-sprite loading="lazy" } | **Incarnation of Morroc**<br>ID: `1921` | **5** |
| 11 | ![Valkyrie](assets/endless-tower/1765.gif){ .tower-monster-sprite loading="lazy" } | **Valkyrie**<br>ID: `1765` | **5** |
| 12 | ![Skeggiold](assets/endless-tower/1755.gif){ .tower-monster-sprite loading="lazy" } | **Skeggiold**<br>ID: `1755` | **10** |
| 13 | ![Skeggiold](assets/endless-tower/1754.gif){ .tower-monster-sprite loading="lazy" } | **Skeggiold**<br>ID: `1754` | **10** |
| 14 | ![Seyren Windsor](assets/endless-tower/1634.gif){ .tower-monster-sprite loading="lazy" } | **Seyren Windsor**<br>ID: `1634` | **15** |
| 15 | ![Bloody Knight](assets/endless-tower/1268.gif){ .tower-monster-sprite loading="lazy" } | **Bloody Knight**<br>ID: `1268` | **10** |
| 16 | ![Abysmal Knight](assets/endless-tower/1219.gif){ .tower-monster-sprite loading="lazy" } | **Abysmal Knight**<br>ID: `1219` | **10** |
| 17 | ![Wanderer](assets/endless-tower/1208.gif){ .tower-monster-sprite loading="lazy" } | **Wanderer**<br>ID: `1208` | **10** |
| 18 | ![Sword Master](assets/endless-tower/1829.gif){ .tower-monster-sprite loading="lazy" } | **Sword Master**<br>ID: `1829` | **15** |
| 19 | ![Bow Master](assets/endless-tower/1830.gif){ .tower-monster-sprite loading="lazy" } | **Bow Master**<br>ID: `1830` | **15** |
| 20 | ![Kathryne Keyron](assets/endless-tower/1639.gif){ .tower-monster-sprite loading="lazy" } | **Kathryne Keyron**<br>ID: `1639` | **15** |
| 21 | ![Elder](assets/endless-tower/1377.gif){ .tower-monster-sprite loading="lazy" } | **Elder**<br>ID: `1377` | **10** |
| 22 | ![Laurell Weinder](assets/endless-tower/1657.gif){ .tower-monster-sprite loading="lazy" } | **Laurell Weinder**<br>ID: `1657` | **10** |
| 23 | ![Wind Ghost](assets/endless-tower/1263.gif){ .tower-monster-sprite loading="lazy" } | **Wind Ghost**<br>ID: `1263` | **10** |
| 24 | ![Marduk](assets/endless-tower/1140.gif){ .tower-monster-sprite loading="lazy" } | **Marduk**<br>ID: `1140` | **10** |
| 25 | ![Cecil Damon](assets/endless-tower/1638.gif){ .tower-monster-sprite loading="lazy" } | **Cecil Damon**<br>ID: `1638` | **10** |
| 26 | ![Bow Master](assets/endless-tower/1830.gif){ .tower-monster-sprite loading="lazy" } | **Bow Master**<br>ID: `1830` | **10** |
| 27 | ![Kavach Icarus](assets/endless-tower/1656.gif){ .tower-monster-sprite loading="lazy" } | **Kavach Icarus**<br>ID: `1656` | **30** |
| 28 | ![Baroness of Retribution](assets/endless-tower/1702.gif){ .tower-monster-sprite loading="lazy" } | **Baroness of Retribution**<br>ID: `1702` | **10** |
| 29 | ![Lady Solace](assets/endless-tower/1703.gif){ .tower-monster-sprite loading="lazy" } | **Lady Solace**<br>ID: `1703` | **10** |
| 30 | ![False Angel](assets/endless-tower/1371.gif){ .tower-monster-sprite loading="lazy" } | **False Angel**<br>ID: `1371` | **10** |

## Floor 100 - Entweihen Crothen

Face **Entweihen Crothen** with the following fixed thorn spawns. **Two additional thorns** also spawn; each is randomly selected from **Thorny Skeleton, Thorn of Magic or Thorn of Pureness**.

| Sprite | Monster | Count |
| --- | --- | ---: |
| ![Entweihen Crothen](assets/endless-tower/1957.gif){ .tower-monster-sprite loading="lazy" } | **Entweihen Crothen**<br>ID: `1957` | **1** |
| ![Thorny Skeleton](assets/endless-tower/1958.gif){ .tower-monster-sprite loading="lazy" } | **Thorny Skeleton**<br>ID: `1958` | **9** |
| ![Thorn of Magic](assets/endless-tower/1960.gif){ .tower-monster-sprite loading="lazy" } | **Thorn of Magic**<br>ID: `1960` | **8** |
| ![Thorn of Pureness](assets/endless-tower/1961.gif){ .tower-monster-sprite loading="lazy" } | **Thorn of Pureness**<br>ID: `1961` | **4** |
| ![Thorn of Recovery](assets/endless-tower/1959.gif){ .tower-monster-sprite loading="lazy" } | **Thorn of Recovery**<br>ID: `1959` | **4** |

## Floor 101 - final encounter

Clear the waves in order. Each wave must be defeated before the next encounter begins; **Naght Sieger** is the final opponent. The names shown below are the tower-specific monster names.

| Wave | Sprite | Monster | Count |
| --- | --- | --- | ---: |
| 1 | ![Watcher's Son](assets/endless-tower/1627.gif){ .tower-monster-sprite loading="lazy" } | **Watcher's Son**<br>ID: `1627` | **10** |
| 2 | ![Bone Guardian](assets/endless-tower/1152.gif){ .tower-monster-sprite loading="lazy" } | **Bone Guardian**<br>ID: `1152` | **100** |
| 3 | ![Wind Guardian](assets/endless-tower/1263.gif){ .tower-monster-sprite loading="lazy" } | **Wind Guardian**<br>ID: `1263` | **60** |
| 4 | ![Sword Edge Guardian](assets/endless-tower/1132.gif){ .tower-monster-sprite loading="lazy" } | **Sword Edge Guardian**<br>ID: `1132` | **40** |
| 5 | ![Naght Sieger](assets/endless-tower/1956.gif){ .tower-monster-sprite loading="lazy" } | **Naght Sieger**<br>ID: `1956` | **1** |

</div>

## Related guides

- [Hunting and Instance Guide](dungeons.md)
- [Warper](warper.md)
- [RODEX mail](quality-of-life.md#rodex-mail)
