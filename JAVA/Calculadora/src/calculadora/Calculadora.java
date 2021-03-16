package calculadora;
import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        
        double num1=0, num2=0, resultado=0;
        String calc = "";
        
        System.out.print("¿Que operación desea realizar? +, -, * o / : ");
        calc = in.nextLine();
        
        System.out.print("Ingrese el primer número: ");
        num1 = in.nextInt();
        
        System.out.print("Ingrese el segundo número: ");
        num2 = in.nextInt();
             
        switch (calc){
            
            case "+":
                resultado = num1 + num2;
            break;
            
            case "-":
                resultado = num1 - num2;
            break;
            
            case "*":
                resultado = num1 * num2;
            break;
            
            case "/":
                if (num2==0){
                    System.out.println("Error Matemático");
                    resultado = 0000000000;
                }
                else {
                    resultado = num1/num2;
                }
            break;
            
            default:
                System.out.println("Usted no ha ingresado una operación valida");
            break;
        }
               System.out.println("El resultado es: " +resultado);
    }
    
}
