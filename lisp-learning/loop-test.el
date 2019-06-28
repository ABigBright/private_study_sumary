;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.

(loop for i in '(1 2 3)
      when (> i 2)
          do (print i)
	  finally (print 'haha))

(dolist (foo '(1 2 3))
  (when (> foo 2)
    (print 'foo)))


(loop for i in '(1 2 3)
      do (print i)
      finally (print 'hoho))
