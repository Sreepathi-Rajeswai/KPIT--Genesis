//inheritence is a accessing from parent class to child class
//EX: my money is my money my parents money also my money
//multile inheritance in java not work
class Calc
{
    public int add(int n1,int n2)
    {
        return n1+n2;
    }
    public int sub(int n1,int n2)
    {
        return n1-n2;
    }

    public int mul(int n1,int n2)
    {
        return n1*n2;
    }
    public int div(int n1,int n2)
    {
        return n1/n2;
    }

    public double power(int n1,int n2)
    {
        return Math.pow(n1,n2);
    }


}
public class demo4 {
    
    public static void main(String a[])
    {
        Calc obj=new Calc();
        int r1=obj.add(4,6);
        int r2=obj.sub(8,3);
        int r3=obj.mul(4,6);
        int r4=obj.div(8,3);
        double r5 =obj.power(4,2);

        System.out.println(r1 + " "+r2+" "+r3+" "+r4+" "+r5+" ");
        // System.out.println(r2);
        // System.out.println(r3);
        // System.out.println(r4);

        //we can also do it in a different file as extend the Calc
        //public class AdvCalc extends Calc
    }
}
