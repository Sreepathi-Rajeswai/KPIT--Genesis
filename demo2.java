class A{

    public A()

    {
        System.out.println("object created");
    }
    public void show()

    {
        System.out.println("in A show");
    }
}

public class demo2 {
    
    public static void main(String a[])
    {
        // int marks;
        // marks=90;
        // A obj;
        // obj=new A();
        // //obj.show();

        new A().show();//anonymous object(can't use another time)
    }
}

//Camel casing
//class and interface- Calc, Runnable
//variable and method -marks,show()
//constants - PIE,BRAND
//showMyMarks()
//MyData

//age, DATA, Human()