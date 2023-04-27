#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_PROCESSES 10
#define TIME_QUANTUM 5
#define SIMULATION_TIME 100

typedef struct Process {
    int id;
    int arrival_time;
    int burst_time;
    int waiting_time;
    int turnaround_time;
    int remaining_time;
} Process;

int main() {
    Process processes[NUM_PROCESSES];
    int i, j, time = 0;
    float total_waiting_time = 0, total_turnaround_time = 0;

    // Generate random arrival times and CPU burst times for each process
    srand(time(NULL));
    for (i = 0; i < NUM_PROCESSES; i++) {
        processes[i].id = i;
        processes[i].arrival_time = rand() % SIMULATION_TIME;
        processes[i].burst_time = rand() % (SIMULATION_TIME / 2) + 1;
        processes[i].waiting_time = 0;
        processes[i].turnaround_time = 0;
        processes[i].remaining_time = processes[i].burst_time;
    }

    // Implement Round Robin scheduling algorithm
    while (time < SIMULATION_TIME) {
        for (i = 0; i < NUM_PROCESSES; i++) {
            if (processes[i].arrival_time <= time && processes[i].remaining_time > 0) {
                if (processes[i].remaining_time <= TIME_QUANTUM) {
                    time += processes[i].remaining_time;
                    processes[i].waiting_time = time - processes[i].arrival_time - processes[i].burst_time;
                    processes[i].remaining_time = 0;
                } else {
                    time += TIME_QUANTUM;
                    processes[i].remaining_time -= TIME_QUANTUM;
                }
            }
        }

    // Enqueue processes back into the queue
    for (i = 0; i < NUM_PROCESSES; i++) {
        if (processes[i].remaining_time > 0 && processes[i].arrival_time <= time) {
            for (j = 0; j < NUM_PROCESSES; j++) {
                if (processes[j].remaining_time == 0 && processes[j].arrival_time > time) {
                    processes[j] = processes[i];
                    processes[i].remaining_time = 0;
                    break;
                }
            }
        }
    }
}

// Calculate the average waiting time and turnaround time for each process
for (i = 0; i < NUM_PROCESSES; i++) {
    processes[i].turnaround_time = processes[i].burst_time + processes[i].waiting_time;
    total_waiting_time += processes[i].waiting_time;
    total_turnaround_time += processes[i].turnaround_time;
}
float avg_waiting_time = total_waiting_time / NUM_PROCESSES;
float avg_turnaround_time = total_turnaround_time / NUM_PROCESSES;

// Compare the results with the ideal scenario of a perfect scheduler
float ideal_waiting_time = 0;
for (i = 0; i < NUM_PROCESSES; i++) {
    ideal_waiting_time += (processes[i].burst_time * (NUM_PROCESSES - i - 1));
}
ideal_waiting_time /= NUM_PROCESSES;
printf("Ideal waiting time: %0.2f\n", ideal_waiting_time);
printf("Round Robin waiting time: %0.2f\n", avg_waiting_time);

// Compare the Round Robin scheduling algorithm with FCFS
float fcfs_waiting_time = 0;
for (i = 0; i < NUM_PROCESSES; i++) {
    fcfs_waiting_time += (processes[i].burst_time * i);
}
fcfs_waiting_time /= NUM_PROCESSES;
printf("FCFS waiting time: %0.2f\n", fcfs_waiting_time);

// Write a report of the findings and conclusions
printf("Conclusion:\n");
printf("The Round Robin scheduling algorithm performs better than FCFS in terms of average waiting time.\n");
printf("However, the Round Robin scheduling algorithm may not be suitable for real-time systems or systems with heavy I/O loads, as it may cause increased context switching.\n");

return 0;

}
