package CCCSenior2017;

import java.util.Arrays;
import java.util.Scanner;

/**
 * This is the solution to the third question of the 
 * 2017 CCC Senior, titled "Nailed It!".
 * 
 * @author Cindy Li
 * @since Sunday, October 7th, 2018
 */
public class S32017 {

	public static void main(String[] args) {
		
		// initialize scanner object (for reading input)
		Scanner input = new Scanner(System.in);
		
		int n = input.nextInt();
		int maxLength = 0;
		int numHeights = 0;
		
		int[] wood = new int[2000]; // to store how many pieces there are of 
									// each length of wood
		
		// fill array
		Arrays.fill(wood, 0);
		
		for (int i = 0; i < n; i++) {
			int height = input.nextInt();
			wood[height-1]++;
		}
		
		input.close();
		
		
		// loop through all possible heights
		for (int h = 2; h <= 4000; h++) {
			
			int length = 0;
			
			// find number of pairs that add up to h
			for (int i = Math.max(1, h-2000); i <= h/2; i++) {
				
				if (i == h-i)
					length += wood[i-1]/2;
				else
					length += Math.min(wood[i-1], wood[h-i-1]);
			}
			
			// if length is greater than current max length, set 
			// max length to this
			if (length > maxLength) {
				maxLength = length;	
				numHeights = 1;
			}
			
			// if length is equal to current max length, increment numHeights
			else if (length == maxLength)
				numHeights++;
		}
		
		System.out.println(maxLength + " " + numHeights);
		return;
		
	}
}
