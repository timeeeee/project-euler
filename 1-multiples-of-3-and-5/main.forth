( Find the sum of all the multiples of 3 or 5 below 1000)

: div-by-3-or-5 ( a -- a if a divisible by 3 or 5, else 0)
    dup dup
    3 mod 0 =
    swap
    5 mod 0 =
    or ( see if one of them was true)
    and ( if so, keep the input)
;

: test 10 0 do I . I div-by-3-or-5 . cr loop ;

: sum-to ( a -- sum 1..a divisible by 3 or 5)
     0 swap ( total)
     1 ( starting number)
     do I div-by-3-or-5 + loop
;

1000 sum-to .
