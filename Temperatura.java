/******************************************************************************
temp=float(input("Temperatura registrada"))
if temp>=27: print("Póngase algo fresco👗")
elif temp>=20 and temp<27: print("Abrígate 🧥")
elif temp>=16 and temp<20: print("Abrígate más 🧥🧣")
else: print("Está helado 🥶")

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	
		System.out.println("Temperatura registrada: ");
		Scanner leer = new Scanner(System.in);
		//nextLine es para String
		//netFloat es para leer decimales
		float temp = leer.nextFloat();
		//&& and || or
		if(temp>=27){System.out.println("Póngase algo fresco👗");}
		else if (temp>=20 && temp<27){System.out.println("Abrígate 🧥");}
		else if (temp>=16 && temp<20){System.out.println("Abrígate más 🧥🧣");}
		else {System.out.println("Está helado 🥶");}
	}
}