import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n, r;

        n = input.nextInt();
        input.close();

        r = ((n+1)*(n+2))/2;
        System.out.printf("%d%n",r);
    }
}