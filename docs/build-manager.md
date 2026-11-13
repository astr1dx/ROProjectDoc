# Build Manager

Updated: **November 13, 2026**.

Save your current stat and skill allocations as named builds, then load them again when you want to switch setups. Builds are saved **per character** and remain available after relogging.

!!! info "Find the Build Manager"
    The Build Manager is in **Prontera at 154,193**, beside **Reset Girl at 150,193**.

    ```text
    /navi prontera 154/193
    ```

## Slots and fees

| Feature | Current rules |
| --- | --- |
| Stat builds | **10 slots** per character |
| Skill builds | **10 separate slots** per character |
| Save or overwrite a build | Free |
| Rename or delete a build | Free |
| Load one stat build | **5,000z** |
| Load one skill build | **5,000z** |

Stat builds and skill builds are managed separately. Loading both means loading each one individually, for **10,000z total**. There is no combined-load option.

## Save your current build

1. Allocate the stats or skills you want to keep.
2. Speak to the Build Manager and choose **Stat Builds** or **Skill Builds**.
3. Select an **Empty Slot**.
4. Enter a name, such as `Hunting Stats` or `Support Skills`.

The NPC saves your **current allocations**; it does not create an unlearned build for you. Names allow **1-24 bytes** and cannot contain colons, color codes, control characters, or spaces at either end. Plain English names fit within the limit as 1-24 characters.

## Load a saved build

1. Choose its build category and saved name.
2. Review the preview. Stat builds show all six base stats; skill builds show the saved class and number of allocated skills.
3. Select **Load Build - 5,000z**.
4. Confirm **Load for 5,000z**, or choose **Cancel** without paying.

Your **Base/Job Levels and EXP stay the same**. The saved allocation replaces the selected type of build, with any additional available points left unspent. Loading a stat build does not also load a skill build, or vice versa.

The server checks eligibility, point budgets, stat caps, skill prerequisites and Job Level requirements **before charging**. Insufficient Zeny or an invalid allocation does not consume the fee.

!!! note "Skill reset effects still apply"
    Loading a skill build performs a normal skill reset. Current buffs are removed, and normal reset handling applies to mounts, carts and homunculi. Permanent platinum skills remain learned. Equipment-granted, temporary, copied and Soul Link skills are not stored as learned build allocations.

## Rename, overwrite or delete

Select an existing build to use these actions:

- **Overwrite with Current Build** replaces its allocations with your current setup, keeping the name. Confirmation is required.
- **Rename Build** changes only its name.
- **Delete Build** permanently frees that slot after confirmation.

These actions are free. Overwriting or deleting does not change your currently allocated stats or skills.

## Class and level safeguards

| Situation | What happens |
| --- | --- |
| Your class changes, including upgrading, transcending or baby conversion | Saved **skill builds are deleted** because they belong to the previous class |
| Your Base Level falls below a stat build's saved Base Level | That **stat build is hidden**, remains saved and still occupies its slot |
| You reach the saved Base Level again | The stat build reappears automatically |
| A build exceeds your current points, stat cap, skill tree or prerequisites | Loading is refused without a fee |

A stat build is not deleted merely because your class changes, but it must still pass your current class's point and stat-limit checks when loaded. A skill build must match your **exact current class**; returning to an earlier class does not recover builds already deleted.

Finish any attack, cast, trade, shop or storage session before using the service, and use it while alive. **Ranked Taekwon characters** cannot use skill-build saving/loading because normal skill resets are unavailable to them; stat builds remain available.

See [Class Changes](class-changes.md) for platinum skills and [Server Information](server-rules.md) for level and stat caps.
