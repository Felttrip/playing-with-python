This was written in response to a discussion about an interview question a friend
brought up on Slack.

"You have 10k integers that are 16 bits each. Design an algorithm to count all of the
bits set to one in all of the numbers.

Slow count shows the simple but least efficient method.

Lookup table builds a table of the number of 1's for a given number, using this and
storing the numbers into "buckets" the algorithm can cut down its runtime by multiplying
the count of a given number with the number of 1's the look up table says it has.

bitwise and shows a method where using the bitwise and operation and a table of the values from 2^1 - 2^16,
you can calculate the number of 1's by finding the value of (the number) & (each table value). This method is nice
because it would be extremely simple to parallelize. The algorithm was orriginally presented by Ben S and was written in python by me.
