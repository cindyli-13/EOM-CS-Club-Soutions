package ccc17;

import java.util.Scanner;

public class J32017 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		//Retrieving inputs
		Scanner sc = new Scanner(System.in);
		
		int x1 = sc.nextInt(), y1 = sc.nextInt(); //starting coordinate
		int x2 = sc.nextInt(), y2 = sc.nextInt(); //ending coordinate
		int charge = sc.nextInt(); //charge;
		
		sc.close();
		
		//minimum charge to reach destination
		int minCharge = Math.abs(x1 - x2) + Math.abs(y1 - y2);
		int leftoverCharge = charge - minCharge;
		
		if(leftoverCharge >= 0 && leftoverCharge % 2 == 0) {
			System.out.println("Y");
			
		}else {
			System.out.println("N");
			
		}
		
	}

}
