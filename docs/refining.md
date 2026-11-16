# Refining System

Equipment refiners offer a choice between **Classic Refiner** and **Visual Refiner**. Both use our **Pre-Renewal** refining rules and stop at **+10**.

## Choose an interface

| Interface | Accepted ores | Equipment | Refining options |
| --- | --- | --- | --- |
| Classic Refiner | **Normal ores only** | Must be equipped | One attempt, safe-limit batch or a chosen target level |
| Visual Refiner | **Enriched ores only** | May be selected from inventory without equipping | One animated attempt, with displayed success chance and material requirements |

**HD ores are not offered in either interface.** Normal ores cannot be used in the Visual Refiner, and enriched ores cannot be used in the Classic Refiner.

!!! warning "Failure destroys the item"
    An unsuccessful attempt destroys the equipment, including its cards and options. Enriched ores improve success chances but do not protect against destruction.

## Classic Refiner

Equip an identified, refinable weapon or armor below +10. Rental equipment cannot be refined. Select the equipment, then choose **Refine once**, **Refine to the safe limit**, or **Choose a target refine level**.

| Equipment | Normal ore per attempt | Fee per attempt | Safe through |
| --- | --- | ---: | ---: |
| Level-1 weapon | 1 Phracon | 50z | +7 |
| Level-2 weapon | 1 Emveretarcon | 200z | +6 |
| Level-3 weapon | 1 Oridecon | 5,000z | +5 |
| Level-4 weapon | 1 Oridecon | 20,000z | +4 |
| Armor | 1 Elunium | 2,000z | +4 |

A bulk order charges **one ore and one fee for each attempt actually made**. It stops on failure, insufficient materials, insufficient Zeny or reaching the selected target. Canceling before confirmation consumes nothing.

## Visual Refiner

Select your equipment in the interface, choose its enriched ore and refine one level at a time. Every attempt costs **one ore and 2,000z**.

| Equipment | Accepted enriched ore | Item ID |
| --- | --- | ---: |
| Weapons | Enriched Oridecon | **7620** |
| Armor | Enriched Elunium | **7619** |

These are the same standard items supplied by existing boxes and reward packages. Duplicate ores were converted to these IDs with their quantities preserved, so the interface offers only one ore option for the selected equipment.

## Success rates

The tables show the chance to reach the listed **new refine level**. For example, the +5 column is the attempt from +4 to +5. Choosing the visual interface keeps Pre-Renewal mechanics; its enriched-ore chances are higher than the normal-ore chances.

### Normal ores

| Equipment | +1 | +2 | +3 | +4 | +5 | +6 | +7 | +8 | +9 | +10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Level-1 weapon | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 60% | 40% | 19% |
| Level-2 weapon | 100% | 100% | 100% | 100% | 100% | 100% | 60% | 40% | 20% | 19% |
| Level-3 weapon | 100% | 100% | 100% | 100% | 100% | 60% | 50% | 20% | 20% | 19% |
| Level-4 weapon / armor | 100% | 100% | 100% | 100% | 60% | 40% | 40% | 20% | 20% | 9% |

### Enriched ores

| Equipment | +1 | +2 | +3 | +4 | +5 | +6 | +7 | +8 | +9 | +10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Level-1 weapon | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 90% | 70% | 30% |
| Level-2 weapon | 100% | 100% | 100% | 100% | 100% | 100% | 90% | 70% | 40% | 30% |
| Level-3 weapon | 100% | 100% | 100% | 100% | 100% | 90% | 80% | 40% | 40% | 30% |
| Level-4 weapon / armor | 100% | 100% | 100% | 100% | 90% | 70% | 70% | 40% | 40% | 20% |

The normal and enriched +1 to +10 tables follow the [RateMyServer refining guide](https://ratemyserver.net/index.php?page=misc_table_refine).

## Refiner locations

| Refiner | Navigation |
| --- | --- |
| Hollgrehenn | `/navi prt_in 63/60` |
| Aragham | `/navi morocc_in 73/38` |
| Antonio | `/navi payon 144/173` |
| Fredrik | `/navi alberta_in 28/58` |
| Lambert | `/navi yuno_in01 171/21` |
| Manthasman | `/navi ein_in01 24/87` |
| Fulerr | `/navi lhz_in02 282/20` |
| Suhnbi | `/navi payon 157/146` |

Each of these refiners provides the same interface choice.
