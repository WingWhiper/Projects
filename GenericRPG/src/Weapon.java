
public class Weapon {
	// The type of dice to roll, 6/8/12/ ect.
	private int damage = 0;
	// The amount of times to roll. Example 2d6. 2 numberOfHits, 6 damage
	private int numberOfHits = 0;
	Dice doDamage = new Dice(damage, numberOfHits);
	
	public Weapon() {
		this(0,0);
		
	}
	public Weapon(int d, int noh) {
		this.damage = d;
		this.numberOfHits = noh;
	}
	//Damage method, should call the dice to roll, return those numbers in the method.
}
