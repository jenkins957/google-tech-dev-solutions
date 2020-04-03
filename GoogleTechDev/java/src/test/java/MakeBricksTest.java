import org.junit.Test;

import static org.junit.Assert.*;

public class MakeBricksTest
{
    @Test
    public void testMakeBricks()
    {
        assertTrue( new MakeBricks().makeBricks( 3, 1, 8 ) );
        assertFalse( new MakeBricks().makeBricks( 3, 2, 9 ) );
        assertFalse( new MakeBricks().makeBricks( 1, 4, 12 ) );
        assertTrue( new MakeBricks().makeBricks( 3, 1, 7 ) );

    }
}