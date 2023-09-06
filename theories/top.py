exec(open('../src/theoriz3r.py').read())

 

## https://en.wikipedia.org/wiki/Topological_property
DeclareMainType('Top')

#want:
#   simple example of two property implication
#   then transitive implication
#   discuss orthogonality
#   give example of nonorthogonoality
#   then say but there's a lot of orthogonality, causing a lot of dumb questiosn:
#   example is, sums ar always disconnectde. so any property preserved by sums is compatible with disconnected. how to represent ? sum function etc. 

countability = ['first_countable', 'second_countable', 'separable', 'Lindelof', ]
## sequential space: a set is open if every sequence convergent to a point in the set is eventually in the set
##def first_countable: every point has a countable neighbourhood basis (local base)
##def second_countable: the topology has a countable base
##def separable space: there exists a countable dense subset
##def Lindelof space: every open cover has a countable subcover
## https://en.wikipedia.org/wiki/Axiom_of_countability

compactness = ['compact', 'sigma_compact',]
## compact space: every cover has a finite subcover 
##def sigma_compact: σ-compact space: there exists a countable cover by compact spaces

connection = ['path_connected', 'connected', 'totally_disconnected',  'locally_connected', 'locally_path_connected', 'arc_connected', 'simply_connected', 'locally_simply_connected', 'semi_locally_simply_connected', 'contractible', 'locally_contractible', 'hyperconnected', 'ultraconnected', 'indiscrete', 'discrete']
##def locally_connected: Locally connected. A space is locally connected if every point has a local base consisting of connected sets.
##def totally_disconnected: A space is totally disconnected if it has no connected subset with more than one point.
##def path_connected: A space X is path-connected if for every two points x, y in X, there is a path p from x to y, i.e., a continuous map p: [0,1] → X with p(0) = x and p(1) = y. 
##def locally_path_connected: A space is locally path-connected if every point has a local base consisting of path-connected sets. 
##def arc_connected: A space X is arc-connected if for every two points x, y in X, there is an arc f from x to y, i.e., an injective continuous map f: [0,1] → X with p(0) = x and p(1) = y. 
##def simply_connected: A space X is simply connected if it is path-connected and every continuous map f: S1 → X is homotopic to a constant map.
##def locally_simply_connected: A space X is locally simply connected if every point x in X has a local base of neighborhoods U that is simply connected.
##def semi_locally_simply_connected: A space X is semi-locally simply connected if every point has a local base of neighborhoods U such that every loop in U is contractible in X (as opposed to in U). does NOT imply path connected.
##def contractible: A space X is contractible if the identity map on X is homotopic to a constant map. 
##def locally_contractible: has everywhere a local base of contractibles.
##def hyperconnected: A space is hyperconnected if no two non-empty open sets are disjoint. 
##def ultraconnected: A space is ultraconnected if no two non-empty closed sets are disjoint. 
##def indiscrete: A space is indiscrete if the only open sets are the empty set and itself. Such a space is said to have the trivial topology.
##def discrete: A space is discrete if all of its points are completely isolated, i.e. if any subset is open.
## later want to define ordering on cardinalities, and then say, if you're bigger than 1 and connected you're not totally disconnected. or rather, if totaly disconnected, then not connected, assuming greater than 1.

separation = ['normal', 'regular', 'Hausdorff', 'points_closed', 'Kolmogorov',]
## Two points x and y are separated if each of them has a neighbourhood that is not a neighbourhood of the other; that is, neither belongs to the other's closure. More generally, two subsets A and B of X are separated if each is disjoint from the other's closure
## Subsets A and B are separated by neighbourhoods if they have disjoint neighbourhoods. They are separated by closed neighbourhoods if they have disjoint closed neighbourhoods. They are separated by a continuous function if there exists a continuous function f from the space X to the real line R such that the image f(A) equals {0} and f(B) equals {1}. Finally, they are precisely separated by a continuous function if there exists a continuous function f from X to R such that the preimage f−1({0}) equals A and f−1({1}) equals B.
##def Kolmogorov: X is T0, or Kolmogorov, if any two distinct points in X are topologically distinguishable. 
## X is R0, or symmetric, if any two topologically distinguishable points in X are separated.
## X is T1, or accessible or Fréchet or Tikhonov, if any two distinct points in X are separated. 
## X is Hausdorff, or T2 or separated, if any two distinct points in X are separated by neighbourhoods. 
## X is T2½, or Urysohn, if any two distinct points in X are separated by closed neighbourhoods. 
##def regular: X is regular if, given any point x and closed set F in X such that x does not belong to F, they are separated by neighbourhoods. 
## X is normal if any two disjoint closed subsets of X are separated by neighbourhoods. 

geometry = ['finite_Euclidean_modeled', 'metrizable', 'manifold']

other = ['ordered', 'Baire', 'transitive', 'locally_homogeneous', 'Alexandrov', 'zero_dimensional', 'almost_discrete', 'boolean', ]
## todo: perfect, homogenous (locally), symmetric (i.e. transitive)
##def ordered: there's a total order on the space such that the set of open intervals (x s.t. a<x<b) is a basis.
##def Baire: X is a Baire space if the intersection of countably many dense open sets is dense.
##def transitive: X is transitive (homogeneous) if for every x and y in X there is a homeomorphism f : X → X such that f(x) = y. 
##def locally_homogeneous: for every x,y, there's a homeomorphism f from a neighborhood of x to  one of y sending x to y.
##def Alexandrov: Finitely generated or Alexandrov. A space X is Alexandrov if arbitrary intersections of open sets in X are open
##def zero_dimensional: A space is zero-dimensional if it has a base of clopen sets. These are precisely the spaces with a small inductive dimension of 0.
##def almost_discrete: A space is almost discrete if every open set is closed (hence clopen). 
##def boolean: A space is Boolean if it is zero-dimensional, compact and Hausdorff (equivalently, totally disconnected, compact and Hausdorff). 

properties(countability)
properties(compactness)
properties(connection)
properties(separation)
properties(geometry)
properties(other)

implies(arc_connected, path_connected)
implies(path_connected, connected)

obj('R', [
arc_connected,
first_countable,
])
##! R

#binary_function('Sum')
#Top.function_assertions.append(ForAll([X,Y], Not(connected(Sum(X,Y)))))
#function_preserves(Sum, And, first_countable)


#! prop 
#-- not first_countable?
#-- second_countable?
#-- not second_countable?
#-- separable?
#-- not separable?
#-- 
#-- total time taken: 0.03
#-- initial consistency check time: 0.01

WriteQuestions('top.py')


