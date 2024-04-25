public class array {
    public static void main(String a[])
    {
        // int nums[]=new int[8];
        // nums[7]=9;
        // nums[3]=9;
        // for(int i=0;i<=8;i++)
        // {
        // System.out.println(nums[i]);//if don't insert any value to particular index then it will ttake the index as 0
        // }

        int nums[][]=new int[3][4];

        for(int i=0;i<3;i++)
        {
            for(int j=0;j<4;j++)
            {
                nums[i][j]=(int)(Math.random()*12);//function for selecting a random valueto the multiple arrays
                System.out.print(nums[i][j]+ " ");
            }
            System.out.println();
           
        }
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<4;j++)
            {
                System.out.print(nums[i][j]+ " ");
            }
            System.out.println();
        }
        //it also give the values like rows and columns //....
                                                        //....
                                                        //....

        for(int n[]:nums) 
        {
            for(int m:n)
            {
                System.out.print(m+ " ");
            }
            System.out.println();
        }


    }
}
