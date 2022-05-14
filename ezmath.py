from funcs import common_divisors, common_multiples, pythagorean_t, quadratic_e
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
              "exit : exits the program\n"
              "pt x y : pythagorean theorem\n"
              "qe a b c : for quadratic equation")
        continue
    if "exit" in choice:
        print("QUITING...")
        sys.exit()
    if len(choice) == 3:
        if "lcm" in choice[0]:
            print(common_multiples.lcm(int(choice[1]), int(choice[2])))
        elif "gcd" in choice[0]:
            print(common_divisors.gcd(int(choice[1]), int(choice[2])))
        if "pt" in choice[0]:
            print(pythagorean_t.pt(
                float(choice[1]), float(choice[2])))
    elif len(choice) == 4:
        if "qe" in choice[0]:
            roots = quadratic_e.qe(
                float(choice[1]), float(choice[2]), float(choice[3]))
            print(f"{roots[0]}, {roots[1]}\n{roots[2]}")
    else:
        pass
