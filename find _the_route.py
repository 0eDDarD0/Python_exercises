#Write a program that will find the shortest route between cities that are connected among many others (represented in the dict)
#Suppose that all paths are the same length

def routing(start, end, current_route, options):
    '''Recursive function that will fill the options array with all the posible ways to go from start to end'''

    if end not in PATHS[start]:
        for son in PATHS[start]:
            if son not in current_route:
                branch = [] 
                branch.extend(current_route) 
                branch.append(son)
                routing(son, end, branch, options)

    else:
        current_route.append(end)
        options.append(current_route)


def shortestRoute(options):
    '''Returns the shortest path between the available options'''

    shortest = options[0]

    for i in options:
        if(len(i) < len(shortest)):
            shortest = i
    
    return shortest

    

PATHS = {'a' : "bcd", 'b' : "ace", 'c' : "abfe", 'd' : "ag", 'e' : "bcfg", 'f' : "ce", 'g' : "de"}

start = 'c'
end = 'g'
options = []

routing(start, end, [start], options)
print('\nThe available options are: ')
print(options)
print('\nThe shortest route is: ')
print(shortestRoute(options))