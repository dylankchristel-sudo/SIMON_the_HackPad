Sorry in advance, I know this isn't the usual format, but I am writing this after the fact, so I'm reorganizing into steps instead of days.
# Step 1 Set Up
I installed KiCad and downloaded the libraries for the parts' footprints and symbols.
Getting the right libraries downloaded took much longer than it should have. There were days of failed downloads, designing with incorrect parts, and starting over.
Eventually, I found out the right libraries were right in front of me all along. But I learned a lot about KiCad.
# Step 2 Schematic
I decided  to put as many parts as I could into SIMOND. I opted for: 5 buttons, a rotary encoder, 4 LEDs, and an OLED display.
The display took an extra amount of energy. I had to research: which display I would have, what SCL and SDA pins are, and where they are on my display and microcontroler.
Overall, it was very rewarding to finally write the schematic.
# Step 3 Edit PCB
I transferred the schematic to the PCB Editor. I arranged the final layout of the board and wired around my own poor planning.
I had a hard time wiring everything together without overlapping traces.
This took a lot of creative and "interesting" looking traces. But the PCB looked like it should work!
# Step 4 Case
I designed the case in Onshape. The case has two main parts: a bottom and a lid. I also printed some supports to take the weight off my microcontroller.
It took several iterations to get the right lid shape. First, I placed the hole for the OLED in the wrong place. After fixing that, I realized I had put the lid too low for the rotary encoder, so the case didn't close.
My final design addresses both of these issues and should fit perfectly.
# Step 4 Assembly
I soldered my very own PCB for the first time!
It took me a while to figure out how to use my soldering iron and clean the tip properly.
Also, I didn't realize that when I put the OLED and the microcontroller on opposite sides of the same place on my board, I would have to solder around my 2 most expensive parts.
Eventually, I got it mostly soldered together. I missed a few pins because I thought I wasn't supposed to solder them. I was very wrong.
# Step 5 Firmware
I wrote KMK firmware using CircuitPython in the MU editor.
I had problems at every turn here. Before I even started, I struggled to get the board to connect to my laptop. Then I couldn't find relevant examples for the longest time. Finally, I realized while I was debugging that I needed to solder both sides of the pins on my microcontroller and OLED display.
I finally figured it out and now the board types! However, I still need to re-solder and see if my code works for the OLED display, and if that fixes the connection to my laptop issue as well.
