import numpy as np
import matplotlib.pyplot as plt

initial_r = 149597870700
initial_v = 29780

G = 0.0000000000667408
Star_mass = 1989000000000000000000000000000

Time = 100
time_steps = 0.2

num_steps = int(Time/time_steps)


positions = np.zeros(num_steps)
Velocities = np.zeros(num_steps)

positions[0] = initial_r
Velocities[0] = initial_v


for i in range(1, num_steps):
    
    r = positions[i - 1]
    v = Velocities[i - 1]
    
    rkr1 = time_steps * v
    rkv1 = time_steps * (-G * Star_mass/r**2)
    
    rkr2 = time_steps * (r + time_steps/2 * rkv1)
    rkv2 = time_steps * (-G * Star_mass/(r + time_steps/2 * rkr1)**2)
    
    rkr3 = time_steps * (r + time_steps/2 * rkv2)
    rkv3 = time_steps * (-G * Star_mass/(r + time_steps/2 * rkr2)**2)
    
    rkr4 = time_steps * (r + time_steps * rkv3)
    rkv4 = time_steps * (-G * Star_mass/(r + time_steps * rkr3)**2)
    
    positions[i] = r + time_steps * (rkr1 + rkr2 + rkr3 + rkr4)/6
    Velocities[i] = v + time_steps * (rkv1 + rkv2 + rkv3 + rkv4)/6

time_array = np.linspace(0, Time, num_steps)

# Plotting position vs time
plt.figure(figsize=(8, 8))
plt.plot(time_array, positions, label="Trajectory")
plt.title("Plot (time vs. position)")
plt.xlabel("Time (t)")
plt.ylabel("Position (r)")
plt.grid()
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.legend()
plt.show()

# Plotting velocity vs time
plt.figure(figsize=(8, 8))
plt.plot(time_array, Velocities, label="Trajectory")
plt.title("Plot (time vs. Velocity)")
plt.xlabel("Time (t)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.legend()
plt.show()
