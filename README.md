# AirPortSimulation
I made this simulation a final project for my  advanced python class in college.
I used data the data structures binaryTree, hashTable , and  ListStack.
I chose the binary tree because I could use it to hold the flight number codes to call back for later and to hold the event data.
I used the hashTable to store the data of flight numbers and airline pairs.
I used the stacks for departure queue, waiting in air, and terminal stack.
I would use a more efficient stack like a list queue because I had to add function to list stack to make it work for my purposes, and quadratic HashMap for better memory usage
I had encountered a problem with the hashMap were I couldn’t figure out how to store multiple data sets in order so that I could call them back so I just use a binary tree to call back to them in order since you can call in order on binary tree.

Side note most of the code I put in a separate file called airport so that it could be more organized and also more object oriented. The print function print out in format like this. (You call output 4 times for the different types event sets this could be made more efficient if I were to code this again)

Planes Departing In Order Event 3------------

Plane Number of 0 of the day PanAm Flight C426
