# a0
ao

Citations : 
I have discussed with Viral Prajapati , Vivek Shresta Bandaru , Kartik  , Prashant Sateesh , Ojaas Hampiholi
Report for AI : 

Part 1 : 


->Here , according to the assignment of finding the shortest path, I have implemented Breadth first search with a Boolean variable array so that the BFS does not revisit the visited states again. 
->The code that was given to us was depth first search and while running the code on the given dataset it was going to infinite loop. The reason behind this was that as it was depth first search it while it was exploring the branch, it kept on exploring a particular branch which was looped and so it was stuck in the loop itself. The solution implemented by me for this problem was to add the constraints of how a person can walk I.e. (row+1 ,column) ,  (row-1 ,column) ,  (row ,column+1) ,  (row ,column-1) and maintain a boolean array(visited array nodes list) so that it doesn’t revisit the visited node. 
->With this one would get a solution in many cases but might not get an optimum solution. To get the optimum solution I changed the data structure that was implementing stack to queue. Hence , it became BFS from DFS.
 -> I also maintained an array to find the minimum path required to each the solution. The logic behind this is that for every move I would save the previous node’s path and the current path’s direction. Hence, when it reaches the Luddy Hall , the coordinates of Luddy Hall when provided to the array maintaining the path would provide us the required path to be taken with directions. 

Successor function :  For N*M matrix here the successor function is :
				that the move cannot be done if the next location of the move is “&”
				and the node does not revisit the already visited nodes. 

Valid states :  Here, the the states is valid if it has “.” for the current position. 
Cost function : the cost of each step is 1 
Goal function : Goal state to reach is @
Initial state. : Initial state here is #

-> In case there is no possible solution I have displayed the path to infinity. 
->Also, if there is no @ or # that is if the current location is not given or if the destination location is not provided it will print the solution as data insufficient

Part 2 : 

Successor function :  For N*M matrix and k friends I have here checked the constraints such that 
				for the particular position for which we check whether that move is valid or not , I check the upper and lower side of the row and left and right side of the column such that given the location there is no friend in between the nearest building to the given position to be checked .
Valid states :  Here the the states is valid if it has “.” for the current position. 
Cost function : the cost here would be traversing each and  every position to check whether that state is valid or not. 
Goal function : Goal state is to arrange k friends 
Initial state. :  Initial map with none friend arranged 

-> Here in the program given I have implemented breadth first search . The program given allows the friends to be side by side with each other and hence to solve this problem, I added constraints. The constraints were as follows that given a location where it is a dot it will check all its four directions I.e(upper and lower row and left and right of the column). It will check such that there is no friend in between of the given position and the building. If there is then it will not validate the mode and then skip to some other state. 

