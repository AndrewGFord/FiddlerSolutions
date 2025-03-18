# Numerical integration attempt to solve the same problem

import math

eps = 1e-8
intervals=16
domain_min = 0
domain_max = math.pi
iterations = 0
diff = 0

def theta_integrand(theta):
	one_plus_sine = 1 + math.sin(theta)
	one_plus_sine_sq = one_plus_sine*one_plus_sine
	value = 1.0/(2.0*one_plus_sine_sq)
	value -= 1.0/(3.0*one_plus_sine_sq*one_plus_sine)
	return value

# make more robust by passing theta_integrand() in as a parameter?
def trapezoid_rule(integrand,theta_1,theta_2):
	return 0.5*(integrand(theta_1)+integrand(theta_2))*(theta_2-theta_1)

def integrate(integrand,a,b,intervals):
	interval_length = (b-a)/intervals
	value = 0
	for ii in range(intervals):
		x_1 = a+ ii*interval_length
		x_2 = x_1 + interval_length
		value += trapezoid_rule(integrand,x_1,x_2)
	return value

integral_value = 0 # saves an if statement inside the loop
prev_integral_value = 0

# looping portion
while (abs(diff) > eps or iterations < 2):
	prev_integral_value = integral_value
	integral_value = integrate(theta_integrand,domain_min,domain_max,intervals)
	diff = integral_value - prev_integral_value
	print(f'Intervals: {intervals}, Integral Value: {integral_value}, Difference: {diff}')
	intervals *= 2
	iterations += 1

numerical_answer = (2.0/15.0+math.pi/6.0-integral_value)/(math.pi/2.0)
analytical_answer = 1.0/3.0-4.0/(9.0*math.pi)
print(f'Final answer, after plugging in result: {numerical_answer}')
print(f'Analytical answer (should match): {analytical_answer}')