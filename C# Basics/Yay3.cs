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
                  
                //this if statement is supposed to catch when a negative number is entered...
                if(NumberOfTimes < 0)
                {
                    Console.WriteLine("You must enter a positive number.");
                }
                //...and if no negative then do the following...                  
                while(NumberOfTimes > 0)
                {
                    Console.WriteLine("Yay!");
                    NumberOfTimes--;
                }                 
            }
            catch (FormatException)
            {
                Console.WriteLine("You must enter a whole number.");
            }
        }
    }
}