/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		System.out.println("Cuál es tu edad");
		Scanner leer = new Scanner(System.in);
		int edad = leer.nextInt();
		System.out.println(edad>=18? "Eres mayor de edad 😊": "Eres menor de edad 😞");
	}
}