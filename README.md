# VibeDeck 🎛️

VibeDeck is a custom 9-key programmable macropad built around the **Seeed XIAO RP2040**.

The goal is to make a compact and simple macropad with:

- 9 mechanical keys arranged in a 3×3 matrix
- A single indicator LED
- USB-C connectivity through the XIAO RP2040
- A custom PCB designed in KiCad
- An edited case exported as STEP files

This project is being developed as part of **Hack Club's Hackpad / Stardance** project.

## Features

- 9-key mechanical keyboard matrix
- 9 × 1N4148 signal diodes
- Seeed XIAO RP2040
- Single indicator LED
- Custom PCB designed in KiCad
- Custom-edited case exported as STEP

> **Note:** VibeDeck does not have a rotary encoder or OLED display.

## Bill of Materials

- 9 × mechanical keyboard switches
- 9 × 1N4148 signal diodes
- 1 × Seeed XIAO RP2040
- 1 × indicator LED
- 1 × custom PCB
- 1 × custom case

## Current Status

### PCB

- Schematic completed
- PCB layout completed
- 3×3 key matrix routed
- Indicator LED connected
- PCB design checked with KiCad DRC
- **0 DRC errors**
- **0 unconnected items**

### Case

The case geometry is based on the **Custom Micropad** case design by **Ben Greenberg**.

I did **not** upload the original case directly. I edited the case geometry for VibeDeck and exported my edited top and bottom case parts as STEP files.

Original case design:

[Ben Greenberg's Custom Micropad](https://github.com/BenGreenberg07/custom-micropad)

### Firmware

Firmware is still to be added.

### Manufacturing Files

Gerber/manufacturing files are still to be added.

## Project Structure

```text
VibeDeck/
├── CAD/
│   ├── VibeDeck_Top.step
│   └── VibeDeck_Bottom.step
│
├── PCB/
│   ├── VibeDeck.kicad_pcb
│   └── Vibedeck schematic.kicad_sch
│
└── README.md

Credits
PCB: Designed by me in KiCad.
Case: Based on the Custom Micropad by Ben Greenberg, then edited by me for VibeDeck.
Project challenge: Hack Club Hackpad / Stardance
License

This project is shared for educational and personal use.

The case design is based on the original work by Ben Greenberg. Please refer to the original repository for its licensing and attribution requirements.

More documentation, firmware and manufacturing files will be added as the project is completed.
