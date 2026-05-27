class Solution {
    public boolean lemonadeChange(int[] bills) {
        // if customer gives 5 dollar, we return nothing
        // if customer gives 10 dollar, we return 5 dollar
        // if customer gives 20 dollar, we return 5 * 3 ot 10 * 1 + 5 * 1
        // we prefer return 10 * 1 + 5 * 2 over 5 * 3 since the more 5 we keep the more flexiblility we have

        int count5 = 0;
        int count10 = 0;

        for (int bill: bills) {
            if (bill == 5) {
                count5++;
            } else if (bill == 10) {
                if (count5 == 0) return false;
                count10++;
                count5--;
            } else if (bill == 20) {
                if (count10 > 0 && count5 > 0) {
                    count10--;
                    count5--;
                } else if (count5 > 2) {
                    count5 -= 3;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}