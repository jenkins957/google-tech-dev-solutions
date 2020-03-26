import org.junit.Test;

import static org.junit.Assert.*;

public class BlackJackTest
{
    @Test
    public void testBlackJack()
    {
        assertEquals( 21, new BlackJack().blackjack( 19, 21 ) );
        assertEquals( 21, new BlackJack().blackjack( 21, 19 ) );
        assertEquals( 19, new BlackJack().blackjack( 19, 22 ) );

        assertEquals( 19, new BlackJack().blackjack( 22, 19 ) );
        assertEquals( 0, new BlackJack().blackjack( 22, 50 ) );
        assertEquals( 0, new BlackJack().blackjack( 22, 22 ) );

        assertEquals( 1, new BlackJack().blackjack( 33, 1 ) );
        assertEquals( 2, new BlackJack().blackjack( 1, 2 ) );
        assertEquals( 0, new BlackJack().blackjack( 34, 33 ) );

        assertEquals( 19, new BlackJack().blackjack( 17, 19 ) );
        assertEquals( 18, new BlackJack().blackjack( 18, 17 ) );
        assertEquals( 16, new BlackJack().blackjack( 16, 23 ) );

        assertEquals( 4, new BlackJack().blackjack( 3, 4 ) );
        assertEquals( 3, new BlackJack().blackjack( 3, 2 ) );
        assertEquals( 21, new BlackJack().blackjack( 21, 20 ) );
    }
}