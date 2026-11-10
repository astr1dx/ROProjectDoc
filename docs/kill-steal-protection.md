# Kill Steal Protection

Updated: **November 10, 2026**.

**`@noks`** protects ordinary monsters you are fighting from other players' attacks. Choose who may help through its menu, or open **`@settings` > Kill Steal Protection**. Both entry points use the same saved choice.

Protection defaults to **Party** for existing and new characters without a saved choice. Your mode is saved **per character** and restored on login. A saved Off choice remains Off.

## Choose a mode

| Mode | Who may attack your protected monsters? |
| --- | --- |
| Self | You and your own companions only. Party and guild membership do not grant access. |
| Party | You and your current party members. |
| Guild | You and your current guild members. Party membership alone does not grant access. |
| Disable protection | No kill-steal protection for your monsters. |

Party and Guild require a matching, nonempty membership. Choosing a mode does not reset a monster's existing protection timers.

## When protection starts

An eligible monster can become protected when:

- It selects you or one of your companions as its combat target.
- You or your companion deal positive damage from **outside the monster's aggro range**, before its targeting catches up.

Merely selecting a passive monster or starting a targeted cast does not claim it. An already-idle player does not gain a fresh protection window just because a monster targets them.

There is **no limit on the number of protected monsters**. Your pet, homunculus, mercenary and elemental follow your ownership and access rules.

## Release timers

Protection ends when **any** applicable deadline is reached:

| Rule | Duration | When it starts |
| --- | --- | --- |
| Idle release | 5 seconds | Since the owner's last attack, skill use or movement. Continuous walking counts as movement. |
| Contest timer | 15 seconds | At the first unauthorized attack or targeted-cast attempt against the protected monster. |
| Hard cap | 30 seconds | When that monster first becomes protected. |

**Chat, item use and emotes do not keep the idle timer alive.** Attacking, helping allies or repeatedly attempting to steal a monster does not restart the contest timer or extend the hard cap.

For example, if protection starts at 0 seconds and an outsider first tries to attack at 20 seconds, the **30-second hard cap** ends the lock before the contest timer would finish at 35 seconds. Idle release can end it earlier.

Once released, the same ongoing encounter stays open. Continuing to attack does not immediately renew its protection; the monster must drop that target or select a different owner before a new encounter can be protected. Owner death, logout, leaving the map or disabling protection also releases the lock. A respawn starts with fresh state.

## Check your party

Type **`@nokscheck`** to see your own mode and your party members' current modes. The report is private and does not change anyone's settings.

Use **Party** when everyone in the party should be able to help attack each other's protected monsters. **Self** can block party members; **Guild** permits only matching guild members.

Offline members and members whose settings are unavailable on another map server are marked **not checked**, rather than being reported as Off. Without a party, the command reports your own mode and explains that you are not in a party.

## Exceptions and normal reward rules

Protection does not apply to:

- **MVPs** and **Boss-mode mini-bosses**.
- Monsters controlled as native summoned slaves.
- **Towns**, **PvP**, **GvG/WoE** and **Battleground** maps.
- Maps explicitly configured to allow kill stealing.

Attack permission does not replace the normal EXP, loot ownership or party-sharing rules. Use [Kill Count](kill-count.md) to review credited kills and [Card Drop Announcements](card-drop-announcements.md) to understand who is credited with receiving a card.

## Verification

**Confirmed in-game:** Self blocks other players, and Party allows party members. Automated checks cover timer boundaries, nonrenewing deadlines, companion ownership, exclusions, ordinary-player access, shared menu state and saved modes across logins.
