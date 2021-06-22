import sys

def checkInRange(number):
    if number in range(13, 20) and number not in range(15, 17):
        return False
    else:
        return True

def sumOfThreeNumbers(num1, num2, num3):
    res = 0
    if checkInRange(num1):
        res += num1
    if checkInRange(num2):
        res += num2
    if checkInRange(num3):
        res += num3
    return res


if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            print(f"Exactly 3 numbers are required")
            exit()

        num1, num2, num3 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        res = sumOfThreeNumbers(num1, num2, num3)
        print(res)
    except Exception:
        print(f'All inputs must be numeric')