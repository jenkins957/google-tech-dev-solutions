/**
 * https://codingbat.com/prob/p117019
 *
 * Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they both go over.
 * blackjack(19, 21) → 21
 * blackjack(21, 19) → 21
 * blackjack(19, 22) → 19
 */
public class BlackJack
{
    private static final int MAX_VALUE = 21;

    public int blackjack( int a, int b )
    {
        final int value1 = a > MAX_VALUE ? 0 : a;
        final int value2 = b > MAX_VALUE ? 0 : b;

        return Math.max( value1, value2 );
    }
}
