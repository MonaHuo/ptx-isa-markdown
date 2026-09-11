---
title: "8. Memory Consistency Model"
section: "8"
version: "9.4"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#memory-consistency-model
---

<a id="memory-consistency-model"></a>

<a id="id110"></a>

#  8\. Memory Consistency Model

In multi-threaded executions, the side-effects of memory operations performed by each thread become visible to other threads in a partial and non-identical order. This means that any two operations may appear to happen in no order, or in different orders, to different threads. The axioms introduced by the memory consistency model specify exactly which contradictions are forbidden between the orders observed by different threads.

In the absence of any constraint, each read operation returns the value committed by some write operation to the same memory location, including the initial write to that memory location. The memory consistency model effectively constrains the set of such candidate writes from which a read operation can return a value.

Subsections:

- [8.1. Scope and applicability of the model](8.1-scope-and-applicability-of-the-model.md)
- [8.2. Memory operations](8.2-memory-operations.md)
- [8.3. State spaces](8.3-state-spaces.md)
- [8.4. Operation types](8.4-operation-types.md)
- [8.5. Scope](8.5-scope.md)
- [8.6. Proxies](8.6-proxies.md)
- [8.7. Morally strong operations](8.7-morally-strong-operations.md)
- [8.8. Release and Acquire Patterns](8.8-release-and-acquire-patterns.md)
- [8.9. Ordering of memory operations](8.9-ordering-of-memory-operations.md)
- [8.10. Axioms](8.10-axioms.md)
- [8.11. Special Cases](8.11-special-cases.md)
