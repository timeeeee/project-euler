; What is the largest prime factor of the number 600851475143?

(use srfi-1)

(define (prime-factors n)
  (prime-factors-above n 3))

(define (prime-factors-above n min-factor)
  (cond ((< n min-factor) '())
	((= n min-factor) (list n))
	(else
	 (if (= (modulo n min-factor) 0)
	     (cons min-factor (prime-factors-above (/ n min-factor) min-factor))
	     (prime-factors-above n (+ min-factor 2))))))

(display (last (prime-factors 600851475143)))
(newline)
