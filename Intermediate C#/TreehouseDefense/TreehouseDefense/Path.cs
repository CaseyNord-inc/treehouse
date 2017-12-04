namespace TreehouseDefense
{
    // The path is a list of adjacent map locations stored in an array. 
    class Path
    {
        private readonly MapLocation[] _path;

        // All of the methods here are designed to only allow certain parts of this class to be accessible to other classes. 
        public int Length => _path.Length;

        public Path(MapLocation[] path)
        {
            _path = path;
        }

        public MapLocation GetLocationAt(int pathStep)
        {
            return (pathStep < _path.Length) ? _path[pathStep] : null;
        }

        public bool IsOnPath(MapLocation location)
        {
            foreach (var pathLocation in _path)
            {
                if (location.Equals(pathLocation))
                {
                    return true;
                }
            }

            return false;
        }
    }
}
