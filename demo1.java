//this and super
//super is a constructor every constructor has super keyword, call the constructor of a super class i.e parameterized constuctor
//every class in java extends the object
class A extends Object{
    public A()
    {
    super();
    System.out.println("in A");
}
    public A(int n){
    super();
    System.out.println("in A int");

}
}

class B extends A{
    public B(){
    
        super();
        System.out.println("in B");
    
    }

    public B(int n)
    {
        this();
        System.out.println("in B int");
    
    }
}

public class demo1 {
    public static void main(String a[])
    {
         B obj=new B(5);
    }
    
}
