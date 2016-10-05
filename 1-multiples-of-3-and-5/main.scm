; Sum of all numbers less than 1000 that are divisible by 3 or 5
(use srfi-1)

(define (range start until)
  (if (= start until)
      '()
      (cons start (range (+ start 1) until))))

(define (divisible-by x n) (= (modulo x n) 0))

(display
 (foldr + 0
	(filter (lambda (x) (or (divisible-by x 3)
				(divisible-by x 5)))
		(range 1 1000))))
(newline)
