import random
import math

number_of_galaxies = 10
total_arrows = 10000
stars_in_galaxy = 2000000
star_radius = 0.5
radius_of_galaxy = 100.0



def cartestian(star):
    x = star[0]*math.cos(star[1])*math.sin(star[2])
    y = star[0]*math.sin(star[1])*math.sin(star[2])
    z = star[0]*math.cos(star[2])
    return x,y,z
#END CARTESIAN



def generate_galaxy():
    galaxy = []
    for star in range(stars_in_galaxy):
        radius = math.pow(random.uniform(0,1), 1/3) * radius_of_galaxy
        phi = random.uniform(0,2*math.pi)
        theta = math.acos( random.uniform(-1,1) )
        star = (radius,phi,theta)
        galaxy.append(star)
    galaxy.sort( key = lambda star: star[0] )
    #for r,p,t in galaxy:
        #print(str(r) + " " + str(p) + " " + str(t))
        #x,y,z = cartestian(star)
        #print(str(x) + " " + str(y) + " " + str(z))
    return galaxy
#END GENERATE_FOREST



def arrow_hit_star(star, arrow_phi_angle, arrow_theta_angle):
    if star_radius > star[0]: #i.e. we start inside a star
        return True

    theta_angular_coverage = math.asin(star_radius / star[0])
    theta_angular_difference = abs(arrow_theta_angle - star[2])
    if theta_angular_difference < theta_angular_coverage:
        arc_length_coverage = abs(star_radius * math.cos(theta_angular_difference))
        radius_from_axis = star[0] * math.sin(arrow_theta_angle)
        if arc_length_coverage > radius_from_axis:
            return True

        phi_angular_coverage = math.asin(arc_length_coverage / radius_from_axis)
        phi_angular_difference = abs(arrow_phi_angle - star[1])
        if phi_angular_difference < phi_angular_coverage:
            return True
        elif phi_angular_difference > 2*math.pi - phi_angular_coverage:
            return True
        else:
            return False
    else:
        return False
#END ARROW_HIT_TREE



def travel_distance(galaxy, arrow_phi_angle, arrow_theta_angle):
    for star in galaxy:
        if arrow_hit_star(star, arrow_phi_angle, arrow_theta_angle):
            #print(str(star) + "  |  " + str(arrow_phi_angle) + ", " + str(arrow_theta_angle) )
            return star[0]
    print("AN ARROW ESCAPED!")
    exit(0)
#END TRAVEL_DISTANCE



def shoot_arrows_into(galaxy):
    total_distance = 0.0
    for shot_num in range(total_arrows):
        arrow_phi_angle = random.uniform(0,2*math.pi)
        arrow_theta_angle = math.acos( random.uniform(-1,1) )
        total_distance += travel_distance(galaxy, arrow_phi_angle, arrow_theta_angle)

    average_distance = total_distance/total_arrows
    return average_distance
#END SHOOT_ARROWS_INTO



def main():
    average_total_distance = 0.0
    for galaxy_number in range(number_of_galaxies):
        galaxy = generate_galaxy()
        galaxy_average = shoot_arrows_into(galaxy)
        average_total_distance += galaxy_average
        print("Finished galaxy " + str(galaxy_number) + ", average = " + str(galaxy_average))
    final_average_distance = average_total_distance / number_of_galaxies
    print("AVERAGE DISTANCE TRAVELLED = " + str(final_average_distance))
#END MAIN



main()
