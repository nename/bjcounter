# Blackjack counter with basic strategy without accounting for deviation

Basic manual blackjack counter with basic strategy. Program is based on running count and playing with 8 decks.


#### TODO

1. account for deviation of true count*
2. add input for already played cards (deferred / discarded cards)
3. work on design (not soon probably)
4. automate, use image processing (not soon)
5. add player advantage (%)


*you can easily account for the deviation by playing with positive true count only (positive true count means there is bigger probabilty of getting larger numbers and vice versa)


#### Preview

![preview](preview.png)

#### Review

After some testing it is not that bad of a tool. Button clicking gets painful over time and the missing possibility of adding discarded cards is not making it better, but if you input cards and get information about basic strategy then the true count can help you decide (positive number means there is bigger probabilty of large numbers and vice versa).
