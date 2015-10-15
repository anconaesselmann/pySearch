"""
quick sort algorithm adapted from Wikipedia page

@author Axel Ancona Esselmann
"""
class QuickSort():
    def sort(self, A):
        self._quicksort(A,0,len(A) - 1);

    def _quicksort(self, A, lo, hi):
      if lo < hi:
        p = self._partition(A, lo, hi);
        self._quicksort(A, lo, p - 1);
        self._quicksort(A, p + 1, hi);

    def _partition(self, A, lo, hi):
        pivot = A[hi];
        i     = lo;
        for j in xrange(lo,hi):
            if A[j] <= pivot:
                temp = A[i];
                A[i] = A[j];
                A[j] = temp;
                i += 1;
        temp  = A[i];
        A[i]  = A[hi];
        A[hi] = temp;
        return i;