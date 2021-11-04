
public class Battle {
	/*
	 * Combat needs to have a few things, combatants, A way to calculate how much damage those combatants do, weather it hits, weather it kills the combatant.
	 * What details does the combat need from the player character to calculate things like damage, chance to hit, and death conditions?
	 * HP, Stats influencing combat.
	 * Optimally, the combat class should only need 2 input variables, one should be the player and the other the enemy.
	 * This obviously limits us to single enemy combat encounters and no other party members, and may need to evolve in the future to take in more combatants.
	 * You could possibly also create a private method inside the class to add a clone of an enemy and create additional combatants, but this should be
	 * considered much later and not a current goal.
	 * 
	 * DamageDiscussion:
	 * Potentially in the future, weapons and their statistics.
	 * For simplicity's sake, We're going to use a random number generator to determine chance to hit and damage output. 
	 * Chance to hit : Random a # between x to y that will return true or false if that number is greater than the number needed to hit(true) or if it is less than return (false)
	 * Damage: Simply a random number x to y and the number will be returned as the amount of damage done.
	 * Later complexity can be added and based on future factors such as dodge/block/agility/ect..
	 * Should we contain the health of the combatants to the class and only return a boolean for the winner? May also need a bool for winner or just return player HP, and then if a player HP
	 * is returned then we know to store that in the setHealth() methods, but if it returns zero/null for player health we would also know the player lost by default.
	 * Think about how we want to return results.
	 * 
	 */
}
