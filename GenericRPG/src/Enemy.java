
public class Enemy extends Character {
	/*
	 * Current things to think about:
	 * What does an enemy do, that a player does not, and will never do.
	 * Enemies will give XP, which a player will never do.
	 * Enemy can also attack the player, which the player shouldn't be able to do.
	 * The enemy will have to follow some sort of logic to know what to do, or else if does nothing.
	 * The enemy should be able to react to player actions(Though the player will also react to things the enemy does, so this is a bit ambiguous.)
	 */
	@Override
	public String toString() {return "\n" + this.getName() + " is a monster who is level " + this.getLevel();};

}
