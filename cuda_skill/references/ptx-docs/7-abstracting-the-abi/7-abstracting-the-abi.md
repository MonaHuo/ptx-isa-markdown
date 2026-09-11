---
title: "7. Abstracting the ABI"
section: "7"
version: "9.4"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#abstracting-abi
---

<a id="abstracting-abi"></a>

<a id="id105"></a>

#  7\. Abstracting the ABI

Rather than expose details of a particular calling convention, stack layout, and Application Binary Interface (ABI), PTX provides a slightly higher-level abstraction and supports multiple ABI implementations. In this section, we describe the features of PTX needed to achieve this hiding of the ABI. These include syntax for function definitions, function calls, parameter passing, and memory allocated on the stack (`alloca`).

Refer to _PTX Writers Guide to Interoperability_ for details on generating PTX compliant with Application Binary Interface (ABI) for the CUDA® architecture.

Subsections:

- [7.1. Function Declarations and Definitions](7.1-function-declarations-and-definitions.md)
- [7.2. Variadic Functions](7.2-variadic-functions.md)
- [7.3. Alloca](7.3-alloca.md)
