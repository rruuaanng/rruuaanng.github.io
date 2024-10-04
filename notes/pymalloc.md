# pymalloc

The default memory allocation strategy in CPython (which also includes mimalloc) is designed to allocate small objects (under 512 bytes) more efficiently by preallocating a certain number of memory blocks, thereby reducing the frequency of allocation requests. Additionally, it is optimized for multi-threaded environments, primarily through the use of the Global Interpreter Lock (GIL). The specific implementation can be found in the source code directory`Object/obmalloc.c`.

## Implementation

### Principle



### Allocation process



### pool_header structure

```C
/* When you say memory, my mind reasons in terms of (pointers to) blocks */
typedef uint8_t pymem_block;

/* Pool for small blocks. */
struct pool_header {
    union { pymem_block *_padding;
            uint count; } ref;          /* number of allocated blocks    */
    pymem_block *freeblock;             /* pool's free list head         */
    struct pool_header *nextpool;       /* next pool of this size class  */
    struct pool_header *prevpool;       /* previous pool       ""        */
    uint arenaindex;                    /* index into arenas of base adr */
    uint szidx;                         /* block size class index        */
    uint nextoffset;                    /* bytes to virgin block         */
    uint maxnextoffset;                 /* largest valid nextoffset      */
};
```

### Public API

- void *PyMem_Malloc(size_t size)
- void *PyMem_Calloc(size_t nelem, size_t elsize)
- void *PyMem_Realloc(void *ptr, size_t new_size)
- void PyMem_Free(void *ptr)

### Private API

- void* _PyObject_Malloc(void *ctx, size_t size)
- void* _PyObject_Calloc(void *ctx, size_t nelem, size_t elsize)
- void* _PyObject_Realloc(void *ctx, void *ptr, size_t size)
- void _PyObject_Free(void *ctx, void *p)