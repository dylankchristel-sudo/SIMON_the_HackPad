# How I cooked my microcontroller

When I first soldered my XIAO onto my PCB, I put the pins through the controller and soldered the ends to the pads of the PCB. I didn't realize I also needed to solder the controller to the pins. Because of this, I left the black bracket over the area I needed to solder.

When I realized that I had messed up, I tried to pull the brackets off, but they were stuck(probably from getting accidentally melted during the first solder attempt), so I tried to clip the bracket off with wire cutters.

This went terribly. I clipped one of the resistors clean off the controller. I thought I was totally cooked.

After I did some research, I realized I could work around the issue in my code. HOWEVER, when I was debugging later, I realized the code wouldn't run properly until I soldered it together properly.
So ever so carefully I used the wire cutters again(I'll never learn ig) to remove the brackets. And it worked! I was able to solder it up with minimal issues.

So I go to plug it in aaaaand nothing. No connection. No lights. I bricked it. I can only assume my soldering iron cooked the chip and broke the internals.


# What Now?

I've ordered a new XAIO RP 2040 board and just have to recode it and replace the broken board with the new one. The only problem now is that my solder job was a mess, and it's going to be tough to remove the first board.
But I trust in the power of YouTube tutorials to help me fix this in time.
