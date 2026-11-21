# Hi there 👋

[![GitHub](https://img.shields.io/badge/GitHub-tom--jerr-181717?style=flat&logo=github)](https://github.com/tom-jerr)
[![Zhihu](https://img.shields.io/badge/Zhihu-blue?style=flat&logo=zhihu&logoColor=white)](https://www.zhihu.com/people/chen-wen-de-jian-ke)
[![Gmail](https://img.shields.io/badge/Gmail-tomlzy213%40gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:tomlzy213@gmail.com)
[![Website](https://img.shields.io/badge/Website-tom--jerr.github.io-4285F4?style=flat&logo=googlechrome&logoColor=white)](https://tom-jerr.github.io/)

<img align="right" width="230" alt="bug cat" src="https://raw.githubusercontent.com/tom-jerr/MyblogImg/main/bug_cat.gif" />

## 👋 Hi, I'm Zhiyi Liu

🎓 M.S. in Computer Science at **UESTC** (Class of **2027**).  
⚡ Focusing on **LLM Inference Systems, Agent Serving Systems, and Agent-Driven System Optimization**.  

📫 [tomlzy213@gmail.com](mailto:tomlzy213@gmail.com) · 🌐 [tom-jerr.github.io](https://tom-jerr.github.io/)

<br clear="right"/>

---

## 🤖 Agent Serving & Agent for LLM Systems

*Current research direction (ongoing work):*

- **Agent for LLM Engine Acceleration** — Exploring agentic workflows to automate kernel/system optimization, configuration tuning, and end-to-end inference acceleration.
- **Agent Serving Systems** — Designing system-level scheduling, KV cache management, and execution pipelines tailored for dynamic, multi-step agentic workloads.

---

## ⚡ LLM Engine & CUDA

- **[MiniInfer](https://github.com/tom-jerr/MiniInfer)** — Lightweight LLM inference engine built from scratch: Paged & Radix KV Cache, Continuous Batching, Chunked Prefill, Overlap Scheduling, Breakable CUDA Graph, FlashAttention2/FlashInfer, Qwen2/3 & MoE, TP/EP execution.
- **[cuda-learn](https://github.com/tom-jerr/cuda-learn)** — Handwritten CUDA kernels (SGEMM, BF16 Tensor Core MMA, FlashAttention, Fused RMSNorm, Softmax, SiLU-and-Mul, Top-K, Parallel Prefix Sum, CUDA Graph/IPC) exposed via TVM FFI + PyTorch bindings and benchmarked against cuBLAS/cuDNN.
- **[SGLang](https://github.com/tom-jerr/sglang)** — Production LLM serving exploration covering Chunked Prefill, mixed scheduling, Breakable CUDA Graph, Speculative Decoding, and Radix Cache.

---

## 🛠️ Systems Engineering

- **[Nebula Graph — ANN Search](https://github.com/tom-jerr/nebula)** — Added native Approximate Nearest Neighbor (ANN) vector search to a distributed C++ graph database (indexing, query execution, storage optimization).
- **[system_design](https://github.com/tom-jerr/system_design):**
  - **Distributed System:** [6.824](https://github.com/tom-jerr/system_design)(Shard KV with distributed transaction go version), [TinyKV](https://github.com/tom-jerr/tinykv) (Raft-based distributed KV store & transactions)
  - **Storage & Databases:** [BusTub](https://github.com/tom-jerr/bustub) (RDBMS execution & concurrency), [miniob-exp](https://github.com/tom-jerr/system_design) (An experimental database project, familiar with vectorized engines, MVCC/OCC transactions, and the complete SQL execution pipeline), [MiniLSM](https://github.com/tom-jerr/MiniLSM) (LSM-Tree storage engine).
  - **OS & Distributed / Networking:** **MIT 6.S081** (xv6 OS kernel labs), **MIT 6.824 MapReduce** (C++ / gRPC distributed implementation), **RelayServer** (high-performance `epoll` network relay server).

---

## 📊 GitHub Stats

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=tom-jerr&show_icons=true&hide_border=true" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=tom-jerr&layout=compact&hide_border=true" />
</p>
