VibeDeck 🎛️
VibeDeck is a custom 9-key programmable macropad built around the Seeed XIAO RP2040.
The goal is to make a compact and simple macropad with:
9 mechanical keys arranged in a 3×3 matrix
A single indicator light
USB-C connectivity through the XIAO RP2040
A custom PCB designed in KiCad
An edited case exported as STEP files
This project is being developed as part of Hack Club's Hackpad / Stardance project.
Features
9-key mechanical keyboard matrix
9 × 1N4148 signal diodes
Seeed XIAO RP2040
Single indicator LED
Custom PCB designed in KiCad
Custom-edited case exported as STEP
There is no rotary encoder and no OLED display in this version of VibeDeck.
Bill of Materials
9 × mechanical keyboard switches
9 × 1N4148 signal diodes
1 × Seeed XIAO RP2040
1 × indicator LED
Custom PCB
Custom case
Current Status
PCB
Schematic completed
PCB layout completed
3×3 key matrix routed
Indicator LED connected
PCB design checked with KiCad DRC
0 DRC errors
0 unconnected items
Case
The case geometry is based on the Custom Micropad case design by Ben Greenberg.
I did not upload the original case directly. I edited the case geometry for VibeDeck and exported my edited top and bottom case parts as STEP files.
Original case design:
https://github.com/BenGreenberg07/custom-micropad
Firmware
Firmware is still to be added.
Manufacturing Files
Gerber/manufacturing files are still to be added.
Project Structure
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
```
Software
KiCad — schematic and PCB design
FreeCAD — case editing
STEP — exported case CAD files
Why?
I wanted to build my own hardware while learning PCB design, CAD and embedded development.
This is my first PCB design, so VibeDeck has been a learning project throughout the Hack Club Hackpad / Stardance challenge.
Credits
PCB: Designed by me in KiCad.
Case: Based on the Custom Micropad by Ben Greenberg, then edited by me for VibeDeck.
Project challenge: Hack Club Hackpad / Stardance.
More documentation, firmware and manufacturing files will be added as the project is completed.
