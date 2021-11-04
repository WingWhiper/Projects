
public class Character {
	/*
	 * It's possible we'll need to add a lot to this class as progression happens and new classes are added later, so there will be a top level comment
	 * here for any discussion on potential additions to the character class
	 * Current ideas for addition are:
	 * 1. Should there be a loop of some sort to check players health, and if it turns zero at any time, send out a bool(false) state that the game receives and knows to give a game over screen?
	 */
	//Character's main attributes needed to make a character
	private String name;
	private String gender;
	private int age;
	private int level;
	private int strength;
	private int intelligence;
	private int defense;
	private int experience;
	Dice chanceToHit = new Dice(20, 1);
	
	//Default  character constructor
	public Character() {
		this("None", "None", 1, 1, 10, 10, 10, 0);
	}
	//Constructor with arguments
	public Character(String n, String g, int a, int l, int s, int i, int d, int x) {
		this.name = n;
		this.gender = g;
		this.age = a;
		this.level = l;
		this.strength = s;
		this.intelligence = i;
		this.defense = d;
		this.experience = x;
	}
	
	//public setter methods
	public void setName(String newName) {this.name = newName;}
	public void setGender(String newGender) {this.gender = newGender;}
	public void setAge(int newAge) {this.age = newAge;}
	
	//Public Getter Methods
	public String getName() {return this.name;}
	public String getGender() {return this.gender;}
	public int getAge() {return this.age;}
	public int getLevel() {return this.level;}
	public int getStrength() {return this.strength;}
	public int getIntelligence() {return this.intelligence;}
	public int getDefense() {return this.defense;}
	public int getCharExperience() {return this.experience;}
	public String getStats() {return "Strength: " + this.strength + "\nIntelligence: " + this.intelligence + "\nDefense: " + this.defense;}
	
	//New toString method to test output from methods
	public String toString() {return "\n" + this.name + " is a " + this.gender + " who is " + this.age + " years old and level " + this.level;};
	
	//EXPERIMENTAL STUFF DOWN HERE
	
	//Method for increasing the players level and attributes
	public void levelUp() {this.level++;}
	public void raiseStrength() {this.strength++;}
	public void raiseIntelligence() {this.intelligence++;}
	public void raiseDefense() {this.defense++;}
	

}
