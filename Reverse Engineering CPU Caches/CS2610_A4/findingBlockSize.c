#include <stdio.h>
#include <stdint.h>
#include <x86intrin.h>
#include <time.h>

#define N 512

int main(){
    // Time fns
    uint64_t t1, t2,lat[N];
    t1 = 0; t2 = 0;
    // Char to access every byte
    char *arr = (char *)malloc(N*sizeof(char));
    char tmp;
    // Initialize
    for (int i = 0; i < N; i++){
        arr[i] = 0;
        lat[i] = 0;
    }
    // Run tests 100 times to remove noise
    for(int i = 0; i < 100; i++){
        // Flush Cache line
        for (int i = 0; i<N; i++){
            _mm_mfence();
            _mm_clflush(&arr[i]);
            _mm_mfence();
        }
        // Access memory and record time
        for (int i = 0; i<N; i++){
            _mm_mfence();
            t1 = _rdtsc();
            _mm_mfence();
            tmp = arr[i];
            _mm_mfence();
            t2 = _rdtsc();
            _mm_mfence();
            lat[i] += (t2 - t1);
        }
    }
    // Print time
    for (int i = 0; i<N; i++)
        printf("%d  %lu \n", i, lat[i]/100);
    // Free
    free(arr);
    return 0;
}

// References:
// 1. https://software.intel.com/sites/landingpage/IntrinsicsGuide/
// 2. Pg : 262 -> https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-system-programming-manual-325384.pdf
// 3. https://stackoverflow.com/questions/13772567/how-to-get-the-cpu-cycle-count-in-x86-64-from-c

// To Run
// $ gcc -O0 bsize.c && ./a.out
