class calculator{
    public int add(int n1,int n2, int n3)
    {
        return n1+n2+n3;

    }
    int num=5;
    public int add(int n1,int n2)
    {
        return n1+n2;//based on the parameters pass it in the obj
    }


}
public class obj1 {
    public static void main(String a[])

    
    {
        int data=10;


        calculator obj=new calculator();
        calculator obj1=new calculator();

        int r1=obj.add(3,4);
        int num=8;
        //System.out.println(r1);
        System.out.println(obj.num);
        System.out.println(obj1.num);



    }
    
}
