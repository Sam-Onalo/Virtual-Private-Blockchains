import random
from math import ceil
from decimal import Decimal



from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy as np

# pip install -r .\requirments.txt

FIELD_SIZE = 10**5


def reconstruct_secret(shares):
	"""
	Combines individual shares (points on graph)
	using Lagranges interpolation.

	`shares` is a list of points (x, y) belonging to a
	polynomial with a constant of our key.
	"""
	sums = 0
	prod_arr = []

	for j, share_j in enumerate(shares):
		xj, yj = share_j
		prod = Decimal(1)

		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				prod *= Decimal(Decimal(xi)/(xi-xj))
		prod *=  yj
		sums += Decimal(prod)

	return int(round(Decimal(sums), 0))

def create_shares(xplist,yplist, d):
	f = lagrange(xplist,yplist)
	pool = []
	for i in range(0, d):
		# eval a polynormial given random value to get the y value
		x = random.randrange(1, FIELD_SIZE)
		# TODO: see if you can find an alternative method that will return an integer value
		y = np.polyval(f, x)

		# NEED BETTER SOLUTION
		y = np.round(y)
		y = int(y)

		# print(f'Additional share {x},{y}')
		pool.append((x, y))
	pool.append((xplist[0], yplist[0]))
	pool.append((xplist[1], yplist[1]))
	return pool

def polynom(x, coefficients):
	"""
	This generates a single point on the graph of given polynomial
	in `x`. The polynomial is given by the list of `coefficients`.
	"""
	point = 0
	# Loop through reversed list, so that indices from enumerate match the
	# actual coefficient indices
	for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
		point += x ** coefficient_index * coefficient_value
	return point


def coeff(t, secret):
	"""
	Randomly generate a list of coefficients for a polynomial with
	degree of `t` - 1, whose constant is `secret`.

	For example with a 3rd degree coefficient like this:
		3x^3 + 4x^2 + 18x + 554

		554 is the secret, and the polynomial degree + 1 is
		how many points are needed to recover this secret.
		(in this case it's 4 points).
	"""
	coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t - 1)]
	coeff.append(secret)
	return coeff


def generate_shares(n, m, secret):
	"""
	Split given `secret` into `n` shares with minimum threshold
	of `m` shares to recover this `secret`, using SSS algorithm.
	"""
	coefficients = coeff(m, secret)
	# Original Secret: 290
	# [43926, 89709, 290]
	shares = []

	for _ in range(0, n):
		x = random.randrange(1, FIELD_SIZE)
		shares.append((x, polynom(x, coefficients)))

	return shares


# Driver code
if __name__ == '__main__':

	# (3,5) sharing scheme
	t, n = 3, 9
	
	# for i in range(10):
    # Generate a random integer
	secret = random.randint(1, 500)
	# 

	#secret = 100

	# TODO: write code...
	print(f'Original Secret: {secret}')
		
	#     # Phase 0: Using Pred-definded shares
	# predefined = [(123,456), (789, 654), (0, 5)]
	x_predefined = [3,4,0]
	y_predefined = [10,20,secret]
	shares = create_shares(x_predefined,y_predefined, n - t + 1 )
	# predefined = [(123,456), (789, 654), (0, 5)]
	# print(f'THIS ONE: {shares}')

	# reconstruct_secret([[3,10],[4,20],[0,5]])
	# 	# Phase I: Generation of shares
	# shares = generate_shares(n, t, secret)

	print(f'Shares: {", ".join(str(share) for share in shares)}')

	# TODO: add predefine to shares list

	# TODO shuffle shares list


		# Phase II: Secret Reconstruction
		# Picking t shares randomly for
		# reconstruction
	pool = random.sample(shares, t)
	print(f'Combining shares: {", ".join(str(share) for share in pool)}')
	print(f'Reconstructed secret: {reconstruct_secret(pool)}')