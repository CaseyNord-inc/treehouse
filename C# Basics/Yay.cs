using System;

namespace Treehouse.CodeChallenges
{
    class Program
    {
        static void Main()
        {  
            while(true)
            {         
                Console.Write("Enter the number of times to print \"Yay!\": ");
                try
                {
                    int times = int.Parse(Console.ReadLine());
                      
                    while (times > 0)
                    {
                        Console.WriteLine("Yay!");
                        times --;
                    }
                }
                catch(FormatException)
                {
                    Console.WriteLine("You must enter a whole number.");
                    continue;
                }   
            }
        }
    }
}