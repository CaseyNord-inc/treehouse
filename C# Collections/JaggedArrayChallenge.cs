
//I don't understand how I could get this to actually print the table to the console.
namespace Treehouse.CodeChallenges
{
    public static class MathHelpers
    {
        public static int[][] BuildMultiplicationTable(int maxFactor)
        {
            int[][] arr = new int[maxFactor + 1][];

            for (int x = 0; x <= maxFactor; x++)
            {
                arr[x] = new int [maxFactor + 1];

                for (int y = 0; y <= maxFactor; y++)
                {
                    arr[x][y] = x * y;
                }
            }

            return arr;
            Console.ReadLine();
        }
    }
}