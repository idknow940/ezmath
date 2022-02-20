import common_multiples
import common_divisors
import sys
import numpy as np

print("""
███████╗███████╗███╗░░░███╗░█████╗░████████╗██╗░░██╗
██╔════╝╚════██║████╗░████║██╔══██╗╚══██╔══╝██║░░██║
█████╗░░░░███╔═╝██╔████╔██║███████║░░░██║░░░███████║
██╔══╝░░██╔══╝░░██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║
███████╗███████╗██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║
╚══════╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝""")

while True:
    choice = np.array(input("command> ").lower().split(" "))
    if "help" in choice:
        print("lcm x y : for least common multiples (limit 2 numbers)\n"
              "gcd x y : for greatest common divisor (limit 2 numbers)\n"
              "exit : exits the program")
        continue
    if "exit" in choice:
        print("QUITING...")
        sys.exit()
    if len(choice) == 3:
        if "lcm" in choice[0]:
            print(common_multiples.lcm(int(choice[1]), int(choice[2])))
        elif "gcd" in choice[0]:
            print(common_divisors.gcd(int(choice[1]), int(choice[2])))
    else:
        pass
