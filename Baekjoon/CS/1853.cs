using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Math


namespace Baekjoon
{
    using LD = List<double>;
    public class Program
    {
        public static int MathMod(int a, int b)
        {
            int c = ((a % b) + b) % b;
            return c;
        }

        public static IEnumerable<T> ShiftRight<T>(IList<T> values, int shift)
        {
            for (int index = 0; index < values.Count; index++)
            {
                yield return values[MathMod(index - shift, values.Count)];
            }
        }

        public static List<T> removeDuplicates<T>(List<T> list)
        {
            return new HashSet<T>(list).ToList();
        }

        public static LD Projection(LD x, LD z1, LD z2)
        {
            int N_x1 = x.Count();
            int N_z2 = z2.Count();
            int i = 0;
            LD list = new LD();

            while (!(z[i]==z2[0] && z[(i+1)%N]>z2[0]))
                i = (i+1) % N;

            x = ShiftRight(x, i);
            z = ShiftRight(z, i);

            LD result = LD(N2);

            return list;
        }

        public static void Main()
        {
            LD P_x1 = new LD();
            LD P_z1 = new LD();
            LD P_y2 = new LD();
            LD P_z2 = new LD();
            string[] ss;

            int N_xz = int.Parse(Console.ReadLine());
            for (int i=0; i<N_xz; i++)
            {
                ss = Console.ReadLine().Split(' ');
                P_x1.Add(double.Parse(ss[0]));
                P_z1.Add(double.Parse(ss[1]));
            }

            int N_yz = int.Parse(Console.ReadLine());
            for (int i=0; i<N_yz; i++)
            {
                ss = Console.ReadLine().Split(' ');
                P_y2.Add(double.Parse(ss[0]));
                P_z2.Add(double.Parse(ss[1]));

            }
            
            LD list = new LD();
            LD z = new LD();
            for (int i=0; i<N_xz; i++)
                list.Add(P_z1[i]);

            for (int i=0; i<N_yz; i++)
                list.Add(P_z2[i]);
            
            list.Sort();
            z = removeDuplicates(list);

            LD XMin = Projection(P_x1, P_z1, z);
            LD YMin = Projection(P_y2, P_z2, z);

            P_x1.Reverse();
            P_z1.Reverse();
            P_y2.Reverse();
            P_z2.Reverse();

            LD XMax = Projection(P_x1, P_z1, z);
            LD YMax = Projection(P_y2, P_z2, z);

            int N = z.Count();
            double result = 0.0;
            for (int i=0; i<N-1; i++)
            {
                int j=(i_1)%N;
                double x1 = XMax[i] - XMin[i];
                double y1 = YMax[i] - YMin[i];
                double x2 = XMax[j] - Xmin[j];
                double y2 = XMax[j] - YMin[j];
                double h = z[j] - z[i];
                result += h * (2*x1*y1 + 2*x2*y2 + x1*y2 + x2*y1) / 6;
            }

            Console.WriteLine("{0}", Math.Round(result, 3))
        }
    }
}