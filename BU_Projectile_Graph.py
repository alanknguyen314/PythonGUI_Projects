import numpy as np
import matplotlib.pyplot as plt

def projectile(gravity, drag_coefficient, density_of_air, drag = True):
    """ This function takes in gravity (in ms-2), drag coefficient, density of air and will draw a projectile 
    motion for the object. The mass (m), initial projection speed (vball), launch angle (theta) and circumference (cir) 
    are all changable.
    All the units are standard SI units"""

     # Declare Variables
    vball = 50 # 50ms-1 #v_initial
    theta = np.pi / 4 # angle = 45 deg or pi/4 rad
    m = 0.142 # Mass = 0.142 kg
    cir = 0.23 # Circumference = 0.23 m
    r = cir / np.pi / 2 # Radius = circumference/pi/2 m
    S = np.pi * pow(r, 2)  

    #Time (time declare, time of flight, change in time)
    time = np.linspace(0, 100, 10000)
    time_of_flight = 0.00 
    dt = time[1] - time[0]
    
    # Velocity (inivelocity x, inivelocity y, final velocity x, final velocity y)
    vel_i_x = vball * np.cos(theta) # x comp
    vel_i_y = vball * np.sin(theta) # y comp
    vel_x = vel_i_x # x comp final = x comp 
    vel_y = vel_i_y # y comp final = y comp
    
    # Displacements
    dis_x = 0.00
    dis_y = 1.00 # Starts at 1m above ground

    # Add to list to keep list of values, later use to plot.
    dis_list_x = list() # Blank list of final x displacement components
    dis_list_x.append(dis_x) # Add value to list
    dis_list_y = list() # Blank list of final y displacement components
    dis_list_y.append(dis_y) # Add value to list

    # Starts 
    for t in time:
        force_x = 0.00
        force_y = 0.00
        if (drag == True): # If drag is on 
            force_y = force_y - 0.5 * drag_coefficient * density_of_air * S * pow(vel_y, 2)
            force_x = force_x - 0.5 * drag_coefficient * S * pow(vel_x, 2) * density_of_air 
        
        # Change in force in y component (no change in force in x component.)
        force_y = force_y + (-gravity * m)

        # Change in displacements in y component and x component (x = x0 + v0t + 1/2(F/m)t^2)
        dis_x = dis_x + vel_x * dt + 0.5 * (force_x / (m)) * dt**2
        dis_y = dis_y + vel_y * dt + 0.5 * (force_y / (m)) * dt**2
        
        # Change in velocity in y component and x component (v = v0 + (F/m)t)
        vel_x = vel_x + (force_x / m) * dt
        vel_y = vel_y + (force_y / m) * dt

        # Add final value to the two lists as the ball hits ground (dis_y = 0.00)
        if (dis_y >= 0.00):
            dis_list_x.append(dis_x)
            dis_list_y.append(dis_y)

            
        else: # If drag is not on 
            time_of_flight = t # total time
            # add one last time
            dis_list_x.append(dis_x)
            dis_list_y.append(dis_y)
            break

    return (dis_list_x, dis_list_y, time_of_flight)

#BOSTON
dis_list_x, dis_list_y, time_of_flight = projectile(9.803, 0.35, 1.2, True)
plt.plot(dis_list_x, dis_list_y, label = "Boston")

#DENVER
dis_list_x, dis_list_y, time_of_flight = projectile(9.796, 0.35, 0.96, True)
plt.plot(dis_list_x, dis_list_y, label = "Denver")

#BOSTON no Drag
dis_list_x, dis_list_y, time_of_flight = projectile(9.803, 0.35, 1.2, False)
plt.plot(dis_list_x, dis_list_y, label = "Boston No Drag")

# Configure the grid and plot
plt.grid(b = True, which = 'major', axis = 'both')
plt.title("x - y tragectory", fontsize = 10)
plt.xlabel("x - displacement (m)")
plt.ylabel("y - displacement (m)")
plt.legend()
plt.show()
