/**
 * Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they both go over.
 * blackjack(19, 21) → 21
 * blackjack(21, 19) → 21
 * blackjack(19, 22) → 19
 */
public class BlackJack
{
    public int blackjack( int a, int b )
    {
        int input1 = a > 21 ? 0 : a;
        int input2 = b > 21 ? 0 : b;

        return Math.max( input1, input2 );
    }

}
