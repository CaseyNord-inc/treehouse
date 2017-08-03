using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Program
    {
        static void Main()
        {
            HashSet<Student> students = new HashSet<Student>
            {
                new Student() { Name = "Sally", GradeLevel = 3 },
                new Student() { Name = "Bob", GradeLevel = 3 },
                new Student() { Name = "Sally", GradeLevel = 2 },
            };

            Student joe = new Student() { Name = "Joe", GradeLevel = 2 };

            students.Add(joe);

            Student duplicateJoe = new Student() { Name = "Joe", GradeLevel = 2 };

            students.Add(duplicateJoe);

            if(students.Contains(joe))
            {
                do something
            }

            foreach (Student student in students)
            {
                Console.WriteLine($"{student.Name} is in grade {student.GradeLevel}");
            }
            Console.ReadKey();
        }
    }
}
