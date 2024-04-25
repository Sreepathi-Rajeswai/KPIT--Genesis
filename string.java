class Mobile
{
    String brand;
    int price;
    static String name;//common value for all the objects update as the latest call of the object

    public Mobile()
    {
        brand="";
        price=209324;
        System.out.println("in constructor");

    }
    static
    {
        name="phone";
        System.out.println("in static block");//static block execute always first
    }

    public void show()
    {
        System.out.println(brand + " : " + price + " : " + name);

    }
}


public class string {
    public static void main(String a[])
    {

        // StringBuffer sb=new StringBuffer("Raji");
        // sb.append("Sreepathi");
        // sb.insert(1,"k");
        // System.out.println(sb);  
        Mobile obj1=new Mobile();
        obj1.brand="Apple";
        obj1.price=90328483;
        obj1.name="smartphone";


        Mobile obj2=new Mobile();
        obj2.brand="Apple";
        obj2.price=90328483;
        obj2.name="ios";



        obj1.show();
        obj2.show();//create an object





    }
}
