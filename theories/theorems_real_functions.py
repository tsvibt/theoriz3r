
def appends(add, strings):
   return [add + string for string in strings]

# https://en.wikipedia.org/wiki/List_of_types_of_functions
# https://en.wikipedia.org/wiki/List_of_mathematical_functions
# everywhere positive, everywhere nonnegative, likewise negative
# operation: negate
# opertaion: flip

#Analytic function: Can be defined locally by a convergent power series.
#Lipschitz function, Holder function: somewhat more than uniformly continuous function.
# continuity
# analytic
global_continuity_properties = ['constant', 'linear', 'polynomial', ]
local_continuity_properties = ['smooth', 'C2', 'differentiable','continuous', ]
continuity = (appends('piecewise_', global_continuity_properties + local_continuity_properties)
              + appends('almost_everywhere_', local_continuity_properties)
              + appends('nowhere_', local_continuity_properties))
properties(global_continuity_properties + local_continuity_properties + continuity)

implies(constant, polynomial)
implies(linear, polynomial)
implies(polynomial, smooth)
implies(smooth, C2)
implies(C2, differentiable)
implies(differentiable, continuous)

implies(constant, piecewise_constant)
implies(linear, piecewise_linear)
implies(polynomial, piecewise_polynomial)
implies(smooth, piecewise_smooth)
implies(C2, piecewise_C2)
implies(differentiable, piecewise_differentiable)
implies(continuous, piecewise_continuous)

implies(piecewise_constant, piecewise_linear)
implies(piecewise_linear, piecewise_polynomial)
implies(piecewise_polynomial, piecewise_smooth)
implies(piecewise_smooth, piecewise_C2)
implies(piecewise_C2, piecewise_differentiable)
implies(piecewise_differentiable, piecewise_continuous)


implies(piecewise_smooth, almost_everywhere_smooth)
implies(piecewise_C2, almost_everywhere_C2)
implies(piecewise_differentiable, almost_everywhere_differentiable)
implies(piecewise_continuous, almost_everywhere_continuous)

implies(nowhere_smooth, not_almost_everywhere_smooth)
implies(nowhere_C2, not_almost_everywhere_C2)
implies(nowhere_differentiable, not_almost_everywhere_differentiable)
implies(nowhere_continuous, not_almost_everywhere_continuous)

implies(nowhere_C2, nowhere_smooth)
implies(nowhere_differentiable, nowhere_C2)
implies(nowhere_continuous, nowhere_differentiable)

implies([linear, not_constant], not_piecewise_constant)
implies([polynomial, not_linear], not_piecewise_linear)
implies([smooth, not_polynomial], not_piecewise_polynomial)

implies(almost_everywhere_smooth, almost_everywhere_C2)
implies(almost_everywhere_C2, almost_everywhere_differentiable)
implies(almost_everywhere_differentiable, almost_everywhere_continuous)

implies([piecewise_constant, not_constant], not_continuous)
implies([piecewise_linear, not_linear], not_differentiable)
implies([piecewise_polynomial, not_polynomial], not_smooth)

# set theory
set_theory = ['injective', 'surjective', 'bijective', 'aux_indicator']
properties(set_theory)

implies(bijective, injective)
implies(bijective, surjective)
implies([injective, surjective], bijective)
implies(aux_indicator, not_injective)
implies(aux_indicator, not_surjective)

# operator
operator_properties = ['even', 'odd', 'additive', 'subadditive', 'superadditive', 'multiplicative', 'submultiplicative', 'supermultiplicative']
properties(operator_properties)
##def additive: f(x)+f(y) = f(x+y)
##def subadditive: f(x)+f(y) ≥ f(x+y)
##def superadditive: f(x)+f(y) ≤ f(x+y)
##def multiplicative: f(x)f(y) = f(xy)
##def submultiplicative: f(x)f(y) ≥ f(xy)
##def supermultiplicative: f(x)f(y) ≤ f(xy)
##def even: f(x) = f(-x)
##def odd: f(x) = -f(-x)


implies(constant, even)
implies(additive, subadditive)
implies(additive, superadditive)
implies(multiplicative, supermultiplicative)
implies(multiplicative, submultiplicative)
implies(constant, not_injective)
implies(constant, not_surjective)
# at least one value nonzero. by conts, at least one x≠0 with fx ≠0. f(-x) cant be fx
implies([odd, not_constant, continuous], not_even)
implies(piecewise_constant, aux_indicator)
implies([subadditive, superadditive], additive)
implies([submultiplicative, supermultiplicative], multiplicative)
# look at 1. not const0 around 1. see above.
implies([nowhere_smooth, even], not_odd)

# fxfy = c^2 fxy=c ≤c^2
implies(constant, submultiplicative)

# f0+f0=f0 so f0=0. f(x) +f-x = f0.
implies(additive, odd)

#if fxy<fxfy then -fxy>-fxfy, so f-xy>f-xfy
implies([odd, not_supermultiplicative], not_submultiplicative)
implies([odd, not_submultiplicative], not_supermultiplicative)

#implies([linear, not_constant], bijective)
implies(even, not_injective)

#linear fx=ax+b. ax+b+ay+b vs ax+ay+b. either b is nonpositive or nonnegative. 
implies(linear, OR(subadditive, superadditive))

#if nt constant, then have fx≠f0. then have 
# x generates f on Qx as y(fx). either everyone on that line , linear, else discontinuous
implies([additive, not_constant, almost_everywhere_continuous], linear)

# if odd, then f0=0. eleswhere, fx=-f-x=f-x=-fx
implies([even, odd], constant)


#topology
topology_properties = ['homeomorphism', 'open_map', 'closed_map', 'compact_support', 'cadlag', 'quasi_continuous', 'upper_semicontinuous', 'lower_semicontinuous', 'right_continuous', 'left_continuous', 'right_limits', 'left_limits', 'uniformly_dispersed']
properties(topology_properties)
#https://en.wikipedia.org/wiki/C%C3%A0dl%C3%A0g
#file:///Users/tbt/Downloads/44151947.pdf
##def quasi_continuous: f:R⟶  R is quasi-continuous at x if for any open U of x,  and any ϵ>0, there's an open G⊂U such that f(G) ⊂ ϵ-ball of f(x)
##def cadlag: f has right and left limits at every x, and f(x) is the right limit.
##def upper_semicontinuous: at every x, limsup_ϵ f(y) ≤ f(x), limit as ϵ⟶  0; sup over ϵ-ball
##def lower_semicontinuous: at every x, liminf_ϵ f(y) ≥ f(x), limit as ϵ⟶  0; sup over ϵ-ball
##def right_continuous: f(x)=lim_ϵ f(x+ϵ)
##def left_continuous: f(x)=lim_ϵ f(x-ϵ)
##def right_limits: lim_ϵ f(x+ϵ) exists
##def left_limits: lim_ϵ f(x-ϵ) exists
##def uniformly_dispersed: (made up) ∃ϵ s.t. for all x, for all U around x, fU not contained in the ϵ-ball around f(x)


implies([linear, not_constant], homeomorphism)
implies(homeomorphism, bijective)
implies(homeomorphism, open_map)
implies(homeomorphism, closed_map)
implies(homeomorphism, continuous)
implies([continuous, open_map, bijective], homeomorphism)
implies(piecewise_constant, not_open_map)
implies(compact_support, not_injective)

implies(continuous, left_continuous)
implies(left_continuous, left_limits)
implies(continuous, right_continuous)
implies(right_continuous, right_limits)
implies([left_limits, right_continuous], cadlag)
implies(cadlag, left_limits)
implies(cadlag, right_continuous)
implies([left_continuous, right_continuous], continuous)
implies(continuous, quasi_continuous)
implies(continuous, upper_semicontinuous)
implies(continuous, lower_semicontinuous)
# where f(y) can be for y in ϵ-ball around x as ϵ⟶  0, is squeezed
implies([upper_semicontinuous, lower_semicontinuous], continuous)

# image of any set is the closed singleton
implies(constant, closed_map)

# suppose there's a right limit at x, so that f(x+ϵ)→y. but there's a global δ that ensures dispersal. so for any ϵ, x+ϵ has δ dispersal. contradiction.
implies(uniformly_dispersed, not_right_limits)
implies(uniformly_dispersed, not_left_limits)



# ordering
order_properties = ['monotonic', 'strictly_monotonic']
properties(order_properties)
##def monotonic: either never f(x)>f(y) for x<y, or never f(x)<f(y) for x<y (decreasing)
##def strictly_monotonic: always f(x)<f(y) for x<y, or always f(x)>f(y) for x<y,

#suppose not, so wlog f(x0)>f(x1)<f(x2), x012 in order. (if had equality, wouldnot be injective). wlog fx0>fx2. but by IVT, for x.5 between x0,x1, f(x.5)=fx2. so not injective
implies(strictly_monotonic, monotonic)
implies([continuous, injective], strictly_monotonic)

implies(constant, monotonic)
implies(strictly_monotonic, injective)

# measurability 
#      baire, singular
#measure_properties = ['measurable', 'borel', ]
##def measurable: the preimage of each lebesgue measurable set is lebesgue measurable https://en.wikipedia.org/wiki/Lebesgue_measure
##def borel: the preimage of each Borel set is a Borel set (generated by countable union / intersection and relative complement)
#properties(measure_properties)


# size
size_properties = ['integrable', 'square_integrable', 'bounded', 'locally_bounded', 'convex']
properties(size_properties)
##def locally_bounded: at each point there's open U neighborhood so fU bounded
##def integrable: the lebesgue integral of |f| is defined and is finite
##def square_integrable: the lebesgue integral of f(x)^2 is defined and is finite
##def convex: the line connecting two points (x,fx) (y,fy) is between x and y never below f
# if integrable (absolute value), then limit to 0. so squaring ... oh wait no maybe not... because you could be unbounded. but if bounded then squaring has bounded effect , and then only decreases outside that compact region
implies([integrable, bounded], square_integrable)
# throw out the discontinuities; only ever finitely many in any interval. then by continuity , bounded
implies(piecewise_continuous, locally_bounded)

# if not bounded, has sequencing with images going to infinity; but on compact support they have a limit, violating continuity
implies([compact_support, continuous], bounded)

implies(constant, convex)


