# VibeDeck 



VibeDeck is my 9-key macropad, built for Hack Club's Hackpad / stardance challenge



I wanted to make something small and simple beacause i was new to these so that I could design and build myself, and decided to use a Seeed XIAO RP2040 as mentioned in (hackclubs docs )with 9 mechanical switches.



## What's in it



- 9 mechanical switches



- Seeed XIAO RP2040



- 9x 1N4148 diodes



- 1x SK6812MINI RGB LED



- USB-C



- Custom PCB (KiCad)



- Custom case (FreeCAD)



## The PCB



Designed in KiCad; has 9 individual switch inputs and 1 SK6812MINI RGB LED input. KiCad's DRC is pretty strict, but I managed to fix all the errors and got a good result

<img width="605" height="706" alt="image" src="https://github.com/user-attachments/assets/2293b751-79ee-4578-bbdd-fe98be769f4f" />

<img width="642" height="662" alt="image" src="https://github.com/user-attachments/assets/727ee534-4015-4b21-b2fd-9d358fdb4c33" />

<img width="525" height="692" alt="image" src="https://github.com/user-attachments/assets/7e4ed0f7-8898-4325-b89d-ab4d231d9be6" />








## The Case



I used the [Custom Micropad](https://github.com/BenGreenberg07/custom-micropad) case by Ben Greenberg as a base for my own design, modifying it to fit my VibeDeck PCB. I exported my modified top and bottom parts as STEP files.

<img width="1015" height="712" alt="image" src="https://github.com/user-attachments/assets/d5d05b85-7214-4eed-8a41-ed4b81142685" />






## Firmware (KMK / CircuitPython)



VibeDeck uses KMK firmware with CircuitPython, located in the `firmware` directory. The 9 keys are directly connected to individual GPIOs on the XIAO RP2040, and the SK6812MINI is connected separately.



## What I learned



This was my first ever PCB, so I learned a lot on the way. KiCad's PCB routing and DRC tools were a bit difficult to get use at first but i eventually learned how to make a complete working design! I also learned how to use FreeCAD and how the case parts interact with the PCB.



The case design was also quite challenging, and required many iterations before I was satisfied with the result.



## Credits
Almost evrything is made by me except the case CAD i edited someone else's CAD files I did not use them directly. i DONt know how to write a readme and this is not AI. 



| Case | [Ben Greenberg's Custom Micropad](https://github.com/BenGreenberg07/custom-micropad) + Me |



| Hack Club's Hackpad / Stardance challenge | [Hack Club](https://hackclub.com/) |
