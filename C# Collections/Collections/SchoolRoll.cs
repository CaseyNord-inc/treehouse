using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class SchoolRoll
    {
        private HashSet<Student> _students = new HashSet<Student>();

        public IEnumerable<Student> Students { get { return _students; } }

        public void AddStudents(IEnumerable<Student> students)
        {
            _students.UnionWith(students);
        }
    }
}
