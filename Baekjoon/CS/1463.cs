using System;
using System.Text;


public class Program
{
    public static void Main()
    {
        StringBuilder sb = new StringBuilder();
        int[] dp = new int[1000001];
        int x = int.Parse(Console.ReadLine());

        dp[1] = 0;
        for (int i = 2; i <= x; i++)
        {
            dp[i] = dp[i - 1] + 1;
            if (i % 2 == 0) dp[i] = Math.Min(dp[(int)(i/2)] + 1, dp[i]);
            if (i % 3 == 0) dp[i] = Math.Min(dp[(int)(i/3)] + 1, dp[i]);
        }
    sb.Append(dp[x]);
    Console.WriteLine(sb.ToString());
    }
}