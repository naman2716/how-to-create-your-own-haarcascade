opencv_traincascade -data data -vec postives.vec -bg bg.txt -numpos 1600 -numNeg 800 -numStages 10 -w 20 -h 20

nohub opencv_traincascade -data data -vec postives.vec -bg bg.txt -numpos 1600 -numNeg 800 -numStages 10 -w 20 -h 20 & 
### second command will allow to run the command even if the terminal of closed it just runs the command in the background..............


