from hospital_simulation import *

if __name__ == '__main__':

    # True for priority, false for normal
    hospital = HospitalSimulation(3, 43800, 4, False)
    hospital_2 = HospitalSimulation(3, 43800, 4, True)

    hospital.run()
    hospital_2.run()

    print("=" * 50)
    print("FIRST HOSPITAL: NORMAL QUEUE")
    print("="*50)
    hospital.print_results()

    print("=" * 50)
    print("SECOND HOSPITAL: PRIORITY QUEUE")
    print("=" * 50)
    hospital_2.print_results()