import requests
import random
import webbrowser
from engine.command import speak 



def simulateRocket(query):
    # Libraries 
    # pip install control for import control 
    import matplotlib.pyplot as plt
    import control as ctrl

    speak("Rocket Control System Simulation complete")
    # systems gain 
    num = [10]
    # defines the denominator
    den = [2, 2, 1]
    # constructs the rocket transfer function
    G = ctrl.TransferFunction(num, den)

    # PID controller (proportional, integral, derivative)

    Kp = 5 # sets proportiinal gain to 5
    Ki = 2 # sets integral gain to 2 
    Kd = 1 # sets derivative gain to 1 
    C = ctrl.TransferFunction([Kd, Kp, Ki], [1,0])

    # Applying pid controller to rocket transfer function
    CL = ctrl.feedback(C * G, 1)

    # Root locus for gain analysis 
    # note: If they are on the left side of the graph, the system is stable. 
    # If they are on the right side, the system is unstable.

    plt.figure(figsize=(10, 6))
    ctrl.root_locus(C * G, grid=True)
    plt.title("Root Locus Plot (Closed-Loop)")
    plt.show()

    # Bode plot for stability analysis
    # note: The magnitude plot measures the gain of a system across different frequencies. 
    # Higher gain means quicker and stronger reactions, which is good for precise control.
    # The phase plot measures the phase shift introduced by the system across different frequencies. 
    # The phase shift is seen when the gain is 0.

    plt.figure(figsize=(10, 6))
    ctrl.bode_plot(CL, dB=True, Hz=False, deg=True)
    plt.suptitle("Bode Plot (Closed-Loop)", fontsize=16)
    plt.show()

    # Nyquist Plot for Stability Analysis
    # note: If there is no circle around the red cross at point (-1 0), the system is stable.
    # If there are circles around the red cross, namely clockwise circles, at point (-1 0), the system is unstable.

    plt.figure(figsize=(10, 6))
    ctrl.nyquist_plot(CL)
    plt.title("Nyquist Plot (Closed-Loop)")
    plt.show()