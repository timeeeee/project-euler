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

(define (fib-not-tail-recursive n)
  (if (< n 2)
      1
      (+ (fib-not-tail-recursive (- n 1)) (fib-not-tail-recursive (- n 2)))))

(define (fib-to until)
  (define (fib-list a b rest until)
    (let ((next (+ a b)))
      (if (< next until)
	  (fib-list next a (cons b rest) until)
	  (reverse (cons a (cons b rest))))))
  (fib-list 1 1 '() until))

(define (sum list) (foldl + 0 list))

(display (sum (filter even? (fib-to 4000000))))
(newline)
