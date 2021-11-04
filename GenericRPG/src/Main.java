import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		/*
		 * Everything currently in the main is strictly for debugging, and there is currently no active game loop state.
		 */
		//New scanner for input
		Dice newDice = new Dice(10,3);
		Scanner keyboard = new Scanner(System.in);
		//Testing stuff
		Character newChar = new Character();
		newChar.setName("Joe");
		newChar.setAge(33);
		newChar.setGender("Male");
		U.ps(newChar.getStats());
		newChar.levelUp();
		System.out.print(newChar);
		keyboard.close();
		Enemy newEnemy = new Enemy();
		newEnemy.setName("Goblin");
		System.out.println(newEnemy);
		newDice.roll();
		U.nl();
		newDice.roll();
		U.nl();
		newDice.roll();
		Weapon oneHandedSword = new Weapon(6, 2);
		System.out.print(oneHandedSword);
		// TODO Auto-generated method stub
		
	}

}
