from time import time
import sys

coins = []
output = False
# dataset format: "50, 1, 20, 50, 2"
f = open(sys.argv[1], 'r').read().split(",")
for num in f:
    coins.append(int(num))
print("Available coins:", coins)


def find_coin_greedy(v):
    ans = []
    # take the biggest coin available, sorting and reversing iteration
    coins_sorted = sorted(coins)
    for coin in reversed(coins_sorted):
        while v >= coin:
            v = v - coin
            ans.append(coin)
    if output:
        print(" Returned coins:", ans)


def find_coin_brutal(v):
    ans = []
    for coin in coins:
        while v >= coin:
            v = v - coin
            ans.append(coin)
    if output:
        print(" Returned coins:", ans)


if len(sys.argv) == 3 and sys.argv[2] == "-o":
    output = True
n = int(input("Money to exchange (in cents): "))
startTime = time()
find_coin_brutal(n)
elapsedTime = time() - startTime
print("     Brutal Force:", elapsedTime, "seconds")
startTime = time()
find_coin_greedy(n)
elapsedTime = time() - startTime
print("     Greedy:", elapsedTime, "seconds")
