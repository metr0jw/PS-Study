using System;
using System.Text;
using System.Collections.Generic;  


namespace Baekjoon
{
    using LD = List<double>;
    public class Program
    {
        public static void Main()
        {
            LD P_xz = new LD();
            LD P_yz = new LD();
            string[] ss;

            int N_xz = int.Parse(Console.ReadLine());
            
            for (int i=0; i<N_xz; i++)
            {
                LD list = new LD();
                ss = Console.ReadLine().Split(' ');
                list.Add(int.Parse(ss[0]));
                list.Add(int.Parse(ss[1]));
                P_xz.AddRange(list);
            }


            int N_yz = int.Parse(Console.ReadLine());
            
            for (int i=0; i<N_yz; i++)
            {
                LD list = new LD();
                ss = Console.ReadLine().Split(' ');
                list.Add(int.Parse(ss[0]));
                list.Add(int.Parse(ss[1]));
                P_yz.AddRange(list);
            }
        }
    }
}