from cs50 import get_float

while True:

    ch = get_float("Change owed: ")

    if ch > 0:

        cents = ch * 100

        q = cents // 25
        d = (cents % 25) // 10
        n = ((cents % 25) % 10) // 5
        p = (((cents % 25) % 10) % 5) // 1

        coins = q + d + n + p

        print(f"{coins:.0f}")

        break
