#!/bin/python3

import game_state

def main():
	gs = game_state.StartScreen()
	while gs != None:
		gs = gs.tick()
	print("Exiting")

if __name__ == "__main__":
	main()
