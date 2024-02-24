This program takes an input image:
![test](https://github.com/pluix/stippler/assets/64772516/7a5ce5ac-b501-43f8-abfa-c7a3fadf061a)

And stipples it (try zooming in):
![new-0](https://github.com/pluix/stippler/assets/64772516/c46a851e-f1cb-4002-919d-d8a7759bb662)

The circles can be colorized and you can adjust the sizing:
![colorized](https://github.com/pluix/stippler/assets/64772516/f0256390-0132-4cff-9eaf-4165fe042b98)

It can also pixelate images (I threw this in for fun):
![pixelate](https://github.com/pluix/stippler/assets/64772516/73059ac3-461e-4006-8a76-c5244f9daa9f)

You can think of it like overlaying a grid on your image with a certain cell size, looking at the pixel in the middle of each cell, and drawing a circle in that cell with a size based on the brightness of that pixel. 

You can vary the cell size, background color, and circle color. You can also choose to blend the circles in the brightess areas and black out the circles in the darkest areas. Try experimenting with different values to see how the results vary. I've had a lot of fun playing with this as I've been making it <3
