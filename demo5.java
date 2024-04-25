//add though the extends of the previous class is known as overriding
//import javax.swing.SpringLayout;
import java.lang.*;
import java.util.*;

class A{
    public int add(int n1,int n2)
    {
        return n1+n2;
    }
    // public void config()
    // {
    //     System.out.println("in A config");
    // }
}

class B extends A{
    public int add(int n1, int n2)
    {
        return n1+n2+1;// adding 1 for testing if it works ,print 8
    }
}


public class demo5 {
    public static void main(String a[])
    {
        A obj=new A();
        int r1=obj.add(3,4);
        System.out.println(r1);

    }
    
}
