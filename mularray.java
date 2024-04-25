public class mularray {
    public static void main(String a[])
    {
        int nums[][]=new int[3][];

        nums[0]=new int[3];
        nums[1]=new int[4];
        nums[2]=new int[2];

    for(int i=0;i<nums.length;i++)
{
    for(int j=0;j<nums[i].length;j++)
    {
        nums[i][j]=(int)(Math.random()*10);

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

