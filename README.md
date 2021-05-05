# Interviewer
## This is a simple program that i was trying to develop trying to get a series of random questions popped into the the CLI

It is an app that i want to use and work on that will allow the use of a pseudo-random algorithm to permit the flow of a series of a questions to imitate the randomness of a job interview. The code is up to date in this site, and i tried to upload and display the images of a glitch running to the CL program. in GitHub but i do not know MarkDown that well so hopefully you are able to see it as a link to dropbox. 

#### So it seems to me that in my attempt to have a randomness i made have tried to experiment with an imitation of Ai. 

I tried using recursivism  and the random method of python to keep the randomness of the program. But i keep getting the problem i showed you in the first screen capture/link. That is i run into questions repeating again and again multiple times. The issue it seems to be is that i am recalling the same function through several iterations and so it resets the variable list that i am calling back into. 
##### This are the pictures 
! [Image of problem 1](https://www.dropbox.com/s/2aqbd4f66g5ceas/ink.png?dl=0)


! [This is the code](https://www.dropbox.com/s/13o2ngnt2um4gx0/pic2.png?dl=0)

## SOLVED!!!! LADIES AND GENTS!!! I FINALLY FIGURED IT OUT. 
Finally after taking stabs at this programs for hours at time since november, i finally figured out how to do it. And cut down about 50-60 lines of code. It turns out i was trying to reinvent the wheel, or in this case.
##### the Random.choice() method! 
which is slighty annoying. 
I tried everything from calling the remove() method of python in a recursive call of the function i was working on to trying to control the number of times it iterated in the function callback. 

Eventually i realized that  there WAS a method that could do the job i wanted with less code. 








