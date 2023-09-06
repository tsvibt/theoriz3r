
"""
exec(open('grp.py').read())
https://groupprops.subwiki.org/wiki/Category:Group_properties
cProfile.run("exec(open('grp.py').read())", sort='cumtime')

WARNING: there are likely inaccuracies in what's asserted here
"""

import cProfile

exec(open('../src/theoriz3r.py').read())
DeclareMainType('Grp')


#Type('coarse_cardinalities')
#obj(['finite', 'aleph_0', 'uncountable'], coarse_cardinalities)
#coarse_cardinality = Function('coarse_cardinality', Grp.z3, coarse_cardinalities.z3)
#proposition(ForAll([X], Or(coarse_cardinality(X) == finite.z3, coarse_cardinality(X) == aleph_0.z3, coarse_cardinality(X) == uncountable.z3)))

sizes = ['finite', 'aleph_0', 'uncountable']
properties(sizes)
MutuallyExclusiveExhaustive(sizes)

properties(['trivial'])

rank_1 = ['cyclic', 'abelian', 'prime_order', 'symmetric']
#https://groupprops.subwiki.org/wiki/Cyclic_group
##def cyclic: has a generating set of size 1
##def abelian: any two elements x,y in G commute: xy = yx
##def prime_order: G has a prime number of elements 
##def symmetric: there is a set S such that G is the group of permutations of S

properties(rank_1)

implies(cyclic, abelian)
implies(cyclic, not_uncountable)
implies(prime_order, finite)
implies(prime_order, cyclic)

implies(symmetric, not_aleph_0)


rank_2 = ['finitely_generated', 'finitely_presentable', 'solvable', 'free', 'prime_power_order', 'torsion_containing']
##def finitely_generated: there's a finite set of elements that generates G
##def finitely_presentable: there's a presentation with finitely many generators and finitely many relations
##def solvable: group with a finite derived series, https://groupprops.subwiki.org/wiki/Derived_series , i.e. taking the commutator subgroups terminates finitely; https://groupprops.subwiki.org/wiki/Commutator_subgroup  is elements of the form xyx⁻¹y⁻¹
##def free: group that's all the reduced words on some subset https://groupprops.subwiki.org/wiki/Free_group
##def prime_order: G has a number of elements that's a prime power

properties(rank_2)


implies(cyclic, finitely_presentable)
implies(finitely_presentable, finitely_generated)
implies(finite, finitely_presentable)
implies(abelian, solvable)
# the commutator subgroup of G is {xyx⁻¹y⁻¹}, which is just {e} if abelian
implies(prime_order, prime_power_order)
implies(prime_power_order, finite)
implies([free, not_cyclic], not_abelian) 
implies(finitely_generated, not_uncountable)
implies([not_trivial, finite], torsion_containing)
implies(torsion_containing, not_free)

implies([free, not_abelian], not_solvable)
# i think...
implies([symmetric, not_trivial], torsion_containing)

implies(trivial, not_torsion_containing)
implies(trivial, finite)
implies(trivial, cyclic) 
implies(trivial, symmetric) 
implies(trivial, free) 
implies(trivial, not_prime_power_order)
obj('one', [
# group with one element
trivial,
])
# technically... free on empty set 
##! one

obj('Z',[
# integers with addition
aleph_0,
cyclic,
not_symmetric,
free,
])
##! Z

obj('R',[
# reals with addition
uncountable,
abelian,
not_symmetric,
])
##! R

obj('S_3',[
# symmetric group on 3 elements. order = 6
finite,
not_abelian,
symmetric,
not_prime_power_order,
solvable,
])
# commutator subgroup is the rotations (commutators are an even number of flips); that's abelian
##! S_3

obj('S_2',[
# symmetric group on 2 elements. order = 2
finite,
abelian,
symmetric,
prime_order,
])
##! S_2

obj('Zup2',[
aleph_0,
not_cyclic,
abelian,
not_symmetric,
finitely_presentable,
])
# <a,b | ab=ba>
##! Zup2



obj('Z_3',[
# cyclic 3 elements
not_symmetric,
cyclic,
prime_order,
])
##! Z_3

obj('S_N',[
symmetric,
uncountable,
not_abelian,
torsion_containing,
not_solvable,
])
# ... erm. presumably there's a nonsolvable finite group. S_N embeds it. 
##! S_N


obj('S_5',[
symmetric,
finite,
not_trivial,
not_solvable,
])
##! S_N

obj('ZupZ',[
# free abelian group on Z
aleph_0,
abelian,
not_finitely_generated,
not_torsion_containing,
])
##! ZupZ

obj('Free2',[
aleph_0,
not_abelian,
not_symmetric,
])
##! Free2

obj('FreeR',[
# free group on the set R
uncountable,
free,
])
##! FreeR

implies([symmetric, not_abelian], not_prime_power_order)
obj('D_4',[
not_abelian,
prime_power_order,
#rotations commute. if you have x,y reflectiosn, commutator is a rotation. likewise if just one. so the derived group is rotations, which is abelian
solvable,
])
##! D_4

#! prop
#-- finitely_generated, not finitely_presentable?
#-- not solvable, prime_power_order?
#-- not finite, cyclic, not free?
#-- not finite, cyclic, torsion_containing?
#-- not finite, abelian, symmetric?
#-- 
#-- total time taken: 18.1
#-- initial consistency check time: 9.42

#rank 1
binary_function('Product')
function_preserves(Product, And, abelian)
function_preserves(Product, Or, not_abelian)
#--  definition: abelian: any two elements x,y in G commute: xy = yx
function_preserves(Product, And, finite)
function_preserves(Product, And, aleph_0)
function_preserves(Product, Or, uncountable)
function_preserves(Product, And, not_trivial)
function_quantify(
      lambda x,y: Implies(And(not_trivial(x),Not(trivial(y))), Not(cyclic(Product(x,y))))) 
function_quantify(
      lambda x,y: Implies(And(Not(trivial(x)),Not(trivial(y))), Not(symmetric(Product(x,y)))))
function_quantify(
      lambda x,y: Implies(And(finite(x),aleph_0(y)), aleph_0(Product(x,y))))


#rank 2
function_preserves(Product, Or, not_solvable)
function_preserves(Product, And, solvable)
function_preserves(Product, Or, torsion_containing)
function_preserves(Product, And, not_torsion_containing)
#function_quantify(
#      lambda x: Implies(prime_power_order(x), prime_power_order(Product(x,x))), arity=1)


#Grp.function_assertions.append(ForAll([X], Implies(prime_power_order(X), prime_power_order(Product(X,X)))))


#cProfile.run("exec(open('grp.py').read())", sort='cumtime')
#cProfile.run("WriteQuestions('grp.py')")
WriteQuestions('grp.py')


