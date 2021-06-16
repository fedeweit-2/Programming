# Used to store and manage information related to a customer.
import random

from mpmath import rand


class Patient:

    # Creates a customer object.
    def __init__(self, id_num, arrival_time):
        self._id_num = id_num
        self._arrival_time = arrival_time
        self._condition_severity = random.randint(15, 240)

    # Gets the customer's id number.
    def id_num(self):
        return self._id_num

    # Gets the customer's arrival time.
    def time_arrived(self):
        return self._arrival_time

    def is_still_alive(self, current_time):
        return current_time - self._arrival_time <= self._condition_severity

    # Getter for severity
    @property
    def condition_severity(self):
        return self._condition_severity

    # Setter for arrival time
    @condition_severity.setter
    def condition_severity(self, value):
        self._condition_severity = value
