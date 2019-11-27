# A Python Program / Project

**This is a Python project from my early days as a Computer Science student**

_This programm was created for the sixth semester class Bioinformatics
and is one of the final projects for the class_

> #### Description of project
>
>>A Python script that implements an HMM with two states a and b. When the model is in state a it is more likely to emit purines A and G. When it is in state b it is more likely to emit pyramidines C and T. Decode the most likely sequence of states for the GGCT sequence using logarithmic scoring instead of normal probability scoring.

> #### Implementtion of project
>
>In more detail, Table A corresponds to:
> 1. probability 0.9 to be found from state a to state a and state b to state b
> 2. probability 0.1 to be found from state a to b and from state b to a.
>Table π corresponds to:<br>
>Initial probability 0.5 to be first in state a, and 0.5 to be first in state b.<br>
>Finally, our model is described by the last figure that matches the shape of the book, adding the 0.5, 0.5 probabilities we have described above.<br>
>Let's make the model more illustrative. This holds that when we are in state a, the probability that A will emit is 0.4, G 0.4, T 0.1 and C 0.1. Also, state b is given the probability of emitting A 0.2, G 0.2, T 0.3 and C 0.3.<br>
>Giving better path for Q = GGTC sequence A -> A -> A -> A.<br>
>And Viterbi score = ln (0.2) + ln (0.072) + ln (0.00648) + ln (0.0005832) = -1.609 - 2.631 - 5.039 - 7.446 ~ = - 16.725

> #### About this project
>
> - The comments to make the code understandable, are within the .py archive
> - This project was written in IDLE, Python’s Integrated Development and Learning Environment.
> - This program runs for Python version 2.7
> - This repository was created to show the variety of the work I did and experience I gained as a student
>

