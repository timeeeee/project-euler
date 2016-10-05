; Sum of all numbers less than 1000 that are divisble by 3 or 5
(define (range start until)
  (if (= start until)
      '()
      (cons start (range (+ start 1) until))))

(display (range 1 1000))
(newline)
