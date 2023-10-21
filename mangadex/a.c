#include <stdio.h>

void swap(int* a, int* b) {
  int t = *a;
  *a = *b;
  *b = t;
}

int main() {
  int a[] = {1, 0, 2, 0, 0, 1, 0, 1, 0, 0, 2, 2, 1, 0};
  int n = 14;
  int l = 0, m = 0, h = n - 1;
  while (m <= h) {
    if (a[m] == 2) {
      swap(&a[m], &a[h]);
      h--;a
    }

    if (a[m] == 1) m++;
    if (a[m] == 0) {
      swap(&a[l], &a[m]);
      m++;
      l++;
    }
  }

  for (int i = 0; i < n; i++) printf("%d, ", a[i]);
}