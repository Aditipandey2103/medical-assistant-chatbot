import java.util.Arrays;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Functions {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int size = sc.nextInt();
        int[] numbers=new int[size];

        for(int i=0;i<size;i++){
            numbers[i]=sc.nextInt();
        }

        System.out.println(Arrays.toString(numbers));
        int x=5;
        for(int j=0;j<size;j++){
            if(numbers[j]==5){
                System.out.println("the no. 5 is at "+j+"th place");
                breintak;
            }
        }
//         j=numbers;
//        if(numbers[int j]!=5){
//            System.out.println();
        }
    }

        // to see how IntelliJ IDEA suggests fixing it.

}







