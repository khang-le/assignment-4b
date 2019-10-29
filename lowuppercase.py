#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program checks whether enter letter is low case or upper case


def main():
    user_input = input("Please Enter Your Own Character : ")

    if(user_input.isupper()):
        print("The Given Character:", user_input, ", is an Uppercase"
              "Alphabet")
    elif(user_input.islower()):
        print("The Given Character:", user_input, ", is a Lowercase Alphabet")
    else:
        print("The Given Character:", user_input, ", is Not a Lower "
              "or Uppercase Alphabet")


if __name__ == "__main__":
    main()
