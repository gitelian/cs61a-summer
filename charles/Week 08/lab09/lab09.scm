(define (cube x)
  (* x x x)
)

(define (over-or-under x y)
  (if (< x y)
    -1
  	(if (> x y)
  	 1
  	 0))
)

(define (make-adder num)
  (lambda (x) (+x num))
)

(define structure
  (cons (cons 1 '())
  	(cons 2
  		(cons (cons 2 4)
  			(cons 5 '()))))
)

(define (remove item lst)
  (cond ((null? lst) '())
  	((equal? item (car lst)) (remove item (cdr lst)))
  	(else (cons (car lst) (remove item (cdr lst)))))
)

