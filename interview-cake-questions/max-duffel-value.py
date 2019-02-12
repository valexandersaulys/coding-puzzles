#! usr/bin/python3
"""
"""
def max_duffel_bag_value_naieve(inventory,capacity,value=0):
    """Naieve -- this will recursively look through everything"""
    if capacity == 0:
        return [value];
    elif capacity < 0:
        return [0];  # nonsensical value
    
    possible_values = []
    for cake in inventory:
        possible_values += max_duffel_bag_value_naieve(inventory,
                                                       capacity=capacity-cake[0],
                                                       value=value + cake[1]);

    if value == 0:
        return max(possible_values)
    else:
        return [max(possible_values)]

def max_duffel_bag_value(inventory,capacity,value=0,memo={}):
    """Use dynamic programming"""
    if (capacity in memo):
        return [memo[capacity]];
    elif (True if 0 in [x for x,y in inventory] else False):
        return float("inf")  # also would need to check for items of 0
    elif capacity == 0:
        return [value]  # no more capacity left
    elif capacity < 0:
        return [0];
    
    possible_values = []
    for cake in inventory:
        possible_values += max_duffel_bag_value(inventory,
                                                capacity=capacity-cake[0],
                                                value=value + cake[1],
                                                memo=memo);
    if value == 0:
        print(memo)
        return max(possible_values)
    else:
        memo[capacity] = max(possible_values);
        return [memo[capacity]];

    
if __name__ == "__main__":
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20
    print("Naive =>  %d" %
          max_duffel_bag_value_naieve(inventory=cake_tuples,capacity=capacity))
    print(max_duffel_bag_value(inventory=cake_tuples,capacity=capacity))

