# OS_CA2
OPERATING SYSTEM CA 2 CODE AND EXPLANATION
A.Design and implement the simulation program using aprogramming language of your choice.

Ans->l have designed and implemented the simulation program using the C programming language.

![image](https://user-images.githubusercontent.com/103503522/234956034-dabfa285-e503-4cb3-bb6a-43f154162589.png)


B. Generate a set of "processes" with random arrival times and CPU burst times using a random number generator.

Ans->l have generated a set of "processes" with random arrival times and CPU burst times using the rand() function from the C standard library.
The arrival time and CPU burst time for each process are generated randomly within a range of 0 to 9 and 1 to 10, respectively.

![image](https://user-images.githubusercontent.com/103503522/234956112-dc641a4e-6d66-48eb-9962-8f8f11d31cdc.png)


C. Implement the Round Robin scheduling algorithm in thesimulation program.

Ans-> I have implemented the Round Robin scheduling algorithm in the simulation program. The algorithm works byrunning each process for a fixed amount of time (time quantum), and then moving on to the next process. The algorithm continues to cycle through the processes until all processes have been completed.

![image](https://user-images.githubusercontent.com/103503522/234956354-e9d47ebc-e9cd-4b85-91bb-6dde71b88a0b.png)


D. Have the simulation program run for a set amount of time (e.g. 100 time units) and record the average waiting time and turnaround time for each process.

Ans-> The simulation program runs for a fixed amount of time (100 time units) and records the waiting time and turnaroundtime for each process.The waiting time is the amount of time a process waits in the queue before it can start running, while the turnaround time is the total amount of time a process takes to complete, including the waiting time and CPU burst time.

![image](https://user-images.githubusercontent.com/103503522/234956279-83d1d881-8cc9-4db4-955b-ca6d98197d5f.png)


E. Compare the results of the simulation with the ideal scenario of a perfect scheduler.

Ans-> The results of the simulation are compared with the ideal scenario of a perfect scheduler, where all processes are completed in the shortest possible time without any waiting time. The comparison shows that the Round Robin scheduling algorithm performs reasonably well, but there is still room for improvement in terms of reducing the waiting time and turnaround time for each process.



F. Write a report of the findings and conclusion with the comparison of the results of the round robin scheduling algorithm with other scheduling algorithms such as First Come First Serve (FCFS).

Ans-> Based on the simulation results,
FCFS->
the Round Robin scheduling algorithm performs better than the First Come First Serve (FCFS) algorithm in terms of reducing the waiting time and turnaround time for each process. The FCFS algorithm is known to cause longer waiting times for processes that arrive later, while the Round Robin algorithm provides a fairer distribution of CPU time among all processes. However, the Round Robin algorithm can still be further optimized by adjusting the time quantum value to find the optimal balance between waiting time and turnaround
time. Overall, the simulation program provides valuable insights into the performance of the Round Robin scheduling algorithm and its potential for improvement in real-world scenarios.

Priority scheduling->
It is another popular scheduling algorithm that assigns priorities to each process and then schedules them based on their priority. In priority scheduling, the process with the highest priority gets executed first, and the other processes wait until it is finished. If two processes have the same priority, then they are scheduled based on their arrival time. Compared to Round Robin scheduling, priority scheduling has the advantage of being able to assign priorities to processes based on their importance or urgency. This can be useful in
real-world scenarios where some processes are more critical than others, such as in real-time systems or mission-critical applications. However, priority scheduling can also suffer from potential issues such as starvation, where low-priority processes may never get a chance to execute if higher-priority processes are always arriving. In contrast, Round Robin scheduling provides a fair distribution of CPU time among all processes and avoids starvation by ensuring that each process gets a chance to execute.


In conclusion, the choice of scheduling algorithm depends on the specific requirements of the system and the priorities of the processes. Priority scheduling can be useful in scenarios where some processes are more critical than others, while Round Robin scheduling can provide a fair distribution of CPU time and avoid starvation. A good understanding of the pros and cons of each algorithm is necessary to choose the right one for the specific use case.


Multi-level Queue Scheduling->
It is another popular scheduling algorithm that divides the ready queue into several separate queues based on process attributes such as priority or process type. Each queue can have its own scheduling algorithm and priority level. The processes are then placed into the appropriate queue based on their attributes. Compared to Round Robin scheduling, multi-level queue scheduling can provide more efficient scheduling by separating processes into different queues based on their characteristics. This can improve the overall system
performance by ensuring that higher-priority processes are executed first and that processes with differentcharacteristics are scheduled optimally.However, multi-level queue scheduling can also suffer from potential issues such as process starvation, where lower-
priority processes may never get a chance to execute if higher-priority processes are always arriving. In contrast, Round Robin scheduling provides a fair distribution of CPU time among all processes and avoids starvation by ensuring that each process gets a chance to execute.

In conclusion, the choice of scheduling algorithm depends on the specific requirements of the system and the priorities of the processes. Multi-level queue scheduling can be useful inscenarios where processes have different characteristics or priorities, while Round Robin scheduling can provide a fairdistribution of CPU time and avoid starvation. A good understanding of the pros and cons of each algorithm is necessary to choose the right one for the specific use case.

Shortest Job First Algorithm->
It is a scheduling algorithm that selects the process with the smallest burst time first. It can be either preemptive or non-preemptive.Compared to Round Robin scheduling, SJF algorithm can provide more efficient scheduling by selecting the shortest job first, which minimizes the average waiting time andturnaround time. In contrast, Round Robin scheduling provides a fair distribution of CPU time among all processes and ensures that each process gets a chance to execute.

However, SJF algorithm can also suffer from potential issuessuch as process starvation, where longer processes may never get a chance to execute if shorter processes are always
arriving. In contrast, Round Robin scheduling avoids starvationby ensuring that each process gets a chance to execute, although this may result in a longer waiting time for some processes.

In conclusion, the choice of scheduling algorithm depends on the specific requirements of the system and the priorities of the processes. SJF algorithm can be useful in scenarios where minimizing the average waiting time and turnaround time is critical, while Round Robin scheduling can provide a fair distribution of CPU time and avoid starvation. A good understanding of the pros and cons of each algorithm is necessary to choose the right one for the specific use case.

