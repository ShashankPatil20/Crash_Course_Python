#1. Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor
# is a number that is prime and divides another without a remainder.
Ans.
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor +=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

#2.
# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it.
# A divisor is a number that divides into another without a remainder.
#Ans.
import math


def sum_divisors(num):
    # Final result of summation of divisors
    if num == 0:
        return 0
    else:
        result = 0

        # find all divisors which divides 'num'
        i = 2
        while i <= (math.sqrt(num)):

            # if 'i' is divisor of 'num'
            if (num % i == 0):

                # if both divisors are same then
                # add it only once else add both
                if (i == (num / i)):
                    result = result + i;
                else:
                    result = result + (i + num / i);
            i = i + 1

        # Add 1 to the result as 1 is also
        # a divisor
        hell = int(result + 1)
        return (hell)


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114

#3. The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# Fill in the blanks to complete the function to satisfy these conditions.
#Ans.
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number*multiplier
		# What is the additional condition to exit out of the loop?
		if result>25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24