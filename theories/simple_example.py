exec(open('../src/theoriz3r.py').read())

## https://en.wikipedia.org/wiki/Topological_property
DeclareMainType('Top')
# the type of nonempty spaces. https://ncatlab.org/nlab/show/empty+space

properties(['first_countable', 'arc_connected', 'path_connected', 'connected', ])
##def connected: A space X is connected if it is not the union of two disjoint non-empty open sets. 
##def path_connected: A space X is path-connected if for every two points x, y in X, there is a path p from x to y, i.e., a continuous map p: [0,1] → X with p(0) = x and p(1) = y. 
##def arc_connected: A space X is arc-connected if for every two points x, y in X, there is an arc f from x to y, i.e., an injective continuous map f: [0,1] → X with p(0) = x and p(1) = y. 
##def first_countable: every point has a countable neighbourhood basis (local base)

implies(arc_connected, path_connected)
implies(path_connected, connected)

obj('R',[
arc_connected,
first_countable,
not_connected,
])
#! R
#-- UNSAT core:
#-- arc_connected(R)
#-- ForAll(X, Implies(arc_connected(X), path_connected(X)))
#-- ForAll(X, Implies(path_connected(X), connected(X)))
#-- Not(connected(R))
#-- total time taken: 0.01

#binary_function('Sum')
#function_quantify(lambda x,y: Not(connected(Sum(x,y))))
#function_preserves(Sum, And, first_countable)

##! prop 

WriteQuestions('simple_example.py')

