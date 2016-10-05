; Find the sum of all even fibonacci numbers below 4000000

(use srfi-1)

(define (range start until)
  (if (= start until)
      '()
      (cons start (range (+ start 1) until))))

(define (prime? x)
  ; is x divisible by n?
  (define (div-by n) (= (modulo x n) 0))

  ; is x divisible by any odd number >= n?
  (define (iter-prime? n)
    (cond ((>= n x) #t)
	  ((div-by n) #f)
	  (else (iter-prime? (+ n 2)))))

  (cond ((= x 2) #t)
	((even? x) #f)
	(else (iter-prime? 3))))
	
(define primes (filter prime? (range 2 10000)))

(display primes)
(newline)
