# Used to store and manage information related to a supermarket checkout agent.
import random


class Doctor:

    # Creates a checkout agent object.
    def __init__(self, id_num):
        self._id_num = id_num
        self._customer = None
        self._stop_time = -1

    # Gets the agent's id number.
    def id_num(self):
        return self._id_num

    # Determines if the agent is free to serve a customer.
    def is_free(self):
        return self._customer is None

    # Determines if the agent has finished serving the customer.
    def is_finished(self, cur_time):
        return self._customer is not None and self._stop_time == cur_time

    # Indicates the agent has begun serving a customer.
    def cure_patient(self, patient, current_time):
        self._customer = patient
        self._cure_time = random.randint(5, 20)
        self._stop_time = current_time + self._cure_time

    # Indicates the agent has finished serving the customer.
    def cure_completed(self):
        the_customer = self._customer
        self._customer = None
        return the_customer

    def current_patient_cure_time(self, current_time):
        return self._stop_time - current_time
