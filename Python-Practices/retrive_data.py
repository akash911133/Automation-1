
import pyjokes
region=['us-east-1', 'us-east-2', 'south-east-1', 'ca-central-1']
for index, ZONE in enumerate(region):
    if (ZONE == 'south-east-1' ) :
        print("hello_world")
        print(index)
        print(pyjokes.get_jokes())
    else: 
        print("this is not mumbai region "+"it is a " + ZONE + " region")