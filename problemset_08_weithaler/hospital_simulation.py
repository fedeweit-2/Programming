# Implementation of the main simulation class.
import sys

from priority_queue import PriorityQueue
from queue import Queue
from patient import Patient
from doctor import Doctor
from random import random

sys.path.append('../problemset_02_weithaler/')

from adt_array import Array


class HospitalSimulation:
    # Create a simulation object.
    def __init__(self, num_doctors, num_minutes, between_time, priority):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._num_minutes = num_minutes
        # Simulation components.

        if priority:
            # PRIORITY QUEUE
            self._patient_q = PriorityQueue()
        else:
            # NORMAL QUEUE
            self._patient_q = Queue()


        self._doctors = Array(num_doctors)
        for i in range(num_doctors):
            self._doctors[i] = Doctor(i + 1)
            # Computed during the simulation.
        self._total_wait_time = 0
        self._num_patients = 0

        # Lists for dead and cured people
        self._cured = []
        self._dead = []

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for cur_time in range(self._num_minutes + 1):
            self._handle_arrival(cur_time)
            self._handle_begin_service(cur_time)
            self._handle_end_service(cur_time)

    # Print the simulation results.
    def print_results(self):
        num_served = self._num_patients - len(self._patient_q)
        avg_wait = round(float(self._total_wait_time) / num_served, 2)
        cure_rate = round((len(self._cured) / num_served)*100, 2)
        death_rate = round((len(self._dead) / num_served)*100, 2)
        print("\nNumber of passengers served - ", num_served)
        print(f"Number of passengers remaining in line = {len(self._patient_q)}")
        print(f"The average wait time was {avg_wait} minutes.")
        print(f"Cure rate is: {cure_rate}% ({len(self._cured)})")
        print(f"Death rate is: {death_rate}% ({len(self._dead)})")

    def _handle_arrival(self, cur_time):
        # Handles simulation rule #1.
        if random() < self._arrive_prob:
            self._num_patients += 1
            pat = Patient(self._num_patients, cur_time)

            self._patient_q.enqueue(pat, pat.condition_severity)
            print("Customer #", self._num_patients, "arrived at time", cur_time)
            print("Queue length is", len(self._patient_q))

    def _handle_begin_service(self, cur_time):
        # Handles simulation rule #2.
        # find a free agent
        doctor = self._doctors[0]
        i = 0
        while not doctor.is_free() and i < len(self._doctors):
            doctor = self._doctors[i]
            i += 1
        # if a free agent has been found
        if doctor and doctor.is_free():
            if not self._patient_q.is_empty():
                pat = self._patient_q.dequeue()
                print(pat)
                if pat.is_still_alive(cur_time):
                    doctor.cure_patient(pat, cur_time)
                    print("Agent #", doctor.id_num(), "starts processing Customer #", pat.id_num(), " at time", cur_time)

    def _handle_end_service(self, cur_time):
        # Handles simulation rule #3.
        for doctor in self._doctors:
            if not doctor.is_free():
                if doctor._stop_time == cur_time:
                    pat = doctor.cure_completed()
                    print("Agent #", doctor.id_num(), " finishes processing Customer #", pat.id_num(), " at time",
                          cur_time)
                    totaltime = cur_time - pat._arrival_time
                    print("Customer #", pat.id_num(), " has spent ", totaltime, " minutes in the system")
                    print("of which ", totaltime, " waiting")
                    self._total_wait_time += totaltime

                    self._cured.append(pat) if pat.is_still_alive(cur_time) else self._dead.append(pat)
