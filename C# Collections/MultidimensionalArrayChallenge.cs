using System;

namespace Treehouse.CodeChallenges
{
    public static class MathHelpers
    {
        public static int[,] BuildMultiplicationTable(int maxFactor)
        {
            int[,] arr = new int[maxFactor + 1, maxFactor + 1];

            for (int x = 0; x < arr.GetLength(0); x++)
            {
                for (int y = 0; y < arr.GetLength(1); y++)
                {
                    arr[x,y] = x * y;
                }
            }

            return arr;
        }
    }
}