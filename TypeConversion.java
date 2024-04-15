public class TypeConversion {

    public static void main(String[] args) {

        byte b=127;
        int a=12;
        //b=a will not work 
        

        b=(byte)a;// the value of b now is 12
        a=b;//the value of a 12

        System.out.println(b);
        System.out.println(a);
        
    }
    
}
