# DataFork - Junior Data Engineer

Interview questions for the position of junior data engineer at DataFork company. 


# Question 1 - Water Tanker Dealer

## Description

There are $N$ water tankers with capacity $C\_i$ containing $W\_i$ amount of water.
The total amount of water is the sum of amount of the water in all the tankers.
The task is to transfer the total amount of water from one city to another.

Find the minimum number of tankers to transfer the total amount of water from one city to another.

## Input format:

  1) the number of tankers to provide ($1 \le N \le 10^5$)
  
  2) the sequence of capacities $C\_i$ of $i^{th}$ tanker ($1 \le C_i \le 10^5$)

  3) the sequence of amounts of water $W\_i$ of $i^{th}$ tanker ($1 \le W\_i \le C\_i$)

## Output format

The minimum integer number of tankers to transfer the total amount of water.

## Example

Input:

  1) 3
  
  2) 4 9 6
  
  3) 3 2 5

Output:

  * 2 tankers ({capacity: water} -> {9: 9} and either {6: 1} or {4: 1})


# Question 2

## Description

There is a fair in a city that contains $N$ shops which are arranged in a straight line at $1, 2, ..., N$ positions. $M$ persons come to the fair and each visits shops in the range between $L\_i$ and $R\_i$ inclusively.

Determine the three most popular shops. The task is to fix the code, not to rewrite it.

## Input format:

  1) the number of test cases ($1 \le N \le 10$)
  
  2) the number of shops and visitors ($3 \le N, M \le 10^5$)

  3) the $M$ lines each containing $i^{th}$ person and the range of shops ($1 \le L \le R \le N$)

## Output format

For each test case three integers denoting the positions of three most popular shops.

## Example

Input:

  1) 1 (one test case)
  
  2) 6 5 ($N$ shops and $M$ visitors)
  
  3-1) 3 5
  
  3-2) 2 3
  
  3-3) 4 6
  
  3-4) 1 6
  
  3-5) 5 6

Output:

  * 5 3 4

Explanation:

The shop 1 is visited by only the fourth customer, the shop 2 by the second and the fourth client and so forth. By counting the frequencies the solution is obtained (the sorting was not envisaged in this explanation, but was encountered in the original code, so the output was corrected).

