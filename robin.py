import random
import math



number_of_forests = 30
total_arrows = 10000
trees_in_forest = 30000
radius_of_forest = 100.0
tree_radius = 1



def cartestian(tree):
    x = tree[0]*math.cos(tree[1])
    y = tree[0]*math.sin(tree[1])
    return x,y
#END CARTESIAN



def generate_forest():
    forest = []
    for tree in range(trees_in_forest):
        radius = math.sqrt(random.uniform(0,1))*radius_of_forest
        angle = random.uniform(0,2*math.pi)
        tree = (radius,angle)
        forest.append(tree)
    forest.sort( key = lambda tree: tree[0] )
    return forest
#END GENERATE_FOREST



def arrow_hit_tree(arrow_angle, tree):
    if tree_radius > tree[0]: #i.e. we start inside a tree
        return True

    minimum_angle = math.asin(tree_radius / tree[0])
    angular_difference = abs(arrow_angle - tree[1])

    if angular_difference < minimum_angle:
        return True
    elif angular_difference > 2*math.pi - minimum_angle:
        #print(angular_difference)
        return True
    else:
        return False
#END ARROW_HIT_TREE



def travel_distance(forest, arrow_angle):
    for tree in forest:
        if arrow_hit_tree(arrow_angle, tree):
            return tree[0]
    print("AN ARROW ESCAPED!")
    exit(0)
#END TRAVEL_DISTANCE



def shoot_arrows_into(forest):
    total_distance = 0.0
    for shot_num in range(total_arrows):
        arrow_angle = random.uniform(0, 2*math.pi)
        total_distance += travel_distance(forest, arrow_angle)

    average_distance = total_distance/total_arrows
    return average_distance
#END SHOOT_ARROWS_INTO



def main():
    average_total_distance = 0.0
    for forest_number in range(number_of_forests):
        forest = generate_forest()
        forest_average = shoot_arrows_into(forest)
        average_total_distance += forest_average
        print("Finished forest " + str(forest_number) + ", average = " + str(forest_average))
    final_average_distance = average_total_distance / number_of_forests
    print("AVERAGE DISTANCE TRAVELLED = " + str(final_average_distance))
#END MAIN



main()
