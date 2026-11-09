# Star Dock

**Play: https://frankamand.github.io/stardock/**

A remake of an old game of mine: a little rocket crosses a field of stars that pop up out of nowhere.
Stars blink for 5 seconds and are harmless, then turn solid and deadly. Dock nose-first with the moving station for 1000 points.

- Your ship rides down the launch station on the left; your first move launches it. Then steer up and down with the slide strip on the right, the arrow keys, or a gamepad (stick or D-pad).
- **Mine** clears nearby stars after 5 seconds. **Brake** fires reverse thrusters to time your docking.
- From level 2, planets drift across: skim past one for a gravity slingshot.
- Three levels with their own ship, station and music (space disco, then a brass march in A Lydian).
- Demo mode with an autopilot and a talkative space trader on channel 7.

Install it on Android: open the link in Chrome, then ⋮ → **Install app** (or Add to Home screen).

## Files
- `index.html`: the whole game (one file). Built from the Claude artifact version with `tools/build_site.py`.
- `sw.js`: offline cache. Bump `VERSION` whenever a file changes.
- `manifest.webmanifest`, `icons/`: app name and icons.
- `fonts/`: Orbitron and Share Tech Mono (SIL Open Font License), so the game works offline.

The voice clips are rendered with sam-js, a port of SAM (1982, Don't Ask Software / SoftVoice, Inc.).
