
"""
import cProfile
cProfile.run("exec(open('real_functions.py').read())", sort='cumtime') 
exec(open('real_functions.py').read())

WARNING: there are likely inaccuracies in what's asserted here
"""




exec(open('../src/theoriz3r.py').read())
DeclareMainType('Fun')
DeclareAuxiliaryFile('theorems_real_functions.py')


obj('const0', [
# λx.0, indicator of everything
constant,
odd,
additive,
multiplicative,
compact_support,
integrable,
])
##! const0

obj('const1', [
# λx.1
constant,
not_odd,
not_additive,
subadditive,
multiplicative,
])
##! const1

obj('constminus2', [
# λx.-2
constant,
not_odd,
not_additive,
# fx+fy=-4 fx+y=-2
superadditive,
not_multiplicative,
# fxfy=4 fxy=-2
submultiplicative,
])
##! constminus2


obj('identity', [
# λx.x
linear,
bijective,
odd,
additive,
multiplicative,
])
##! identity

obj('plus1', [
# λx.x+1
linear,
not_constant,
# can go down: f0+f0=2>f0=1
not_superadditive,
not_odd,

])
##! plus1


obj('minus1', [
# λx.x-1
linear,
bijective,
not_odd,
not_even,
#can go up: f2f2=1<f4=3
not_submultiplicative,
#can go down: f0f0=1>f0=-1
not_supermultiplicative,
# f1+f1=0<f2=1
not_subadditive,
#x-1+y-1<x+y-1
#superadditive,

])
##! minus1

obj('times2', [
# λx.2x
linear,
bijective,
odd,
additive,
# f1f1=4>f1=2
not_supermultiplicative,
])
##! times2


obj('step01', [
# indicator of >0
not_continuous,
piecewise_linear,
piecewise_constant,
not_odd,
not_even,
not_additive,
#for f(x+y) to be bigger, it's 1 and fx=fy=0. but then x,y≤0 so x+y≤0.
subadditive,
#f-1 f-1 = 0 but f1 = 1
not_multiplicative,
#for f(xy) to be smaller, it's 0 and fx=fy=1. but then x,y>0 so xy>0,so fxy=1
supermultiplicative,
])
##! step01

obj('indicator_rational', [
# 1 on ratioals, 0 elsewhere
nowhere_continuous,
aux_indicator,
even,
# when you add, it can get smaller. eg f(2)=1<f1+f1=2
not_superadditive,
# when you add, it can get bigger. eg f(1)=1>f(π)+f(1-π)=0
not_subadditive,
# eg π and 1/π are 0 but product is valued 1
not_submultiplicative,
#for f(xy) to be smaller, it's 0 and fx=fy=1. but then x,y ∈ ℚ so xy ∈ ℚ. 
supermultiplicative,
uniformly_dispersed,
])
##! indicator_rational

obj('x2', [
# x^2
not_linear,
polynomial,
not_injective,
not_surjective,
even,
#hm is there some relation between additivity and convexity / concavity??
# can go up: f1+f1=2<4=f1+1
not_subadditive,
# can go down: f1+f-1=2>0=f1-1
not_superadditive,
#fxfy=x²y²=(xy)²=fxy
multiplicative,
])
##! x2


obj('x3', [
# x^3 
not_linear,
polynomial,
bijective,
odd,
#can go up: f1+f1=2<f2=8
not_subadditive,
#can go down: f1.5+f-.5=3.25>1=f1
not_superadditive,
multiplicative,
])
##! x3


obj('x3_x2', [
# x^3 - x^2
not_linear,
polynomial,
not_injective,
surjective,
# eg f1=0, f-1=-2
not_even, 
not_odd,
# can go up: at some big number, multiplying by two nearly 8x the value
not_subadditive,
# can go down: at some very negative number, multiplying by two nearly 8x the value
not_superadditive,
# can go up: f2=4 f4=48
not_submultiplicative,
# can go down: f(1/2)^2=-1/8^2 = 1/64> f(1/4) = 1/64 - 1/16
not_supermultiplicative,
])
##! x3_x2


obj('ex', [
# e^x
smooth,
not_polynomial,
injective,
not_surjective,
not_even,
not_odd,
# 2e^x vs e^2x
# x=0, goes down
not_superadditive,
# x=1, goes up 
not_subadditive,
# e^2x vs e^x²
# x=1, goes down
not_supermultiplicative,
# x=3, goes up
not_submultiplicative,
# fR = R+ which is open
not_closed_map,
open_map,
not_square_integrable,
not_integrable,
not_bounded,
strictly_monotonic,
convex,
])
##! ex


obj('int_step01', [
# take step01. then integrate. that's a _/, continuous. 
continuous,
not_differentiable,
piecewise_linear,
not_injective,
not_surjective,
not_piecewise_constant,
not_even,
not_odd,
not_superadditive,
subadditive,
# can go up: f-1f-1=0<f1=1
not_submultiplicative,
# if fxy is less, at least one of x and y is negative. but fxy can't be <0
supermultiplicative,
])
##! int_step01

obj('int_int_step01', [
# take step01. then integrate. that's a _/, continuous. integrate again, getting a wiggle _/ that's differentiable but not C2. 
differentiable,
not_C2,
piecewise_polynomial,
not_piecewise_linear,
not_injective,
not_surjective,
not_even, 
not_odd,
# 1 and -1
not_superadditive, 
# 1 and 1 (quadratic on the right)
not_subadditive,
# can go up: f-1f-1=0<f1=1
not_submultiplicative,
# if fxy is less, at least one of x and y is negative. but fxy can't be <0
supermultiplicative,
])
##! int_int_step01

obj('int_int_int_step01', [
# take step01. then integrate. that's a _/, continuous. integrate again, getting a _/ curve that's differentiable but not C2. integrate again, getting C2 but not C3, hence not smooth.
C2,
not_smooth,
piecewise_polynomial,
not_piecewise_linear,
not_injective,
not_surjective,
not_odd,
not_even,
# 1 and -1
not_superadditive, 
# 1 and 1 (cubic on the right)
not_subadditive,
# can go up: f-1f-1=0<f1=1
not_submultiplicative,
# if fxy is less, at least one of x and y is negative. but fxy can't be <0
supermultiplicative,
])
##! int_int_int_step01

obj('jagged_steps', [
# write x in binary. then interpret it as a ternary number with 2. there's discontinuities at every dyadic rational. wwhen youflip 0.1111111 -> 1.00000, you go up by 1 and down by 1/3+1/9+... = 1/2
injective,
not_surjective,
odd,
#f1=1, f2=3
not_subadditive,
#f-1=-1, f-2=-3
not_superadditive,
# f3 = 4.  f9 = 3'1001 =28 > f3²
not_submultiplicative,
# f-3 = -4.  f-9 = -3'1001 = -28 < f3f-3
not_supermultiplicative,
])
##! jagged_steps

obj('int_jagged_steps', [
# integrate jagged steps. integrations always have f(0)=0
continuous,
# not actually..? differentiable for nonQ
#nowhere_differentiable,
# jagged steps has f(x) = -f(-x), so this thing is U shaped, min at 0
not_surjective,
not_injective,
])
##! int_jagged_steps

obj('int_int_jagged_steps', [
# integrate jagged steps twice
differentiable,
nowhere_C2,
# since int_jagged is always positive except 0 at 0, unbounded in each direction , we're monotone increasing
bijective,
])
##! int_int_jagged_steps

obj('int_int_int_jagged_steps', [
# integrate jagged steps thrice
C2,
nowhere_smooth,
# back to being u shaped
not_surjective,
not_injective,
])
##! int_int_int_jagged_steps

obj('indicator_one_hot_binary')
# 1 if binary expansion has exactly 1 1, else 0
almost_everywhere_smooth(indicator_one_hot_binary)
not_piecewise_continuous(indicator_one_hot_binary)
aux_indicator(indicator_one_hot_binary)
##! indicator_one_hot_binary

#stich them together; biject domains R to R- and the other R to R+
locally_satisfiable_properties = [not_almost_everywhere_continuous, not_almost_everywhere_differentiable, not_almost_everywhere_C2, not_almost_everywhere_smooth, not_nowhere_continuous, not_nowhere_differentiable, not_nowhere_C2, not_nowhere_smooth]
for property1, property2 in itertools.combinations(locally_satisfiable_properties, 2):
   Fun.assertions.append(Implies(And(Exists(X, property1(X)), Exists(X, property2(X))), Exists(X, And(property1(X), property2(X)))))


implies([piecewise_linear, differentiable], linear)

obj('identity_rationals_offset', [
# λx. x+1 if x ∈ ℚ else x
bijective,
nowhere_continuous,
])
##! identity_rationals_offset

obj('identity_rationals_offset_broken', [
# λx. rationals_offset(x) if x<0 else rationals_offset(x-1)
surjective,
not_injective,
nowhere_continuous,
])
##! identity_rationals_offset_broken


obj('half_crook', [
# λx. x if x<0 else x/2
bijective,
piecewise_linear,
not_linear,
continuous,
])
##! crook

implies([linear, surjective], bijective)
implies([linear, injective], bijective)

obj('sinh', [
# e^x - e^-x  /2
bijective,
smooth,
not_polynomial,
])
##! sinh

obj('cosh', [
# e^x + e^-x  /2
not_injective,
not_surjective,
smooth,
not_polynomial,
])
##! cosh

# because you have to be nonconstant, and the highest power has to be odd, else you'll eventually in either direction of the input be going the same dircetion in output
implies([polynomial, injective], surjective)

obj('int_int_half_crook', [
# twice integral of half_crook. so like x^3 but different coefficients
piecewise_polynomial,
bijective,
not_smooth,
C2,
])
##! int_int_half_crook

obj('stitch_e_x_ex', [
# e^-x for x<0 else e^x
not_smooth,
piecewise_smooth,
not_differentiable,
not_piecewise_polynomial,
continuous,
not_injective,
not_surjective,
])
##! stitch_e_x_ex

obj('linear_dust', [
# identity on rationals. then take a positive irrational and assign the value 1, say. extend by additivity. then choose another undefined one to send to 1, and so on. but make the ones you choose have a limit point at 0, to make it non continuous at 0
additive,
nowhere_continuous,
not_injective,
# everything gets sent to rationals
not_surjective,
])
##! linear_dust

#shaky
obj('linear_dust_log_scale', [
# λx. e^linear_dust ln x (0 at 0, negative at negative)
# fxfy = e^linear_dust ln x + linear_dust ln y = e^linear_dust ln(xy) = fxy
multiplicative,
nowhere_continuous,
not_injective,
# everything gets sent to rationals
not_surjective,
odd,
])
##! linear_dust_log_scale


obj('x2cosx', [
even,
surjective,
not_polynomial,
smooth,

])
##! x2cosx

obj('sign', [
# -1,0,1 for negative, 0 , positive
odd, 
not_constant, 
piecewise_constant,
# to go down, f(x+y) = 0 or -1. if 0, x=-y, so f(x+y)=0. if -1, not both x,y>0
superadditive,
])
##! sign


obj('indicator_1ball', [
# indicator of within 1 of 0
aux_indicator,
even, 
not_constant, 
piecewise_constant,
])
##! indicator_1ball

obj('indicator_0', [
# indicator of 0
aux_indicator,
even, 
not_constant, 
piecewise_constant,
# can go up: f01 > f0f1
not_submultiplicative,
# can't go down: if fxy < fxfy, it's 0, so x and y not 0, but then fxfy=º
supermultiplicative,
])
##! indicator_0


obj('indicator_nonzero', [
# indicator of not 0 
aux_indicator,
even, 
not_constant, 
piecewise_constant,
# eevyrthing goes to 1, except 0 which is absorbing.
multiplicative,
])
##! indicator_nonzero


#! prop
#-- not quasi_continuous?
#-- not upper_semicontinuous?
#-- not lower_semicontinuous?
#-- not monotonic?
#-- not locally_bounded?
#-- 
#-- total time taken: 4.79
#-- initial consistency check time: 0.19


WriteQuestions('real_functions.py')


