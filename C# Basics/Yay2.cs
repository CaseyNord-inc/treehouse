using System;

namespace Treehouse.CodeChallenges
{
    class Program
    {
        static void Main()
        {
            Console.Write("Enter the number of times to print \"Yay!\": ");

            var entry = Console.ReadLine();
            try
            {
                var NumberOfTimes = int.Parse(entry);

                while(NumberOfTimes>0)
                {
                    Console.WriteLine("Yay!");
                    NumberOfTimes--;
                }
            }
            catch (FormatException)//ArgumentNullException
            {
                Console.WriteLine("You must enter a whole number.");
            }
        }
    }
}

//for some reason this one works in the final test but my other one doesn't even though it totally works in the console here.