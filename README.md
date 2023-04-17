# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Karla Vasquez
- Gila Kohanbash 

## Lab Question Answers

**Question 1: Under what circumstances do you think it will be worthwhile to offload one or both of the processing tasks to your PC? And conversely, under what circumstances will it not be worthwhile?**

It would be worthwhile to offload some tasks to a more powerful computer when the Raspberry Pi’s computing power is not enough to do the task efficiently or will take a long time to do it. Sending the task off to a PC will reduce the time it takes to complete tasks as well as improve the overall efficiency since the PC is likely more capable. On the other hand, it may not be worthwhile if you are on a budget and the overhead cost of accumulating a PC is not worth the time that will be saved with the PC processing time. Also, if the processing time is not a big difference then transferring the tasks and data may not really be so beneficial or make a difference. 


#Main.py Questions:
ChatGPT as well as pythonbasics.org was used to answer these questions! ChatGPT was used for explanations while pythonbasics was used for the documentation and better understanding of some of the functions/methods.

**Question 2: Why do we need to join the thread here?**

The join() method is called here specifically to make sure that the program waits for the offloaded function to finish completely first. The method makes the calling thread wait until the joining completes. In this code, we start the offloading case for process1 and the data1 variable is updated when results are returned from the server. Since the code will run on its own simply through the main method, if we did not put the thread.join() line then the program would not wait for the offloading process to finish and simply move on to process2(). By joining the thread here, we force the program to wait and complete data1 before moving on. 


**Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?
See this article: https://oxylabs.io/blog/concurrency-vs-parallelism
ChatGPT is also good at explaining the difference between parallel and concurrent execution!
Make sure to cite any sources you use to answer this question.**

As explained by ChatGPT, concurrency is when 2+ processes or threads make progress together, while parallelism refers to when 2+ tasks execute simultaneously. To explain more, concurrency is more of a multi-threading process where it seems as though more than one process is being done at a time, but they actually never execute at the same time - processes executions are switched off between each other (OxyLabs article used here for the clarification). 
With these definitions, the processing functions executing here in this code are running concurrently, not parallel. This is because they are not being run at the exact same time, but rather process1 and process2 switch off between each other. 

**Question 4: What is the best offloading mode? Why do you think that is?**

In order to determine the best offloading method, I looked at the time taken by each one. The ‘both’ method seems to work the fastest leading me to believe it is the best choice. 

**Question 5: What is the worst offloading mode? Why do you think that is?**

The worst offloading mode was ‘process2’ since it had the slowest processing time. It is most likely the slowest since it has to be run locally. 

**Question 6: The processing functions in the example aren't very likely to be used in a real-world application. What kind of processing functions would be more likely to be used in a real-world application? When would you want to offload these functions to a server?**

In a real-world application these processing functions would most likely involve large amounts of data like images or any kind of video processing. These processing functions might apply filters to an image or video stream in real time. You would want to offload these functions to a server when they are computationally expansive and require a lot of processing power.  
