---
title: "10. Special Registers"
section: "10"
version: "9.4"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#special-registers
---

<a id="special-registers"></a>

<a id="id615"></a>

#  10\. Special Registers

PTX includes a number of predefined, read-only variables, which are visible as special registers and accessed through `mov` or `cvt` instructions.

The special registers are:

  * `%tid`

  * `%ntid`

  * `%laneid`

  * `%warpid`

  * `%nwarpid`

  * `%ctaid`

  * `%nctaid`

  * `%smid`

  * `%nsmid`

  * `%gridid`

  * `%is_explicit_cluster`

  * `%clusterid`

  * `%nclusterid`

  * `%cluster_ctaid`

  * `%cluster_nctaid`

  * `%cluster_ctarank`

  * `%cluster_nctarank`

  * `%lanemask_eq`, `%lanemask_le`, `%lanemask_lt`, `%lanemask_ge`, `%lanemask_gt`

  * `%clock`, `%clock_hi`, `%clock64`

  * `%pm0, ..., %pm7`

  * `%pm0_64, ..., %pm7_64`

  * `%envreg0, ..., %envreg31`

  * `%globaltimer`, `%globaltimer_lo`, `%globaltimer_hi`

  * `%reserved_smem_offset_begin`, `%reserved_smem_offset_end`, `%reserved_smem_offset_cap`, `%reserved_smem_offset<2>`

  * `%total_smem_size`

  * `%aggr_smem_size`

  * `%dynamic_smem_size`

  * `%current_graph_exec`

  * `%perctamemoryoffset`

  * `%perctamemorysize`

Subsections:

- [10.1. Special Registers: %tid](10.1-special-registerstid.md)
- [10.2. Special Registers: %ntid](10.2-special-registersntid.md)
- [10.3. Special Registers: %laneid](10.3-special-registerslaneid.md)
- [10.4. Special Registers: %warpid](10.4-special-registerswarpid.md)
- [10.5. Special Registers: %nwarpid](10.5-special-registersnwarpid.md)
- [10.6. Special Registers: %ctaid](10.6-special-registersctaid.md)
- [10.7. Special Registers: %nctaid](10.7-special-registersnctaid.md)
- [10.8. Special Registers: %smid](10.8-special-registerssmid.md)
- [10.9. Special Registers: %nsmid](10.9-special-registersnsmid.md)
- [10.10. Special Registers: %gridid](10.10-special-registersgridid.md)
- [10.11. Special Registers: %is_explicit_cluster](10.11-special-registersis_explicit_cluster.md)
- [10.12. Special Registers: %clusterid](10.12-special-registersclusterid.md)
- [10.13. Special Registers: %nclusterid](10.13-special-registersnclusterid.md)
- [10.14. Special Registers: %cluster_ctaid](10.14-special-registerscluster_ctaid.md)
- [10.15. Special Registers: %cluster_nctaid](10.15-special-registerscluster_nctaid.md)
- [10.16. Special Registers: %cluster_ctarank](10.16-special-registerscluster_ctarank.md)
- [10.17. Special Registers: %cluster_nctarank](10.17-special-registerscluster_nctarank.md)
- [10.18. Special Registers: %lanemask_eq](10.18-special-registerslanemask_eq.md)
- [10.19. Special Registers: %lanemask_le](10.19-special-registerslanemask_le.md)
- [10.20. Special Registers: %lanemask_lt](10.20-special-registerslanemask_lt.md)
- [10.21. Special Registers: %lanemask_ge](10.21-special-registerslanemask_ge.md)
- [10.22. Special Registers: %lanemask_gt](10.22-special-registerslanemask_gt.md)
- [10.23. Special Registers: %clock , %clock_hi](10.23-special-registersclockclock_hi.md)
- [10.24. Special Registers: %clock64](10.24-special-registersclock64.md)
- [10.25. Special Registers: %pm0 … %pm7](10.25-special-registerspm0pm7.md)
- [10.26. Special Registers: %pm0_64 … %pm7_64](10.26-special-registerspm0_64pm7_64.md)
- [10.27. Special Registers: %envreg<32>](10.27-special-registersenvreg32.md)
- [10.28. Special Registers: %globaltimer , %globaltimer_lo , %globaltimer_hi](10.28-special-registersglobaltimerglobaltimer_loglobaltimer_hi.md)
- [10.29. Special Registers: %reserved_smem_offset_begin , %reserved_smem_offset_end , %reserved_smem_offset_cap , %reserved_smem_offset_<2>](10.29-special-registersreserved_smem_offset_beginreserved_smem_offset_endreserved_smem_offset_capreserved_smem_offset_2.md)
- [10.30. Special Registers: %total_smem_size](10.30-special-registerstotal_smem_size.md)
- [10.31. Special Registers: %aggr_smem_size](10.31-special-registersaggr_smem_size.md)
- [10.32. Special Registers: %dynamic_smem_size](10.32-special-registersdynamic_smem_size.md)
- [10.33. Special Registers: %current_graph_exec](10.33-special-registerscurrent_graph_exec.md)
- [10.34. Special Registers: %perctamemoryoffset](10.34-special-registersperctamemoryoffset.md)
- [10.35. Special Registers: %perctamemorysize](10.35-special-registersperctamemorysize.md)
