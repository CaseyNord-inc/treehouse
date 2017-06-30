using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Nord.SimpleConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // This is a comment
            string greeting = "Hello World";

            string input = "Casey Nord";

            Console.Write(greeting + ' ');
            Console.WriteLine(SplitName(input)[0]);
        }

        static string[] SplitName(string input)
        {
            return input.Split(' ');
        }
    }
}
