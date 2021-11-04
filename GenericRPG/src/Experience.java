
public class Experience {
	private int currentLevel;
	private int xpNeededToLevel;
	private int currentXp;
	private int earnedXp;
	
	//default Experience constructor
	public Experience() {this(1, 0, 0, 0);}
	
	//default constructor arguments
	public Experience (int cl, int xpn, int cxp, int exp) {
		this.currentLevel = cl;
		this.xpNeededToLevel = xpn;
		this.currentXp = cxp;
		this.earnedXp = exp;
	}
	
	//setters
	//The 2 set methods are set from the player character
	public void setCurrentLevel(int newLevel) {this.currentLevel = newLevel;}
	public void setCurrentXp(int newXp) {this.currentXp = newXp;}
	
	/*This method needs to be more robust. Current just brings in player XP but there really isn't a need for this value to be set from the player class.
	 * Optimally you would pull in current player XP and reference that against an array of values that store XP needed for each level
	 *And then use the returned amount minus the current XP to determine what remaining XP is needed.
	 */
	public void setXpNeededToLevel(int newXpNeeded) {this.xpNeededToLevel = newXpNeeded;}
	/*
	 * Method to set the xp earned by the character from various sources
	 * This should function by pulling in an integer amount from something like a enemy kill or a quest completion. 
	 * 
	 */
	public void setEarnedXp(int newXpEarned) {this.earnedXp = newXpEarned;}
	
	//getters
	public int getCurrentLevel() {return this.currentLevel;}
	public int getCurrentXp() {return this.currentXp;}	
	public int getXpNeededToLevel() {return this.xpNeededToLevel;}
	public int getXpEarned() {return this.earnedXp;}

}
