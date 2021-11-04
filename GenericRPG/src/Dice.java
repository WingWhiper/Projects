import java.util.Random;

public class Dice {
	private int numberOfSides;
	private int timesToRoll;
	private int rollResult = 0;
	
	Random randomNumbers = new Random();
	
	//default the dice to be 20 sided and roll only once
	public Dice() {
		this(20, 0);
	}
	
	public Dice(int sides, int rolls) {
		this.numberOfSides = sides;
		this.timesToRoll = rolls;
	}
	
	public void setNumberOfSides(int newDice) {this.numberOfSides = newDice;}
	public void setTimesToRoll(int newRolls) {this.timesToRoll = newRolls;}
	public void setRollResult(int newRollResults) {this.rollResult = newRollResults;}
	
	/*
	 * Main way to return the results of the rolls. This shouldn't use a print function, 
	 * and in the future will just return an int with the result, 
	 * that can then be store, and used elsewhere
	 */
	public void roll() {
		for (int i = 0; i < this.timesToRoll; i++) {
			//only for testing - should be a return statement and int type not void. I think
			System.out.println(rollDice()); 
		}	
	}
	
	private int rollDice() {
		//If it's a 10 sided die, we need it to be in increments of 10, this loops makes sure we account for that.
		if (numberOfSides == 10) {
			rollResult = randomNumbers.nextInt(10) + 1;
			rollResult = rollResult * 10;
			return this.rollResult;
		}
		//If it's not a 10 sided, standard roll rules apply, no need to multiply the result.
		else {
			rollResult = randomNumbers.nextInt(numberOfSides) + 1;
			return this.rollResult;
		}
	}
	
	/* TODO The roll public method is only rolling 1 time
	 */

}
