# Fiddler on the Proof: May 2, 2025 problem

Refer to the problem statement found [here.](https://thefiddler.substack.com/p/how-many-rides-can-you-reserve)

## Main problem

Code to solve the main problem is included in DisneyWorld.py.
The code initially computes the expected number of rides *after the third,*
then iterates through all of the possible initial triplets to get the average
over all possible triplets.
Of course, it adds 3 to account for riding the first three rides in the triplet.

## Extra credit problem

Code to solve the extra credit problem is included in ECDisneyWorld.py.
Note that you (the person attending Disney World) always ride rides
in each of the last three time slots, so the expected value of 3 rides is initialized
for this triplet. After that, the code works backwards through all triplets which
you could have on your Lightning Lane pass throughout the day, and simultaneously tracks
the sum of these expected values (in case the triplet is the one you initially get).
Finally, the average is computed based on the total number of initial triplets.