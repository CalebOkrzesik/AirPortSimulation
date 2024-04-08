# Airport Simulator Project
# Main Simulation Controller

from Plane import *
from AirPort import *
import random

def main():
    # TODO: Create data structures for the simulation
    plane = Plane()
    airPort = AirPort(plane)

    #hash table to hold plane value that can be called later
    hashTarrives = HashTable(31)
    hashTlands = HashTable(31)
    hashTready = HashTable(31)
    hashTtakenOff = HashTable(31)

    #Binary trees save the plan numbers in different states
    binaryTreeArrive = BinaryTree()
    binaryTreeLands = BinaryTree()
    binaryTreeReady = BinaryTree()
    binaryTreeTakenOff = BinaryTree()

    #stores the event data for output
    binaryTreeStateZero = BinaryTree()
    binaryTreeStateOne = BinaryTree()
    binaryTreeStateTwo = BinaryTree()
    binaryTreeStateThree = BinaryTree()

    #Stack for the different queue and arrival system terminals
    terminalStack = ListStack() #stack for terminal to hold 4 at time
    waitingStackInAir = ListStack() #planes waiting to land
    departureStack = ListStack() #for planes leaving

    for i in range(50): # simulate 50 events happening today
        event = random.randint(0, 3)

        #check if planes are in queue for landing if so check terminal if there are any spots and adds if openings are there
        if airPort.checkForPlanes(terminalStack) == 1:
            terminalStack.push(waitingStackInAir.peekBottom())
            waitingStackInAir.popBottom()

        if event == 0: # a plane arrives
            plane = Plane()
            print("Arriving:",plane)
            hashTarrives.insert(plane) #adds plane to data structure for later use
            binaryTreeArrive.insert(plane.flightNo) #add plane num to data structure
            binaryTreeStateZero.insert(event) # Add the event for later refrences
            # TODO: Add plane to arrivals queue
            waitingStackInAir.push(plane) #add plane to queue air waiting stack

        elif event == 1: # a plane lands
            # TODO: If plane waiting to land, dequeue it
            # TODO: Add landed plane to terminal structure
            print("Landing:",plane)
            hashTlands.insert(plane)#adds plane to data structure for later use
            binaryTreeLands.insert(plane.flightNo)#add plane num to data structure
            binaryTreeStateOne.insert(event)  # Add the event for later refrences

            #Adds to plane to terminal or denies and pusehes back into the air
            size = terminalStack.size()
            if terminalStack.isEmpty() or size <= 3:
                print("Spots are open land please")
                terminalStack.push(plane) #add to terminal
            else:
                print("No spots open do not land")
                waitingStackInAir.push(plane) #add to air waiting stack


        elif event == 2: # a plane is ready to take off
            # TODO: Remove plane from terminal structure and add it to departures queue
            print("Taxiing:",plane)
            hashTready.insert(plane)#adds plane to data structure for later use
            binaryTreeReady.insert(plane.flightNo)#add plane num to data structure
            binaryTreeStateTwo.insert(event)  # Add the event for later refrences

        elif event == 3: # a plane has taken off
            # TODO: Dequeue plane from departure queue and archive it
            print("Departing:",plane)
            hashTtakenOff.insert(plane)#adds plane to data structure for later use
            binaryTreeTakenOff.insert(plane.flightNo)#add plane num to data structure
            binaryTreeStateThree.insert(event)  # Add the event for later refrences


            # check if planes are in queue for landing if so check terminal if there are any spots and adds if openings are there and
            # add to departure queue
            if airPort.checkForPlanes(terminalStack) == 1:
                terminalStack.push(waitingStackInAir.peekBottom())
                waitingStackInAir.popBottom()
            if event == 2:
                departureStack.push(plane)
            if event == 3 and False != departureStack.isEmpty():
                departureStack.popBottom()


    # TODO: Print a report of all today's planes
    airPort.output(binaryTreeArrive,hashTarrives, "Arriving", binaryTreeStateZero)
    airPort.output(binaryTreeLands, hashTlands, "Landing", binaryTreeStateOne)
    airPort.output(binaryTreeReady, hashTready, "Taxiing", binaryTreeStateTwo)
    airPort.output(binaryTreeTakenOff, hashTtakenOff, "Departing", binaryTreeStateThree)






if __name__ == "__main__":
    main()
