namespace TreehouseDefense
{
    class Map
    {
        public readonly int Width;
        public readonly int Height;

        // Map is constructed by passing a width and heigth value. 
        public Map(int width, int height)
        {
            Width = width;
            Height = height;
        }

        // Determines is a point is on the map.
        public bool OnMap(Point point)
        {
            return point.X >= 0 && point.X < Width &&
                   point.Y >= 0 && point.Y < Height;
        }
    }
}
