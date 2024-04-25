//including encapsulation as methods
//this is a keyword which represents the current object
//constuctor lools like a method here constuctor name public Human
//everytime create a object call the constructor
class Human
{
    private int age;
    private String name;

    public Human()
    {
        age=19;
        name="Likki";
    }

    public int getAge()
    {
        return age;
    }
    public void setAge(int a)// this is a instance variable if we create obj here
    {
       age =a; //if we make this.age then it will give null
    }
    
    public String getName()
    {
        return name;
    }
    public void setName(String n)
    {
        name =n; 
    }


}


public class demo {
    public static void main(String a[])
    {
        Human obj=new Human();
        Human obj1=new Human();
        //obj.setAge(21);
        //obj.setName("Raji");

        System.out.println(obj.getName()+" : "+obj.getAge());
    }
    
}
