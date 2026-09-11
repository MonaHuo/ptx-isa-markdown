---
title: "13. Release Notes"
section: "13"
version: "9.4"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#release-notes
---

<a id="release-notes"></a>

<a id="id700"></a>

#  13\. Release Notes

This section describes the history of change in the PTX ISA and implementation. The first section describes ISA and implementation changes in the current release of PTX ISA version 9.4, and the remaining sections provide a record of changes in previous releases of PTX ISA versions back to PTX ISA version 2.0.

[Table 71](#release-notes-ptx-release-history) shows the PTX release history.

<a id="release-notes-ptx-release-history"></a>

Table 71 PTX Release History

<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><p>PTX ISA Version</p></th>
<th><p>CUDA Release</p></th>
<th><p>Supported Targets</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PTX ISA 1.0</p></td>
<td><p>CUDA 1.0</p></td>
<td><p><code><span>sm_{10,11}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 1.1</p></td>
<td><p>CUDA 1.1</p></td>
<td><p><code><span>sm_{10,11}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 1.2</p></td>
<td><p>CUDA 2.0</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 1.3</p></td>
<td><p>CUDA 2.1</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 1.4</p></td>
<td><p>CUDA 2.2</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 1.5</p></td>
<td><p>driver r190</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 2.0</p></td>
<td><p>CUDA 3.0, driver r195</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 2.1</p></td>
<td><p>CUDA 3.1, driver r256</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 2.2</p></td>
<td><p>CUDA 3.2, driver r260</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 2.3</p></td>
<td><p>CUDA 4.0, driver r270</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>PTX ISA 3.0</p></td>
<td><p>CUDA 4.1, driver r285</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code></p></td>
</tr>
<tr>
<td><p>CUDA 4.2, driver r295</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_30</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 3.1</p></td>
<td><p>CUDA 5.0, driver r302</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,35}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 3.2</p></td>
<td><p>CUDA 5.5, driver r319</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,35}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 4.0</p></td>
<td><p>CUDA 6.0, driver r331</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35}</span></code>, <code><span>sm_50</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 4.1</p></td>
<td><p>CUDA 6.5, driver r340</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 4.2</p></td>
<td><p>CUDA 7.0, driver r346</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 4.3</p></td>
<td><p>CUDA 7.5, driver r352</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 5.0</p></td>
<td><p>CUDA 8.0, driver r361</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.0</p></td>
<td><p>CUDA 9.0, driver r384</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.1</p></td>
<td><p>CUDA 9.1, driver r387</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code>, <code><span>sm_72</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.2</p></td>
<td><p>CUDA 9.2, driver r396</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code>, <code><span>sm_72</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.3</p></td>
<td><p>CUDA 10.0, driver r400</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code>, <code><span>sm_72</span></code>, <code><span>sm_75</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.4</p></td>
<td><p>CUDA 10.1, driver r418</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code>, <code><span>sm_72</span></code>, <code><span>sm_75</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 6.5</p></td>
<td><p>CUDA 10.2, driver r440</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_70</span></code>, <code><span>sm_72</span></code>, <code><span>sm_75</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.0</p></td>
<td><p>CUDA 11.0, driver r445</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_80</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.1</p></td>
<td><p>CUDA 11.1, driver r455</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.2</p></td>
<td><p>CUDA 11.2, driver r460</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.3</p></td>
<td><p>CUDA 11.3, driver r465</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.4</p></td>
<td><p>CUDA 11.4, driver r470</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.5</p></td>
<td><p>CUDA 11.5, driver r495</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.6</p></td>
<td><p>CUDA 11.6, driver r510</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.7</p></td>
<td><p>CUDA 11.7, driver r515</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 7.8</p></td>
<td><p>CUDA 11.8, driver r520</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_90</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.0</p></td>
<td><p>CUDA 12.0, driver r525</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.1</p></td>
<td><p>CUDA 12.1, driver r530</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.2</p></td>
<td><p>CUDA 12.2, driver r535</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.3</p></td>
<td><p>CUDA 12.3, driver r545</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.4</p></td>
<td><p>CUDA 12.4, driver r550</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>PTX ISA 8.5</p></td>
<td><p>CUDA 12.5, driver r555</p></td>
<td rowspan="2"><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>, <code><span>sm_{90,90a}</span></code></p></td>
</tr>
<tr>
<td><p>CUDA 12.6, driver r560</p></td>
</tr>
<tr>
<td><p>PTX ISA 8.6</p></td>
<td><p>CUDA 12.7, driver r565</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100a,101,101a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.7</p></td>
<td><p>CUDA 12.8, driver r570</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100,101,101a}</span></code>, <code><span>sm_{120,120a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 8.8</p></td>
<td><p>CUDA 12.9, driver r575</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,101,101f,101a,103,103f,103a}</span></code>,
<code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 9.0</p></td>
<td><p>CUDA 13.0, driver r580</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,88,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,103,103f,103a}</span></code>,
<code><span>sm_{110,110f,110a}</span></code>, <code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 9.1</p></td>
<td><p>CUDA 13.1, driver r590</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,88,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,103,103f,103a}</span></code>,
<code><span>sm_{110,110f,110a}</span></code>, <code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 9.2</p></td>
<td><p>CUDA 13.2, driver r595</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,88,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,103,103f,103a}</span></code>,
<code><span>sm_{110,110f,110a}</span></code>, <code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 9.3</p></td>
<td><p>CUDA 13.3, driver r610</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,88,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,103,103f,103a}</span></code>,
<code><span>sm_{110,110f,110a}</span></code>, <code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
<tr>
<td><p>PTX ISA 9.4</p></td>
<td><p>CUDA 13.4, driver r615</p></td>
<td><p><code><span>sm_{10,11,12,13}</span></code>, <code><span>sm_20</span></code>, <code><span>sm_{30,32,35,37}</span></code>, <code><span>sm_{50,52,53}</span></code>,
<code><span>sm_{60,61,62}</span></code>, <code><span>sm_{70,72,75}</span></code>, <code><span>sm_{80,86,87,88,89}</span></code>,
<code><span>sm_{90,90a}</span></code>, <code><span>sm_{100,100f,100a,103,103f,103a,107,107f,107a}</span></code>,
<code><span>sm_{110,110f,110a}</span></code>, <code><span>sm_{120,120f,120a,121,121f,121a}</span></code></p></td>
</tr>
</tbody>
</table>

[Table 72](#release-notes-a-spec-f-spec-ptx-feature-release-history) shows the release history of arch-specific and family-specific PTX instructions. Apart from PTX instructions, other features and constructs that are architecture-specific and family-specific are described in following sections:

  * [Restriction on Tensor Copy instructions](../9-instruction-set/9.7.10.28-data-movement-and-conversion-instructions-asynchronous-copy.md#data-movement-and-conversion-instructions-tensor-copy-restrictions)

  * [TensorCore 5th Generation Matrix Shape Target ISA Notes](../9-instruction-set/9.7.18.2-matrix-and-data-movement-shape.md#tcgen05-matrix-shape-target-isa-note)

  * [TensorCore 5th Generation Instruction Memory Descriptor Target ISA Notes](../9-instruction-set/9.7.18.4-matrix-descriptors.md#tcgen05-instruction-memory-descriptor-target-isa-note)

  * [Block Scaling for tcgen05.mma](../9-instruction-set/9.7.18.10-tensorcore-5th-generation-matrix-multiply-and-accumulate-operations.md#tcgen05-block-scaling)

<a id="release-notes-a-spec-f-spec-ptx-feature-release-history"></a>

Table 72 Arch-specific/ Family-specific PTX Features Release History

<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><p>Instruction</p></th>
<th><p>Variant</p></th>
<th><p>PTX ISA Version</p></th>
<th><p>Supported Targets</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="12"><p><code><span>tensormap.replace</span></code></p></td>
<td rowspan="4"><p>Base variant</p></td>
<td><p>8.3</p></td>
<td><p><code><span>sm_90a</span></code></p></td>
</tr>
<tr>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>tensormap.replace.swizzle_atomicity</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>.elemtype</span></code> for <code><span>.field3</span></code> with values
<code><span>13</span></code>, <code><span>14</span></code>, <code><span>15</span></code> for <code><span>new_val</span></code></p></td>
<td><p>8.7</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>.swizzle_mode</span></code> for <code><span>.field3</span></code> with value
<code><span>4</span></code> for <code><span>new_val</span></code></p></td>
<td><p>8.8</p></td>
<td><p><code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>wgmma.mma_async</span></code>,
<code><span>wgmma.mma_async.sp</span></code>,
<code><span>wgmma.fence</span></code>,
<code><span>wgmma.commit_group</span></code>,
<code><span>wgmma.wait_group</span></code></p></td>
<td><p>Base variant</p></td>
<td><p>8.0</p></td>
<td><p><code><span>sm_90a</span></code></p></td>
</tr>
<tr>
<td rowspan="4"><p><code><span>setmaxnreg</span></code></p></td>
<td rowspan="4"><p>Base variant</p></td>
<td><p>8.0</p></td>
<td><p><code><span>sm_90a</span></code></p></td>
</tr>
<tr>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>set</span></code></p></td>
<td><p>Types <code><span>.u8x4</span></code>, <code><span>.s8x4</span></code>,
<code><span>.u16x2</span></code>, <code><span>.s16x2</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="6"><p><code><span>multimem.ld_reduce</span></code>,
<code><span>multimem.st</span></code>,
<code><span>multimem.red</span></code></p></td>
<td rowspan="3"><p>Types <code><span>.e5m2</span></code>, <code><span>.e4m3</span></code>, <code><span>.e5m2x2</span></code>,
<code><span>.e4m3x2</span></code>, <code><span>.e4m3x4</span></code>, <code><span>.e5m2x4</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code>, <code><span>sm_121a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>.acc::f16</span></code> qualifier</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code>, <code><span>sm_121a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="13"><p><code><span>cvt</span></code></p></td>
<td rowspan="3">
<ul>
<li><p><code><span>.f32</span></code> to <code><span>.e2m1x2</span></code>/<code><span>.e2m3x2</span></code>/
<code><span>.e3m2x2</span></code>/<code><span>.ue8m0x2</span></code></p></li>
<li><p><code><span>.e2m1x2</span></code>/<code><span>.e2m3x2</span></code>/<code><span>.e3m2x2</span></code> to
<code><span>.f16x2</span></code></p></li>
<li><p><code><span>.ue8m0x2</span></code> to <code><span>.bf16x2</span></code></p></li>
<li><p><code><span>.bf16x2</span></code> to <code><span>.ue8m0x2</span></code></p></li>
</ul>
</td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>.rs</span></code> rounding mode</p></td>
<td><p>8.7</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.s2f6x2</span></code> type</p></td>
<td><p>9.1</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_103a</span></code>, <code><span>sm_110a</span></code>,
<code><span>sm_120a</span></code>, <code><span>sm_121a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.f16x2</span></code> to <code><span>.e2m1x2</span></code>/
<code><span>.e2m3x2</span></code>/<code><span>.e3m2x2</span></code></p></td>
<td><p>9.1</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_110f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.bf16x2</span></code> to <code><span>.e2m1x2</span></code>/
<code><span>.e2m3x2</span></code>/<code><span>.e3m2x2</span></code>/<code><span>.e4m3x2</span></code>/
<code><span>.e5m2x2</span></code></p></td>
<td><p>9.1</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_110f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.e2m1x2</span></code>/<code><span>.e2m3x2</span></code>/
<code><span>.e3m2x2</span></code>/<code><span>.e4m3x2</span></code>/<code><span>.e5m2x2</span></code> to
<code><span>.bf16x2</span></code></p></td>
<td><p>9.2</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_110f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.ue5m3x2</span></code> type</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.scaled::n1::ue8m0</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.pzo</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>.rz</span></code> rounding mode for
<code><span>.e4m3x2</span></code>/<code><span>.e5m2x2</span></code>/<code><span>.e2m3x2</span></code>/
<code><span>.e3m2x2</span></code>/<code><span>.e2m1x2</span></code> types</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="13"><p><code><span>cp.async.bulk.tensor</span></code></p></td>
<td rowspan="3"><p><code><span>.tile::gather4</span></code> and <code><span>.im2col::w</span></code> with
<code><span>.shared::cluster</span></code> as destination state
space</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>.tile::scatter4</span></code> and <code><span>.im2col::w::128</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>.cta_group</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.multicast::cluster::32b</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.im2col_no_offs::w</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.override::global_address</span></code> and
<code><span>.override_attribute</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.report_mechanism</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="5"><p><code><span>cp.async.bulk.prefetch.tensor</span></code></p></td>
<td rowspan="3"><p><code><span>.tile::gather4</span></code>, <code><span>.im2col::w</span></code>,
<code><span>.im2col::w::128</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.level::eviction_priority</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.override::global_address</span></code> and
<code><span>.override_attribute</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>redux.sync</span></code></p></td>
<td rowspan="2"><p>Type <code><span>.f32</span></code> and <code><span>.abs</span></code>, <code><span>.NaN</span></code>
qualifiers</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>clusterlaunchcontrol.try_cancel</span></code></p></td>
<td rowspan="3"><p><code><span>.multicast::cluster::all</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="4"><p><code><span>ldmatrix</span></code></p></td>
<td rowspan="3">
<ul>
<li><p>Shapes <code><span>.m16n16</span></code>, <code><span>.m8n16</span></code></p></li>
<li><p>Type <code><span>.b8</span></code></p></li>
<li><p>Qualifiers <code><span>.src_fmt</span></code>, <code><span>.dst_fmt</span></code></p></li>
</ul>
</td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p>Types <code><span>.s8</span></code>, <code><span>.s4</span></code> for <code><span>.m8n16</span></code> shape</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_90a</span></code>, <code><span>sm_100f</span></code>, <code><span>sm_110f</span></code>,
<code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>stmatrix</span></code></p></td>
<td rowspan="3">
<ul>
<li><p>Shapes <code><span>.m16n8</span></code></p></li>
<li><p>Type <code><span>.b8</span></code></p></li>
</ul>
</td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>tcgen05.alloc</span></code>,
<code><span>tcgen05.dealloc</span></code>,
<code><span>tcgen05.relinquish_alloc_permit</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>tcgen05.alloc</span></code>,
<code><span>tcgen05.dealloc</span></code></p></td>
<td><p>Qualifier <code><span>.exclusive</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>tcgen05.ld</span></code>, <code><span>tcgen05.st</span></code>,
<code><span>tcgen05.wait</span></code>, <code><span>tcgen05.cp</span></code>,
<code><span>tcgen05.fence</span></code>,
<code><span>tcgen05.commit</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="5"><p><code><span>tcgen05.commit</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier
<code><span>.sync_restrict::shared::read::mma::a</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.multicast::cluster::32b</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>tcgen05.ld.red</span></code></p></td>
<td rowspan="2"><p>Base variant</p></td>
<td><p>8.8</p></td>
<td><p><code><span>sm_103f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="4"><p><code><span>tcgen05.shift</span></code></p></td>
<td rowspan="4"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110a</span></code></p></td>
</tr>
<tr>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
<tr>
<td rowspan="14"><p><code><span>tcgen05.mma</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Kind <code><span>.kind::i8</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110a</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Argument <code><span>scale-input-d</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.scale_vec::1X</span></code>,
<code><span>.scale_vec::2X</span></code>, <code><span>.scale_vec::4X</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.block16</span></code>, <code><span>.block32</span></code></p></td>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>K shape value <code><span>96</span></code></p></td>
<td><p>8.8</p></td>
<td><p><code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.decompress::lut::b</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.collector::b::*</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.kind::ti16</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="15"><p><code><span>tcgen05.mma.sp</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Kind <code><span>.kind::i8</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110a</span></code></p></td>
</tr>
<tr>
<td rowspan="4"><p>Kind <code><span>.kind::mxf4nvf4</span></code> and <code><span>.kind::mxf4</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110a</span></code></p></td>
</tr>
<tr>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Argument <code><span>scale-input-d</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.scale_vec::1X</span></code>,
<code><span>.scale_vec::2X</span></code>, <code><span>.scale_vec::4X</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.block16</span></code>, <code><span>.block32</span></code></p></td>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code>, <code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.collector::b::*</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.kind::ti16</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="6"><p><code><span>tcgen05.mma.ws</span></code>,
<code><span>tcgen05.mma.ws.sp</span></code></p></td>
<td rowspan="3"><p>Base variant</p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_100f</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Kind <code><span>.kind::i8</span></code></p></td>
<td><p>8.6</p></td>
<td><p><code><span>sm_100a</span></code></p></td>
</tr>
<tr>
<td><p>9.0</p></td>
<td><p><code><span>sm_110a</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.kind::ti16</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>mma</span></code></p></td>
<td rowspan="2">
<ul>
<li><p>Types <code><span>.e3m2</span></code>, <code><span>.e2m3</span></code>, <code><span>.e2m1</span></code></p></li>
<li><p>Qualifiers <code><span>.kind</span></code>, <code><span>.block_scale</span></code>,
<code><span>.scale_vec_size</span></code></p></li>
</ul>
</td>
<td><p>8.7</p></td>
<td><p><code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td rowspan="3"><p><code><span>mma.sp</span></code></p></td>
<td rowspan="2">
<ul>
<li><p>Types <code><span>.e3m2</span></code>, <code><span>.e2m3</span></code>, <code><span>.e2m1</span></code></p></li>
<li><p>Qualifiers <code><span>.kind</span></code>, <code><span>.block_scale</span></code>,
<code><span>.scale_vec_size</span></code></p></li>
</ul>
</td>
<td><p>8.7</p></td>
<td><p><code><span>sm_120a</span></code></p></td>
</tr>
<tr>
<td><p>8.8</p></td>
<td><p><code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p>Kind <code><span>.kind::mxf4nvf4</span></code> and <code><span>.kind::mxf4</span></code></p></td>
<td><p>8.7</p></td>
<td><p><code><span>sm_120a</span></code>, <code><span>sm_121a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>add</span></code>, <code><span>sub</span></code>, <code><span>min</span></code>, <code><span>max</span></code>,
<code><span>neg</span></code></p></td>
<td><p>Types <code><span>.u8x4</span></code>, <code><span>.s8x4</span></code></p></td>
<td><p>9.2</p></td>
<td><p><code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>add</span></code></p></td>
<td><p>Types <code><span>.u16x2</span></code>, <code><span>.s16x2</span></code>, <code><span>.u32</span></code> with
<code><span>.sat</span></code> qualifier</p></td>
<td><p>9.2</p></td>
<td><p><code><span>sm_120f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>add</span></code>, <code><span>sub</span></code>, <code><span>mul</span></code>, <code><span>fma</span></code></p></td>
<td><p>Types <code><span>.f16x2</span></code>, <code><span>.bf16x2</span></code>, <code><span>.f32x2</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>FP8/FP6/FP4 x4 packed types</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_100a</span></code>, <code><span>sm_103a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>applypriority.async.bulk</span></code>,
<code><span>applypriority.async.bulk.tensor</span></code></p></td>
<td><p>Base variant</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>cp.async.bulk</span></code></p></td>
<td><p>Qualifier <code><span>.multicast::cluster::32b</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifier <code><span>.report_mechanism</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>cp.async.bulk.prefetch</span></code></p></td>
<td><p>Qualifier <code><span>.level::eviction_priority</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td rowspan="2"><p><code><span>cp.reduce.async.bulk.tensor</span></code></p></td>
<td><p>Qualifier <code><span>.im2col_no_offs::w</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p>Qualifiers <code><span>.override::global_address</span></code> and
<code><span>.override_attribute</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>mbarrier.expect_tx</span></code>,
<code><span>mbarrier.complete_tx</span></code>,
<code><span>mbarrier.arrive</span></code>,
<code><span>mbarrier.arrive_drop</span></code></p></td>
<td><p>Qualifier <code><span>.multicast::cluster::32b</span></code></p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107f</span></code></p></td>
</tr>
<tr>
<td><p><code><span>spcompress</span></code>, <code><span>spdecompress</span></code></p></td>
<td><p>Base variant</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
<tr>
<td><p><code><span>tcgen05.ld{.red}.spcompress</span></code></p></td>
<td><p>Base variant</p></td>
<td><p>9.4</p></td>
<td><p><code><span>sm_107a</span></code></p></td>
</tr>
</tbody>
</table>

Subsections:

- [13.1. Changes in PTX ISA Version 9.4](13.1-changes-in-ptx-isa-version-9.4.md)
- [13.2. Changes in PTX ISA Version 9.3](13.2-changes-in-ptx-isa-version-9.3.md)
- [13.3. Changes in PTX ISA Version 9.2](13.3-changes-in-ptx-isa-version-9.2.md)
- [13.4. Changes in PTX ISA Version 9.1](13.4-changes-in-ptx-isa-version-9.1.md)
- [13.5. Changes in PTX ISA Version 9.0](13.5-changes-in-ptx-isa-version-9.0.md)
- [13.6. Changes in PTX ISA Version 8.8](13.6-changes-in-ptx-isa-version-8.8.md)
- [13.7. Changes in PTX ISA Version 8.7](13.7-changes-in-ptx-isa-version-8.7.md)
- [13.8. Changes in PTX ISA Version 8.6](13.8-changes-in-ptx-isa-version-8.6.md)
- [13.9. Changes in PTX ISA Version 8.5](13.9-changes-in-ptx-isa-version-8.5.md)
- [13.10. Changes in PTX ISA Version 8.4](13.10-changes-in-ptx-isa-version-8.4.md)
- [13.11. Changes in PTX ISA Version 8.3](13.11-changes-in-ptx-isa-version-8.3.md)
- [13.12. Changes in PTX ISA Version 8.2](13.12-changes-in-ptx-isa-version-8.2.md)
- [13.13. Changes in PTX ISA Version 8.1](13.13-changes-in-ptx-isa-version-8.1.md)
- [13.14. Changes in PTX ISA Version 8.0](13.14-changes-in-ptx-isa-version-8.0.md)
- [13.15. Changes in PTX ISA Version 7.8](13.15-changes-in-ptx-isa-version-7.8.md)
- [13.16. Changes in PTX ISA Version 7.7](13.16-changes-in-ptx-isa-version-7.7.md)
- [13.17. Changes in PTX ISA Version 7.6](13.17-changes-in-ptx-isa-version-7.6.md)
- [13.18. Changes in PTX ISA Version 7.5](13.18-changes-in-ptx-isa-version-7.5.md)
- [13.19. Changes in PTX ISA Version 7.4](13.19-changes-in-ptx-isa-version-7.4.md)
- [13.20. Changes in PTX ISA Version 7.3](13.20-changes-in-ptx-isa-version-7.3.md)
- [13.21. Changes in PTX ISA Version 7.2](13.21-changes-in-ptx-isa-version-7.2.md)
- [13.22. Changes in PTX ISA Version 7.1](13.22-changes-in-ptx-isa-version-7.1.md)
- [13.23. Changes in PTX ISA Version 7.0](13.23-changes-in-ptx-isa-version-7.0.md)
- [13.24. Changes in PTX ISA Version 6.5](13.24-changes-in-ptx-isa-version-6.5.md)
- [13.25. Changes in PTX ISA Version 6.4](13.25-changes-in-ptx-isa-version-6.4.md)
- [13.26. Changes in PTX ISA Version 6.3](13.26-changes-in-ptx-isa-version-6.3.md)
- [13.27. Changes in PTX ISA Version 6.2](13.27-changes-in-ptx-isa-version-6.2.md)
- [13.28. Changes in PTX ISA Version 6.1](13.28-changes-in-ptx-isa-version-6.1.md)
- [13.29. Changes in PTX ISA Version 6.0](13.29-changes-in-ptx-isa-version-6.0.md)
- [13.30. Changes in PTX ISA Version 5.0](13.30-changes-in-ptx-isa-version-5.0.md)
- [13.31. Changes in PTX ISA Version 4.3](13.31-changes-in-ptx-isa-version-4.3.md)
- [13.32. Changes in PTX ISA Version 4.2](13.32-changes-in-ptx-isa-version-4.2.md)
- [13.33. Changes in PTX ISA Version 4.1](13.33-changes-in-ptx-isa-version-4.1.md)
- [13.34. Changes in PTX ISA Version 4.0](13.34-changes-in-ptx-isa-version-4.0.md)
- [13.35. Changes in PTX ISA Version 3.2](13.35-changes-in-ptx-isa-version-3.2.md)
- [13.36. Changes in PTX ISA Version 3.1](13.36-changes-in-ptx-isa-version-3.1.md)
- [13.37. Changes in PTX ISA Version 3.0](13.37-changes-in-ptx-isa-version-3.0.md)
- [13.38. Changes in PTX ISA Version 2.3](13.38-changes-in-ptx-isa-version-2.3.md)
- [13.39. Changes in PTX ISA Version 2.2](13.39-changes-in-ptx-isa-version-2.2.md)
- [13.40. Changes in PTX ISA Version 2.1](13.40-changes-in-ptx-isa-version-2.1.md)
- [13.41. Changes in PTX ISA Version 2.0](13.41-changes-in-ptx-isa-version-2.0.md)
