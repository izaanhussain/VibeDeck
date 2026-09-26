# VibeDeck 



VibeDeck is my 9-key macropad, built for Hack Club's Hackpad / Stardance challenge



I wanted to make something small and simple that I could design and build myself, and decided to use a Seeed XIAO RP2040 with 9 mechanical switches.



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



<img width="657" height="672" alt="image" src="https://github.com/user-attachments/assets/0b1e42f6-eaed-405a-95eb-6a3169754674" />
<img width="696" height="682" alt="image" src="https://github.com/user-attachments/assets/7a1669e1-019d-42bf-8736-22a7cae94044" />
<img width="618" height="675" alt="image" src="https://github.com/user-attachments/assets/b31bbd06-1c76-4abf-b77a-7c5738970958" />





## The Case



I used the [Custom Micropad](https://github.com/BenGreenberg07/custom-micropad) case by Ben Greenberg as a base for my own design, modifying it to fit my VibeDeck PCB. I exported my modified top and bottom parts as STEP files.



<img width="1037" height="726" alt="image" src="https://github.com/user-attachments/assets/a0dc9cc3-7058-44f3-8926-e2c60d1d4789" />



## Firmware (KMK / CircuitPython)



VibeDeck uses KMK firmware with CircuitPython, located in the `firmware` directory. The 9 keys are directly connected to individual GPIOs on the XIAO RP2040, and the SK6812MINI is connected separately.



## What I learned



This was my first ever PCB, so I learned a lot on the way. KiCad's PCB routing and DRC tools were a bit difficult to get used to, but I eventually learned how to make a complete working design! I also learned how to use FreeCAD and how the case parts interact with the PCB.



The case design was also quite challenging, and required many iterations before I was satisfied with the result.



## Credits



| Category | Contributor(s) |



| --- | --- |



| PCB + Electronics | Me |



| Case | [Ben Greenberg's Custom Micropad](https://github.com/BenGreenberg07/custom-micropad) + Me |



| Hack Club's Hackpad / Stardance challenge | [Hack Club](https://hackclub.com/) |
