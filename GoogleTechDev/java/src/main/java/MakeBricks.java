public class MakeBricks
{
    public boolean makeBricks( int small, int big, int goal )
    {
        // Early out if we dont have enough bricks to reach the goal
        if ( goal > small + (big * 5) )
        {
            return false;
        }

        return ( goal % 5 > small ) ? false : true;
    }
}
